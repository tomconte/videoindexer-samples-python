import json
import os
import zipfile

import azure.videoindexer

from utils import get_avam_access_token, download_file

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

api_instance = azure.videoindexer.VideosApi()

list_videos = api_instance.list_videos(
    location=avam_location,
    account_id=avam_account_id,
    access_token=avam_access_token,
    page_size=100)

# For each video, download the corresponding keyframe thumbnails
# Each thumbnails zip file is named `{video_name}__{video_id}.zip`
# The thumbnails are extracted in a directory named `{video_name}__{video_id}`

for video in list_videos['results']:
    video_name = video['name']
    video_id = video['id']

    print(f"Processing {video_name} ...")
    artifact_url = api_instance.get_video_artifact_download_url(
        location=avam_location,
        account_id=avam_account_id,
        access_token=avam_access_token,
        video_id=video_id,
        type='KeyframesThumbnails')

    # Get the artifact URL from AVAM
    print(f"Downloading {artifact_url} ...")

    # Extract the file name from the URL
    zipfile_name = video_name + '__' + video_id + '.zip'

    # Download the file locally
    download_file(artifact_url, zipfile_name)

    # Unzip in a new directory
    target_dir = zipfile_name[0:-4]
    print(f"Extracting {zipfile_name} into {target_dir} ...")

    os.mkdir(target_dir)

    with zipfile.ZipFile(zipfile_name, "r") as zip_ref:
        zip_ref.extractall(target_dir)
