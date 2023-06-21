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
module: appfwprofile_sqlinjection_binding
short_description: Binding Resource definition for describing association between
  appfwprofile and sqlinjection resources
description: Binding Resource definition for describing association between appfwprofile
  and sqlinjection resources
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
  as_scan_location_sql:
    description:
      - Location of SQL injection exception - form field, header or cookie.
    type: str
    choices:
      - FORMFIELD
      - HEADER
      - COOKIE
  as_value_expr_sql:
    description:
      - The web form value expression.
    type: str
  as_value_type_sql:
    description:
      - The web form value type.
    type: str
    choices:
      - Keyword
      - SpecialString
      - Wildchar
  comment:
    description:
      - Any comments about the purpose of profile, or other useful information about
        the profile.
    type: str
  formactionurl_sql:
    description:
      - The web form action URL.
    type: str
  isautodeployed:
    description:
      - Is the rule auto deployed by dynamic profile ?
    type: str
    choices:
      - AUTODEPLOYED
      - NOTAUTODEPLOYED
  isregex_sql:
    description:
      - Is the web form field name a regular expression?
    type: str
    choices:
      - REGEX
      - NOTREGEX
  isvalueregex_sql:
    description:
      - Is the web form field value a regular expression?
    type: str
    choices:
      - REGEX
      - NOTREGEX
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
  sqlinjection:
    description:
      - The web form field name.
    type: str
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
