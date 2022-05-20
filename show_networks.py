#
# Copyright (c) 2022 Cisco and/or its affiliates.
# This software is licensed to you under the terms of the Cisco Sample
# Code License, Version 1.1 (the "License"). You may obtain a copy of the
# License at
#                https://developer.cisco.com/docs/licenses
# All use of the material herein must be in accordance with the terms of
# the License. All rights not expressly granted by the License are
# reserved. Unless required by applicable law or agreed to separately in
# writing, software distributed under the License is distributed on an "AS
# IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.
#

import api as API

def getOrgaAndNetworkOverview():
    print("-------------API enabled organizations and their networks-----------------")
    
    organizations = API.getOrganization()
    for orga in organizations:

        orga_name = orga['name']
        orga_id = orga['id']
        
        print("----------------------------------------------------------------------")
        print("ORGANIZATION:")
        print(str(orga_name) + ": " + str(orga_id))
        print("NETWORKS:")
        
        if orga['api']['enabled'] == True:

            networks = API.getNetworks(orga_id)
            for network in networks:

                network_name = network['name']
                network_id = network['id']
                
                print(str(network_name) + ": " + str(network_id))


if __name__ == '__main__':
    getOrgaAndNetworkOverview()
    