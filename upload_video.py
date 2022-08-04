import os

import videoindexer

from utils import get_avam_access_token

avam_subscription = os.environ['AVAM_SUBSCRIPTION']
avam_resource_group = os.environ['AVAM_RESOURCE_GROUP']
avam_account_name = os.environ['AVAM_ACCOUNT_NAME']
avam_account_id = os.environ['AVAM_ACCOUNT_ID']
avam_location = os.environ['AVAM_LOCATION']

avam_access_token = get_avam_access_token(
    avam_subscription,
    avam_resource_group,
    avam_account_name)

api_instance = videoindexer.IndexingApi()

api_instance.upload_video(
    location=avam_location,
    account_id=avam_account_id,
    access_token=avam_access_token,
    name="sample-30s.mp4",
    file_name='sample-30s.mp4',
    video_url='https://download.samplelib.com/mp4/sample-30s.mp4',
)
