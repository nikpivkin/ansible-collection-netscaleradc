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
module: auditmessageaction
short_description: Configuration for message action resource.
description: Configuration for message action resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  bypasssafetycheck:
    description:
      - Bypass the safety check and allow unsafe expressions.
    type: str
    choices:
      - true
      - false
  loglevel:
    description:
      - 'Audit log level, which specifies the severity level of the log message being
        generated.. '
      - 'The following loglevels are valid: '
      - '* EMERGENCY - Events that indicate an immediate crisis on the server.'
      - '* ALERT - Events that might require action.'
      - '* CRITICAL - Events that indicate an imminent server crisis.'
      - '* ERROR - Events that indicate some type of error.'
      - '* WARNING - Events that require action in the near future.'
      - '* NOTICE - Events that the administrator should know about.'
      - '* INFORMATIONAL - All but low-level events.'
      - '* DEBUG - All events, in extreme detail.'
    type: str
    choices:
      - EMERGENCY
      - ALERT
      - CRITICAL
      - ERROR
      - WARNING
      - NOTICE
      - INFORMATIONAL
      - DEBUG
  logtonewnslog:
    description:
      - Send the message to the new nslog.
    type: str
    choices:
      - true
      - false
  name:
    description:
      - Name of the audit message action. Must begin with a letter, number, or the
        underscore character (_), and must contain only letters, numbers, and the
        hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:),
        and underscore characters. Cannot be changed after the message action is added.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my message action" or 'my message action').
    type: str
  stringbuilderexpr:
    description:
      - Default-syntax expression that defines the format and content of the log message.
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
