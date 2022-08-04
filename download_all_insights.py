"""Download all the JSON insights from a Video Indexer account."""

import json
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

# Retrieve a list of all videos

video_api_instance = videoindexer.VideosApi()
index_api_instance = videoindexer.IndexingApi()

list_videos = list_all_videos(
    api_instance=video_api_instance,
    location=avam_location,
    account_id=avam_account_id,
    access_token=avam_access_token)

# For each video, download the corresponding insights JSON file

for video in list_videos:
    video_name = video['name']
    video_id = video['id']

    insights = index_api_instance.get_video_index(
        location=avam_location,
        account_id=avam_account_id,
        access_token=avam_access_token,
        video_id=video_id)

    # Assemble file name
    insights_file_name = video_name + '__' + video_id + '.json'

    # Get the insights JSON document
    print(f"Downloading {video_name} insights ...")

    with open(insights_file_name, 'w') as f:
        json.dump(insights, f)
