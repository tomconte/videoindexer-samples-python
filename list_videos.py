#!/usr/bin/env python
import os

import videoindexer

from utils import get_avam_access_token, list_all_videos

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

api_instance = videoindexer.VideosApi()

list_videos = list_all_videos(
    api_instance=api_instance,
    location=avam_location,
    account_id=avam_account_id,
    access_token=avam_access_token)

for i in list_videos:
    print(i['name'], i['state'], i['processingProgress'])
