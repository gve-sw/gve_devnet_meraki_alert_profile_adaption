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

import json
import api as API

'''
Read file and return json data
'''
def get_json(filepath):
	with open(filepath, 'r') as f:
		jsondata = json.loads(f.read())
		f.close()
	return jsondata

'''
Class with defined future values and alert setting functions.
'''
class alertProfil:

    def __init__(self, default_recipients, gateway_alert_recipients, rouge_ap_alert_recipients, webhook_name, webhook_url, shared_secret):
        self.default_recipients = default_recipients
        self.gateway_alert_recipients = gateway_alert_recipients
        self.rouge_ap_alert_recipients = rouge_ap_alert_recipients
        self.webhook_name = webhook_name
        self.webhook_url = webhook_url
        self.shared_secret = shared_secret

    #Update `default recipients`, `A gateway becomes a repeater` and `A rouge AP is detected` settings
    def updateAlertRecipients(self, network_id, webhook_id):
        response = API.customAlerts(network_id, self.default_recipients, self.gateway_alert_recipients, self.rouge_ap_alert_recipients, webhook_id)
        return response

    #Create or update a webhook
    def updateWebhooks(self, network_id):
        #Webhook with same URL already present:
        available_webhooks = API.getNetworkWebhooks(network_id)
        for webhook in available_webhooks:
            if webhook['url'] == self.webhook_url:
                #if yes delete old Webhook
                response = API.updateWebhook(network_id, webhook['id'], self.webhook_name, self.shared_secret)
                return response
        #Webhook with same URL not present:
        response = API.createWebhook(network_id, self.webhook_name, self.webhook_url, self.shared_secret)
        return response


if __name__ == '__main__':

    print("-----------Read config file-------------")
    config_data = get_json('config.json')

    networks = config_data['networks']
    default_recipients = config_data['default_recipients']
    gateway_alert_recipients = config_data['gateway_alert_recipients']
    rouge_ap_alert_recipients = config_data['rouge_ap_alert_recipients']
    webhook_name = config_data['webhook_name']
    webhook_url = config_data['webhook_url']
    shared_secret = config_data['shared_secret']

    alert_profil = alertProfil(default_recipients, gateway_alert_recipients, rouge_ap_alert_recipients, webhook_name, webhook_url, shared_secret)
    
    for network_id in networks:
        print("Updating Network: " + str(network_id))
        response = alert_profil.updateWebhooks(network_id)
        webhook_id = response['id']
        response = alert_profil.updateAlertRecipients(network_id, webhook_id)

    print('Updating finished')