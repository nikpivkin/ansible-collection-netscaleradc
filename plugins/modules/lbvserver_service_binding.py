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
module: lbvserver_service_binding
short_description: Binding Resource definition for describing association between
  lbvserver and service resources
description: Binding Resource definition for describing association between lbvserver
  and service resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  name:
    description:
      - Name for the virtual server. Must begin with an ASCII alphanumeric or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen
        (-) characters. Can be changed after the virtual server is created.
      - ''
      - 'CLI Users: If the name includes one or more spaces, enclose the name in double
        or single quotation marks (for example, "my vserver" or ''my vserver'').'
    type: str
  order:
    description:
      - Order number to be assigned to the service when it is bound to the lb vserver.
    type: float
  servicegroupname:
    description:
      - Name of the service group.
    type: str
  servicename:
    description:
      - Service to bind to the virtual server.
    type: str
  weight:
    description:
      - Weight to assign to the specified service.
    type: float
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---

- name: Simple lbvserver_service_binding playbook
  hosts: demo_netscalers

  gather_facts: false

  tasks:
    - name: Sample Task | lbvserver_service_binding
      delegate_to: localhost
      netscaler.adc.lbvserver_service_binding:
        # nsip: 10.0.0.1 # This can also be given via NETSCALER_NSIP environment variable
        # nitro_user: nitrouser # This can also be given via NETSCALER_NITRO_USER environment variable
        # nitro_pass: verysecretpassword # This can also be given via NETSCALER_NITRO_PASS environment variable
        # nitro_protocol: https # This can also be given via NETSCALER_NITRO_PROTOCOL environment variable
        # validate_certs: false # This can also be given via NETSCALER_VALIDATE_CERTS environment variable
        # save_config: false # This can also be given via NETSCALER_SAVE_CONFIG environment variable

        state: present

        name: test_lbvser
        servicename: s1
        weight: 16

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