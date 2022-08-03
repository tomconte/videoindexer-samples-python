# videoindexer.VideosApi

All URIs are relative to *https://api.videoindexer.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_video**](VideosApi.md#delete_video) | **DELETE** /{location}/Accounts/{accountId}/Videos/{videoId} | Delete Video
[**delete_video_face**](VideosApi.md#delete_video_face) | **DELETE** /{location}/Accounts/{accountId}/Videos/{videoId}/Index/Faces/{faceId} | Delete Video Face
[**delete_video_source_file**](VideosApi.md#delete_video_source_file) | **DELETE** /{location}/Accounts/{accountId}/Videos/{videoId}/SourceFile | Delete Video Source File
[**get_video_artifact_download_url**](VideosApi.md#get_video_artifact_download_url) | **GET** /{location}/Accounts/{accountId}/Videos/{videoId}/ArtifactUrl | Get Video Artifact Download Url
[**get_video_captions**](VideosApi.md#get_video_captions) | **GET** /{location}/Accounts/{accountId}/Videos/{videoId}/Captions | Get Video Captions
[**get_video_id_by_external_id**](VideosApi.md#get_video_id_by_external_id) | **GET** /{location}/Accounts/{accountId}/Videos/GetIdByExternalId | Get Video Id By External Id
[**get_video_source_file_download_url**](VideosApi.md#get_video_source_file_download_url) | **GET** /{location}/Accounts/{accountId}/Videos/{videoId}/SourceFile/DownloadUrl | Get Video Source File Download Url
[**get_video_streaming_url**](VideosApi.md#get_video_streaming_url) | **GET** /{location}/Accounts/{accountId}/Videos/{videoId}/streaming-url | Get Video Streaming URL
[**get_video_thumbnail**](VideosApi.md#get_video_thumbnail) | **GET** /{location}/Accounts/{accountId}/Videos/{videoId}/Thumbnails/{thumbnailId} | Get Video Thumbnail
[**list_videos**](VideosApi.md#list_videos) | **GET** /{location}/Accounts/{accountId}/Videos | List Videos
[**search_videos**](VideosApi.md#search_videos) | **GET** /{location}/Accounts/{accountId}/Videos/Search | Search Videos
[**update_video_face**](VideosApi.md#update_video_face) | **PUT** /{location}/Accounts/{accountId}/Videos/{videoId}/Index/Faces/{faceId} | Update Video Face
[**update_video_index**](VideosApi.md#update_video_index) | **PATCH** /{location}/Accounts/{accountId}/Videos/{videoId}/Index | Update Video Index
[**update_video_transcript**](VideosApi.md#update_video_transcript) | **PUT** /{location}/Accounts/{accountId}/Videos/{videoId}/Index/Transcript | Update Video Transcript

# **delete_video**
> object delete_video(location, account_id, video_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Delete Video

Deletes the specified video and all related insights created from when the video was indexed

### Example
```python
from __future__ import print_function
import time
import videoindexer
from videoindexer.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = videoindexer.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = videoindexer.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = videoindexer.VideosApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
video_id = 'video_id_example' # str | The video id
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account/Video</b> and permission should be <b>Contributor</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Delete Video
    api_response = api_instance.delete_video(location, account_id, video_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->delete_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **video_id** | **str**| The video id | 
 **access_token** | **str**| Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be &lt;b&gt;Account/Video&lt;/b&gt; and permission should be &lt;b&gt;Contributor&lt;/b&gt;.&lt;br&gt;  Note that Access tokens expire within 1 hour&lt;br&gt; See more details for &lt;b&gt;Classic Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/DocsObtainAccessToken target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;, for &lt;b&gt;ARM Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/vi-classic-access-token target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

**object**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_video_face**
> delete_video_face(location, account_id, video_id, face_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Delete Video Face

Delete Video Face.

### Example
```python
from __future__ import print_function
import time
import videoindexer
from videoindexer.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = videoindexer.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = videoindexer.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = videoindexer.VideosApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
video_id = 'video_id_example' # str | The video id
face_id = 56 # int | Format - int32. The face id to delete
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account/Video</b> and permission should be <b>Contributor</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Delete Video Face
    api_instance.delete_video_face(location, account_id, video_id, face_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
except ApiException as e:
    print("Exception when calling VideosApi->delete_video_face: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **video_id** | **str**| The video id | 
 **face_id** | **int**| Format - int32. The face id to delete | 
 **access_token** | **str**| Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be &lt;b&gt;Account/Video&lt;/b&gt; and permission should be &lt;b&gt;Contributor&lt;/b&gt;.&lt;br&gt;  Note that Access tokens expire within 1 hour&lt;br&gt; See more details for &lt;b&gt;Classic Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/DocsObtainAccessToken target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;, for &lt;b&gt;ARM Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/vi-classic-access-token target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_video_source_file**
> delete_video_source_file(location, account_id, video_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Delete Video Source File

Deletes only the video source file, while keeping all insights created from when the video was indexed.

### Example
```python
from __future__ import print_function
import time
import videoindexer
from videoindexer.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = videoindexer.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = videoindexer.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = videoindexer.VideosApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
video_id = 'video_id_example' # str | The video id
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account/Video</b> and permission should be <b>Contributor</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Delete Video Source File
    api_instance.delete_video_source_file(location, account_id, video_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
except ApiException as e:
    print("Exception when calling VideosApi->delete_video_source_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **video_id** | **str**| The video id | 
 **access_token** | **str**| Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be &lt;b&gt;Account/Video&lt;/b&gt; and permission should be &lt;b&gt;Contributor&lt;/b&gt;.&lt;br&gt;  Note that Access tokens expire within 1 hour&lt;br&gt; See more details for &lt;b&gt;Classic Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/DocsObtainAccessToken target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;, for &lt;b&gt;ARM Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/vi-classic-access-token target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video_artifact_download_url**
> object get_video_artifact_download_url(location, account_id, video_id, type=type, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Get Video Artifact Download Url

Artifacts are intermediate outputs of the indexing process. They are essentially raw outputs of the various AI engines that analyze the videos. For this reason, the output formats may change over time. <br>We do not recommend that you use data directly from the artifacts folder for production purposes. It is recommended that you use the Get Video Index API for most insights. <br>This API returns a URL only with a link to the specific resource type you request. An additional GET request must be made to this URL for the specific artifact. <br>The file types for each artifact type vary depending on the artifact. For the specific schemas of the output JSON see <a href=https://docs.microsoft.com/en-us/azure/azure-video-indexer/video-indexer-output-json-v2 target=\"_blank\">here</a>.

### Example
```python
from __future__ import print_function
import time
import videoindexer
from videoindexer.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = videoindexer.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = videoindexer.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = videoindexer.VideosApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
video_id = 'video_id_example' # str | The video id
type = 'type_example' # str | The artifact type to get. Allowed values: Ocr / Faces / FacesThumbnails / VisualContentModeration / KeyframesThumbnails / Emotions / TextualContentModeration / AudioEffects / ObservedPeople / Labels / Transcript / FeaturedClothing / Clapperboards / DigitalPatterns (optional)
access_token = 'access_token_example' # str | Required for private videos<br>  Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account/Video</b> and permission should be <b>Reader</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Get Video Artifact Download Url
    api_response = api_instance.get_video_artifact_download_url(location, account_id, video_id, type=type, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_video_artifact_download_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **video_id** | **str**| The video id | 
 **type** | **str**| The artifact type to get. Allowed values: Ocr / Faces / FacesThumbnails / VisualContentModeration / KeyframesThumbnails / Emotions / TextualContentModeration / AudioEffects / ObservedPeople / Labels / Transcript / FeaturedClothing / Clapperboards / DigitalPatterns | [optional] 
 **access_token** | **str**| Required for private videos&lt;br&gt;  Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be &lt;b&gt;Account/Video&lt;/b&gt; and permission should be &lt;b&gt;Reader&lt;/b&gt;.&lt;br&gt;  Note that Access tokens expire within 1 hour&lt;br&gt; See more details for &lt;b&gt;Classic Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/DocsObtainAccessToken target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;, for &lt;b&gt;ARM Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/vi-classic-access-token target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

**object**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video_captions**
> object get_video_captions(location, account_id, video_id, index_id=index_id, format=format, language=language, include_audio_effects=include_audio_effects, include_speakers=include_speakers, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Get Video Captions

Get video captions

### Example
```python
from __future__ import print_function
import time
import videoindexer
from videoindexer.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = videoindexer.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = videoindexer.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = videoindexer.VideosApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
video_id = 'video_id_example' # str | The video id
index_id = 'index_id_example' # str | The video id (optional)
format = 'Vtt' # str | The captions format. Allowed values: Vtt / Ttml / Srt / Txt / Csv (optional) (default to Vtt)
language = 'language_example' # str | The language of the captions. Supported languages: Afrikaans: af-ZA, Arabic (United Arab Emirates): ar-AE, Arabic Modern Standard (Bahrain): ar-BH, Arabic Egypt: ar-EG, Arabic (Israel): ar-IL, Arabic (Iraq): ar-IQ, Arabic (Jordan): ar-JO, Arabic (Kuwait): ar-KW, Arabic (Lebanon): ar-LB, Arabic (Oman): ar-OM, Arabic (Palestinian Authority): ar-PS, Arabic (Qatar): ar-QA, Arabic (Saudi Arabia): ar-SA, Arabic Syrian Arab Republic: ar-SY, Bulgarian: bg-BG, Bangla: bn-BD, Bosnian: bs-Latn, Catalan: ca-ES, Czech: cs-CZ, Danish: da-DK, German: de-DE, Greek: el-GR, English Australia: en-AU, Fijian: en-FJ, English United Kingdom: en-GB, English United States: en-US, Samoan: en-WS, Spanish: es-ES, Spanish (Mexico): es-MX, Estonian: et-EE, Persian: fa-IR, Finnish: fi-FI, Filipino: fil-PH, French (Canada): fr-CA, French: fr-FR, Haitian: fr-HT, Hebrew: he-IL, Hindi: hi-IN, Croatian: hr-HR, Hungarian: hu-HU, Indonesian: id-ID, Italian: it-IT, Japanese: ja-JP, Korean: ko-KR, Lithuanian: lt-LT, Latvian: lv-LV, Malagasy: mg-MG, Malay: ms-MY, Maltese: mt-MT, Norwegian: nb-NO, Dutch: nl-NL, Polish: pl-PL, Portuguese: pt-BR, Portuguese (Portugal): pt-PT, Romanian: ro-RO, Russian: ru-RU, Slovak: sk-SK, Slovenian: sl-SI, Serbian (Cyrillic): sr-Cyrl-RS, Serbian (Latin): sr-Latn-RS, Swedish: sv-SE, Kiswahili: sw-KE, Tamil: ta-IN, Thai: th-TH, Tongan: to-TO, Turkish: tr-TR, Ukrainian: uk-UA, Urdu: ur-PK, Vietnamese: vi-VN, Chinese (Simplified): zh-Hans, Chinese (Traditional): zh-Hant, Chinese (Cantonese, Traditional): zh-HK. (optional)
include_audio_effects = false # bool | Include audio effects (optional) (default to false)
include_speakers = false # bool | Include speakers (optional) (default to false)
access_token = 'access_token_example' # str | Required for private videos<br>  Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account/Video</b> and permission should be <b>Reader</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Get Video Captions
    api_response = api_instance.get_video_captions(location, account_id, video_id, index_id=index_id, format=format, language=language, include_audio_effects=include_audio_effects, include_speakers=include_speakers, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_video_captions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **video_id** | **str**| The video id | 
 **index_id** | **str**| The video id | [optional] 
 **format** | **str**| The captions format. Allowed values: Vtt / Ttml / Srt / Txt / Csv | [optional] [default to Vtt]
 **language** | **str**| The language of the captions. Supported languages: Afrikaans: af-ZA, Arabic (United Arab Emirates): ar-AE, Arabic Modern Standard (Bahrain): ar-BH, Arabic Egypt: ar-EG, Arabic (Israel): ar-IL, Arabic (Iraq): ar-IQ, Arabic (Jordan): ar-JO, Arabic (Kuwait): ar-KW, Arabic (Lebanon): ar-LB, Arabic (Oman): ar-OM, Arabic (Palestinian Authority): ar-PS, Arabic (Qatar): ar-QA, Arabic (Saudi Arabia): ar-SA, Arabic Syrian Arab Republic: ar-SY, Bulgarian: bg-BG, Bangla: bn-BD, Bosnian: bs-Latn, Catalan: ca-ES, Czech: cs-CZ, Danish: da-DK, German: de-DE, Greek: el-GR, English Australia: en-AU, Fijian: en-FJ, English United Kingdom: en-GB, English United States: en-US, Samoan: en-WS, Spanish: es-ES, Spanish (Mexico): es-MX, Estonian: et-EE, Persian: fa-IR, Finnish: fi-FI, Filipino: fil-PH, French (Canada): fr-CA, French: fr-FR, Haitian: fr-HT, Hebrew: he-IL, Hindi: hi-IN, Croatian: hr-HR, Hungarian: hu-HU, Indonesian: id-ID, Italian: it-IT, Japanese: ja-JP, Korean: ko-KR, Lithuanian: lt-LT, Latvian: lv-LV, Malagasy: mg-MG, Malay: ms-MY, Maltese: mt-MT, Norwegian: nb-NO, Dutch: nl-NL, Polish: pl-PL, Portuguese: pt-BR, Portuguese (Portugal): pt-PT, Romanian: ro-RO, Russian: ru-RU, Slovak: sk-SK, Slovenian: sl-SI, Serbian (Cyrillic): sr-Cyrl-RS, Serbian (Latin): sr-Latn-RS, Swedish: sv-SE, Kiswahili: sw-KE, Tamil: ta-IN, Thai: th-TH, Tongan: to-TO, Turkish: tr-TR, Ukrainian: uk-UA, Urdu: ur-PK, Vietnamese: vi-VN, Chinese (Simplified): zh-Hans, Chinese (Traditional): zh-Hant, Chinese (Cantonese, Traditional): zh-HK. | [optional] 
 **include_audio_effects** | **bool**| Include audio effects | [optional] [default to false]
 **include_speakers** | **bool**| Include speakers | [optional] [default to false]
 **access_token** | **str**| Required for private videos&lt;br&gt;  Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be &lt;b&gt;Account/Video&lt;/b&gt; and permission should be &lt;b&gt;Reader&lt;/b&gt;.&lt;br&gt;  Note that Access tokens expire within 1 hour&lt;br&gt; See more details for &lt;b&gt;Classic Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/DocsObtainAccessToken target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;, for &lt;b&gt;ARM Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/vi-classic-access-token target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

**object**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video_id_by_external_id**
> object get_video_id_by_external_id(location, account_id, external_id=external_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Get Video Id By External Id

Get Video Id by External Id.

### Example
```python
from __future__ import print_function
import time
import videoindexer
from videoindexer.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = videoindexer.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = videoindexer.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = videoindexer.VideosApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
external_id = 'external_id_example' # str | The external id (optional)
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account</b> and permission should be <b>Reader</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Get Video Id By External Id
    api_response = api_instance.get_video_id_by_external_id(location, account_id, external_id=external_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_video_id_by_external_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **external_id** | **str**| The external id | [optional] 
 **access_token** | **str**| Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be &lt;b&gt;Account&lt;/b&gt; and permission should be &lt;b&gt;Reader&lt;/b&gt;.&lt;br&gt;  Note that Access tokens expire within 1 hour&lt;br&gt; See more details for &lt;b&gt;Classic Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/DocsObtainAccessToken target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;, for &lt;b&gt;ARM Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/vi-classic-access-token target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

**object**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video_source_file_download_url**
> object get_video_source_file_download_url(location, account_id, video_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Get Video Source File Download Url

Get video source file download url.

### Example
```python
from __future__ import print_function
import time
import videoindexer
from videoindexer.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = videoindexer.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = videoindexer.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = videoindexer.VideosApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
video_id = 'video_id_example' # str | The video id
access_token = 'access_token_example' # str | Required for private videos<br>  Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account/Video</b> and permission should be <b>Reader</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Get Video Source File Download Url
    api_response = api_instance.get_video_source_file_download_url(location, account_id, video_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_video_source_file_download_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **video_id** | **str**| The video id | 
 **access_token** | **str**| Required for private videos&lt;br&gt;  Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be &lt;b&gt;Account/Video&lt;/b&gt; and permission should be &lt;b&gt;Reader&lt;/b&gt;.&lt;br&gt;  Note that Access tokens expire within 1 hour&lt;br&gt; See more details for &lt;b&gt;Classic Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/DocsObtainAccessToken target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;, for &lt;b&gt;ARM Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/vi-classic-access-token target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

**object**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video_streaming_url**
> object get_video_streaming_url(location, account_id, video_id, use_proxy=use_proxy, url_format=url_format, token_lifetime_in_minutes=token_lifetime_in_minutes, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Get Video Streaming URL

Get Video Streaming URL

### Example
```python
from __future__ import print_function
import time
import videoindexer
from videoindexer.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = videoindexer.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = videoindexer.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = videoindexer.VideosApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
video_id = 'video_id_example' # str | The video id
use_proxy = false # bool | Wrap the streaming endpoint with proxy. Required for delivering content to Safari browsers. See more details <a href=https://aka.ms/blog-hls-stream-working-in-safari/ />here</a> (optional) (default to false)
url_format = 'MPEG_DASH' # str | <a href=https://aka.ms/vi-swagger-stream-url-formats />Streaming URL format</a>.. Allowed values: SMOOTH_STREAMING_FORMAT / MPEG_DASH / HLS_V4 / HLS_V3 (optional) (default to MPEG_DASH)
token_lifetime_in_minutes = 56 # int | Format - int32. Streaming URL token lifetime in minutes. Value must be positive. Default is 60 minutes (optional)
access_token = 'access_token_example' # str | Required for private videos<br>  Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account/Video</b> and permission should be <b>Reader</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Get Video Streaming URL
    api_response = api_instance.get_video_streaming_url(location, account_id, video_id, use_proxy=use_proxy, url_format=url_format, token_lifetime_in_minutes=token_lifetime_in_minutes, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_video_streaming_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **video_id** | **str**| The video id | 
 **use_proxy** | **bool**| Wrap the streaming endpoint with proxy. Required for delivering content to Safari browsers. See more details &lt;a href&#x3D;https://aka.ms/blog-hls-stream-working-in-safari/ /&gt;here&lt;/a&gt; | [optional] [default to false]
 **url_format** | **str**| &lt;a href&#x3D;https://aka.ms/vi-swagger-stream-url-formats /&gt;Streaming URL format&lt;/a&gt;.. Allowed values: SMOOTH_STREAMING_FORMAT / MPEG_DASH / HLS_V4 / HLS_V3 | [optional] [default to MPEG_DASH]
 **token_lifetime_in_minutes** | **int**| Format - int32. Streaming URL token lifetime in minutes. Value must be positive. Default is 60 minutes | [optional] 
 **access_token** | **str**| Required for private videos&lt;br&gt;  Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be &lt;b&gt;Account/Video&lt;/b&gt; and permission should be &lt;b&gt;Reader&lt;/b&gt;.&lt;br&gt;  Note that Access tokens expire within 1 hour&lt;br&gt; See more details for &lt;b&gt;Classic Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/DocsObtainAccessToken target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;, for &lt;b&gt;ARM Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/vi-classic-access-token target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

**object**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video_thumbnail**
> object get_video_thumbnail(location, account_id, video_id, thumbnail_id, format=format, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Get Video Thumbnail

Get thumbnail of a video

### Example
```python
from __future__ import print_function
import time
import videoindexer
from videoindexer.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = videoindexer.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = videoindexer.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = videoindexer.VideosApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
video_id = 'video_id_example' # str | The video id
thumbnail_id = 'thumbnail_id_example' # str | Format - guid. Thumbnail id
format = 'Jpeg' # str | Thumbnail format. Allowed values: Jpeg / Base64 (optional) (default to Jpeg)
access_token = 'access_token_example' # str | Required for private videos<br>  Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account/Video</b> and permission should be <b>Reader</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Get Video Thumbnail
    api_response = api_instance.get_video_thumbnail(location, account_id, video_id, thumbnail_id, format=format, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_video_thumbnail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **video_id** | **str**| The video id | 
 **thumbnail_id** | **str**| Format - guid. Thumbnail id | 
 **format** | **str**| Thumbnail format. Allowed values: Jpeg / Base64 | [optional] [default to Jpeg]
 **access_token** | **str**| Required for private videos&lt;br&gt;  Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be &lt;b&gt;Account/Video&lt;/b&gt; and permission should be &lt;b&gt;Reader&lt;/b&gt;.&lt;br&gt;  Note that Access tokens expire within 1 hour&lt;br&gt; See more details for &lt;b&gt;Classic Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/DocsObtainAccessToken target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;, for &lt;b&gt;ARM Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/vi-classic-access-token target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

**object**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_videos**
> object list_videos(location, account_id, created_after=created_after, created_before=created_before, page_size=page_size, skip=skip, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

List Videos

Get a list of videos and projects in the account

### Example
```python
from __future__ import print_function
import time
import videoindexer
from videoindexer.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = videoindexer.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = videoindexer.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = videoindexer.VideosApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
created_after = 'created_after_example' # str | Filter items created before the specified date. Accepted format: RFC 3339, section 5.6. Example: '2017-07-21T17:32:28Z' (optional)
created_before = 'created_before_example' # str | Filter items created after the specified date. Accepted format: RFC 3339, section 5.6. Example: '2017-07-21T17:32:28Z' (optional)
page_size = 25 # int | Format - int32. page size (optional) (default to 25)
skip = 0 # int | Format - int32. The number of records to skip (optional) (default to 0)
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account</b> and permission should be <b>Reader</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # List Videos
    api_response = api_instance.list_videos(location, account_id, created_after=created_after, created_before=created_before, page_size=page_size, skip=skip, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->list_videos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **created_after** | **str**| Filter items created before the specified date. Accepted format: RFC 3339, section 5.6. Example: &#x27;2017-07-21T17:32:28Z&#x27; | [optional] 
 **created_before** | **str**| Filter items created after the specified date. Accepted format: RFC 3339, section 5.6. Example: &#x27;2017-07-21T17:32:28Z&#x27; | [optional] 
 **page_size** | **int**| Format - int32. page size | [optional] [default to 25]
 **skip** | **int**| Format - int32. The number of records to skip | [optional] [default to 0]
 **access_token** | **str**| Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be &lt;b&gt;Account&lt;/b&gt; and permission should be &lt;b&gt;Reader&lt;/b&gt;.&lt;br&gt;  Note that Access tokens expire within 1 hour&lt;br&gt; See more details for &lt;b&gt;Classic Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/DocsObtainAccessToken target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;, for &lt;b&gt;ARM Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/vi-classic-access-token target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

**object**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_videos**
> object search_videos(location, account_id, source_language=source_language, is_base=is_base, has_source_video_file=has_source_video_file, source_video_id=source_video_id, state=state, privacy=privacy, id=id, partition=partition, external_id=external_id, owner=owner, face=face, animatedcharacter=animatedcharacter, query=query, text_scope=text_scope, language=language, created_after=created_after, created_before=created_before, page_size=page_size, skip=skip, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Search Videos

Search videos and projects in the specified account

### Example
```python
from __future__ import print_function
import time
import videoindexer
from videoindexer.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = videoindexer.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = videoindexer.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = videoindexer.VideosApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
source_language = 'source_language_example' # str | Include only videos/projects with that source language. Supported languages: Arabic (United Arab Emirates): ar-AE, Arabic Modern Standard (Bahrain): ar-BH, Arabic Egypt: ar-EG, Arabic (Israel): ar-IL, Arabic (Iraq): ar-IQ, Arabic (Jordan): ar-JO, Arabic (Kuwait): ar-KW, Arabic (Lebanon): ar-LB, Arabic (Oman): ar-OM, Arabic (Palestinian Authority): ar-PS, Arabic (Qatar): ar-QA, Arabic (Saudi Arabia): ar-SA, Arabic Syrian Arab Republic: ar-SY, Czech: cs-CZ, Danish: da-DK, German: de-DE, English Australia: en-AU, English United Kingdom: en-GB, English United States: en-US, Spanish: es-ES, Spanish (Mexico): es-MX, Persian: fa-IR, Finnish: fi-FI, French (Canada): fr-CA, French: fr-FR, Hebrew: he-IL, Hindi: hi-IN, Italian: it-IT, Japanese: ja-JP, Korean: ko-KR, Norwegian: nb-NO, Dutch: nl-NL, Polish: pl-PL, Portuguese: pt-BR, Portuguese (Portugal): pt-PT, Russian: ru-RU, Swedish: sv-SE, Thai: th-TH, Turkish: tr-TR, Chinese (Simplified): zh-Hans, Chinese (Cantonese, Traditional): zh-HK. (optional)
is_base = true # bool | true will include only videos; false will include only projects (optional)
has_source_video_file = true # bool | true will include videos that have a source file; false will include projects as well as videos without a source file (optional)
source_video_id = 'source_video_id_example' # str | Include only the video with the given id as well as projects that have a source video with the given id (optional)
state = NULL # list | A processing state of videos. Projects are always in 'Processed' state. Allowed values: Uploaded / Processing / Processed / Failed / Quarantined (optional)
privacy = NULL # list | A privacy level. Allowed values: Private / Public (optional)
id = NULL # list | A video id to search for. (optional)
partition = NULL # list | A partition to search for. (optional)
external_id = NULL # list | An external id to search for (which was associated with the video at upload). (optional)
owner = NULL # list | An owner to search for. (optional)
face = NULL # list | A face to search for. (optional)
animatedcharacter = NULL # list | An animated character to search for. (optional)
query = NULL # list | Free text to search for.  Example 1: '&query=north america' -> searches for videos with 'north' and / or 'america' and ranks videos with more hits higher.   Example 2: '&query=north+america' -> search for videos with all of the words (AND operator).   Example 3: '&query=north|america' -> searches for videos with any of the words (OR operator).   Example 4: '&query=north&query=america' -> searches for videos with any of the words (OR operator).   Example 5: '&query=-north' -> searches for videos without the word 'north' (NOT operator).   Example 6: '&query=\"north america\"' -> searches for videos with the phrase 'north america' (exact match).   Example 7: '&query=\"north america\"'&query=-east -> searches for videos with the phrase 'north america' (exact match) OR videos without the word 'east'.   NOTICE: These parameters should be sent url-encoded. This is confusing because a space ' ' is encoded as '+' and '+' is encoded as '%2B'. Open text query like '&query=north america' is sent as '&query=north+america' and an AND query like '&query=north+america' is sent as '&query=north%2Bamerica'. (optional)
text_scope = NULL # list | The text scope to search in. Allowed values: Transcript / Topics / Ocr / Annotations / Brands / NamedLocations / NamedPeople (optional)
language = NULL # list | The language to search in. You can specify multiple language parameters (e.g. $language=English&language=French) to search multiple languages. Having no language parameter will search all languages. Videos/projects are searchable in their source language as well as any language they were translated to by another operation. Supported languages: Afrikaans: af-ZA, Arabic (United Arab Emirates): ar-AE, Arabic Modern Standard (Bahrain): ar-BH, Arabic Egypt: ar-EG, Arabic (Israel): ar-IL, Arabic (Iraq): ar-IQ, Arabic (Jordan): ar-JO, Arabic (Kuwait): ar-KW, Arabic (Lebanon): ar-LB, Arabic (Oman): ar-OM, Arabic (Palestinian Authority): ar-PS, Arabic (Qatar): ar-QA, Arabic (Saudi Arabia): ar-SA, Arabic Syrian Arab Republic: ar-SY, Bulgarian: bg-BG, Bangla: bn-BD, Bosnian: bs-Latn, Catalan: ca-ES, Czech: cs-CZ, Danish: da-DK, German: de-DE, Greek: el-GR, English Australia: en-AU, Fijian: en-FJ, English United Kingdom: en-GB, English United States: en-US, Samoan: en-WS, Spanish: es-ES, Spanish (Mexico): es-MX, Estonian: et-EE, Persian: fa-IR, Finnish: fi-FI, Filipino: fil-PH, French (Canada): fr-CA, French: fr-FR, Haitian: fr-HT, Hebrew: he-IL, Hindi: hi-IN, Croatian: hr-HR, Hungarian: hu-HU, Indonesian: id-ID, Italian: it-IT, Japanese: ja-JP, Korean: ko-KR, Lithuanian: lt-LT, Latvian: lv-LV, Malagasy: mg-MG, Malay: ms-MY, Maltese: mt-MT, Norwegian: nb-NO, Dutch: nl-NL, Polish: pl-PL, Portuguese: pt-BR, Portuguese (Portugal): pt-PT, Romanian: ro-RO, Russian: ru-RU, Slovak: sk-SK, Slovenian: sl-SI, Serbian (Cyrillic): sr-Cyrl-RS, Serbian (Latin): sr-Latn-RS, Swedish: sv-SE, Kiswahili: sw-KE, Tamil: ta-IN, Thai: th-TH, Tongan: to-TO, Turkish: tr-TR, Ukrainian: uk-UA, Urdu: ur-PK, Vietnamese: vi-VN, Chinese (Simplified): zh-Hans, Chinese (Traditional): zh-Hant, Chinese (Cantonese, Traditional): zh-HK. (optional)
created_after = 'created_after_example' # str | Filter items created before the specified date Accepted format: RFC 3339, section 5.6. Example: '2017-07-21T17:32:28Z' (optional)
created_before = 'created_before_example' # str | Filter items created after the specified date Accepted format: RFC 3339, section 5.6. Example: '2017-07-21T17:32:28Z' (optional)
page_size = 25 # int | Format - int32. The number of results to return. (optional) (default to 25)
skip = 0 # int | Format - int32. The number of results to skip (used for paging). (optional) (default to 0)
access_token = 'access_token_example' # str | Required for private videos/projects or account scope search. If searching an account, you must provide a token with an Account scope.<br>  Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account/Video/Project</b> and permission should be <b>Reader</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Search Videos
    api_response = api_instance.search_videos(location, account_id, source_language=source_language, is_base=is_base, has_source_video_file=has_source_video_file, source_video_id=source_video_id, state=state, privacy=privacy, id=id, partition=partition, external_id=external_id, owner=owner, face=face, animatedcharacter=animatedcharacter, query=query, text_scope=text_scope, language=language, created_after=created_after, created_before=created_before, page_size=page_size, skip=skip, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->search_videos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **source_language** | **str**| Include only videos/projects with that source language. Supported languages: Arabic (United Arab Emirates): ar-AE, Arabic Modern Standard (Bahrain): ar-BH, Arabic Egypt: ar-EG, Arabic (Israel): ar-IL, Arabic (Iraq): ar-IQ, Arabic (Jordan): ar-JO, Arabic (Kuwait): ar-KW, Arabic (Lebanon): ar-LB, Arabic (Oman): ar-OM, Arabic (Palestinian Authority): ar-PS, Arabic (Qatar): ar-QA, Arabic (Saudi Arabia): ar-SA, Arabic Syrian Arab Republic: ar-SY, Czech: cs-CZ, Danish: da-DK, German: de-DE, English Australia: en-AU, English United Kingdom: en-GB, English United States: en-US, Spanish: es-ES, Spanish (Mexico): es-MX, Persian: fa-IR, Finnish: fi-FI, French (Canada): fr-CA, French: fr-FR, Hebrew: he-IL, Hindi: hi-IN, Italian: it-IT, Japanese: ja-JP, Korean: ko-KR, Norwegian: nb-NO, Dutch: nl-NL, Polish: pl-PL, Portuguese: pt-BR, Portuguese (Portugal): pt-PT, Russian: ru-RU, Swedish: sv-SE, Thai: th-TH, Turkish: tr-TR, Chinese (Simplified): zh-Hans, Chinese (Cantonese, Traditional): zh-HK. | [optional] 
 **is_base** | **bool**| true will include only videos; false will include only projects | [optional] 
 **has_source_video_file** | **bool**| true will include videos that have a source file; false will include projects as well as videos without a source file | [optional] 
 **source_video_id** | **str**| Include only the video with the given id as well as projects that have a source video with the given id | [optional] 
 **state** | [**list**](.md)| A processing state of videos. Projects are always in &#x27;Processed&#x27; state. Allowed values: Uploaded / Processing / Processed / Failed / Quarantined | [optional] 
 **privacy** | [**list**](.md)| A privacy level. Allowed values: Private / Public | [optional] 
 **id** | [**list**](.md)| A video id to search for. | [optional] 
 **partition** | [**list**](.md)| A partition to search for. | [optional] 
 **external_id** | [**list**](.md)| An external id to search for (which was associated with the video at upload). | [optional] 
 **owner** | [**list**](.md)| An owner to search for. | [optional] 
 **face** | [**list**](.md)| A face to search for. | [optional] 
 **animatedcharacter** | [**list**](.md)| An animated character to search for. | [optional] 
 **query** | [**list**](.md)| Free text to search for.  Example 1: &#x27;&amp;query&#x3D;north america&#x27; -&gt; searches for videos with &#x27;north&#x27; and / or &#x27;america&#x27; and ranks videos with more hits higher.   Example 2: &#x27;&amp;query&#x3D;north+america&#x27; -&gt; search for videos with all of the words (AND operator).   Example 3: &#x27;&amp;query&#x3D;north|america&#x27; -&gt; searches for videos with any of the words (OR operator).   Example 4: &#x27;&amp;query&#x3D;north&amp;query&#x3D;america&#x27; -&gt; searches for videos with any of the words (OR operator).   Example 5: &#x27;&amp;query&#x3D;-north&#x27; -&gt; searches for videos without the word &#x27;north&#x27; (NOT operator).   Example 6: &#x27;&amp;query&#x3D;\&quot;north america\&quot;&#x27; -&gt; searches for videos with the phrase &#x27;north america&#x27; (exact match).   Example 7: &#x27;&amp;query&#x3D;\&quot;north america\&quot;&#x27;&amp;query&#x3D;-east -&gt; searches for videos with the phrase &#x27;north america&#x27; (exact match) OR videos without the word &#x27;east&#x27;.   NOTICE: These parameters should be sent url-encoded. This is confusing because a space &#x27; &#x27; is encoded as &#x27;+&#x27; and &#x27;+&#x27; is encoded as &#x27;%2B&#x27;. Open text query like &#x27;&amp;query&#x3D;north america&#x27; is sent as &#x27;&amp;query&#x3D;north+america&#x27; and an AND query like &#x27;&amp;query&#x3D;north+america&#x27; is sent as &#x27;&amp;query&#x3D;north%2Bamerica&#x27;. | [optional] 
 **text_scope** | [**list**](.md)| The text scope to search in. Allowed values: Transcript / Topics / Ocr / Annotations / Brands / NamedLocations / NamedPeople | [optional] 
 **language** | [**list**](.md)| The language to search in. You can specify multiple language parameters (e.g. $language&#x3D;English&amp;language&#x3D;French) to search multiple languages. Having no language parameter will search all languages. Videos/projects are searchable in their source language as well as any language they were translated to by another operation. Supported languages: Afrikaans: af-ZA, Arabic (United Arab Emirates): ar-AE, Arabic Modern Standard (Bahrain): ar-BH, Arabic Egypt: ar-EG, Arabic (Israel): ar-IL, Arabic (Iraq): ar-IQ, Arabic (Jordan): ar-JO, Arabic (Kuwait): ar-KW, Arabic (Lebanon): ar-LB, Arabic (Oman): ar-OM, Arabic (Palestinian Authority): ar-PS, Arabic (Qatar): ar-QA, Arabic (Saudi Arabia): ar-SA, Arabic Syrian Arab Republic: ar-SY, Bulgarian: bg-BG, Bangla: bn-BD, Bosnian: bs-Latn, Catalan: ca-ES, Czech: cs-CZ, Danish: da-DK, German: de-DE, Greek: el-GR, English Australia: en-AU, Fijian: en-FJ, English United Kingdom: en-GB, English United States: en-US, Samoan: en-WS, Spanish: es-ES, Spanish (Mexico): es-MX, Estonian: et-EE, Persian: fa-IR, Finnish: fi-FI, Filipino: fil-PH, French (Canada): fr-CA, French: fr-FR, Haitian: fr-HT, Hebrew: he-IL, Hindi: hi-IN, Croatian: hr-HR, Hungarian: hu-HU, Indonesian: id-ID, Italian: it-IT, Japanese: ja-JP, Korean: ko-KR, Lithuanian: lt-LT, Latvian: lv-LV, Malagasy: mg-MG, Malay: ms-MY, Maltese: mt-MT, Norwegian: nb-NO, Dutch: nl-NL, Polish: pl-PL, Portuguese: pt-BR, Portuguese (Portugal): pt-PT, Romanian: ro-RO, Russian: ru-RU, Slovak: sk-SK, Slovenian: sl-SI, Serbian (Cyrillic): sr-Cyrl-RS, Serbian (Latin): sr-Latn-RS, Swedish: sv-SE, Kiswahili: sw-KE, Tamil: ta-IN, Thai: th-TH, Tongan: to-TO, Turkish: tr-TR, Ukrainian: uk-UA, Urdu: ur-PK, Vietnamese: vi-VN, Chinese (Simplified): zh-Hans, Chinese (Traditional): zh-Hant, Chinese (Cantonese, Traditional): zh-HK. | [optional] 
 **created_after** | **str**| Filter items created before the specified date Accepted format: RFC 3339, section 5.6. Example: &#x27;2017-07-21T17:32:28Z&#x27; | [optional] 
 **created_before** | **str**| Filter items created after the specified date Accepted format: RFC 3339, section 5.6. Example: &#x27;2017-07-21T17:32:28Z&#x27; | [optional] 
 **page_size** | **int**| Format - int32. The number of results to return. | [optional] [default to 25]
 **skip** | **int**| Format - int32. The number of results to skip (used for paging). | [optional] [default to 0]
 **access_token** | **str**| Required for private videos/projects or account scope search. If searching an account, you must provide a token with an Account scope.&lt;br&gt;  Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be &lt;b&gt;Account/Video/Project&lt;/b&gt; and permission should be &lt;b&gt;Reader&lt;/b&gt;.&lt;br&gt;  Note that Access tokens expire within 1 hour&lt;br&gt; See more details for &lt;b&gt;Classic Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/DocsObtainAccessToken target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;, for &lt;b&gt;ARM Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/vi-classic-access-token target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

**object**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_video_face**
> update_video_face(location, account_id, video_id, face_id, new_name=new_name, person_id=person_id, create_new_person=create_new_person, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Update Video Face

Update Video Face.

### Example
```python
from __future__ import print_function
import time
import videoindexer
from videoindexer.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = videoindexer.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = videoindexer.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = videoindexer.VideosApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
video_id = 'video_id_example' # str | The video id
face_id = 56 # int | Format - int32. The face id to update
new_name = 'new_name_example' # str | The face's new name (optional)
person_id = 'person_id_example' # str | Format - guid. The person id to update (if you have multiple persons with that name) (optional)
create_new_person = false # bool | Whether to create a new person and not update an existing person with that name. (optional) (default to false)
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account/Video</b> and permission should be <b>Contributor</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Update Video Face
    api_instance.update_video_face(location, account_id, video_id, face_id, new_name=new_name, person_id=person_id, create_new_person=create_new_person, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
except ApiException as e:
    print("Exception when calling VideosApi->update_video_face: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **video_id** | **str**| The video id | 
 **face_id** | **int**| Format - int32. The face id to update | 
 **new_name** | **str**| The face&#x27;s new name | [optional] 
 **person_id** | **str**| Format - guid. The person id to update (if you have multiple persons with that name) | [optional] 
 **create_new_person** | **bool**| Whether to create a new person and not update an existing person with that name. | [optional] [default to false]
 **access_token** | **str**| Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be &lt;b&gt;Account/Video&lt;/b&gt; and permission should be &lt;b&gt;Contributor&lt;/b&gt;.&lt;br&gt;  Note that Access tokens expire within 1 hour&lt;br&gt; See more details for &lt;b&gt;Classic Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/DocsObtainAccessToken target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;, for &lt;b&gt;ARM Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/vi-classic-access-token target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_video_index**
> object update_video_index(location, account_id, video_id, body=body, x_ms_client_request_id=x_ms_client_request_id, language=language, access_token=access_token)

Update Video Index

Updates the video index. The method accepts a JsonPatchDocument (in the request body) consisting of the operations that need to be applied. <br> <a href= http://jsonpatch.com/ target=\"_blank\">How to construct a JSON patch request.</a>.

### Example
```python
from __future__ import print_function
import time
import videoindexer
from videoindexer.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = videoindexer.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = videoindexer.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = videoindexer.VideosApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
video_id = 'video_id_example' # str | The video id
body = [ {
  "op" : "add",
  "path" : "/videos/0/insights/transcript/0",
  "value" : {
    "confidence" : 1,
    "instances" : {
      "end" : "2022-07-31",
      "start" : "2022-07-31"
    },
    "language" : "en-US",
    "text" : "lorem ipsum"
  }
}, {
  "op" : "remove",
  "path" : "/videos/0/insights/transcript/0"
}, {
  "op" : "replace",
  "path" : "/videos/0/insights/transcript/0/text",
  "value" : "lorem ipsum"
}, {
  "op" : "replace",
  "path" : "/videos/0/insights/transcript/0/instences/0/start",
  "value" : "2022-07-31"
}, {
  "op" : "replace",
  "path" : "/videos/0/insights/transcript/0/instences/0/end",
  "value" : "2022-07-31"
} ] # object | The JSON Patch containing the operation to run in order to update the video index. 
Currently supporting paths: 
1. /videos/0/insights/transcript/0 (Add/Remove operations) 
2. /videos/0/insights/transcript/0/text (Replace operation) 
3. /videos/0/insights/transcript/0/instances/0/start (Replace operation) 
4. /videos/0/insights/transcript/0/instances/0/end (Replace operation) 
5. /videos/0/insights/ocr/0/text (Replace operation) (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)
language = 'language_example' # str | The language to get the video index by. Supported languages: Afrikaans: af-ZA, Arabic (United Arab Emirates): ar-AE, Arabic Modern Standard (Bahrain): ar-BH, Arabic Egypt: ar-EG, Arabic (Israel): ar-IL, Arabic (Iraq): ar-IQ, Arabic (Jordan): ar-JO, Arabic (Kuwait): ar-KW, Arabic (Lebanon): ar-LB, Arabic (Oman): ar-OM, Arabic (Palestinian Authority): ar-PS, Arabic (Qatar): ar-QA, Arabic (Saudi Arabia): ar-SA, Arabic Syrian Arab Republic: ar-SY, Bulgarian: bg-BG, Bangla: bn-BD, Bosnian: bs-Latn, Catalan: ca-ES, Czech: cs-CZ, Danish: da-DK, German: de-DE, Greek: el-GR, English Australia: en-AU, Fijian: en-FJ, English United Kingdom: en-GB, English United States: en-US, Samoan: en-WS, Spanish: es-ES, Spanish (Mexico): es-MX, Estonian: et-EE, Persian: fa-IR, Finnish: fi-FI, Filipino: fil-PH, French (Canada): fr-CA, French: fr-FR, Haitian: fr-HT, Hebrew: he-IL, Hindi: hi-IN, Croatian: hr-HR, Hungarian: hu-HU, Indonesian: id-ID, Italian: it-IT, Japanese: ja-JP, Korean: ko-KR, Lithuanian: lt-LT, Latvian: lv-LV, Malagasy: mg-MG, Malay: ms-MY, Maltese: mt-MT, Norwegian: nb-NO, Dutch: nl-NL, Polish: pl-PL, Portuguese: pt-BR, Portuguese (Portugal): pt-PT, Romanian: ro-RO, Russian: ru-RU, Slovak: sk-SK, Slovenian: sl-SI, Serbian (Cyrillic): sr-Cyrl-RS, Serbian (Latin): sr-Latn-RS, Swedish: sv-SE, Kiswahili: sw-KE, Tamil: ta-IN, Thai: th-TH, Tongan: to-TO, Turkish: tr-TR, Ukrainian: uk-UA, Urdu: ur-PK, Vietnamese: vi-VN, Chinese (Simplified): zh-Hans, Chinese (Traditional): zh-Hant, Chinese (Cantonese, Traditional): zh-HK. (optional)
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account/Video</b> and permission should be <b>Contributor</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)

try:
    # Update Video Index
    api_response = api_instance.update_video_index(location, account_id, video_id, body=body, x_ms_client_request_id=x_ms_client_request_id, language=language, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->update_video_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **video_id** | **str**| The video id | 
 **body** | [**object**](object.md)| The JSON Patch containing the operation to run in order to update the video index. 
Currently supporting paths: 
1. /videos/0/insights/transcript/0 (Add/Remove operations) 
2. /videos/0/insights/transcript/0/text (Replace operation) 
3. /videos/0/insights/transcript/0/instances/0/start (Replace operation) 
4. /videos/0/insights/transcript/0/instances/0/end (Replace operation) 
5. /videos/0/insights/ocr/0/text (Replace operation) | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 
 **language** | **str**| The language to get the video index by. Supported languages: Afrikaans: af-ZA, Arabic (United Arab Emirates): ar-AE, Arabic Modern Standard (Bahrain): ar-BH, Arabic Egypt: ar-EG, Arabic (Israel): ar-IL, Arabic (Iraq): ar-IQ, Arabic (Jordan): ar-JO, Arabic (Kuwait): ar-KW, Arabic (Lebanon): ar-LB, Arabic (Oman): ar-OM, Arabic (Palestinian Authority): ar-PS, Arabic (Qatar): ar-QA, Arabic (Saudi Arabia): ar-SA, Arabic Syrian Arab Republic: ar-SY, Bulgarian: bg-BG, Bangla: bn-BD, Bosnian: bs-Latn, Catalan: ca-ES, Czech: cs-CZ, Danish: da-DK, German: de-DE, Greek: el-GR, English Australia: en-AU, Fijian: en-FJ, English United Kingdom: en-GB, English United States: en-US, Samoan: en-WS, Spanish: es-ES, Spanish (Mexico): es-MX, Estonian: et-EE, Persian: fa-IR, Finnish: fi-FI, Filipino: fil-PH, French (Canada): fr-CA, French: fr-FR, Haitian: fr-HT, Hebrew: he-IL, Hindi: hi-IN, Croatian: hr-HR, Hungarian: hu-HU, Indonesian: id-ID, Italian: it-IT, Japanese: ja-JP, Korean: ko-KR, Lithuanian: lt-LT, Latvian: lv-LV, Malagasy: mg-MG, Malay: ms-MY, Maltese: mt-MT, Norwegian: nb-NO, Dutch: nl-NL, Polish: pl-PL, Portuguese: pt-BR, Portuguese (Portugal): pt-PT, Romanian: ro-RO, Russian: ru-RU, Slovak: sk-SK, Slovenian: sl-SI, Serbian (Cyrillic): sr-Cyrl-RS, Serbian (Latin): sr-Latn-RS, Swedish: sv-SE, Kiswahili: sw-KE, Tamil: ta-IN, Thai: th-TH, Tongan: to-TO, Turkish: tr-TR, Ukrainian: uk-UA, Urdu: ur-PK, Vietnamese: vi-VN, Chinese (Simplified): zh-Hans, Chinese (Traditional): zh-Hant, Chinese (Cantonese, Traditional): zh-HK. | [optional] 
 **access_token** | **str**| Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be &lt;b&gt;Account/Video&lt;/b&gt; and permission should be &lt;b&gt;Contributor&lt;/b&gt;.&lt;br&gt;  Note that Access tokens expire within 1 hour&lt;br&gt; See more details for &lt;b&gt;Classic Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/DocsObtainAccessToken target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;, for &lt;b&gt;ARM Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/vi-classic-access-token target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | [optional] 

### Return type

**object**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_video_transcript**
> update_video_transcript(location, account_id, video_id, body=body, x_ms_client_request_id=x_ms_client_request_id, language=language, set_as_source_language=set_as_source_language, callback_url=callback_url, send_success_email=send_success_email, access_token=access_token)

Update Video Transcript

Updates the video with the given transcript. If the specified language is the source language of the video, then the video will be re-indexed with the given transcript, and the transcript of all the other languages will be re-generated. If the specified language is not the source language, the transcript of that language will be updated and the new text will be written into the existing lines and blocks of that language.

### Example
```python
from __future__ import print_function
import time
import videoindexer
from videoindexer.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = videoindexer.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = videoindexer.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = videoindexer.VideosApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
video_id = 'video_id_example' # str | The video id
body = '\"00:00:05.110 --> 00:00:10.880 Galga dot. I'm AI'm a I'm a.\\n00:00:10.880 --> 00:00:15.460 I am amazed is that award I'm a be wondering.\\n00:00:15.460 --> 00:00:18.980 Why that woman got noughties?\\n00:00:18.980 --> 00:00:22.436 They're here they're here don't worry Emma Watson seems like\\n00:00:22.494 --> 00:00:25.028 the type of girl who I would be friends with\\n00:00:25.086 --> 00:00:25.950 for like 3 days\\n00:00:25.950 --> 00:00:29.990 and then get really sick of button on tell her.\"' # str |  (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)
language = 'language_example' # str | The language to update its transcription. Supported languages: Afrikaans: af-ZA, Arabic (United Arab Emirates): ar-AE, Arabic Modern Standard (Bahrain): ar-BH, Arabic Egypt: ar-EG, Arabic (Israel): ar-IL, Arabic (Iraq): ar-IQ, Arabic (Jordan): ar-JO, Arabic (Kuwait): ar-KW, Arabic (Lebanon): ar-LB, Arabic (Oman): ar-OM, Arabic (Palestinian Authority): ar-PS, Arabic (Qatar): ar-QA, Arabic (Saudi Arabia): ar-SA, Arabic Syrian Arab Republic: ar-SY, Bulgarian: bg-BG, Bangla: bn-BD, Bosnian: bs-Latn, Catalan: ca-ES, Czech: cs-CZ, Danish: da-DK, German: de-DE, Greek: el-GR, English Australia: en-AU, Fijian: en-FJ, English United Kingdom: en-GB, English United States: en-US, Samoan: en-WS, Spanish: es-ES, Spanish (Mexico): es-MX, Estonian: et-EE, Persian: fa-IR, Finnish: fi-FI, Filipino: fil-PH, French (Canada): fr-CA, French: fr-FR, Haitian: fr-HT, Hebrew: he-IL, Hindi: hi-IN, Croatian: hr-HR, Hungarian: hu-HU, Indonesian: id-ID, Italian: it-IT, Japanese: ja-JP, Korean: ko-KR, Lithuanian: lt-LT, Latvian: lv-LV, Malagasy: mg-MG, Malay: ms-MY, Maltese: mt-MT, Norwegian: nb-NO, Dutch: nl-NL, Polish: pl-PL, Portuguese: pt-BR, Portuguese (Portugal): pt-PT, Romanian: ro-RO, Russian: ru-RU, Slovak: sk-SK, Slovenian: sl-SI, Serbian (Cyrillic): sr-Cyrl-RS, Serbian (Latin): sr-Latn-RS, Swedish: sv-SE, Kiswahili: sw-KE, Tamil: ta-IN, Thai: th-TH, Tongan: to-TO, Turkish: tr-TR, Ukrainian: uk-UA, Urdu: ur-PK, Vietnamese: vi-VN, Chinese (Simplified): zh-Hans, Chinese (Traditional): zh-Hant, Chinese (Cantonese, Traditional): zh-HK. (optional)
set_as_source_language = false # bool | If true the language parameter will be set as source language. (optional) (default to false)
callback_url = 'callback_url_example' # str | Format - uri. A callback url to call with the status once the operation completes, relevant only when the video is re-indexed (optional)
send_success_email = false # bool | Indicates whether to send a success mail once video was succesfully re-indexed with new transcript, relevant only when the video is re-indexed (optional) (default to false)
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account/Video</b> and permission should be <b>Contributor</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)

try:
    # Update Video Transcript
    api_instance.update_video_transcript(location, account_id, video_id, body=body, x_ms_client_request_id=x_ms_client_request_id, language=language, set_as_source_language=set_as_source_language, callback_url=callback_url, send_success_email=send_success_email, access_token=access_token)
except ApiException as e:
    print("Exception when calling VideosApi->update_video_transcript: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **video_id** | **str**| The video id | 
 **body** | [**str**](str.md)|  | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 
 **language** | **str**| The language to update its transcription. Supported languages: Afrikaans: af-ZA, Arabic (United Arab Emirates): ar-AE, Arabic Modern Standard (Bahrain): ar-BH, Arabic Egypt: ar-EG, Arabic (Israel): ar-IL, Arabic (Iraq): ar-IQ, Arabic (Jordan): ar-JO, Arabic (Kuwait): ar-KW, Arabic (Lebanon): ar-LB, Arabic (Oman): ar-OM, Arabic (Palestinian Authority): ar-PS, Arabic (Qatar): ar-QA, Arabic (Saudi Arabia): ar-SA, Arabic Syrian Arab Republic: ar-SY, Bulgarian: bg-BG, Bangla: bn-BD, Bosnian: bs-Latn, Catalan: ca-ES, Czech: cs-CZ, Danish: da-DK, German: de-DE, Greek: el-GR, English Australia: en-AU, Fijian: en-FJ, English United Kingdom: en-GB, English United States: en-US, Samoan: en-WS, Spanish: es-ES, Spanish (Mexico): es-MX, Estonian: et-EE, Persian: fa-IR, Finnish: fi-FI, Filipino: fil-PH, French (Canada): fr-CA, French: fr-FR, Haitian: fr-HT, Hebrew: he-IL, Hindi: hi-IN, Croatian: hr-HR, Hungarian: hu-HU, Indonesian: id-ID, Italian: it-IT, Japanese: ja-JP, Korean: ko-KR, Lithuanian: lt-LT, Latvian: lv-LV, Malagasy: mg-MG, Malay: ms-MY, Maltese: mt-MT, Norwegian: nb-NO, Dutch: nl-NL, Polish: pl-PL, Portuguese: pt-BR, Portuguese (Portugal): pt-PT, Romanian: ro-RO, Russian: ru-RU, Slovak: sk-SK, Slovenian: sl-SI, Serbian (Cyrillic): sr-Cyrl-RS, Serbian (Latin): sr-Latn-RS, Swedish: sv-SE, Kiswahili: sw-KE, Tamil: ta-IN, Thai: th-TH, Tongan: to-TO, Turkish: tr-TR, Ukrainian: uk-UA, Urdu: ur-PK, Vietnamese: vi-VN, Chinese (Simplified): zh-Hans, Chinese (Traditional): zh-Hant, Chinese (Cantonese, Traditional): zh-HK. | [optional] 
 **set_as_source_language** | **bool**| If true the language parameter will be set as source language. | [optional] [default to false]
 **callback_url** | **str**| Format - uri. A callback url to call with the status once the operation completes, relevant only when the video is re-indexed | [optional] 
 **send_success_email** | **bool**| Indicates whether to send a success mail once video was succesfully re-indexed with new transcript, relevant only when the video is re-indexed | [optional] [default to false]
 **access_token** | **str**| Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be &lt;b&gt;Account/Video&lt;/b&gt; and permission should be &lt;b&gt;Contributor&lt;/b&gt;.&lt;br&gt;  Note that Access tokens expire within 1 hour&lt;br&gt; See more details for &lt;b&gt;Classic Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/DocsObtainAccessToken target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;, for &lt;b&gt;ARM Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/vi-classic-access-token target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: text/vtt
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

