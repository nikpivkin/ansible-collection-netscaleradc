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
module: botprofile_ipreputation_binding
short_description: Binding Resource definition for describing association between
  botprofile and ipreputation resources
description: Binding Resource definition for describing association between botprofile
  and ipreputation resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  bot_bind_comment:
    description:
      - Any comments about this binding.
    type: str
  bot_iprep_action:
    description:
      - One or more actions to be taken if bot is detected based on this IP Reputation
        binding. Only LOG action can be combinded with DROP, RESET, REDIRECT or MITIGATION
        action.
    type: list
    elements: str
    default: NONE
    choices:
      - NONE
      - LOG
      - DROP
      - REDIRECT
      - RESET
      - MITIGATION
  bot_iprep_enabled:
    description:
      - Enabled or disabled IP-repuation binding.
    type: str
    choices:
      - true
      - false
  bot_ipreputation:
    description:
      - IP reputation binding. For each category, only one binding is allowed. To
        update the values of an existing binding, user has to first unbind that binding,
        and then needs to bind again with the new values.
    type: bool
  category:
    description:
      - 'IP Repuation category. Following IP Reuputation categories are allowed:'
      - '*IP_BASED - This category checks whether client IP is malicious or not.'
      - '*BOTNET - This category includes Botnet C&C channels, and infected zombie
        machines controlled by Bot master.'
      - '*SPAM_SOURCES - This category includes tunneling spam messages through a
        proxy, anomalous SMTP activities, and forum spam activities.'
      - '*SCANNERS - This category includes all reconnaissance such as probes, host
        scan, domain scan, and password brute force attack.'
      - '*DOS - This category includes DOS, DDOS, anomalous sync flood, and anomalous
        traffic detection.'
      - '*REPUTATION - This category denies access from IP addresses currently known
        to be infected with malware. This category also includes IPs with average
        low Webroot Reputation Index score. Enabling this category will prevent access
        from sources identified to contact malware distribution points.'
      - '*PHISHING - This category includes IP addresses hosting phishing sites and
        other kinds of fraud activities such as ad click fraud or gaming fraud.'
      - '*PROXY - This category includes IP addresses providing proxy services.'
      - '*NETWORK - IPs providing proxy and anonymization services including The Onion
        Router aka TOR or darknet.'
      - '*MOBILE_THREATS - This category checks client IP with the list of IPs harmful
        for mobile devices.'
      - '*WINDOWS_EXPLOITS - This category includes active IP address offering or
        distributig malware, shell code, rootkits, worms or viruses.'
      - '*WEB_ATTACKS - This category includes cross site scripting, iFrame injection,
        SQL injection, cross domain injection or domain password brute force attack.'
      - '*TOR_PROXY - This category includes IP address acting as exit nodes for the
        Tor Network.'
      - '*CLOUD - This category checks client IP with list of public cloud IPs.'
      - '*CLOUD_AWS - This category checks client IP with list of public cloud IPs
        from Amazon Web Services.'
      - '*CLOUD_GCP - This category checks client IP with list of public cloud IPs
        from Google Cloud Platform.'
      - '*CLOUD_AZURE - This category checks client IP with list of public cloud IPs
        from Azure.'
      - '*CLOUD_ORACLE - This category checks client IP with list of public cloud
        IPs from Oracle.'
      - '*CLOUD_IBM - This category checks client IP with list of public cloud IPs
        from IBM.'
      - '*CLOUD_SALESFORCE - This category checks client IP with list of public cloud
        IPs from Salesforce.'
    type: str
    choices:
      - IP
      - BOTNETS
      - SPAM_SOURCES
      - SCANNERS
      - DOS
      - REPUTATION
      - PHISHING
      - PROXY
      - NETWORK
      - MOBILE_THREATS
      - WINDOWS_EXPLOITS
      - WEB_ATTACKS
      - TOR_PROXY
      - CLOUD
      - CLOUD_AWS
      - CLOUD_GCP
      - CLOUD_AZURE
      - CLOUD_ORACLE
      - CLOUD_IBM
      - CLOUD_SALESFORCE
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