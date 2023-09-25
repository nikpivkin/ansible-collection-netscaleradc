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
module: vlan_linkset_binding
short_description: Binding Resource definition for describing association between
  vlan and linkset resources
description: Binding Resource definition for describing association between vlan and
  linkset resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  id:
    description:
      - Specifies the virtual LAN ID.
    type: float
  ifnum:
    description:
      - The interface to be bound to the VLAN, specified in slot/port notation (for
        example, 1/3).
    type: str
  ownergroup:
    description:
      - The owner node group in a Cluster for this vlan.
    type: str
    default: DEFAULT_NG
  tagged:
    description:
      - Make the interface an 802.1q tagged interface. Packets sent on this interface
        on this VLAN have an additional 4-byte 802.1q tag, which identifies the VLAN.
        To use 802.1q tagging, you must also configure the switch connected to the
        appliance's interfaces.
    type: bool
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
