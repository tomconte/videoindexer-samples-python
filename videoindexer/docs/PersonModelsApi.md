# videoindexer.PersonModelsApi

All URIs are relative to *https://api.videoindexer.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_face**](PersonModelsApi.md#create_custom_face) | **POST** /{location}/Accounts/{accountId}/Customization/PersonModels/{personModelId}/Persons/{personId}/Faces | Create Custom Face
[**create_person**](PersonModelsApi.md#create_person) | **POST** /{location}/Accounts/{accountId}/Customization/PersonModels/{personModelId}/Persons | Create Person
[**create_person_model**](PersonModelsApi.md#create_person_model) | **POST** /{location}/Accounts/{accountId}/Customization/PersonModels | Create Person Model
[**delete_custom_face**](PersonModelsApi.md#delete_custom_face) | **DELETE** /{location}/Accounts/{accountId}/Customization/PersonModels/{personModelId}/Persons/{personId}/Faces/{faceId} | Delete Custom Face
[**delete_person**](PersonModelsApi.md#delete_person) | **DELETE** /{location}/Accounts/{accountId}/Customization/PersonModels/{personModelId}/Persons/{personId} | Delete Person
[**delete_person_model**](PersonModelsApi.md#delete_person_model) | **DELETE** /{location}/Accounts/{accountId}/Customization/PersonModels/{personModelId} | Delete Person Model
[**get_custom_face_picture**](PersonModelsApi.md#get_custom_face_picture) | **GET** /{location}/Accounts/{accountId}/Customization/PersonModels/{personModelId}/Persons/{personId}/Faces/{faceId} | Get Custom Face Picture
[**get_custom_faces**](PersonModelsApi.md#get_custom_faces) | **GET** /{location}/Accounts/{accountId}/Customization/PersonModels/{personModelId}/Persons/{personId}/Faces | Get Custom Faces
[**get_custom_faces_sprite**](PersonModelsApi.md#get_custom_faces_sprite) | **GET** /{location}/Accounts/{accountId}/Customization/PersonModels/{personModelId}/Persons/{personId}/Faces/sprite | Get Custom Faces Sprite
[**get_person_models**](PersonModelsApi.md#get_person_models) | **GET** /{location}/Accounts/{accountId}/Customization/PersonModels | Get Person Models
[**get_persons**](PersonModelsApi.md#get_persons) | **GET** /{location}/Accounts/{accountId}/Customization/PersonModels/{personModelId}/Persons | Get Persons
[**update_person**](PersonModelsApi.md#update_person) | **PUT** /{location}/Accounts/{accountId}/Customization/PersonModels/{personModelId}/Persons/{personId} | Update Person
[**update_person_model**](PersonModelsApi.md#update_person_model) | **PUT** /{location}/Accounts/{accountId}/Customization/PersonModels/{personModelId} | Update Person Model

# **create_custom_face**
> object create_custom_face(location, account_id, person_model_id, person_id, body=body, x_ms_client_request_id=x_ms_client_request_id, access_token=access_token)

Create Custom Face

Creates new faces in the specified person.

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
api_instance = videoindexer.PersonModelsApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
person_model_id = 'person_model_id_example' # str | Format - guid. The person model id
person_id = 'person_id_example' # str | Format - guid. The person id
body = {
  "urls" : [ "https://www.myserver.com/pictures/picture_1", "https://www.myserver.com/pictures/picture_2", "https://www.myserver.com/pictures/picture_3" ]
} # object |  (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account</b> and permission should be <b>Contributor</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)

try:
    # Create Custom Face
    api_response = api_instance.create_custom_face(location, account_id, person_model_id, person_id, body=body, x_ms_client_request_id=x_ms_client_request_id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonModelsApi->create_custom_face: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **person_model_id** | **str**| Format - guid. The person model id | 
 **person_id** | **str**| Format - guid. The person id | 
 **body** | [**object**](object.md)|  | [optional] 
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

# **create_person**
> object create_person(location, account_id, person_model_id, name=name, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Create Person

Creates a new person in the specified person model.

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
api_instance = videoindexer.PersonModelsApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
person_model_id = 'person_model_id_example' # str | Format - guid. The person model id
name = 'name_example' # str | The new person name (optional)
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account</b> and permission should be <b>Contributor</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Create Person
    api_response = api_instance.create_person(location, account_id, person_model_id, name=name, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonModelsApi->create_person: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **person_model_id** | **str**| Format - guid. The person model id | 
 **name** | **str**| The new person name | [optional] 
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

# **create_person_model**
> object create_person_model(location, account_id, name=name, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Create Person Model

Creates a new person model in the specified account.

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
api_instance = videoindexer.PersonModelsApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
name = 'name_example' # str | The person model name (optional)
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account</b> and permission should be <b>Contributor</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Create Person Model
    api_response = api_instance.create_person_model(location, account_id, name=name, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonModelsApi->create_person_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **name** | **str**| The person model name | [optional] 
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

# **delete_custom_face**
> delete_custom_face(location, account_id, person_model_id, person_id, face_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Delete Custom Face

Deletes the given face.

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
api_instance = videoindexer.PersonModelsApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
person_model_id = 'person_model_id_example' # str | Format - guid. The person model id
person_id = 'person_id_example' # str | Format - guid. The person id
face_id = 'face_id_example' # str | Format - guid. The face id
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account</b> and permission should be <b>Contributor</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Delete Custom Face
    api_instance.delete_custom_face(location, account_id, person_model_id, person_id, face_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
except ApiException as e:
    print("Exception when calling PersonModelsApi->delete_custom_face: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **person_model_id** | **str**| Format - guid. The person model id | 
 **person_id** | **str**| Format - guid. The person id | 
 **face_id** | **str**| Format - guid. The face id | 
 **access_token** | **str**| Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be &lt;b&gt;Account&lt;/b&gt; and permission should be &lt;b&gt;Contributor&lt;/b&gt;.&lt;br&gt;  Note that Access tokens expire within 1 hour&lt;br&gt; See more details for &lt;b&gt;Classic Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/DocsObtainAccessToken target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;, for &lt;b&gt;ARM Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/vi-classic-access-token target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_person**
> delete_person(location, account_id, person_model_id, person_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Delete Person

Deletes the given person.

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
api_instance = videoindexer.PersonModelsApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
person_model_id = 'person_model_id_example' # str | Format - guid. The person model id
person_id = 'person_id_example' # str | Format - guid. The person id
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account</b> and permission should be <b>Contributor</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Delete Person
    api_instance.delete_person(location, account_id, person_model_id, person_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
except ApiException as e:
    print("Exception when calling PersonModelsApi->delete_person: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **person_model_id** | **str**| Format - guid. The person model id | 
 **person_id** | **str**| Format - guid. The person id | 
 **access_token** | **str**| Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be &lt;b&gt;Account&lt;/b&gt; and permission should be &lt;b&gt;Contributor&lt;/b&gt;.&lt;br&gt;  Note that Access tokens expire within 1 hour&lt;br&gt; See more details for &lt;b&gt;Classic Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/DocsObtainAccessToken target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;, for &lt;b&gt;ARM Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/vi-classic-access-token target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_person_model**
> delete_person_model(location, account_id, person_model_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Delete Person Model

Deletes the given person model.

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
api_instance = videoindexer.PersonModelsApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
person_model_id = 'person_model_id_example' # str | Format - guid. The person model id
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account</b> and permission should be <b>Contributor</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Delete Person Model
    api_instance.delete_person_model(location, account_id, person_model_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
except ApiException as e:
    print("Exception when calling PersonModelsApi->delete_person_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **person_model_id** | **str**| Format - guid. The person model id | 
 **access_token** | **str**| Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be &lt;b&gt;Account&lt;/b&gt; and permission should be &lt;b&gt;Contributor&lt;/b&gt;.&lt;br&gt;  Note that Access tokens expire within 1 hour&lt;br&gt; See more details for &lt;b&gt;Classic Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/DocsObtainAccessToken target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;, for &lt;b&gt;ARM Account&lt;/b&gt; &lt;a href&#x3D;https://aka.ms/vi-classic-access-token target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | [optional] 
 **x_ms_client_request_id** | **str**| Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_face_picture**
> object get_custom_face_picture(location, account_id, person_model_id, person_id, face_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Get Custom Face Picture

Gets the picture of the given face.

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
api_instance = videoindexer.PersonModelsApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
person_model_id = 'person_model_id_example' # str | Format - guid. The person model id
person_id = 'person_id_example' # str | Format - guid. The person id
face_id = 'face_id_example' # str | Format - guid. The face id
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account</b> and permission should be <b>Reader</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Get Custom Face Picture
    api_response = api_instance.get_custom_face_picture(location, account_id, person_model_id, person_id, face_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonModelsApi->get_custom_face_picture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **person_model_id** | **str**| Format - guid. The person model id | 
 **person_id** | **str**| Format - guid. The person id | 
 **face_id** | **str**| Format - guid. The face id | 
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

# **get_custom_faces**
> object get_custom_faces(location, account_id, person_model_id, person_id, page_size=page_size, skip=skip, source_type=source_type, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Get Custom Faces

Gets all the faces in the given person with the given source type.

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
api_instance = videoindexer.PersonModelsApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
person_model_id = 'person_model_id_example' # str | Format - guid. The person model id
person_id = 'person_id_example' # str | Format - guid. The person id
page_size = 25 # int | Format - int32. The number of results to return (optional) (default to 25)
skip = 0 # int | Format - int32. The number of results to skip (for paging) (optional) (default to 0)
source_type = 'source_type_example' # str | The face source type. Allowed values: UploadedPicture / UploadedVideo (optional)
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account</b> and permission should be <b>Reader</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Get Custom Faces
    api_response = api_instance.get_custom_faces(location, account_id, person_model_id, person_id, page_size=page_size, skip=skip, source_type=source_type, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonModelsApi->get_custom_faces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **person_model_id** | **str**| Format - guid. The person model id | 
 **person_id** | **str**| Format - guid. The person id | 
 **page_size** | **int**| Format - int32. The number of results to return | [optional] [default to 25]
 **skip** | **int**| Format - int32. The number of results to skip (for paging) | [optional] [default to 0]
 **source_type** | **str**| The face source type. Allowed values: UploadedPicture / UploadedVideo | [optional] 
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

# **get_custom_faces_sprite**
> object get_custom_faces_sprite(location, account_id, person_model_id, person_id, page_size=page_size, skip=skip, source_type=source_type, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Get Custom Faces Sprite

Gets a sprite of all the faces in the given person and with the given source type.

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
api_instance = videoindexer.PersonModelsApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
person_model_id = 'person_model_id_example' # str | Format - guid. The person model id
person_id = 'person_id_example' # str | Format - guid. The person id
page_size = 25 # int | Format - int32. The number of results to return (optional) (default to 25)
skip = 0 # int | Format - int32. The number of results to skip (for paging) (optional) (default to 0)
source_type = 'source_type_example' # str | The face source type. Allowed values: UploadedPicture / UploadedVideo (optional)
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account</b> and permission should be <b>Reader</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Get Custom Faces Sprite
    api_response = api_instance.get_custom_faces_sprite(location, account_id, person_model_id, person_id, page_size=page_size, skip=skip, source_type=source_type, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonModelsApi->get_custom_faces_sprite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **person_model_id** | **str**| Format - guid. The person model id | 
 **person_id** | **str**| Format - guid. The person id | 
 **page_size** | **int**| Format - int32. The number of results to return | [optional] [default to 25]
 **skip** | **int**| Format - int32. The number of results to skip (for paging) | [optional] [default to 0]
 **source_type** | **str**| The face source type. Allowed values: UploadedPicture / UploadedVideo | [optional] 
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

# **get_person_models**
> object get_person_models(location, account_id, person_name_prefix=person_name_prefix, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Get Person Models

Gets all person models with persons who start with the given prefix in the account.

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
api_instance = videoindexer.PersonModelsApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
person_name_prefix = 'person_name_prefix_example' # str | A person name prefix to search for (optional)
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account</b> and permission should be <b>Reader</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Get Person Models
    api_response = api_instance.get_person_models(location, account_id, person_name_prefix=person_name_prefix, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonModelsApi->get_person_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **person_name_prefix** | **str**| A person name prefix to search for | [optional] 
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

# **get_persons**
> object get_persons(location, account_id, person_model_id, name_prefix=name_prefix, page_size=page_size, skip=skip, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Get Persons

Gets all the persons that start with the given prefix in the given person model.

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
api_instance = videoindexer.PersonModelsApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
person_model_id = 'person_model_id_example' # str | Format - guid. The person model id
name_prefix = 'name_prefix_example' # str | A person name prefix to filter by (optional)
page_size = 25 # int | Format - int32. The number of results to return (optional) (default to 25)
skip = 0 # int | Format - int32. The number of results to skip (for paging) (optional) (default to 0)
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account</b> and permission should be <b>Reader</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Get Persons
    api_response = api_instance.get_persons(location, account_id, person_model_id, name_prefix=name_prefix, page_size=page_size, skip=skip, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonModelsApi->get_persons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **person_model_id** | **str**| Format - guid. The person model id | 
 **name_prefix** | **str**| A person name prefix to filter by | [optional] 
 **page_size** | **int**| Format - int32. The number of results to return | [optional] [default to 25]
 **skip** | **int**| Format - int32. The number of results to skip (for paging) | [optional] [default to 0]
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

# **update_person**
> object update_person(location, account_id, person_model_id, person_id, name=name, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Update Person

Update a person.

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
api_instance = videoindexer.PersonModelsApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
person_model_id = 'person_model_id_example' # str | Format - guid. The person model id
person_id = 'person_id_example' # str | Format - guid. The person id
name = 'name_example' # str | The person's new name (optional)
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account</b> and permission should be <b>Contributor</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Update Person
    api_response = api_instance.update_person(location, account_id, person_model_id, person_id, name=name, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonModelsApi->update_person: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **person_model_id** | **str**| Format - guid. The person model id | 
 **person_id** | **str**| Format - guid. The person id | 
 **name** | **str**| The person&#x27;s new name | [optional] 
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

# **update_person_model**
> object update_person_model(location, account_id, person_model_id, name=name, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Update Person Model

Update a person model.

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
api_instance = videoindexer.PersonModelsApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
person_model_id = 'person_model_id_example' # str | Format - guid. The person model id
name = 'name_example' # str | The person model new name (optional)
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account</b> and permission should be <b>Contributor</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Update Person Model
    api_response = api_instance.update_person_model(location, account_id, person_model_id, name=name, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonModelsApi->update_person_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **person_model_id** | **str**| Format - guid. The person model id | 
 **name** | **str**| The person model new name | [optional] 
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

