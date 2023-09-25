#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2020 Citrix Systems, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: dnsparameter
short_description: Configuration for DNS parameter resource.
description: Configuration for DNS parameter resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  cacheecszeroprefix:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Cache ECS responses with a Scope Prefix length of zero. Such a cached response
        will be used for all queries with this domain name and any subnet. When disabled,
        ECS responses with Scope Prefix length of zero will be cached, but not tied
        to any subnet. This option has no effect if caching of ECS responses is disabled
        in the corresponding DNS profile.
    type: str
    default: ENABLED
  cachehitbypass:
    choices:
      - ENABLED
      - DISABLED
    description:
      - This parameter is applicable only in proxy mode and if this parameter is enabled  we
        will forward all the client requests to the backend DNS server and the response
        served will be cached on Citrix ADC
    type: str
    default: DISABLED
  cachenoexpire:
    choices:
      - ENABLED
      - DISABLED
    description:
      - If this flag is set to YES, the existing entries in cache do not age out.
        On reaching the max limit the cache records are frozen
    type: str
    default: DISABLED
  cacherecords:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Cache resource records in the DNS cache. Applies to resource records obtained
        through proxy configurations only. End resolver and forwarder configurations
        always cache records in the DNS cache, and you cannot disable this behavior.
        When you disable record caching, the appliance stops caching server responses.
        However, cached records are not flushed. The appliance does not serve requests
        from the cache until record caching is enabled again.
    type: str
    default: 'YES'
  dns64timeout:
    description:
      - While doing DNS64 resolution, this parameter specifies the time to wait before
        sending an A query if no response is received from backend DNS server for
        AAAA query.
    type: float
  dnsrootreferral:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Send a root referral if a client queries a domain name that is unrelated to
        the domains configured/cached on the Citrix ADC. If the setting is disabled,
        the appliance sends a blank response instead of a root referral. Applicable
        to domains for which the appliance is authoritative. Disable the parameter
        when the appliance is under attack from a client that is sending a flood of
        queries for unrelated domains.
    type: str
    default: DISABLED
  dnssec:
    choices:
      - ENABLED
      - DISABLED
    description:
      - 'Enable or disable the Domain Name System Security Extensions (DNSSEC) feature
        on the appliance. Note: Even when the DNSSEC feature is enabled, forwarder
        configurations (used by internal Citrix ADC features such as SSL VPN and Cache
        Redirection for name resolution) do not support the DNSSEC OK (DO) bit in
        the EDNS0 OPT header.'
    type: str
    default: ENABLED
  ecsmaxsubnets:
    description:
      - Maximum number of subnets that can be cached corresponding to a single domain.
        Subnet caching will occur for responses with EDNS Client Subnet (ECS) option.
        Caching of such responses can be disabled using DNS profile settings. A value
        of zero indicates that the number of subnets cached is limited only by existing
        memory constraints. The default value is zero.
    type: float
  maxcachesize:
    description:
      - Maximum memory, in megabytes, that can be used for dns caching per Packet
        Engine.
    type: float
  maxnegativecachesize:
    description:
      - Maximum memory, in megabytes, that can be used for caching of negative DNS
        responses per packet engine.
    type: float
  maxnegcachettl:
    description:
      - Maximum time to live (TTL) for all negative records ( NXDONAIN and NODATA
        ) cached in the DNS cache by DNS proxy, end resolver, and forwarder configurations.
        If the TTL of a record that is to be cached is higher than the value configured
        for maxnegcacheTTL, the TTL of the record is set to the value of maxnegcacheTTL
        before caching. When you modify this setting, the new value is applied only
        to those records that are cached after the modification. The TTL values of
        existing records are not changed.
    type: float
    default: 604800
  maxpipeline:
    description:
      - Maximum number of concurrent DNS requests to allow on a single client connection,
        which is identified by the <clientip:port>-<vserver ip:port> tuple. A value
        of 0 (zero) applies no limit to the number of concurrent DNS requests allowed
        on a single client connection.
    type: float
  maxttl:
    description:
      - Maximum time to live (TTL) for all records cached in the DNS cache by DNS
        proxy, end resolver, and forwarder configurations. If the TTL of a record
        that is to be cached is higher than the value configured for maxTTL, the TTL
        of the record is set to the value of maxTTL before caching. When you modify
        this setting, the new value is applied only to those records that are cached
        after the modification. The TTL values of existing records are not changed.
    type: float
    default: 604800
  maxudppacketsize:
    description:
      - Maximum UDP packet size that can be handled by Citrix ADC. This is the value
        advertised by Citrix ADC when responding as an authoritative server and it
        is also used when Citrix ADC queries other name servers as a forwarder. When
        acting as a proxy, requests from clients are limited by this parameter - if
        a request contains a size greater than this value in the OPT record, it will
        be replaced.
    type: float
    default: 1280
  minttl:
    description:
      - Minimum permissible time to live (TTL) for all records cached in the DNS cache
        by DNS proxy, end resolver, and forwarder configurations. If the TTL of a
        record that is to be cached is lower than the value configured for minTTL,
        the TTL of the record is set to the value of minTTL before caching. When you
        modify this setting, the new value is applied only to those records that are
        cached after the modification. The TTL values of existing records are not
        changed.
    type: float
  namelookuppriority:
    choices:
      - WINS
      - DNS
    description:
      - Type of lookup (C(DNS) or C(WINS)) to attempt first. If the first-priority
        lookup fails, the second-priority lookup is attempted. Used only by the SSL
        VPN feature.
    type: str
    default: WINS
  nxdomainratelimitthreshold:
    description:
      - Rate limit threshold for Non-Existant domain (NXDOMAIN) responses generated
        from Citrix ADC. Once the threshold is breached , DNS queries leading to NXDOMAIN
        response will be dropped. This threshold will not be applied for NXDOMAIN
        responses got from the backend. The threshold will be applied per packet engine
        and per second.
    type: float
  recursion:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Function as an end resolver and recursively resolve queries for domains that
        are not hosted on the Citrix ADC. Also resolve queries recursively when the
        external name servers configured on the appliance (for a forwarder configuration)
        are unavailable. When external name servers are unavailable, the appliance
        queries a root server and resolves the request recursively, as it does for
        an end resolver configuration.
    type: str
    default: DISABLED
  resolutionorder:
    choices:
      - OnlyAQuery
      - OnlyAAAAQuery
      - AThenAAAAQuery
      - AAAAThenAQuery
    description:
      - 'Type of DNS queries (A, AAAA, or both) to generate during the routine functioning
        of certain Citrix ADC features, such as SSL VPN, cache redirection, and the
        integrated cache. The queries are sent to the external name servers that are
        configured for the forwarder function. If you specify both query types, you
        can also specify the order. Available settings function as follows:'
      - '* C(OnlyAQuery). Send queries for IPv4 address records (A records) only. '
      - '* C(OnlyAAAAQuery). Send queries for IPv6 address records (AAAA records)
        instead of queries for IPv4 address records (A records).'
      - '* C(AThenAAAAQuery). Send a query for an A record, and then send a query
        for an AAAA record if the query for the A record results in a NODATA response
        from the name server.'
      - '* C(AAAAThenAQuery). Send a query for an AAAA record, and then send a query
        for an A record if the query for the AAAA record results in a NODATA response
        from the name server.'
    type: str
    default: OnlyAQuery
  retries:
    description:
      - Maximum number of retry attempts when no response is received for a query
        sent to a name server. Applies to end resolver and forwarder configurations.
    type: float
    default: 5
  splitpktqueryprocessing:
    choices:
      - ALLOW
      - DROP
    description:
      - Processing requests split across multiple packets
    type: str
    default: ALLOW
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