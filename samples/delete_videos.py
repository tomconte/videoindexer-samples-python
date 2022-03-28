import os
import sys

import azure.videoindexer

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

# Parse arguments

if len(sys.argv) < 2:
    print(f"usage: {sys.argv[0]} <string to match in video name>")
    sys.exit(1)
else:
    string_to_match = sys.argv[1]
    print(f"this will delete all video with name matching '{string_to_match}'")
    print("are you sure? type YES in uppercase to confirm")
    confirm = input()
    if confirm != 'YES':
        sys.exit(1)

# Call the AVAM API

api_instance = azure.videoindexer.VideosApi()

list_videos = list_all_videos(
    api_instance=api_instance,
    location=avam_location,
    account_id=avam_account_id,
    access_token=avam_access_token)

for i in list_videos:
    video_name = i['name']
    video_id = i['id']
    if string_to_match in video_name:
        print('deleting', video_id, video_name)
        api_instance.delete_video(
            location=avam_location,
            account_id=avam_account_id,
            access_token=avam_access_token,
            video_id=video_id)
