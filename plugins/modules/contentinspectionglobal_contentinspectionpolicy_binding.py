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
module: contentinspectionglobal_contentinspectionpolicy_binding
short_description: Binding Resource definition for describing association between
  contentinspectionglobal and contentinspectionpolicy resources
description: Binding Resource definition for describing association between contentinspectionglobal
  and contentinspectionpolicy resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  globalbindtype:
    description:
      - '0'
    type: str
    default: SYSTEM_GLOBAL
    choices:
      - SYSTEM_GLOBAL
      - VPN_GLOBAL
      - RNAT_GLOBAL
      - APPFW_GLOBAL
  gotopriorityexpression:
    description:
      - Expression specifying the priority of the next policy which will get evaluated
        if the current policy rule evaluates to TRUE.
    type: str
  invoke:
    description:
      - Terminate evaluation of policies bound to the current policy label, and then
        forward the request to the specified virtual server or evaluate the specified
        policy label.
    type: bool
  labelname:
    description:
      - '* If labelType is policylabel, name of the policy label to invoke.'
      - '* If labelType is reqvserver or resvserver, name of the virtual server to
        which to forward the request of response.'
    type: str
  labeltype:
    description:
      - 'Type of invocation. Available settings function as follows:'
      - '* reqvserver - Forward the request to the specified request virtual server.'
      - '* resvserver - Forward the response to the specified response virtual server.'
      - '* policylabel - Invoke the specified policy label.'
    type: str
    choices:
      - reqvserver
      - resvserver
      - policylabel
  policyname:
    description:
      - Name of the contentInspection policy.
    type: str
  priority:
    description:
      - Specifies the priority of the policy.
    type: int
  type:
    description:
      - The bindpoint to which to policy is bound.
    type: str
    choices:
      - REQ_OVERRIDE
      - REQ_DEFAULT
      - RES_OVERRIDE
      - RES_DEFAULT
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
