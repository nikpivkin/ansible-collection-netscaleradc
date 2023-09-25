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
module: vpnsamlssoprofile
short_description: Configuration for SAML sso action resource.
description: Configuration for SAML sso action resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  assertionconsumerserviceurl:
    description:
      - URL to which the assertion is to be sent.
    type: str
  attribute1:
    description:
      - Name of attribute1 that needs to be sent in SAML Assertion
    type: str
  attribute10:
    description:
      - Name of attribute10 that needs to be sent in SAML Assertion
    type: str
  attribute10expr:
    description:
      - Expression that will be evaluated to obtain attribute10's value to be sent
        in Assertion
    type: str
  attribute10format:
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute10 to be sent in Assertion.
    type: str
  attribute10friendlyname:
    description:
      - User-Friendly Name of attribute10 that needs to be sent in SAML Assertion
    type: str
  attribute11:
    description:
      - Name of attribute11 that needs to be sent in SAML Assertion
    type: str
  attribute11expr:
    description:
      - Expression that will be evaluated to obtain attribute11's value to be sent
        in Assertion
    type: str
  attribute11format:
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute11 to be sent in Assertion.
    type: str
  attribute11friendlyname:
    description:
      - User-Friendly Name of attribute11 that needs to be sent in SAML Assertion
    type: str
  attribute12:
    description:
      - Name of attribute12 that needs to be sent in SAML Assertion
    type: str
  attribute12expr:
    description:
      - Expression that will be evaluated to obtain attribute12's value to be sent
        in Assertion
    type: str
  attribute12format:
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute12 to be sent in Assertion.
    type: str
  attribute12friendlyname:
    description:
      - User-Friendly Name of attribute12 that needs to be sent in SAML Assertion
    type: str
  attribute13:
    description:
      - Name of attribute13 that needs to be sent in SAML Assertion
    type: str
  attribute13expr:
    description:
      - Expression that will be evaluated to obtain attribute13's value to be sent
        in Assertion
    type: str
  attribute13format:
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute13 to be sent in Assertion.
    type: str
  attribute13friendlyname:
    description:
      - User-Friendly Name of attribute13 that needs to be sent in SAML Assertion
    type: str
  attribute14:
    description:
      - Name of attribute14 that needs to be sent in SAML Assertion
    type: str
  attribute14expr:
    description:
      - Expression that will be evaluated to obtain attribute14's value to be sent
        in Assertion
    type: str
  attribute14format:
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute14 to be sent in Assertion.
    type: str
  attribute14friendlyname:
    description:
      - User-Friendly Name of attribute14 that needs to be sent in SAML Assertion
    type: str
  attribute15:
    description:
      - Name of attribute15 that needs to be sent in SAML Assertion
    type: str
  attribute15expr:
    description:
      - Expression that will be evaluated to obtain attribute15's value to be sent
        in Assertion
    type: str
  attribute15format:
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute15 to be sent in Assertion.
    type: str
  attribute15friendlyname:
    description:
      - User-Friendly Name of attribute15 that needs to be sent in SAML Assertion
    type: str
  attribute16:
    description:
      - Name of attribute16 that needs to be sent in SAML Assertion
    type: str
  attribute16expr:
    description:
      - Expression that will be evaluated to obtain attribute16's value to be sent
        in Assertion
    type: str
  attribute16format:
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute16 to be sent in Assertion.
    type: str
  attribute16friendlyname:
    description:
      - User-Friendly Name of attribute16 that needs to be sent in SAML Assertion
    type: str
  attribute1expr:
    description:
      - Expression that will be evaluated to obtain attribute1's value to be sent
        in Assertion
    type: str
  attribute1format:
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute1 to be sent in Assertion.
    type: str
  attribute1friendlyname:
    description:
      - User-Friendly Name of attribute1 that needs to be sent in SAML Assertion
    type: str
  attribute2:
    description:
      - Name of attribute2 that needs to be sent in SAML Assertion
    type: str
  attribute2expr:
    description:
      - Expression that will be evaluated to obtain attribute2's value to be sent
        in Assertion
    type: str
  attribute2format:
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute2 to be sent in Assertion.
    type: str
  attribute2friendlyname:
    description:
      - User-Friendly Name of attribute2 that needs to be sent in SAML Assertion
    type: str
  attribute3:
    description:
      - Name of attribute3 that needs to be sent in SAML Assertion
    type: str
  attribute3expr:
    description:
      - Expression that will be evaluated to obtain attribute3's value to be sent
        in Assertion
    type: str
  attribute3format:
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute3 to be sent in Assertion.
    type: str
  attribute3friendlyname:
    description:
      - User-Friendly Name of attribute3 that needs to be sent in SAML Assertion
    type: str
  attribute4:
    description:
      - Name of attribute4 that needs to be sent in SAML Assertion
    type: str
  attribute4expr:
    description:
      - Expression that will be evaluated to obtain attribute4's value to be sent
        in Assertion
    type: str
  attribute4format:
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute4 to be sent in Assertion.
    type: str
  attribute4friendlyname:
    description:
      - User-Friendly Name of attribute4 that needs to be sent in SAML Assertion
    type: str
  attribute5:
    description:
      - Name of attribute5 that needs to be sent in SAML Assertion
    type: str
  attribute5expr:
    description:
      - Expression that will be evaluated to obtain attribute5's value to be sent
        in Assertion
    type: str
  attribute5format:
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute5 to be sent in Assertion.
    type: str
  attribute5friendlyname:
    description:
      - User-Friendly Name of attribute5 that needs to be sent in SAML Assertion
    type: str
  attribute6:
    description:
      - Name of attribute6 that needs to be sent in SAML Assertion
    type: str
  attribute6expr:
    description:
      - Expression that will be evaluated to obtain attribute6's value to be sent
        in Assertion
    type: str
  attribute6format:
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute6 to be sent in Assertion.
    type: str
  attribute6friendlyname:
    description:
      - User-Friendly Name of attribute6 that needs to be sent in SAML Assertion
    type: str
  attribute7:
    description:
      - Name of attribute7 that needs to be sent in SAML Assertion
    type: str
  attribute7expr:
    description:
      - Expression that will be evaluated to obtain attribute7's value to be sent
        in Assertion
    type: str
  attribute7format:
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute7 to be sent in Assertion.
    type: str
  attribute7friendlyname:
    description:
      - User-Friendly Name of attribute7 that needs to be sent in SAML Assertion
    type: str
  attribute8:
    description:
      - Name of attribute8 that needs to be sent in SAML Assertion
    type: str
  attribute8expr:
    description:
      - Expression that will be evaluated to obtain attribute8's value to be sent
        in Assertion
    type: str
  attribute8format:
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute8 to be sent in Assertion.
    type: str
  attribute8friendlyname:
    description:
      - User-Friendly Name of attribute8 that needs to be sent in SAML Assertion
    type: str
  attribute9:
    description:
      - Name of attribute9 that needs to be sent in SAML Assertion
    type: str
  attribute9expr:
    description:
      - Expression that will be evaluated to obtain attribute9's value to be sent
        in Assertion
    type: str
  attribute9format:
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute9 to be sent in Assertion.
    type: str
  attribute9friendlyname:
    description:
      - User-Friendly Name of attribute9 that needs to be sent in SAML Assertion
    type: str
  audience:
    description:
      - Audience for which assertion sent by IdP is applicable. This is typically
        entity name or url that represents ServiceProvider
    type: str
  digestmethod:
    choices:
      - SHA1
      - SHA256
    description:
      - Algorithm to be used to compute/verify digest for SAML transactions
    type: str
    default: SHA256
  encryptassertion:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Option to encrypt assertion when Citrix ADC sends one.
    type: str
    default: 'OFF'
  encryptionalgorithm:
    choices:
      - DES3
      - AES128
      - AES192
      - AES256
    description:
      - Algorithm to be used to encrypt SAML assertion
    type: str
    default: AES256
  name:
    description:
      - Name for the new saml single sign-on profile. Must begin with an ASCII alphanumeric
        or underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
        characters. Cannot be changed after an SSO action is created.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my action" or 'my action').
    type: str
  nameidexpr:
    description:
      - Expression that will be evaluated to obtain NameIdentifier to be sent in assertion
    type: str
  nameidformat:
    choices:
      - Unspecified
      - emailAddress
      - X509SubjectName
      - WindowsDomainQualifiedName
      - kerberos
      - entity
      - persistent
      - transient
    description:
      - Format of Name Identifier sent in Assertion.
    type: str
    default: transient
  relaystaterule:
    description:
      - Expression to extract relaystate to be sent along with assertion. Evaluation
        of this expression should return TEXT content. This is typically a target
        url to which user is redirected after the recipient validates SAML token
    type: str
  samlissuername:
    description:
      - The name to be used in requests sent from Citrix ADC to IdP to uniquely identify
        Citrix ADC.
    type: str
  samlsigningcertname:
    description:
      - Name of the signing authority as given in the SAML server's SSL certificate.
    type: str
  samlspcertname:
    description:
      - Name of the SSL certificate of peer/receving party using which Assertion is
        encrypted.
    type: str
  sendpassword:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Option to send password in assertion.
    type: str
    default: 'OFF'
  signassertion:
    choices:
      - NONE
      - ASSERTION
      - RESPONSE
      - BOTH
    description:
      - Option to sign portions of assertion when Citrix ADC IDP sends one. Based
        on the user selection, either Assertion or Response or Both or none can be
        signed
    type: str
    default: ASSERTION
  signaturealg:
    choices:
      - RSA-SHA1
      - RSA-SHA256
    description:
      - Algorithm to be used to sign/verify SAML transactions
    type: str
    default: RSA-SHA256
  signatureservice:
    description:
      - Name of the service in cloud used to sign the data
    type: str
  skewtime:
    description:
      - This option specifies the number of minutes on either side of current time
        that the assertion would be valid. For example, if skewTime is 10, then assertion
        would be valid from (current time - 10) min to (current time + 10) min, ie
        20min in all.
    type: float
    default: 5
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