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
module: appfwprofile_jsonxssurl_binding
short_description: Binding Resource definition for describing association between
  appfwprofile and jsonxssurl resources
description: Binding Resource definition for describing association between appfwprofile
  and jsonxssurl resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  alertonly:
    description:
      - Send SNMP alert?
    type: str
    choices:
      - true
      - false
  as_value_expr_json_xss:
    description:
      - JSON_XSS key value expressions consistituting expressions for Keyword and
        SpecialString
    type: str
  as_value_type_json_xss:
    description:
      - JSON Command key value type. (Keyword | SpecialString)
    type: str
    choices:
      - Tag
      - Attribute
      - Pattern
  comment:
    description:
      - Any comments about the purpose of profile, or other useful information about
        the profile.
    type: str
  isautodeployed:
    description:
      - Is the rule auto deployed by dynamic profile ?
    type: str
    choices:
      - AUTODEPLOYED
      - NOTAUTODEPLOYED
  iskeyregex_json_xss:
    description:
      - Is a regular expression?
    type: str
    choices:
      - REGEX
      - NOTREGEX
  isvalueregex_json_xss:
    description:
      - Is a regular expression?
    type: str
    choices:
      - REGEX
      - NOTREGEX
  jsonxssurl:
    description:
      - A regular expression that designates a URL on the Json XSS URL list for which
        XSS violations are relaxed.
      - Enclose URLs in double quotes to ensure preservation of any embedded spaces
        or non-alphanumeric characters.
    type: str
  keyname_json_xss:
    description:
      - JSON XSS Key name
    type: str
  name:
    description:
      - Name of the profile to which to bind an exemption or rule.
    type: str
  resourceid:
    description:
      - A "id" that identifies the rule.
    type: str
  ruletype:
    description:
      - Specifies rule type of binding
    type: str
    choices:
      - ALLOW
      - DENY
  state:
    description:
      - Enabled.
    type: str
    choices:
      - ENABLED
      - DISABLED
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