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
module: videooptimizationdetectionpolicy
short_description: Configuration for videooptimization detectionpolicy resource.
description: Configuration for videooptimization detectionpolicy resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  action:
    description:
      - 'Name of the videooptimization detection action to perform if the request
        matches this videooptimization detection policy. Built-in actions should be
        used. These are:'
      - '* DETECT_CLEARTEXT_PD - Cleartext PD is detected and increment related counters.'
      - '* DETECT_CLEARTEXT_ABR - Cleartext ABR is detected and increment related
        counters.'
      - '* DETECT_ENCRYPTED_ABR - Encrypted ABR is detected and increment related
        counters.'
      - '* TRIGGER_ENC_ABR_DETECTION - This is potentially encrypted ABR. Internal
        traffic heuristics algorithms will further process traffic to confirm detection.'
      - '* TRIGGER_CT_ABR_BODY_DETECTION -  This is potentially cleartext ABR. Internal
        traffic heuristics algorithms will further process traffic to confirm detection.'
      - '* RESET - Reset the client connection by closing it.'
      - '* DROP - Drop the connection without sending a response.'
    type: str
  comment:
    description:
      - Any type of information about this videooptimization detection policy.
    type: str
  logaction:
    description:
      - Name of the messagelog action to use for requests that match this policy.
    type: str
  name:
    description:
      - Name for the videooptimization detection policy. Must begin with a letter,
        number, or the underscore character (_), and must contain only letters, numbers,
        and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon
        (:), and underscore characters.Can be modified, removed or renamed.
    type: str
  newname:
    description:
      - New name for the videooptimization detection policy. Must begin with a letter,
        number, or the underscore character (_), and must contain only letters, numbers,
        and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon
        (:), and underscore characters.
    type: str
  rule:
    description:
      - Expression that determines which request or response match the video optimization
        detection policy.
      - ''
      - 'The following requirements apply only to the Citrix ADC CLI:'
      - '* If the expression includes one or more spaces, enclose the entire expression
        in double quotation marks.'
      - '* If the expression itself includes double quotation marks, escape the quotations
        by using the \ character.'
      - '* Alternatively, you can use single quotation marks to enclose the rule,
        in which case you do not have to escape the double quotation marks.'
    type: str
  undefaction:
    description:
      - Action to perform if the result of policy evaluation is undefined (UNDEF).
        An UNDEF event indicates an internal error condition. Only the above built-in
        actions can be used.
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
