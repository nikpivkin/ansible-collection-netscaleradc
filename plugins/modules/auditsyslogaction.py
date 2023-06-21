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
module: auditsyslogaction
short_description: Configuration for system log action resource.
description: Configuration for system log action resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  acl:
    description:
      - Log access control list (ACL) messages.
    type: str
    choices:
      - ENABLED
      - DISABLED
  alg:
    description:
      - Log alg info
    type: str
    choices:
      - ENABLED
      - DISABLED
  appflowexport:
    description:
      - Export log messages to AppFlow collectors.
      - Appflow collectors are entities to which log messages can be sent so that
        some action can be performed on them.
    type: str
    choices:
      - ENABLED
      - DISABLED
  contentinspectionlog:
    description:
      - Log Content Inspection event information
    type: str
    choices:
      - ENABLED
      - DISABLED
  dateformat:
    description:
      - Format of dates in the logs.
      - 'Supported formats are: '
      - '* MMDDYYYY. -U.S. style month/date/year format.'
      - '* DDMMYYYY - European style date/month/year format.'
      - '* YYYYMMDD - ISO style year/month/date format.'
    type: str
    choices:
      - MMDDYYYY
      - DDMMYYYY
      - YYYYMMDD
  dns:
    description:
      - Log DNS related syslog messages
    type: str
    choices:
      - ENABLED
      - DISABLED
  domainresolvenow:
    description:
      - Immediately send a DNS query to resolve the server's domain name.
    type: bool
  domainresolveretry:
    description:
      - Time, in seconds, for which the Citrix ADC waits before sending another DNS
        query to resolve the host name of the syslog server if the last query failed.
    type: int
    default: 5
  lbvservername:
    description:
      - Name of the LB vserver. Mutually exclusive with syslog serverIP/serverName
    type: str
  logfacility:
    description:
      - 'Facility value, as defined in RFC 3164, assigned to the log message. '
      - Log facility values are numbers 0 to 7 (LOCAL0 through LOCAL7). Each number
        indicates where a specific message originated from, such as the Citrix ADC
        itself, the VPN, or external.
    type: str
    choices:
      - LOCAL0
      - LOCAL1
      - LOCAL2
      - LOCAL3
      - LOCAL4
      - LOCAL5
      - LOCAL6
      - LOCAL7
  loglevel:
    description:
      - 'Audit log level, which specifies the types of events to log. '
      - 'Available values function as follows: '
      - '* ALL - All events.'
      - '* EMERGENCY - Events that indicate an immediate crisis on the server.'
      - '* ALERT - Events that might require action.'
      - '* CRITICAL - Events that indicate an imminent server crisis.'
      - '* ERROR - Events that indicate some type of error.'
      - '* WARNING - Events that require action in the near future.'
      - '* NOTICE - Events that the administrator should know about.'
      - '* INFORMATIONAL - All but low-level events.'
      - '* DEBUG - All events, in extreme detail.'
      - '* NONE - No events.'
    type: list
    elements: str
    choices:
      - ALL
      - EMERGENCY
      - ALERT
      - CRITICAL
      - ERROR
      - WARNING
      - NOTICE
      - INFORMATIONAL
      - DEBUG
      - NONE
  lsn:
    description:
      - Log lsn info
    type: str
    choices:
      - ENABLED
      - DISABLED
  maxlogdatasizetohold:
    description:
      - Max size of log data that can be held in NSB chain of server info.
    type: int
    default: 500
  name:
    description:
      - Name of the syslog action. Must begin with a letter, number, or the underscore
        character (_), and must contain only letters, numbers, and the hyphen (-),
        period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore
        characters. Cannot be changed after the syslog action is added.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my syslog action" or 'my syslog action').
    type: str
  netprofile:
    description:
      - Name of the network profile.
      - The SNIP configured in the network profile will be used as source IP while
        sending log messages.
    type: str
  serverdomainname:
    description:
      - SYSLOG server name as a FQDN.  Mutually exclusive with serverIP/lbVserverName
    type: str
  serverip:
    description:
      - IP address of the syslog server.
    type: str
  serverport:
    description:
      - Port on which the syslog server accepts connections.
    type: int
  sslinterception:
    description:
      - Log SSL Interception event information
    type: str
    choices:
      - ENABLED
      - DISABLED
  subscriberlog:
    description:
      - Log subscriber session event information
    type: str
    choices:
      - ENABLED
      - DISABLED
  tcp:
    description:
      - Log TCP messages.
    type: str
    choices:
      - NONE
      - ALL
  tcpprofilename:
    description:
      - Name of the TCP profile whose settings are to be applied to the audit server
        info to tune the TCP connection parameters.
    type: str
  timezone:
    description:
      - 'Time zone used for date and timestamps in the logs. '
      - 'Supported settings are: '
      - '* GMT_TIME. Coordinated Universal time.'
      - '* LOCAL_TIME. Use the server''s timezone setting.'
    type: str
    choices:
      - GMT_TIME
      - LOCAL_TIME
  transport:
    description:
      - Transport type used to send auditlogs to syslog server. Default type is UDP.
    type: str
    choices:
      - TCP
      - UDP
  urlfiltering:
    description:
      - Log URL filtering event information
    type: str
    choices:
      - ENABLED
      - DISABLED
  userdefinedauditlog:
    description:
      - 'Log user-configurable log messages to syslog. '
      - Setting this parameter to NO causes auditing to ignore all user-configured
        message actions. Setting this parameter to YES causes auditing to log user-configured
        message actions that meet the other logging criteria.
    type: str
    choices:
      - true
      - false
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
