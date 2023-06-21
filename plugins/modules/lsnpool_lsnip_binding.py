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
module: lsnpool_lsnip_binding
short_description: Binding Resource definition for describing association between
  lsnpool and lsnip resources
description: Binding Resource definition for describing association between lsnpool
  and lsnip resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  lsnip:
    description:
      - IPv4 address or a range of IPv4 addresses to be used as NAT IP address(es)
        for LSN.
      - 'After the pool is created, these IPv4 addresses are added to the Citrix ADC
        as Citrix ADC owned IP address of type LSN. A maximum of 4096 IP addresses
        can be bound to an LSN pool. An LSN IP address associated with an LSN pool
        cannot be shared with other LSN pools. IP addresses specified for this parameter
        must not already exist on the Citrix ADC as any Citrix ADC owned IP addresses.
        In the command line interface, separate the range with a hyphen. For example:
        10.102.29.30-10.102.29.189. You can later remove some or all the LSN IP addresses
        from the pool, and add IP addresses to the LSN pool.'
      - By default , arp is enabled on LSN IP address but, you can disable it using
        command - "set ns ip"
    type: str
  ownernode:
    description:
      - ID(s) of cluster node(s) on which command is to be executed
    type: int
  poolname:
    description:
      - 'Name for the LSN pool. Must begin with an ASCII alphanumeric or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
        Cannot be changed after the LSN pool is created. The following requirement
        applies only to the Citrix ADC CLI: If the name includes one or more spaces,
        enclose the name in double or single quotation marks (for example, "lsn pool1"
        or ''lsn pool1'').'
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