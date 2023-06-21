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
module: lsnappsprofile
short_description: Configuration for LSN Application Profile resource.
description: Configuration for LSN Application Profile resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  appsprofilename:
    description:
      - 'Name for the LSN application profile. Must begin with an ASCII alphanumeric
        or underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
        characters. Cannot be changed after the LSN application profile is created.
        The following requirement applies only to the Citrix ADC CLI: If the name
        includes one or more spaces, enclose the name in double or single quotation
        marks (for example, "lsn application profile1" or ''lsn application profile1'').'
    type: str
  filtering:
    description:
      - Type of filter to apply to packets originating from external hosts.
      - ''
      - Consider an example of an LSN mapping that includes the mapping of subscriber
        IP:port (X:x), NAT IP:port (N:n), and external host IP:port (Y:y).
      - ''
      - 'Available options function as follows:'
      - '* ENDPOINT INDEPENDENT - Filters out only packets not destined to the subscriber
        IP address and port X:x, regardless of the external host IP address and port
        source (Z:z).  The Citrix ADC forwards any packets destined to X:x.  In other
        words, sending packets from the subscriber to any external IP address is sufficient
        to allow packets from any external hosts to the subscriber.'
      - ''
      - '* ADDRESS DEPENDENT - Filters out packets not destined to subscriber IP address
        and port X:x.  In addition, the ADC filters out packets from Y:y destined
        for the subscriber (X:x) if the client has not previously sent packets to
        Y:anyport (external port independent). In other words, receiving packets from
        a specific external host requires that the subscriber first send packets to
        that specific external host''s IP address.'
      - ''
      - '* ADDRESS PORT DEPENDENT (the default) - Filters out  packets not destined
        to subscriber IP address and port (X:x).  In addition, the Citrix ADC filters
        out packets from Y:y destined for the subscriber (X:x) if the subscriber has
        not previously sent packets to Y:y.  In other words, receiving packets from
        a specific external host requires that the subscriber first send packets first
        to that external IP address and port.'
    type: str
    default: ADDRESS-PORT-DEPENDENT
    choices:
      - ENDPOINT-INDEPENDENT
      - ADDRESS-DEPENDENT
      - ADDRESS-PORT-DEPENDENT
  ippooling:
    description:
      - NAT IP address allocation options for sessions associated with the same subscriber.
      - ''
      - 'Available options function as follows:'
      - '* Paired - The Citrix ADC allocates the same NAT IP address for all sessions
        associated with the same subscriber. When all the ports of a NAT IP address
        are used in LSN sessions (for same or multiple subscribers), the Citrix ADC
        ADC drops any new connection from the subscriber.'
      - '* Random - The Citrix ADC allocates random NAT IP addresses, from the pool,
        for different sessions associated with the same subscriber.'
      - ''
      - This parameter is applicable to dynamic NAT allocation only.
    type: str
    default: RANDOM
    choices:
      - PAIRED
      - RANDOM
  l2info:
    description:
      - Enable l2info by creating natpcbs for LSN, which enables the Citrix ADC to
        use L2CONN/MBF with LSN.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  mapping:
    description:
      - Type of LSN mapping to apply to subsequent packets originating from the same
        subscriber IP address and port.
      - ''
      - Consider an example of an LSN mapping that includes the mapping of the subscriber
        IP:port (X:x), NAT IP:port (N:n), and external host IP:port (Y:y).
      - ''
      - 'Available options function as follows: '
      - ''
      - '* ENDPOINT-INDEPENDENT - Reuse the LSN mapping for subsequent packets sent
        from the same subscriber IP address and port (X:x) to any external IP address
        and port. '
      - ''
      - '* ADDRESS-DEPENDENT - Reuse the LSN mapping for subsequent packets sent from
        the same subscriber IP address and port (X:x) to the same external IP address
        (Y), regardless of the external port.'
      - ''
      - '* ADDRESS-PORT-DEPENDENT - Reuse the LSN mapping for subsequent packets sent
        from the same internal IP address and port (X:x) to the same external IP address
        and port (Y:y) while the mapping is still active.'
    type: str
    default: ADDRESS-PORT-DEPENDENT
    choices:
      - ENDPOINT-INDEPENDENT
      - ADDRESS-DEPENDENT
      - ADDRESS-PORT-DEPENDENT
  tcpproxy:
    description:
      - Enable TCP proxy, which enables the Citrix ADC to optimize the  TCP traffic
        by using Layer 4 features.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  td:
    description:
      - 'ID of the traffic domain through which the Citrix ADC sends the outbound
        traffic after performing LSN. '
      - ''
      - If you do not specify an ID, the ADC sends the outbound traffic through the
        default traffic domain, which has an ID of 0.
    type: int
    default: 4095
  transportprotocol:
    description:
      - Name of the protocol for which the parameters of this LSN application profile
        applies.
    type: str
    choices:
      - TCP
      - UDP
      - ICMP
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
