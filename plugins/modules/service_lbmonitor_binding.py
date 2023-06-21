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
module: service_lbmonitor_binding
short_description: Binding Resource definition for describing association between
  service and lbmonitor resources
description: Binding Resource definition for describing association between service
  and lbmonitor resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  monitor_name:
    description:
      - The monitor Names.
    type: str
  monstate:
    description:
      - The configured state (enable/disable) of the monitor on this server.
    type: str
    choices:
      - ENABLED
      - DISABLED
  name:
    description:
      - Name of the service to which to bind a monitor.
    type: str
  passive:
    description:
      - Indicates if load monitor is passive. A passive load monitor does not remove
        service from LB decision when threshold is breached.
    type: bool
  weight:
    description:
      - Weight to assign to the monitor-service binding. When a monitor is UP, the
        weight assigned to its binding with the service determines how much the monitor
        contributes toward keeping the health of the service above the value configured
        for the Monitor Threshold parameter.
    type: int
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
