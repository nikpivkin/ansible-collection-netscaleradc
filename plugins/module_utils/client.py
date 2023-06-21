import codecs
import json

from ansible.module_utils._text import to_text
from ansible.module_utils.six.moves.urllib.parse import quote
from ansible.module_utils.urls import fetch_url

from .decorators import trace
from .log import log


class NitroAPIClient(object):
    def __init__(self, module):
        self._module = module
        self.check_mode = module.check_mode  # Dry run mode
        module_api_path = self._module.params.get("api_path")
        self.api_path = (
            module_api_path if (module_api_path is not None) else "nitro/v1/config"
        )

        # Prepare the http headers according to module arguments
        self._headers = {}
        self._headers["Content-Type"] = "application/json"
        self._headers["User-Agent"] = "ansible-ctxadc"

        # Check for conflicting authentication methods
        have_token = self._module.params.get("nitro_auth_token") is not None
        have_userpass = None not in (
            self._module.params.get("nitro_user"),
            self._module.params.get("nitro_pass"),
        )

        if have_token and have_userpass:
            # FIXME:
            self._module.fail_json(
                msg="Cannot define both authentication token and username/password"
            )

        if have_token:
            self._headers["Cookie"] = (
                "NITRO_AUTH_TOKEN=%s" % self._module.params["nitro_auth_token"]
            )

        if have_userpass:
            self._headers["X-NITRO-USER"] = self._module.params["nitro_user"]
            self._headers["X-NITRO-PASS"] = self._module.params["nitro_pass"]

        if self._module.params.get("is_cloud", False):
            self._headers["isCloud"] = "true"

        bearer_token = self._module.params.get("bearer_token")
        if bearer_token is not None:
            self._headers["Authorization"] = "CwsAuth bearer=%s" % bearer_token

        # Do header manipulation when doing a MAS proxy call
        if self._module.params.get(
            "mas_proxy_call"
        ) is not None and self._module.params.get("mas_proxy_call"):
            if self._module.params.get("instance_ip") is not None:
                self._headers[
                    "_MPS_API_PROXY_MANAGED_INSTANCE_IP"
                ] = self._module.params["instance_ip"]
            elif self._module.params.get("instance_name") is not None:
                self._headers[
                    "_MPS_API_PROXY_MANAGED_INSTANCE_NAME"
                ] = self._module.params["instance_name"]
            elif self._module.params.get("instance_id") is not None:
                self._headers[
                    "_MPS_API_PROXY_MANAGED_INSTANCE_ID"
                ] = self._module.params["instance_id"]
            else:
                self._module.fail_json(
                    msg="Target NetScaler ADC is undefined for NetScaler ADM proxied NITRO call"
                )

    def url_builder(
        self,
        resource,
        id=None,
        args=None,
        attrs=None,
        filter=None,
        action=None,
        count=False,
    ):
        args = args if args is not None else {}
        attrs = attrs if attrs is not None else []
        filter = filter if filter is not None else {}

        # Construct basic URL
        url = "%s://%s/%s/%s" % (
            self._module.params["nitro_protocol"],
            self._module.params["nsip"],
            self.api_path,
            resource,
        )

        # Append resource id
        if id is not None:
            url = "%s/%s" % (url, id)

        # Query String Builder
        # Construct args
        args_val = ",".join(
            ["%s:%s" % (k, quote(codecs.encode(str(args[k])), safe="")) for k in args]
        )
        args_val = ("args=%s" % args_val) if args_val != "" else ""

        # Construct attrs
        attrs_val = ",".join(attrs)
        attrs_val = ("attrs=%s" % attrs_val) if attrs_val != "" else ""

        # Construct filters
        # if filter = {'key1':'value1', 'key2':'value2'}
        # filter_val=key1:value1,key2:value2
        # filter_val = ",".join(["%s:%s" % (k, filter[k]) for k in filter])
        filter_val = ",".join(
            [
                "%s:%s" % (k, quote(codecs.encode(str(filter[k])), safe=""))
                for k in filter
            ]
        )
        filter_val = ("filter=%s" % filter_val) if filter_val != "" else ""

        # Construct action
        action_val = "action=%s" % action if action is not None else ""

        # Construct count
        count_val = "count=yes" if count else ""

        # Filter out empty string parameters
        val_list = [args_val, attrs_val, filter_val, action_val, count_val]
        query_params = "&".join([v for v in val_list if v != ""])

        return "%s?%s" % (url, query_params) if query_params != "" else url

    @trace
    def send(self, method, url, data=None):
        # log the self object contents
        log("DEBUG: self=%s" % self.__dict__)
        if self.check_mode and method != "GET":
            log("DEBUG: check_mode is enabled, skipping %s:%s request" % (method, url))
            return 0, {}

        r, info = fetch_url(
            self._module, url=url, headers=self._headers, method=method, data=data
        )
        log("DEBUG: fetch_url()-resonse-info=%s" % info)
        status_code = info["status"]
        # if status_code == -1:
        #     log("ERROR: Could not connect to the target Netscaler instance: %s" % url)
        #     return status_code, {}
        body = r.read() if r else None
        # info['body'] will not be present for status_codes < 400
        if status_code >= 400:
            return status_code, json.loads(to_text(info["body"]))
        else:
            if not body:
                if "body" in info:
                    return status_code, json.loads(to_text(info["body"]))
                else:
                    return status_code, {}
            else:
                return status_code, json.loads(to_text(body))

    def get(self, resource, id=None, args=None, attrs=None, filter=None):
        url = self.url_builder(resource, id=id, args=args, attrs=attrs, filter=filter)
        return self.send("GET", url)

    def post(self, post_data, resource, action=None):
        url = self.url_builder(resource, action=action)
        data = self._module.jsonify(post_data)
        return self.send("POST", url, data)

    def put(self, put_data, resource=None, id=None):
        url = self.url_builder(resource, id=id)
        data = self._module.jsonify(put_data)
        return self.send("PUT", url, data)

    def delete(self, resource, id=None, args=None):
        url = self.url_builder(resource, id=id, args=args)
        return self.send("DELETE", url)