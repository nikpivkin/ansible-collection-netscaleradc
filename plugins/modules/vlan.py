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
module: vlan
short_description: Configuration for "VLAN" resource.
description: Configuration for "VLAN" resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  aliasname:
    description:
      - A name for the VLAN. Must begin with a letter, a number, or the underscore
        symbol, and can consist of from 1 to 31 letters, numbers, and the hyphen (-),
        period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore
        (_) characters. You should choose a name that helps identify the VLAN. However,
        you cannot perform any VLAN operation by specifying this name instead of the
        VLAN ID.
    type: str
  dynamicrouting:
    description:
      - Enable dynamic routing on this VLAN.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  id:
    description:
      - A positive integer that uniquely identifies a VLAN.
    type: int
  ipv6dynamicrouting:
    description:
      - 'Enable all IPv6 dynamic routing protocols on this VLAN. Note: For the ENABLED
        setting to work, you must configure IPv6 dynamic routing protocols from the
        VTYSH command line.'
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  mtu:
    description:
      - Specifies the maximum transmission unit (MTU), in bytes. The MTU is the largest
        packet size, excluding 14 bytes of ethernet header and 4 bytes of crc, that
        can be transmitted and received over this VLAN.
    type: int
  sharing:
    description:
      - If sharing is enabled, then this vlan can be shared across multiple partitions
        by binding it to all those partitions. If sharing is disabled, then this vlan
        can be bound to only one of the partitions.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
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
