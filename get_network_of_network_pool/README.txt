INTRODUCTION:
------------

This module contains script files to get network of network pools.

REQUIREMENTS:
------------

This module requires the following modules:

 * Python 2.7.x
   Libraries
  * requests
  * sys
  * json
  * time

 * The scripts must be run outside sddc-manager environment.

 * DNS resolution must be done for sddc-manager.


PREREQUSITES:
-------------

The following data is required

ID of the network


USAGE:
-----
Usage:	python get_network_of_network_pools.py <hostname> <username> <password> <network pool ID> <network ID>
