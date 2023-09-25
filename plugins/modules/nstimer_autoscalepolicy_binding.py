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
module: nstimer_autoscalepolicy_binding
short_description: Binding Resource definition for describing association between
  nstimer and autoscalepolicy resources
description: Binding Resource definition for describing association between nstimer
  and autoscalepolicy resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  gotopriorityexpression:
    description:
      - Expression specifying the priority of the next policy which will get evaluated
        if the current policy rule evaluates to TRUE.
    type: str
  name:
    description:
      - Timer name.
    type: str
  policyname:
    description:
      - The timer policy associated with the timer.
    type: str
  priority:
    description:
      - Specifies the priority of the timer policy.
    type: float
  samplesize:
    description:
      - Denotes the sample size. Sample size value of 'x' means that previous '(x
        - 1)' policy's rule evaluation results and the current evaluation result are
        present with the binding. For example, sample size of 10 means that there
        is a state of previous 9 policy evaluation results and also the current policy
        evaluation result.
    type: float
    default: 3
  threshold:
    description:
      - Denotes the threshold. If the rule of the policy in the binding relation evaluates
        'threshold size' number of times in 'sample size' to true, then the corresponding
        action is taken. Its value needs to be less than or equal to the sample size
        value.
    type: float
    default: 3
  vserver:
    description:
      - Name of the vserver which provides the context for the rule in timer policy.
        When not specified it is treated as a Global Default context.
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