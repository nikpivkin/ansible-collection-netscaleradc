#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2023 Cloud Software Group, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: vpnnexthopserver
short_description: Configuration for Next Hop Server resource.
description: Configuration for Next Hop Server resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  state:
    choices:
      - present
      - absent
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present) the resource will be created if needed and configured according
        to the module's parameters.
      - When C(absent) the resource will be deleted from the NetScaler ADC node.
    type: str
  name:
    type: str
    description:
      - Name for the Citrix Gateway appliance in the first DMZ.
  nexthopfqdn:
    type: str
    description:
      - FQDN of the Citrix Gateway proxy in the second DMZ.
  nexthopip:
    type: str
    description:
      - IP address of the Citrix Gateway proxy in the second DMZ.
  nexthopport:
    type: int
    description:
      - Port number of the Citrix Gateway proxy in the second DMZ.
  resaddresstype:
    type: str
    choices:
      - IPV4
      - IPV6
    description:
      - Address Type (C(IPV4)/IPv6) of DNS name of nextHopServer FQDN.
  secure:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Use of a secure port, such as 443, for the double-hop configuration.
    default: 'OFF'
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
