import json

import requests
from azure.identity import DefaultAzureCredential


def get_avam_access_token(subscription, resource_group, account_name):
    azure_cred = DefaultAzureCredential()
    arm_token = azure_cred.get_token('https://management.azure.com/.default')

    params = {
        'permissionType': 'Contributor',
        'scope': 'Account'
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + arm_token.token
    }

    access_token_req = requests.post(
        f"https://management.azure.com/subscriptions/{subscription}/resourceGroups/{resource_group}/providers/Microsoft.VideoIndexer/accounts/{account_name}/generateAccessToken?api-version=2021-11-10-preview", # noqa
        data=json.dumps(params),
        headers=headers
    )

    return access_token_req.json()['accessToken']
