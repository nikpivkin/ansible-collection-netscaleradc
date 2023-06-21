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
module: mapbmr_bmrv4network_binding
short_description: Binding Resource definition for describing association between
  mapbmr and bmrv4network resources
description: Binding Resource definition for describing association between mapbmr
  and bmrv4network resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  name:
    description:
      - 'Name for the Basic Mapping Rule. Must begin with an ASCII alphanumeric or
        underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
        characters. Cannot be changed after the  MAP Basic Mapping Rule is created.
        The following requirement applies only to the Citrix ADC CLI: If the name
        includes one or more spaces, enclose the name in double or single quotation
        marks (for example, "add network MapBmr bmr1 -natprefix 2005::/64 -EAbitLength
        16 -psidoffset 6 -portsharingratio 8" ).'
      - "\t\t\tThe Basic Mapping Rule information allows a MAP BR to determine source\
        \ IPv4 address from the IPv6 packet sent from MAP CE device."
      - "\t\t\tAlso it allows to determine destination IPv6 address of MAP CE before\
        \ sending packets to MAP CE"
    type: str
  netmask:
    description:
      - Subnet mask for the IPv4 address specified in the Network parameter.
    type: str
  network:
    description:
      - IPv4 NAT address range of Customer Edge (CE).
    type: str
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