# videoindexer.WidgetsApi

All URIs are relative to *https://api.videoindexer.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_video_insights_widget**](WidgetsApi.md#get_video_insights_widget) | **GET** /{location}/Accounts/{accountId}/Videos/{videoId}/InsightsWidget | Get Video Insights Widget
[**get_video_player_widget**](WidgetsApi.md#get_video_player_widget) | **GET** /{location}/Accounts/{accountId}/Videos/{videoId}/PlayerWidget | Get Video Player Widget

# **get_video_insights_widget**
> get_video_insights_widget(location, account_id, video_id, widget_type=widget_type, allow_edit=allow_edit, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Get Video Insights Widget

Get Video Insights Widget

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
api_instance = videoindexer.WidgetsApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
video_id = 'video_id_example' # str | The video id
widget_type = NULL # list | The type of widgets to include. Allowed values: People / Sentiments / Keywords / Search (optional)
allow_edit = false # bool | Whether the widget allows editing of the insights (optional) (default to false)
access_token = 'access_token_example' # str | Required for private videos or if edit should be allowed. Reader or Contributor depending on whether widget should allow edit.<br>  Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Video</b> and permission should be <b>Reader/Contributor</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Get Video Insights Widget
    api_instance.get_video_insights_widget(location, account_id, video_id, widget_type=widget_type, allow_edit=allow_edit, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
except ApiException as e:
    print("Exception when calling WidgetsApi->get_video_insights_widget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **video_id** | **str**| The video id | 
 **widget_type** | [**list**](.md)| The type of widgets to include. Allowed values: People / Sentiments / Keywords / Search | [optional] 
 **allow_edit** | **bool**| Whether the widget allows editing of the insights | [optional] [default to false]
 **access_token** | **str**| Required for private videos or if edit should be allowed. Reader or Contributor depending on whether widget should allow edit.&lt;br&gt;  Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be &lt;b&gt;Video&lt;/b&gt; and permission should be &lt;b&gt;Reader/Contributor&lt;/b&gt;.&lt;br&gt;  Note that Access tokens expire within 1 hour&lt;br&gt; See more details for &lt;b&gt;Classic Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/DocsObtainAccessToken target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;, for &lt;b&gt;ARM Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/vi-classic-access-token target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video_player_widget**
> get_video_player_widget(location, account_id, video_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Get Video Player Widget

Get Video Player Widget

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
api_instance = videoindexer.WidgetsApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
video_id = 'video_id_example' # str | The video id
access_token = 'access_token_example' # str | Required for private videos<br>  Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Video</b> and permission should be <b>Reader</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Get Video Player Widget
    api_instance.get_video_player_widget(location, account_id, video_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
except ApiException as e:
    print("Exception when calling WidgetsApi->get_video_player_widget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **video_id** | **str**| The video id | 
 **access_token** | **str**| Required for private videos&lt;br&gt;  Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be &lt;b&gt;Video&lt;/b&gt; and permission should be &lt;b&gt;Reader&lt;/b&gt;.&lt;br&gt;  Note that Access tokens expire within 1 hour&lt;br&gt; See more details for &lt;b&gt;Classic Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/DocsObtainAccessToken target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;, for &lt;b&gt;ARM Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/vi-classic-access-token target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

