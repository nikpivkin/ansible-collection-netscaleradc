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
module: authenticationnegotiateaction
short_description: Configuration for Negotiate action resource.
description: Configuration for Negotiate action resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  defaultauthenticationgroup:
    description:
      - This is the default group that is chosen when the authentication succeeds
        in addition to extracted groups.
    type: str
  domain:
    description:
      - Domain name of the service principal that represnts Citrix ADC.
    type: str
  domainuser:
    description:
      - User name of the account that is mapped with Citrix ADC principal. This can
        be given along with domain and password when keytab file is not available.
        If username is given along with keytab file, then that keytab file will be
        searched for this user's credentials.
    type: str
  domainuserpasswd:
    description:
      - Password of the account that is mapped to the Citrix ADC principal.
    type: str
  keytab:
    description:
      - The path to the keytab file that is used to decrypt kerberos tickets presented
        to Citrix ADC. If keytab is not available, domain/username/password can be
        specified in the negotiate action configuration
    type: str
  name:
    description:
      - 'Name for the AD KDC server profile (negotiate action). '
      - Must begin with a letter, number, or the underscore character (_), and must
        contain only letters, numbers, and the hyphen (-), period (.) pound (#), space
        ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed
        after AD KDC server profile is created.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my authentication action" or 'my authentication
        action').
    type: str
  ntlmpath:
    description:
      - The path to the site that is enabled for NTLM authentication, including FQDN
        of the server. This is used when clients fallback to NTLM.
    type: str
  ou:
    description:
      - Active Directory organizational units (OU) attribute.
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