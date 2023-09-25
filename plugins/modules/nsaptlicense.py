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
module: nsaptlicense
short_description: Configuration for aptlicense resource.
description: Configuration for aptlicense resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  bindtype:
    description:
      - Bind type
    type: str
  countavailable:
    description:
      - The user can allocate one or more licenses. Ensure the value is less than
        (for partial allocation) or equal to the total number of available licenses
    type: str
  id:
    description:
      - License ID
    type: str
  licensedir:
    description:
      - License Directory
    type: str
  serialno:
    description:
      - Hardware Serial Number/License Activation Code(LAC)
    type: str
  sessionid:
    description:
      - Session ID
    type: str
  useproxy:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Specifies whether to use the licenseproxyserver to reach the internet. Make
        sure to configure licenseproxyserver to use this option.
    type: str
    default: 'NO'
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