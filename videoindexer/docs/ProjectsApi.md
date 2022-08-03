# videoindexer.ProjectsApi

All URIs are relative to *https://api.videoindexer.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_project_render_operation**](ProjectsApi.md#cancel_project_render_operation) | **PUT** /{location}/Accounts/{accountId}/Projects/{projectId}/renderoperation/cancel | Cancel Project Render Operation
[**create_project**](ProjectsApi.md#create_project) | **POST** /{location}/Accounts/{accountId}/Projects | Create Project
[**delete_project**](ProjectsApi.md#delete_project) | **DELETE** /{location}/Accounts/{accountId}/Projects/{projectId} | Delete Project
[**download_project_rendered_file_url**](ProjectsApi.md#download_project_rendered_file_url) | **GET** /{location}/Accounts/{accountId}/Projects/{projectId}/renderedfile/downloadurl | Download Project Rendered File Url
[**get_project_captions**](ProjectsApi.md#get_project_captions) | **GET** /{location}/Accounts/{accountId}/Projects/{projectId}/Captions | Get Project Captions
[**get_project_index**](ProjectsApi.md#get_project_index) | **GET** /{location}/Accounts/{accountId}/Projects/{projectId}/Index | Get Project Index
[**get_project_insights_widget**](ProjectsApi.md#get_project_insights_widget) | **GET** /{location}/Accounts/{accountId}/Projects/{projectId}/InsightsWidget | Get Project Insights Widget
[**get_project_player_widget**](ProjectsApi.md#get_project_player_widget) | **GET** /{location}/Accounts/{accountId}/Projects/{projectId}/PlayerWidget | Get Project Player Widget
[**get_project_render_operation**](ProjectsApi.md#get_project_render_operation) | **GET** /{location}/Accounts/{accountId}/Projects/{projectId}/renderoperation | Get Project Render Operation
[**get_project_thumbnail**](ProjectsApi.md#get_project_thumbnail) | **GET** /{location}/Accounts/{accountId}/Projects/{projectId}/Thumbnails/{thumbnailId} | Get Project Thumbnail
[**render_project**](ProjectsApi.md#render_project) | **POST** /{location}/Accounts/{accountId}/Projects/{projectId}/render | Render Project
[**update_project**](ProjectsApi.md#update_project) | **PUT** /{location}/Accounts/{accountId}/Projects/{projectId} | Update Project

# **cancel_project_render_operation**
> object cancel_project_render_operation(location, account_id, project_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Cancel Project Render Operation

Cancels the ongoing render operation of an existing project. If the project's render operation's state isn't 'InProgress', the request won't do anything.<br/>If the render operation's state is 'InProgress' it will transition to state 'Cancelling' from which it usually reaches the 'Canceled' state but can reach another terminal state if the render operation already completed by the time cancellation was acknowledged. The API to get a project's render operation has documentation that explains possible render operation states in detail.

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
api_instance = videoindexer.ProjectsApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
project_id = 'project_id_example' # str | The project id
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account/Project</b> and permission should be <b>Contributor</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Cancel Project Render Operation
    api_response = api_instance.cancel_project_render_operation(location, account_id, project_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->cancel_project_render_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **project_id** | **str**| The project id | 
 **access_token** | **str**| Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be &lt;b&gt;Account/Project&lt;/b&gt; and permission should be &lt;b&gt;Contributor&lt;/b&gt;.&lt;br&gt;  Note that Access tokens expire within 1 hour&lt;br&gt; See more details for &lt;b&gt;Classic Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/DocsObtainAccessToken target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;, for &lt;b&gt;ARM Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/vi-classic-access-token target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

**object**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> object create_project(location, account_id, body=body, x_ms_client_request_id=x_ms_client_request_id, access_token=access_token)

Create Project

Creates a new project. Projects can be empty, e.g. a not have video ranges, but such projects can't be rendered

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
api_instance = videoindexer.ProjectsApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
body = {
  "name" : "My project",
  "videosRanges" : [ {
    "range" : {
      "end" : "2022-07-31",
      "start" : "2022-07-31"
    },
    "videoId" : "3a9220459b"
  }, {
    "range" : {
      "end" : "2022-07-31",
      "start" : "2022-07-31"
    },
    "videoId" : "3a9220459b"
  }, {
    "range" : {
      "end" : "2022-07-31",
      "start" : "2022-07-31"
    },
    "videoId" : "6b3948578"
  } ]
} # object | The request body consists of the video ranges that make the project and the project name (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account</b> and permission should be <b>Contributor</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)

try:
    # Create Project
    api_response = api_instance.create_project(location, account_id, body=body, x_ms_client_request_id=x_ms_client_request_id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **body** | [**object**](object.md)| The request body consists of the video ranges that make the project and the project name | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 
 **access_token** | **str**| Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be &lt;b&gt;Account&lt;/b&gt; and permission should be &lt;b&gt;Contributor&lt;/b&gt;.&lt;br&gt;  Note that Access tokens expire within 1 hour&lt;br&gt; See more details for &lt;b&gt;Classic Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/DocsObtainAccessToken target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;, for &lt;b&gt;ARM Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/vi-classic-access-token target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | [optional] 

### Return type

**object**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(location, account_id, project_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Delete Project

Deletes an existing project. If the project is rendered the rendered media file will be deleted as well.

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
api_instance = videoindexer.ProjectsApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
project_id = 'project_id_example' # str | The project id
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account/Project</b> and permission should be <b>Contributor</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Delete Project
    api_instance.delete_project(location, account_id, project_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **project_id** | **str**| The project id | 
 **access_token** | **str**| Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be &lt;b&gt;Account/Project&lt;/b&gt; and permission should be &lt;b&gt;Contributor&lt;/b&gt;.&lt;br&gt;  Note that Access tokens expire within 1 hour&lt;br&gt; See more details for &lt;b&gt;Classic Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/DocsObtainAccessToken target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;, for &lt;b&gt;ARM Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/vi-classic-access-token target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_project_rendered_file_url**
> object download_project_rendered_file_url(location, account_id, project_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Download Project Rendered File Url

Gets a download url for the media file of an existing project that is rendered. Can be used to download the rendered media file, and also to index it as a new independent video by using the API to upload a video from URL.

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
api_instance = videoindexer.ProjectsApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
project_id = 'project_id_example' # str | The project id
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account/Project</b> and permission should be <b>Reader</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Download Project Rendered File Url
    api_response = api_instance.download_project_rendered_file_url(location, account_id, project_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->download_project_rendered_file_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **project_id** | **str**| The project id | 
 **access_token** | **str**| Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be &lt;b&gt;Account/Project&lt;/b&gt; and permission should be &lt;b&gt;Reader&lt;/b&gt;.&lt;br&gt;  Note that Access tokens expire within 1 hour&lt;br&gt; See more details for &lt;b&gt;Classic Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/DocsObtainAccessToken target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;, for &lt;b&gt;ARM Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/vi-classic-access-token target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

**object**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_captions**
> object get_project_captions(location, account_id, project_id, index_id=index_id, format=format, language=language, include_audio_effects=include_audio_effects, include_speakers=include_speakers, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Get Project Captions

Get project captions

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
api_instance = videoindexer.ProjectsApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
project_id = 'project_id_example' # str | The project id
index_id = 'index_id_example' # str | The video id (optional)
format = 'Vtt' # str | The captions format. Allowed values: Vtt / Ttml / Srt / Txt / Csv (optional) (default to Vtt)
language = 'language_example' # str | The language of the captions. Supported languages: Afrikaans: af-ZA, Arabic (United Arab Emirates): ar-AE, Arabic Modern Standard (Bahrain): ar-BH, Arabic Egypt: ar-EG, Arabic (Israel): ar-IL, Arabic (Iraq): ar-IQ, Arabic (Jordan): ar-JO, Arabic (Kuwait): ar-KW, Arabic (Lebanon): ar-LB, Arabic (Oman): ar-OM, Arabic (Palestinian Authority): ar-PS, Arabic (Qatar): ar-QA, Arabic (Saudi Arabia): ar-SA, Arabic Syrian Arab Republic: ar-SY, Bulgarian: bg-BG, Bangla: bn-BD, Bosnian: bs-Latn, Catalan: ca-ES, Czech: cs-CZ, Danish: da-DK, German: de-DE, Greek: el-GR, English Australia: en-AU, Fijian: en-FJ, English United Kingdom: en-GB, English United States: en-US, Samoan: en-WS, Spanish: es-ES, Spanish (Mexico): es-MX, Estonian: et-EE, Persian: fa-IR, Finnish: fi-FI, Filipino: fil-PH, French (Canada): fr-CA, French: fr-FR, Haitian: fr-HT, Hebrew: he-IL, Hindi: hi-IN, Croatian: hr-HR, Hungarian: hu-HU, Indonesian: id-ID, Italian: it-IT, Japanese: ja-JP, Korean: ko-KR, Lithuanian: lt-LT, Latvian: lv-LV, Malagasy: mg-MG, Malay: ms-MY, Maltese: mt-MT, Norwegian: nb-NO, Dutch: nl-NL, Polish: pl-PL, Portuguese: pt-BR, Portuguese (Portugal): pt-PT, Romanian: ro-RO, Russian: ru-RU, Slovak: sk-SK, Slovenian: sl-SI, Serbian (Cyrillic): sr-Cyrl-RS, Serbian (Latin): sr-Latn-RS, Swedish: sv-SE, Kiswahili: sw-KE, Tamil: ta-IN, Thai: th-TH, Tongan: to-TO, Turkish: tr-TR, Ukrainian: uk-UA, Urdu: ur-PK, Vietnamese: vi-VN, Chinese (Simplified): zh-Hans, Chinese (Traditional): zh-Hant, Chinese (Cantonese, Traditional): zh-HK. (optional)
include_audio_effects = false # bool | Include audio effects (optional) (default to false)
include_speakers = false # bool | Include speakers (optional) (default to false)
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account/Project</b> and permission should be <b>Reader</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Get Project Captions
    api_response = api_instance.get_project_captions(location, account_id, project_id, index_id=index_id, format=format, language=language, include_audio_effects=include_audio_effects, include_speakers=include_speakers, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_project_captions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **project_id** | **str**| The project id | 
 **index_id** | **str**| The video id | [optional] 
 **format** | **str**| The captions format. Allowed values: Vtt / Ttml / Srt / Txt / Csv | [optional] [default to Vtt]
 **language** | **str**| The language of the captions. Supported languages: Afrikaans: af-ZA, Arabic (United Arab Emirates): ar-AE, Arabic Modern Standard (Bahrain): ar-BH, Arabic Egypt: ar-EG, Arabic (Israel): ar-IL, Arabic (Iraq): ar-IQ, Arabic (Jordan): ar-JO, Arabic (Kuwait): ar-KW, Arabic (Lebanon): ar-LB, Arabic (Oman): ar-OM, Arabic (Palestinian Authority): ar-PS, Arabic (Qatar): ar-QA, Arabic (Saudi Arabia): ar-SA, Arabic Syrian Arab Republic: ar-SY, Bulgarian: bg-BG, Bangla: bn-BD, Bosnian: bs-Latn, Catalan: ca-ES, Czech: cs-CZ, Danish: da-DK, German: de-DE, Greek: el-GR, English Australia: en-AU, Fijian: en-FJ, English United Kingdom: en-GB, English United States: en-US, Samoan: en-WS, Spanish: es-ES, Spanish (Mexico): es-MX, Estonian: et-EE, Persian: fa-IR, Finnish: fi-FI, Filipino: fil-PH, French (Canada): fr-CA, French: fr-FR, Haitian: fr-HT, Hebrew: he-IL, Hindi: hi-IN, Croatian: hr-HR, Hungarian: hu-HU, Indonesian: id-ID, Italian: it-IT, Japanese: ja-JP, Korean: ko-KR, Lithuanian: lt-LT, Latvian: lv-LV, Malagasy: mg-MG, Malay: ms-MY, Maltese: mt-MT, Norwegian: nb-NO, Dutch: nl-NL, Polish: pl-PL, Portuguese: pt-BR, Portuguese (Portugal): pt-PT, Romanian: ro-RO, Russian: ru-RU, Slovak: sk-SK, Slovenian: sl-SI, Serbian (Cyrillic): sr-Cyrl-RS, Serbian (Latin): sr-Latn-RS, Swedish: sv-SE, Kiswahili: sw-KE, Tamil: ta-IN, Thai: th-TH, Tongan: to-TO, Turkish: tr-TR, Ukrainian: uk-UA, Urdu: ur-PK, Vietnamese: vi-VN, Chinese (Simplified): zh-Hans, Chinese (Traditional): zh-Hant, Chinese (Cantonese, Traditional): zh-HK. | [optional] 
 **include_audio_effects** | **bool**| Include audio effects | [optional] [default to false]
 **include_speakers** | **bool**| Include speakers | [optional] [default to false]
 **access_token** | **str**| Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be &lt;b&gt;Account/Project&lt;/b&gt; and permission should be &lt;b&gt;Reader&lt;/b&gt;.&lt;br&gt;  Note that Access tokens expire within 1 hour&lt;br&gt; See more details for &lt;b&gt;Classic Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/DocsObtainAccessToken target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;, for &lt;b&gt;ARM Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/vi-classic-access-token target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

**object**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_index**
> object get_project_index(location, account_id, project_id, language=language, re_translate=re_translate, included_insights=included_insights, excluded_insights=excluded_insights, include_summarized_insights=include_summarized_insights, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Get Project Index

Get an existing project's index, which includes indices of all project's source videos, and if the project is rendered then render info that enables streaming in a player is included in the response

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
api_instance = videoindexer.ProjectsApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
project_id = 'project_id_example' # str | The project id
language = 'language_example' # str | The language to translate video insights. Supported languages: Afrikaans: af-ZA, Arabic (United Arab Emirates): ar-AE, Arabic Modern Standard (Bahrain): ar-BH, Arabic Egypt: ar-EG, Arabic (Israel): ar-IL, Arabic (Iraq): ar-IQ, Arabic (Jordan): ar-JO, Arabic (Kuwait): ar-KW, Arabic (Lebanon): ar-LB, Arabic (Oman): ar-OM, Arabic (Palestinian Authority): ar-PS, Arabic (Qatar): ar-QA, Arabic (Saudi Arabia): ar-SA, Arabic Syrian Arab Republic: ar-SY, Bulgarian: bg-BG, Bangla: bn-BD, Bosnian: bs-Latn, Catalan: ca-ES, Czech: cs-CZ, Danish: da-DK, German: de-DE, Greek: el-GR, English Australia: en-AU, Fijian: en-FJ, English United Kingdom: en-GB, English United States: en-US, Samoan: en-WS, Spanish: es-ES, Spanish (Mexico): es-MX, Estonian: et-EE, Persian: fa-IR, Finnish: fi-FI, Filipino: fil-PH, French (Canada): fr-CA, French: fr-FR, Haitian: fr-HT, Hebrew: he-IL, Hindi: hi-IN, Croatian: hr-HR, Hungarian: hu-HU, Indonesian: id-ID, Italian: it-IT, Japanese: ja-JP, Korean: ko-KR, Lithuanian: lt-LT, Latvian: lv-LV, Malagasy: mg-MG, Malay: ms-MY, Maltese: mt-MT, Norwegian: nb-NO, Dutch: nl-NL, Polish: pl-PL, Portuguese: pt-BR, Portuguese (Portugal): pt-PT, Romanian: ro-RO, Russian: ru-RU, Slovak: sk-SK, Slovenian: sl-SI, Serbian (Cyrillic): sr-Cyrl-RS, Serbian (Latin): sr-Latn-RS, Swedish: sv-SE, Kiswahili: sw-KE, Tamil: ta-IN, Thai: th-TH, Tongan: to-TO, Turkish: tr-TR, Ukrainian: uk-UA, Urdu: ur-PK, Vietnamese: vi-VN, Chinese (Simplified): zh-Hans, Chinese (Traditional): zh-Hant, Chinese (Cantonese, Traditional): zh-HK. (optional)
re_translate = false # bool | Indicates whether to re-translate the video insights and overwrite existing translation for the given language or leave existing translation. (optional) (default to false)
included_insights = 'included_insights_example' # str | Insights to include in the response. For example, to include only Transcript and Faces in the insights, pass the value 'Transcript,Faces'. Only array fields under the insights element are supported. An empty value will include all insights. (optional)
excluded_insights = 'excluded_insights_example' # str | Insights to exclude from the response. For example, to get all insights except Transcript and Faces, pass the value 'Transcript,Faces'. Only array fields under the insights element are supported. An empty value will exclude no insight. This query parameter cannot be provided if the 'includeInsights' parameter is provided. (optional)
include_summarized_insights = true # bool | Whether to include the deprecated SummarizedInsights field. It is recommended to pass 'false'. (optional) (default to true)
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account/Project</b> and permission should be <b>Reader</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Get Project Index
    api_response = api_instance.get_project_index(location, account_id, project_id, language=language, re_translate=re_translate, included_insights=included_insights, excluded_insights=excluded_insights, include_summarized_insights=include_summarized_insights, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_project_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **project_id** | **str**| The project id | 
 **language** | **str**| The language to translate video insights. Supported languages: Afrikaans: af-ZA, Arabic (United Arab Emirates): ar-AE, Arabic Modern Standard (Bahrain): ar-BH, Arabic Egypt: ar-EG, Arabic (Israel): ar-IL, Arabic (Iraq): ar-IQ, Arabic (Jordan): ar-JO, Arabic (Kuwait): ar-KW, Arabic (Lebanon): ar-LB, Arabic (Oman): ar-OM, Arabic (Palestinian Authority): ar-PS, Arabic (Qatar): ar-QA, Arabic (Saudi Arabia): ar-SA, Arabic Syrian Arab Republic: ar-SY, Bulgarian: bg-BG, Bangla: bn-BD, Bosnian: bs-Latn, Catalan: ca-ES, Czech: cs-CZ, Danish: da-DK, German: de-DE, Greek: el-GR, English Australia: en-AU, Fijian: en-FJ, English United Kingdom: en-GB, English United States: en-US, Samoan: en-WS, Spanish: es-ES, Spanish (Mexico): es-MX, Estonian: et-EE, Persian: fa-IR, Finnish: fi-FI, Filipino: fil-PH, French (Canada): fr-CA, French: fr-FR, Haitian: fr-HT, Hebrew: he-IL, Hindi: hi-IN, Croatian: hr-HR, Hungarian: hu-HU, Indonesian: id-ID, Italian: it-IT, Japanese: ja-JP, Korean: ko-KR, Lithuanian: lt-LT, Latvian: lv-LV, Malagasy: mg-MG, Malay: ms-MY, Maltese: mt-MT, Norwegian: nb-NO, Dutch: nl-NL, Polish: pl-PL, Portuguese: pt-BR, Portuguese (Portugal): pt-PT, Romanian: ro-RO, Russian: ru-RU, Slovak: sk-SK, Slovenian: sl-SI, Serbian (Cyrillic): sr-Cyrl-RS, Serbian (Latin): sr-Latn-RS, Swedish: sv-SE, Kiswahili: sw-KE, Tamil: ta-IN, Thai: th-TH, Tongan: to-TO, Turkish: tr-TR, Ukrainian: uk-UA, Urdu: ur-PK, Vietnamese: vi-VN, Chinese (Simplified): zh-Hans, Chinese (Traditional): zh-Hant, Chinese (Cantonese, Traditional): zh-HK. | [optional] 
 **re_translate** | **bool**| Indicates whether to re-translate the video insights and overwrite existing translation for the given language or leave existing translation. | [optional] [default to false]
 **included_insights** | **str**| Insights to include in the response. For example, to include only Transcript and Faces in the insights, pass the value &#x27;Transcript,Faces&#x27;. Only array fields under the insights element are supported. An empty value will include all insights. | [optional] 
 **excluded_insights** | **str**| Insights to exclude from the response. For example, to get all insights except Transcript and Faces, pass the value &#x27;Transcript,Faces&#x27;. Only array fields under the insights element are supported. An empty value will exclude no insight. This query parameter cannot be provided if the &#x27;includeInsights&#x27; parameter is provided. | [optional] 
 **include_summarized_insights** | **bool**| Whether to include the deprecated SummarizedInsights field. It is recommended to pass &#x27;false&#x27;. | [optional] [default to true]
 **access_token** | **str**| Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be &lt;b&gt;Account/Project&lt;/b&gt; and permission should be &lt;b&gt;Reader&lt;/b&gt;.&lt;br&gt;  Note that Access tokens expire within 1 hour&lt;br&gt; See more details for &lt;b&gt;Classic Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/DocsObtainAccessToken target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;, for &lt;b&gt;ARM Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/vi-classic-access-token target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

**object**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_insights_widget**
> get_project_insights_widget(location, account_id, project_id, widget_type=widget_type, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Get Project Insights Widget

Get Project Insights Widget

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
api_instance = videoindexer.ProjectsApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
project_id = 'project_id_example' # str | The project id
widget_type = NULL # list | The type of widgets to include. Allowed values: People / Sentiments / Keywords / Search (optional)
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Project</b> and permission should be <b>Reader</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Get Project Insights Widget
    api_instance.get_project_insights_widget(location, account_id, project_id, widget_type=widget_type, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_project_insights_widget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **project_id** | **str**| The project id | 
 **widget_type** | [**list**](.md)| The type of widgets to include. Allowed values: People / Sentiments / Keywords / Search | [optional] 
 **access_token** | **str**| Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be &lt;b&gt;Project&lt;/b&gt; and permission should be &lt;b&gt;Reader&lt;/b&gt;.&lt;br&gt;  Note that Access tokens expire within 1 hour&lt;br&gt; See more details for &lt;b&gt;Classic Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/DocsObtainAccessToken target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;, for &lt;b&gt;ARM Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/vi-classic-access-token target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_player_widget**
> get_project_player_widget(location, account_id, project_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Get Project Player Widget

Get Project Player Widget

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
api_instance = videoindexer.ProjectsApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
project_id = 'project_id_example' # str | The project id
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Project</b> and permission should be <b>Reader</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Get Project Player Widget
    api_instance.get_project_player_widget(location, account_id, project_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_project_player_widget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **project_id** | **str**| The project id | 
 **access_token** | **str**| Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be &lt;b&gt;Project&lt;/b&gt; and permission should be &lt;b&gt;Reader&lt;/b&gt;.&lt;br&gt;  Note that Access tokens expire within 1 hour&lt;br&gt; See more details for &lt;b&gt;Classic Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/DocsObtainAccessToken target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;, for &lt;b&gt;ARM Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/vi-classic-access-token target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_render_operation**
> object get_project_render_operation(location, account_id, project_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Get Project Render Operation

Gets the render operation of an existing project that was requested to render. Meant to be used to check the status of an ongoing render operation following a successful request to render a project. A render operation can be in one of the following states: InProgress/Cancelling/Succeeded/Failed/Canceled:<br/>The state 'InProgress' is a non-terminal state that means the render operation is in progress, and cancellation can be requested using the cancellation API. While in this state, the project is render-locked, meaning until the render completes or cancellation is requested the project's video ranges can't be updated and it's not allowed to request render.<br/>The state 'Cancelling' is a non-terminal state that means that cancellation was requested for the render operation but it hasn't completed yet. In this state the project is no longer render-locked, so its video ranges can be updated and it's allowed to request render. From this state the project doesn't necessarily transition to the 'Canceled' state, since it's possible render already completed by the time the cancellation request was acknowledged.<br/>The state 'Canceled' is a terminal state that means that cancellation was requested for the render operation and the cancellation completed.<br/>The state 'Failed' is a terminal state that means that the render operation has completed with failure during processing. In that case the response body will contain error information.<br/>The state 'Succeeded' is a terminal state that means that the render operation has completed successfully. In that case the response body will contain the operation's result. A project is referred to as a rendered project if it has a render operation in this state.

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
api_instance = videoindexer.ProjectsApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
project_id = 'project_id_example' # str | The project id
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account/Project</b> and permission should be <b>Reader</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Get Project Render Operation
    api_response = api_instance.get_project_render_operation(location, account_id, project_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_project_render_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **project_id** | **str**| The project id | 
 **access_token** | **str**| Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be &lt;b&gt;Account/Project&lt;/b&gt; and permission should be &lt;b&gt;Reader&lt;/b&gt;.&lt;br&gt;  Note that Access tokens expire within 1 hour&lt;br&gt; See more details for &lt;b&gt;Classic Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/DocsObtainAccessToken target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;, for &lt;b&gt;ARM Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/vi-classic-access-token target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

**object**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_thumbnail**
> object get_project_thumbnail(location, account_id, project_id, thumbnail_id, format=format, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Get Project Thumbnail

Get thumbnail of a project

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
api_instance = videoindexer.ProjectsApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
project_id = 'project_id_example' # str | The project id
thumbnail_id = 'thumbnail_id_example' # str | Format - guid. Thumbnail id
format = 'Jpeg' # str | Thumbnail format. Allowed values: Jpeg / Base64 (optional) (default to Jpeg)
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account/Project</b> and permission should be <b>Reader</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Get Project Thumbnail
    api_response = api_instance.get_project_thumbnail(location, account_id, project_id, thumbnail_id, format=format, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_project_thumbnail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **project_id** | **str**| The project id | 
 **thumbnail_id** | **str**| Format - guid. Thumbnail id | 
 **format** | **str**| Thumbnail format. Allowed values: Jpeg / Base64 | [optional] [default to Jpeg]
 **access_token** | **str**| Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be &lt;b&gt;Account/Project&lt;/b&gt; and permission should be &lt;b&gt;Reader&lt;/b&gt;.&lt;br&gt;  Note that Access tokens expire within 1 hour&lt;br&gt; See more details for &lt;b&gt;Classic Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/DocsObtainAccessToken target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;, for &lt;b&gt;ARM Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/vi-classic-access-token target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

**object**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_project**
> object render_project(location, account_id, project_id, send_completion_email=send_completion_email, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Render Project

Renders a media file for an existing project. If the project is already rendered the response body will include the last render operation result, otherwise an asynchronous render operation will start and a 202 Accepted response will be returned and then you can poll for the operation's status by using the API to get a project's render operation.<br/>A project can have a single ongoing render operation at a time, therefore requesting a project render is not allowed if there's already an ongoing render operation. Additionally, while a project is ongoing rendering it's not allowed to update its video ranges, you can use the cancellation API to cancel an ongoing render operation in order to be allowed to update the project's video ranges.

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
api_instance = videoindexer.ProjectsApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
project_id = 'project_id_example' # str | The project id
send_completion_email = false # bool | An indication whether to send a mail when the render operation completes, whether it completed successfully or with failure or it was canceled. (optional) (default to false)
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account</b> and permission should be <b>Contributor</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Render Project
    api_response = api_instance.render_project(location, account_id, project_id, send_completion_email=send_completion_email, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->render_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **project_id** | **str**| The project id | 
 **send_completion_email** | **bool**| An indication whether to send a mail when the render operation completes, whether it completed successfully or with failure or it was canceled. | [optional] [default to false]
 **access_token** | **str**| Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be &lt;b&gt;Account&lt;/b&gt; and permission should be &lt;b&gt;Contributor&lt;/b&gt;.&lt;br&gt;  Note that Access tokens expire within 1 hour&lt;br&gt; See more details for &lt;b&gt;Classic Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/DocsObtainAccessToken target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;, for &lt;b&gt;ARM Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/vi-classic-access-token target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

**object**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> object update_project(location, account_id, project_id, body=body, x_ms_client_request_id=x_ms_client_request_id, access_token=access_token)

Update Project

Updates an existing project. If the project has an ongoing render operation, updating its video ranges isn't allowed; you can use the cancellation API to cancel the render operation so video ranges update is allowed.<br/>If the project's video ranges are updated, it resets any render information available for the project, which means it will no longer be possible to get the project's render operation, and if the project has a rendered media file it will be deleted and no longer be available for download.

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
api_instance = videoindexer.ProjectsApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
project_id = 'project_id_example' # str | The project id
body = {
  "name" : "My project",
  "videosRanges" : [ {
    "range" : {
      "end" : "2022-07-31",
      "start" : "2022-07-31"
    },
    "videoId" : "3a9220459b"
  }, {
    "range" : {
      "end" : "2022-07-31",
      "start" : "2022-07-31"
    },
    "videoId" : "3a9220459b"
  }, {
    "range" : {
      "end" : "2022-07-31",
      "start" : "2022-07-31"
    },
    "videoId" : "6b3948578"
  } ]
} # object | The request body consists of the video ranges that make the project and the project name (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account</b> and permission should be <b>Contributor</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)

try:
    # Update Project
    api_response = api_instance.update_project(location, account_id, project_id, body=body, x_ms_client_request_id=x_ms_client_request_id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **project_id** | **str**| The project id | 
 **body** | [**object**](object.md)| The request body consists of the video ranges that make the project and the project name | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 
 **access_token** | **str**| Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be &lt;b&gt;Account&lt;/b&gt; and permission should be &lt;b&gt;Contributor&lt;/b&gt;.&lt;br&gt;  Note that Access tokens expire within 1 hour&lt;br&gt; See more details for &lt;b&gt;Classic Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/DocsObtainAccessToken target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;, for &lt;b&gt;ARM Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/vi-classic-access-token target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | [optional] 

### Return type

**object**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

