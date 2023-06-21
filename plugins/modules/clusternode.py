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
module: clusternode
short_description: Configuration for cluster node resource.
description: Configuration for cluster node resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  backplane:
    description:
      - Interface through which the node communicates with the other nodes in the
        cluster. Must be specified in the three-tuple form n/c/u, where n represents
        the node ID and c/u refers to the interface on the appliance.
    type: str
  clearnodegroupconfig:
    description:
      - Option to remove nodegroup config
    type: str
    default: true
    choices:
      - true
      - false
  delay:
    description:
      - Applicable for Passive node and node becomes passive after this timeout (in
        minutes)
    type: int
  ipaddress:
    description:
      - Citrix ADC IP (NSIP) address of the appliance to add to the cluster. Must
        be an IPv4 address.
    type: str
  nodegroup:
    description:
      - The default node group in a Cluster system.
    type: str
    default: DEFAULT_NG
  nodeid:
    description:
      - Unique number that identifies the cluster node.
    type: int
  priority:
    description:
      - Preference for selecting a node as the configuration coordinator. The node
        with the lowest priority value is selected as the configuration coordinator.
      - When the current configuration coordinator goes down, the node with the next
        lowest priority is made the new configuration coordinator. When the original
        node comes back up, it will preempt the new configuration coordinator and
        take over as the configuration coordinator.
      - 'Note: When priority is not configured for any of the nodes or if multiple
        nodes have the same priority, the cluster elects one of the nodes as the configuration
        coordinator.'
    type: int
    default: 31
  state:
    description:
      - 'Admin state of the cluster node. The available settings function as follows:'
      - ACTIVE - The node serves traffic.
      - SPARE - The node does not serve traffic unless an ACTIVE node goes down.
      - PASSIVE - The node does not serve traffic, unless you change its state. PASSIVE
        state is useful during temporary maintenance activities in which you want
        the node to take part in the consensus protocol but not to serve traffic.
    type: str
    default: PASSIVE
    choices:
      - ACTIVE
      - SPARE
      - PASSIVE
  tunnelmode:
    description:
      - To set the tunnel mode
    type: str
    default: NONE
    choices:
      - NONE
      - GRE
      - UDP
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
