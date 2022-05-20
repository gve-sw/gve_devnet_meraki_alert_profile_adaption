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

import meraki
from dotenv import load_dotenv
import os

load_dotenv()

base_url = "https://api.meraki.com/api/v1"

DASHBOARD = meraki.DashboardAPI(
            api_key=os.environ['MERAKI_DASHBOARD_API_KEY'],
            base_url=base_url,
            print_console=False)


#API calls
'''
Organizations
'''
def getOrganization():
    try:
        response = DASHBOARD.organizations.getOrganizations()

        return response

    except meraki.APIError as e:
        print(f'{e.reason} ({e.status}) - {e.message}')
    except Exception as e:
        print(f'some other error: {e}')

'''
Networks
'''
def getNetworks(orgID):
    try:
        response = DASHBOARD.organizations.getOrganizationNetworks(
            orgID, total_pages='all'
        )

        return response
    
    except meraki.APIError as e:
        print(f'{e.reason} ({e.status}) - {e.message}')
    except Exception as e:
        print(f'some other error: {e}')

'''
Webhooks
'''
def getNetworkWebhooks(network_id):
    try:
        response = DASHBOARD.networks.getNetworkWebhooksHttpServers(
            network_id
        )

        return response

    except meraki.APIError as e:
        print(f'{e.reason} ({e.status}) - {e.message}')
    except Exception as e:
        print(f'some other error: {e}')


def updateWebhook(network_id, http_server_id, webhook_name, shared_secret):
    try:
        response = DASHBOARD.networks.updateNetworkWebhooksHttpServer(
            network_id, http_server_id, 
            name=webhook_name, 
            sharedSecret=shared_secret, 
            payloadTemplate={'payloadTemplateId': 'wpt_00001', 'name': 'Meraki (included)'}
        )

        return response

    except meraki.APIError as e:
        print(f'{e.reason} ({e.status}) - {e.message}')
    except Exception as e:
        print(f'some other error: {e}')


def createWebhook(network_id, name, url, sharedSecret):
    try:
        response = DASHBOARD.networks.createNetworkWebhooksHttpServer(
            network_id, name, url, 
            sharedSecret=sharedSecret, 
            payloadTemplate={'payloadTemplateId': 'wpt_00001', 'name': 'Meraki (included)'}
        )
        return response
    
    except meraki.APIError as e:
        print(f'{e.reason} ({e.status}) - {e.message}')
    except Exception as e:
        print(f'some other error: {e}')

'''
Alert Settings
'''
def customAlerts(network_id, default_recipients, gateway_alert_recipients, rouge_ap_alert_recipients, webhook_id):
    try:
        defaultDestinations = {
            'emails': default_recipients, 
            'allAdmins': False, 
            'snmp': False, 
            'httpServerIds': [webhook_id]} 

        alerts = [{
            'type': 'gatewayToRepeater', 
            'enabled': True, 
            'alertDestinations': 
                {'emails': gateway_alert_recipients, 
                'allAdmins': False, 
                'snmp': False, 
                'httpServerIds': []
                }, 
            'filters': {}
            },{
            "type": "rogueAp",
            "enabled": True,
            "alertDestinations": {
                "emails": rouge_ap_alert_recipients,
                "snmp": False,
                "allAdmins": False,
                "httpServerIds": []
            },
            "filters": {}
            }]

        response = DASHBOARD.networks.updateNetworkAlertsSettings(
            network_id, 
            defaultDestinations=defaultDestinations,
            alerts=alerts
        )

        return response
    
    except meraki.APIError as e:
        print(f'{e.reason} ({e.status}) - {e.message}')
    except Exception as e:
        print(f'some other error: {e}')
