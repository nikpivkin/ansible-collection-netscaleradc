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
module: endpointinfo
short_description: Configuration for Information resource.
description: Configuration for Information resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  endpointkind:
    choices:
      - IP
    description:
      - Endpoint kind. Currently, C(IP) endpoints are supported
    type: str
    default: IP
  endpointlabelsjson:
    description:
      - String representing labels in json form. Maximum length 16K
    type: str
  endpointmetadata:
    description:
      - 'String of qualifiers, in dotted notation, structured metadata for an endpoint.
        Each qualifier is more specific than the one that precedes it, as in cluster.namespace.service.
        For example: cluster.default.frontend. '
      - 'Note: A qualifier that includes a dot (.) or space ( ) must be enclosed in
        double quotation marks.'
    type: str
  endpointname:
    description:
      - Name of endpoint, depends on kind. For IP Endpoint - IP address.
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