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
module: dnstxtrec
short_description: Configuration for TXT record resource.
description: Configuration for TXT record resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  String:
    description:
      - Information to store in the TXT resource record. Enclose the string in single
        or double quotation marks. A TXT resource record can contain up to six strings,
        each of which can contain up to 255 characters. If you want to add a string
        of more than 255 characters, evaluate whether splitting it into two or more
        smaller strings, subject to the six-string limit, works for you.
    type: list
    elements: str
  domain:
    description:
      - Name of the domain for the TXT record.
    type: str
  ecssubnet:
    description:
      - Subnet for which the cached TXT record need to be removed.
    type: str
  nodeid:
    description:
      - Unique number that identifies the cluster node.
    type: float
  recordid:
    description:
      - Unique, internally generated record ID. View the details of the TXT record
        to obtain its record ID. Mutually exclusive with the string parameter.
    type: float
  ttl:
    description:
      - Time to Live (TTL), in seconds, for the record. TTL is the time for which
        the record must be cached by DNS proxies. The specified TTL is applied to
        all the resource records that are of the same record type and belong to the
        specified domain name. For example, if you add an address record, with a TTL
        of 36000, to the domain name example.com, the TTLs of all the address records
        of example.com are changed to 36000. If the TTL is not specified, the Citrix
        ADC uses either the DNS zone's minimum TTL or, if the SOA record is not available
        on the appliance, the default value of 3600.
    type: float
    default: 3600
  type:
    choices:
      - ALL
      - ADNS
      - PROXY
    description:
      - 'Type of records to display. Available settings function as follows:'
      - '* C(ADNS) - Display all authoritative address records.'
      - '* C(PROXY) - Display all proxy address records.'
      - '* C(ALL) - Display all address records.'
    type: str
    default: ADNS
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