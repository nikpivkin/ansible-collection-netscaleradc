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
module: nssimpleacl6
short_description: Configuration for simple ACL6 resource.
description: Configuration for simple ACL6 resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  aclaction:
    description:
      - Drop incoming IPv6 packets that match the simple ACL6 rule.
    type: str
    choices:
      - DENY
  aclname:
    description:
      - Name for the simple ACL6 rule. Must begin with an ASCII alphabetic or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
        Cannot be changed after the simple ACL6 rule is created.
    type: str
  destport:
    description:
      - Port number to match against the destination port number of an incoming IPv6
        packet.
      - ''
      - DestPort is mandatory while setting Protocol. Omitting the port number and
        protocol creates an all-ports  and all protocol simple ACL6 rule, which matches
        any port and any protocol. In that case, you cannot create another simple
        ACL6 rule specifying a specific port and the same source IPv6 address.
    type: int
  estsessions:
    description:
      - '0'
    type: bool
  protocol:
    description:
      - Protocol to match against the protocol of an incoming IPv6 packet. You must
        set this parameter if you set the Destination Port parameter.
    type: str
    choices:
      - TCP
      - UDP
  srcipv6:
    description:
      - IP address to match against the source IP address of an incoming IPv6 packet.
    type: str
  td:
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
    type: int
  ttl:
    description:
      - Number of seconds, in multiples of four, after which the simple ACL6 rule
        expires. If you do not want the simple ACL6 rule to expire, do not specify
        a TTL value.
    type: int
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
