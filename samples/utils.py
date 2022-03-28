import json

import requests
from azure.identity import DefaultAzureCredential


def get_avam_access_token(subscription, resource_group, account_name):
    """Retrieve an AVAM access token using the ARM API."""
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


def download_file(url, local_filename, chunk_size=1024*1024):
    """Download a file using requests. Default chunk size 1MB."""
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size):
                f.write(chunk)


def list_all_videos(api_instance, location, account_id, access_token, page_size=100): # noqa
    """List all videos, using the API paging mechanism.
    The default page_size is set to 100 (the API default is 25).
    """
    done = False
    skip = 0

    all_videos = []

    while not done:
        list_videos = api_instance.list_videos(
            location=location,
            account_id=account_id,
            access_token=access_token,
            page_size=page_size,
            skip=skip)

        all_videos += list_videos['results']

        page_size = list_videos['nextPage']['pageSize']
        skip = list_videos['nextPage']['skip']
        done = list_videos['nextPage']['done']

    return all_videos
