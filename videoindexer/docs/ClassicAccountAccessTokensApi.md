# videoindexer.ClassicAccountAccessTokensApi

All URIs are relative to *https://api.videoindexer.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_access_token**](ClassicAccountAccessTokensApi.md#get_account_access_token) | **GET** /Auth/{location}/Accounts/{accountId}/AccessToken | Get Account Access Token
[**get_account_access_token_with_permission**](ClassicAccountAccessTokensApi.md#get_account_access_token_with_permission) | **GET** /Auth/{location}/Accounts/{accountId}/AccessTokenWithPermission | Get Account Access Token With Permission (PREVIEW)
[**get_accounts_authorization**](ClassicAccountAccessTokensApi.md#get_accounts_authorization) | **GET** /Auth/{location}/Accounts | Get Accounts Authorization
[**get_project_access_token**](ClassicAccountAccessTokensApi.md#get_project_access_token) | **GET** /Auth/{location}/Accounts/{accountId}/Projects/{projectId}/AccessToken | Get Project Access Token
[**get_user_access_token**](ClassicAccountAccessTokensApi.md#get_user_access_token) | **GET** /Auth/{location}/Users/me/AccessToken | Get User Access Token
[**get_video_access_token**](ClassicAccountAccessTokensApi.md#get_video_access_token) | **GET** /Auth/{location}/Accounts/{accountId}/Videos/{videoId}/AccessToken | Get Video Access Token

# **get_account_access_token**
> object get_account_access_token(location, account_id, allow_edit=allow_edit, x_ms_client_request_id=x_ms_client_request_id)

Get Account Access Token

Gets an account access token

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
api_instance = videoindexer.ClassicAccountAccessTokensApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
allow_edit = false # bool | Determines the token's permission. 'false' is the equivalent of a Reader permission (read-only) and 'true' is the equivalent of a Contributor permission (read-write). (optional) (default to false)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Get Account Access Token
    api_response = api_instance.get_account_access_token(location, account_id, allow_edit=allow_edit, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassicAccountAccessTokensApi->get_account_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **allow_edit** | **bool**| Determines the token&#x27;s permission. &#x27;false&#x27; is the equivalent of a Reader permission (read-only) and &#x27;true&#x27; is the equivalent of a Contributor permission (read-write). | [optional] [default to false]
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

**object**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_access_token_with_permission**
> object get_account_access_token_with_permission(location, account_id, permission=permission, x_ms_client_request_id=x_ms_client_request_id)

Get Account Access Token With Permission (PREVIEW)

This API is a preview API subject to preview terms available <a href=\"https://aka.ms/vi-api-preview-terms\" target=\"_blank\">here</a>. It’s not final and might change.<br/>Gets an account access token with permission

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
api_instance = videoindexer.ClassicAccountAccessTokensApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
permission = 'permission_example' # str | The requested permission. Allowed values: Reader (allows reading content) / Contributor (allows modifying content) / MyAccessAdministrator (allows managing the acting user's permission) / Owner (allows managing permissions and modifying content) (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Get Account Access Token With Permission (PREVIEW)
    api_response = api_instance.get_account_access_token_with_permission(location, account_id, permission=permission, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassicAccountAccessTokensApi->get_account_access_token_with_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **permission** | **str**| The requested permission. Allowed values: Reader (allows reading content) / Contributor (allows modifying content) / MyAccessAdministrator (allows managing the acting user&#x27;s permission) / Owner (allows managing permissions and modifying content) | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

**object**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts_authorization**
> object get_accounts_authorization(location, generate_access_tokens=generate_access_tokens, allow_edit=allow_edit, x_ms_client_request_id=x_ms_client_request_id)

Get Accounts Authorization

Get Accounts, authentication by subscription key

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
api_instance = videoindexer.ClassicAccountAccessTokensApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
generate_access_tokens = false # bool | Whether to generate an access token for each account. (optional) (default to false)
allow_edit = false # bool | Determines the token's permission. 'false' is the equivalent of a Reader permission (read-only) and 'true' is the equivalent of a Contributor permission (read-write). (optional) (default to false)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Get Accounts Authorization
    api_response = api_instance.get_accounts_authorization(location, generate_access_tokens=generate_access_tokens, allow_edit=allow_edit, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassicAccountAccessTokensApi->get_accounts_authorization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **generate_access_tokens** | **bool**| Whether to generate an access token for each account. | [optional] [default to false]
 **allow_edit** | **bool**| Determines the token&#x27;s permission. &#x27;false&#x27; is the equivalent of a Reader permission (read-only) and &#x27;true&#x27; is the equivalent of a Contributor permission (read-write). | [optional] [default to false]
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

**object**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_access_token**
> object get_project_access_token(location, account_id, project_id, allow_edit=allow_edit, x_ms_client_request_id=x_ms_client_request_id)

Get Project Access Token

Gets a project access token

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
api_instance = videoindexer.ClassicAccountAccessTokensApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
project_id = 'project_id_example' # str | The project id
allow_edit = true # bool | Determines the token's permission. 'false' is the equivalent of a Reader permission (read-only) and 'true' is the equivalent of a Contributor permission (read-write). When not specified, it will be determined by whether the current user has read-write permissions. (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Get Project Access Token
    api_response = api_instance.get_project_access_token(location, account_id, project_id, allow_edit=allow_edit, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassicAccountAccessTokensApi->get_project_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **project_id** | **str**| The project id | 
 **allow_edit** | **bool**| Determines the token&#x27;s permission. &#x27;false&#x27; is the equivalent of a Reader permission (read-only) and &#x27;true&#x27; is the equivalent of a Contributor permission (read-write). When not specified, it will be determined by whether the current user has read-write permissions. | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

**object**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_access_token**
> object get_user_access_token(location, allow_edit=allow_edit, x_ms_client_request_id=x_ms_client_request_id)

Get User Access Token

Gets a user access token

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
api_instance = videoindexer.ClassicAccountAccessTokensApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
allow_edit = false # bool | Determines the token's permission. 'false' is the equivalent of a Reader permission (read-only) and 'true' is the equivalent of a Contributor permission (read-write). (optional) (default to false)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Get User Access Token
    api_response = api_instance.get_user_access_token(location, allow_edit=allow_edit, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassicAccountAccessTokensApi->get_user_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **allow_edit** | **bool**| Determines the token&#x27;s permission. &#x27;false&#x27; is the equivalent of a Reader permission (read-only) and &#x27;true&#x27; is the equivalent of a Contributor permission (read-write). | [optional] [default to false]
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

**object**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video_access_token**
> object get_video_access_token(location, account_id, video_id, allow_edit=allow_edit, x_ms_client_request_id=x_ms_client_request_id)

Get Video Access Token

Gets a video access token

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
api_instance = videoindexer.ClassicAccountAccessTokensApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
video_id = 'video_id_example' # str | The video id
allow_edit = true # bool | Determines the token's permission. 'false' is the equivalent of a Reader permission (read-only) and 'true' is the equivalent of a Contributor permission (read-write). When not specified, it will be determined by whether the current user has read-write permissions. (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Get Video Access Token
    api_response = api_instance.get_video_access_token(location, account_id, video_id, allow_edit=allow_edit, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassicAccountAccessTokensApi->get_video_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **video_id** | **str**| The video id | 
 **allow_edit** | **bool**| Determines the token&#x27;s permission. &#x27;false&#x27; is the equivalent of a Reader permission (read-only) and &#x27;true&#x27; is the equivalent of a Contributor permission (read-write). When not specified, it will be determined by whether the current user has read-write permissions. | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

**object**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

