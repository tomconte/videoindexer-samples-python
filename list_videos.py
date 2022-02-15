import json
import os

import azure.videoindexer

from utils import get_avam_access_token

avam_subscription = os.environ['AVAM_SUBSCRIPTION']
avam_resource_group = os.environ['AVAM_RESOURCE_GROUP']
avam_account_name = os.environ['AVAM_ACCOUNT_NAME']
avam_account_id = os.environ['AVAM_ACCOUNT_ID']
avam_location = os.environ['AVAM_LOCATION']

# Retrieve an AVAM access token

avam_access_token = get_avam_access_token(
    avam_subscription,
    avam_resource_group,
    avam_account_name)

# Call the AVAM API

api_instance = azure.videoindexer.VideosApi()

list_videos_response = api_instance.list_videos(
    location=avam_location,
    account_id=avam_account_id,
    access_token=avam_access_token,
    page_size=1000,
    _preload_content=False)

list_videos = json.loads(list_videos_response.read())

for i in list_videos['results']:
    print(i['name'])
