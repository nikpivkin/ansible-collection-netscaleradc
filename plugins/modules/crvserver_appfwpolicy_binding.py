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
module: crvserver_appfwpolicy_binding
short_description: Binding Resource definition for describing association between
  crvserver and appfwpolicy resources
description: Binding Resource definition for describing association between crvserver
  and appfwpolicy resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  bindpoint:
    description:
      - The bindpoint to which the policy is bound
    type: str
    choices:
      - REQUEST
      - RESPONSE
      - ICA_REQUEST
  gotopriorityexpression:
    description:
      - Expression specifying the priority of the next policy which will get evaluated
        if the current policy rule evaluates to TRUE.
    type: str
  invoke:
    description:
      - Invoke flag.
    type: bool
  labelname:
    description:
      - Name of the label invoked.
    type: str
  labeltype:
    description:
      - The invocation type.
    type: str
    choices:
      - reqvserver
      - resvserver
      - policylabel
  name:
    description:
      - Name of the cache redirection virtual server to which to bind the cache redirection
        policy.
    type: str
  policyname:
    description:
      - Policies bound to this vserver.
    type: str
  priority:
    description:
      - The priority for the policy.
    type: int
  targetvserver:
    description:
      - Name of the virtual server to which content is forwarded. Applicable only
        if the policy is a map policy and the cache redirection virtual server is
        of type REVERSE.
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
