# gve_devnet_meraki_alert_profile_adaption
The purpose of this sample code is to ease the adaption of the alert and webhook settings for multiple networks.
It allows defining the values for a webhook, the `default recipients`, `A gateway becomes a repeater` and `A rouge AP is detected` alert. The defined values get automatically deployed in multiple networks by running the script.

## Contacts
* Ramona Renner

## Solution Components
* Meraki Dashboard API
* Meraki Environment with 1 or more networks and writing permissions for the following page: `Network-wide > Configure:Alerts`

## Workflow

![/IMAGES/giturl.png](/IMAGES/workflow.png)

The sample code does the following in the background via RESTful API endpoints:

* Creates a new webhook or updates an available webhook with the same URL. Other beforehand available webhooks are not modified or deleted. The `Meraki included` template is used.
* Updates the list of `default recipients`. Only the recipients defined in the configuration file for this script are present after execution. The mentioned webhook is automatically added as default recipient.
* Selects the alert checkbox and updates the recipients as defined in the configuration file for the `A gateway becomes a repeater` and `A rouge AP is detected` option. Recipients other than the beforehand defined values are removed. Other alert options are not modified or deleted.

## Prerequisites
#### Meraki API Keys
In order to use the Meraki API, you need to enable the API for your organization first. After enabling API access, you can generate an API key. Follow these instructions to enable API access and generate an API key:
1. Login to the Meraki dashboard
2. In the left-hand menu, navigate to `Organization > Settings > Dashboard API access`
3. Click on `Enable access to the Cisco Meraki Dashboard API`
4. Go to `My Profile > API access`
5. Under API access, click on `Generate API key`
6. Save the API key in a safe place. The API key will only be shown once for security purposes, so it is very important to take note of the key then. In case you lose the key, you have to revoke the key and generate a new key. Moreover, there is a limit of only two API keys per profile.

> For more information on how to generate an API key, please click [here](https://developer.cisco.com/meraki/api-v1/#!authorization/authorization). 

> Note: You can add your account as Full Organization Admin to your organizations by following the instructions [here](https://documentation.meraki.com/General_Administration/Managing_Dashboard_Access/Managing_Dashboard_Administrators_and_Permissions).


## Installation/Configuration
1. Make sure Python 3 and Git is installed in your environment, and if not, you may download Python 3 [here](https://www.python.org/downloads/) and Git as described [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
2. Create and activate a virtual environment for the project ([Instructions](https://docs.python.org/3/tutorial/venv.html)).
3. Access the created virtual environment folder
    ```
    cd [add name of virtual environment here] 
    ```
4. Clone this Github repository:  
  ```git clone [add github link here]```
  * For Github link: 
      In Github, click on the **Clone or download** button in the upper part of the page > click the **copy icon**  
      ![/IMAGES/giturl.png](/IMAGES/giturl.png)
  * Or simply download the repository as zip file using 'Download ZIP' button and extract it
4. Access the downloaded folder:  
    ```cd gve_devnet_meraki_alert_profile_adaption```

5. Install all dependencies:  
  ```pip3 install -r requirements.txt```

6. Fill in the Meraki API key in the `.env` file
```python
MERAKI_DASHBOARD_API_KEY="API key goes here"
```
> Note: Mac OS hides the .env file in the finder by default. View the demo folder for example with your preferred IDE to make the file visible.

> Note: Windows doesn't download the .env file via the git clone command. Create e.g. a new .env file in the project root folder in this case.

7. Define the networks to update and preferred other future field values in the `config.json` file:
```
"networks":["Network 1 ID goes here","Network 2 ID goes here", ...],
"default_recipients":["Recipient 1 goes here", "Recipient 2 goes here", ...],
"rouge_ap_alert_recipients":["Recipient 1 goes here", "Recipient 2 goes here", ...],
"gateway_alert_recipients":["Recipient 1 goes here", "Recipient 2 goes here", ...],
"webhook_name":"Webhook name goes here",
"webhook_url":"Webhook url goes here (starting with https://)",
"shared_secret":"Webhook secret goes here"
```

> The helper script `show_networks.py` can help to fill in the networks IDs in the above list. Run `python3 show_networks.py` to view the IDs of all networks of API enabled organizations associated to an API key.

## Usage

Run the script by using the command:
```
python3 update_alert_profiles.py
```

Check the applied changes by accessing the alert profile page under `Network-wide`>`Configure:Alerts` for all updated networks.


# Screenshots
## Output for 'python3 show_networks.py' Script:
![/IMAGES/0image.png](/IMAGES/show_networks.png)

## Output and Result for 'python3 update_alert_profiles.py' Script:
### Before Script Execution
![/IMAGES/0image.png](/IMAGES/update_before.png)
### After Script Execution
![/IMAGES/0image.png](/IMAGES/update_after.png)


## LICENSE
Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

## CODE_OF_CONDUCT
Our code of conduct is available [here](CODE_OF_CONDUCT.md)

## CONTRIBUTING
See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not      responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.

