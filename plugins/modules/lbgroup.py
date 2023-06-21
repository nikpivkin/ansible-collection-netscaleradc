#!/usr/bin/python

# -*- coding: utf-8 -*-

# TODO: Add license

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: lbgroup
short_description: Configuration for LB group resource.
description: Configuration for LB group resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  backuppersistencetimeout:
    description:
      - Time period, in minutes, for which backup persistence is in effect.
    type: int
    default: 2
  cookiedomain:
    description:
      - Domain attribute for the HTTP cookie.
    type: str
  cookiename:
    description:
      - Use this parameter to specify the cookie name for COOKIE peristence type.
        It specifies the name of cookie with a maximum of 32 characters. If not specified,
        cookie name is internally generated.
    type: str
  mastervserver:
    description:
      - When USE_VSERVER_PERSISTENCE is enabled, one can use this setting to designate
        a member vserver as master which is responsible to create the persistence
        sessions
    type: str
  name:
    description:
      - Name of the load balancing virtual server group.
    type: str
  newname:
    description:
      - New name for the load balancing virtual server group.
    type: str
  persistencebackup:
    description:
      - Type of backup persistence for the group.
    type: str
    choices:
      - SOURCEIP
      - NONE
  persistencetype:
    description:
      - 'Type of persistence for the group. Available settings function as follows:'
      - '* SOURCEIP - Create persistence sessions based on the client IP.'
      - '* COOKIEINSERT - Create persistence sessions based on a cookie in client
        requests. The cookie is inserted by a Set-Cookie directive from the server,
        in its first response to a client.'
      - '* RULE - Create persistence sessions based on a user defined rule.'
      - '* NONE - Disable persistence for the group.'
    type: str
    choices:
      - SOURCEIP
      - COOKIEINSERT
      - RULE
      - NONE
  persistmask:
    description:
      - Persistence mask to apply to source IPv4 addresses when creating source IP
        based persistence sessions.
    type: str
  rule:
    description:
      - Expression, or name of a named expression, against which traffic is evaluated.
      - ''
      - 'The following requirements apply only to the Citrix ADC CLI:'
      - '* If the expression includes one or more spaces, enclose the entire expression
        in double quotation marks.'
      - '* If the expression itself includes double quotation marks, escape the quotations
        by using the \ character. '
      - '* Alternatively, you can use single quotation marks to enclose the rule,
        in which case you do not have to escape the double quotation marks.'
    type: str
    default: '"None"'
  timeout:
    description:
      - Time period for which a persistence session is in effect.
    type: int
    default: 2
  usevserverpersistency:
    description:
      - Use this parameter to enable vserver level persistence on group members. This
        allows member vservers to have their own persistence, but need to be compatible
        with other members persistence rules. When this setting is enabled persistence
        sessions created by any of the members can be shared by other member vservers.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  v6persistmasklen:
    description:
      - Persistence mask to apply to source IPv6 addresses when creating source IP
        based persistence sessions.
    type: int
    default: 128
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
"""

RETURN = r"""
changed:
    description: Indicates if any change is made by the module
    returned: always
    type: bool
    sample: true
diff:
    description: Dictionary of before and after changes
    returned: always
    type: dict
    sample: { 'before': { 'key1': 'xyz' }, 'after': { 'key2': 'pqr' }, 'prepared': 'changes done' }
diff_list:
    description: List of differences between the actual configured object and the configuration specified in the module
    returned: when changed
    type: list
    sample: ["Attribute `key1` differs. Desired: (<class 'str'>) XYZ. Existing: (<class 'str'>) PQR"]
failed:
    description: Indicates if the module failed or not
    returned: always
    type: bool
    sample: false
loglines:
    description: list of logged messages by the module
    returned: always
    type: list
    sample: ['message 1', 'message 2']

"""


import os

from ..module_utils.module_executor import ModuleExecutor

RESOURCE_NAME = os.path.basename(__file__).replace(".py", "")


def main():
    executor = ModuleExecutor(RESOURCE_NAME)
    executor.main()


if __name__ == "__main__":
    main()