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
module: botglobal_botpolicy_binding
short_description: Binding Resource definition for describing association between
  botglobal and botpolicy resources
description: Binding Resource definition for describing association between botglobal
  and botpolicy resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  globalbindtype:
    choices:
      - SYSTEM_GLOBAL
      - VPN_GLOBAL
      - RNAT_GLOBAL
      - APPFW_GLOBAL
    description:
      - '0'
    type: str
    default: SYSTEM_GLOBAL
  gotopriorityexpression:
    description:
      - Expression specifying the priority of the next policy which will get evaluated
        if the current policy rule evaluates to TRUE.
    type: str
  invoke:
    description:
      - If the current policy evaluates to TRUE, terminate evaluation of policies
        bound to the current policy label, and then forward the request to the specified
        virtual server.
    type: bool
  labelname:
    description:
      - Name of the policy label to invoke. If the current policy evaluates to TRUE,
        the invoke parameter is set, and Label Type is policylabel.
    type: str
  labeltype:
    choices:
      - vserver
      - policylabel
    description:
      - 'Type of invocation, Available settings function as follows:'
      - '* C(vserver) - Forward the request to the specified virtual server.'
      - '* C(policylabel) - Invoke the specified policy label.'
    type: str
  policyname:
    description:
      - Name of the bot policy.
    type: str
  priority:
    description:
      - Specifies the priority of the policy.
    type: int
  type:
    choices:
      - REQ_OVERRIDE
      - REQ_DEFAULT
    description:
      - 'Specifies the bind point whose policies you want to display. Available settings
        function as follows:'
      - '* C(REQ_OVERRIDE) - Request override. Binds the policy to the priority request
        queue.'
      - '* C(REQ_DEFAULT) - Binds the policy to the default request queue.'
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
