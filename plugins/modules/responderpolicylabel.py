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
module: responderpolicylabel
short_description: Configuration for responder policy label resource.
description: Configuration for responder policy label resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  comment:
    description:
      - Any comments to preserve information about this responder policy label.
    type: str
  labelname:
    description:
      - Name for the responder policy label. Must begin with a letter, number, or
        the underscore character (_), and must contain only letters, numbers, and
        the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon
        (:), and underscore characters. Cannot be changed after the responder policy
        label is added.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my responder policy label" or my responder
        policy label').
    type: str
  newname:
    description:
      - New name for the responder policy label. Must begin with a letter, number,
        or the underscore character (_), and must contain only letters, numbers, and
        the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon
        (:), and underscore characters.
    type: str
  policylabeltype:
    description:
      - 'Type of responses sent by the policies bound to this policy label. Types
        are:'
      - '* HTTP - HTTP responses. '
      - '* OTHERTCP - NON-HTTP TCP responses.'
      - '* SIP_UDP - SIP responses.'
      - '* RADIUS - RADIUS responses.'
      - '* MYSQL - SQL responses in MySQL format.'
      - '* MSSQL - SQL responses in Microsoft SQL format.'
      - '* NAT - NAT response.'
      - '* MQTT - Trigger policies bind with MQTT type.'
      - '* MQTT_JUMBO - Trigger policies bind with MQTT Jumbo type.'
    type: str
    default: HTTP
    choices:
      - HTTP
      - OTHERTCP
      - SIP_UDP
      - SIP_TCP
      - MYSQL
      - MSSQL
      - NAT
      - DIAMETER
      - RADIUS
      - DNS
      - MQTT
      - MQTT_JUMBO
      - QUIC_BRIDGE
      - HTTP_QUIC
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