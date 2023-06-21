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
module: botprofile_blacklist_binding
short_description: Binding Resource definition for describing association between
  botprofile and blacklist resources
description: Binding Resource definition for describing association between botprofile
  and blacklist resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  bot_bind_comment:
    description:
      - Any comments about this binding.
    type: str
  bot_blacklist:
    description:
      - Blacklist binding. Maximum 32 bindings can be configured per profile for Blacklist
        detection.
    type: bool
  bot_blacklist_action:
    description:
      - One or more actions to be taken if  bot is detected based on this Blacklist
        binding. Only LOG action can be combined with DROP or RESET action.
    type: list
    elements: str
    default: NONE
    choices:
      - NONE
      - LOG
      - DROP
      - RESET
      - REDIRECT
  bot_blacklist_enabled:
    description:
      - Enabled or disbaled black-list binding.
    type: str
    choices:
      - true
      - false
  bot_blacklist_type:
    description:
      - Type of the black-list entry.
    type: str
    choices:
      - IPv4
      - SUBNET
      - IPv6
      - IPv6_SUBNET
      - EXPRESSION
  bot_blacklist_value:
    description:
      - Value of the bot black-list entry.
    type: str
  logmessage:
    description:
      - Message to be logged for this binding.
    type: str
  name:
    description:
      - Name for the profile. Must begin with a letter, number, or the underscore
        character (_), and must contain only letters, numbers, and the hyphen (-),
        period (.), pound (#), space ( ), at (@), equals (=), colon (:), and underscore
        (_) characters. Cannot be changed after the profile is added.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my profile" or 'my profile').
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
