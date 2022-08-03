# videoindexer.LanguagesApi

All URIs are relative to *https://api.videoindexer.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_training_model**](LanguagesApi.md#cancel_training_model) | **DELETE** /{location}/Accounts/{accountId}/Customization/Language/{modelId}/Train | Cancel Training Model
[**create_language_model**](LanguagesApi.md#create_language_model) | **POST** /{location}/Accounts/{accountId}/Customization/Language | Create Language Model
[**delete_language_model**](LanguagesApi.md#delete_language_model) | **DELETE** /{location}/Accounts/{accountId}/Customization/Language/{modelId} | Delete Language Model
[**delete_language_model_file**](LanguagesApi.md#delete_language_model_file) | **DELETE** /{location}/Accounts/{accountId}/Customization/Language/{modelId}/Files/{fileId} | Delete Language Model File
[**download_language_model_file_content**](LanguagesApi.md#download_language_model_file_content) | **GET** /{location}/Accounts/{accountId}/Customization/Language/{modelId}/Files/{fileId}/download | Download Language Model File Content
[**get_language_model**](LanguagesApi.md#get_language_model) | **GET** /{location}/Accounts/{accountId}/Customization/Language/{modelId} | Get Language Model
[**get_language_model_edits_history**](LanguagesApi.md#get_language_model_edits_history) | **GET** /{location}/Accounts/{accountId}/Customization/Language/{modelId}/edits | Get Language Model Edits History (PREVIEW)
[**get_language_model_file_data**](LanguagesApi.md#get_language_model_file_data) | **GET** /{location}/Accounts/{accountId}/Customization/Language/{modelId}/Files/{fileId} | Get Language Model File Data
[**get_language_models**](LanguagesApi.md#get_language_models) | **GET** /{location}/Accounts/{accountId}/Customization/Language | Get Language Models
[**train_language_model**](LanguagesApi.md#train_language_model) | **PUT** /{location}/Accounts/{accountId}/Customization/Language/{modelId}/Train | Train Language Model
[**update_language_model**](LanguagesApi.md#update_language_model) | **PUT** /{location}/Accounts/{accountId}/Customization/Language/{modelId} | Update Language Model
[**update_language_model_file**](LanguagesApi.md#update_language_model_file) | **PUT** /{location}/Accounts/{accountId}/Customization/Language/{modelId}/Files/{fileId} | Update Language Model file

# **cancel_training_model**
> cancel_training_model(location, account_id, model_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Cancel Training Model

Cancel the training model operation.

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
api_instance = videoindexer.LanguagesApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
model_id = 'model_id_example' # str | Format - guid. Model id
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account</b> and permission should be <b>Contributor</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Cancel Training Model
    api_instance.cancel_training_model(location, account_id, model_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
except ApiException as e:
    print("Exception when calling LanguagesApi->cancel_training_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **model_id** | **str**| Format - guid. Model id | 
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

# **create_language_model**
> object create_language_model(location, account_id, model_name=model_name, language=language, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Create Language Model

Creates a language model. There are two ways to upload files in the body using form-data. 1. Key will be the file name and value will be the file. 2. Key will be the file name and value will be a URL to a txt/vtt/srt/ttml file.

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
api_instance = videoindexer.LanguagesApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
model_name = 'model_name_example' # str | Model name (optional)
language = 'language_example' # str | Model language. Supported languages: Arabic (United Arab Emirates): ar-AE, Arabic Modern Standard (Bahrain): ar-BH, Arabic Egypt: ar-EG, Arabic (Israel): ar-IL, Arabic (Iraq): ar-IQ, Arabic (Jordan): ar-JO, Arabic (Kuwait): ar-KW, Arabic (Lebanon): ar-LB, Arabic (Oman): ar-OM, Arabic (Palestinian Authority): ar-PS, Arabic (Qatar): ar-QA, Arabic (Saudi Arabia): ar-SA, Arabic Syrian Arab Republic: ar-SY, Czech: cs-CZ, Danish: da-DK, German: de-DE, English Australia: en-AU, English United Kingdom: en-GB, English United States: en-US, Spanish: es-ES, Spanish (Mexico): es-MX, Persian: fa-IR, Finnish: fi-FI, French (Canada): fr-CA, French: fr-FR, Hebrew: he-IL, Hindi: hi-IN, Italian: it-IT, Japanese: ja-JP, Korean: ko-KR, Norwegian: nb-NO, Dutch: nl-NL, Polish: pl-PL, Portuguese: pt-BR, Portuguese (Portugal): pt-PT, Russian: ru-RU, Swedish: sv-SE, Thai: th-TH, Turkish: tr-TR, Chinese (Simplified): zh-Hans, Chinese (Cantonese, Traditional): zh-HK. (optional)
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account</b> and permission should be <b>Contributor</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Create Language Model
    api_response = api_instance.create_language_model(location, account_id, model_name=model_name, language=language, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguagesApi->create_language_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **model_name** | **str**| Model name | [optional] 
 **language** | **str**| Model language. Supported languages: Arabic (United Arab Emirates): ar-AE, Arabic Modern Standard (Bahrain): ar-BH, Arabic Egypt: ar-EG, Arabic (Israel): ar-IL, Arabic (Iraq): ar-IQ, Arabic (Jordan): ar-JO, Arabic (Kuwait): ar-KW, Arabic (Lebanon): ar-LB, Arabic (Oman): ar-OM, Arabic (Palestinian Authority): ar-PS, Arabic (Qatar): ar-QA, Arabic (Saudi Arabia): ar-SA, Arabic Syrian Arab Republic: ar-SY, Czech: cs-CZ, Danish: da-DK, German: de-DE, English Australia: en-AU, English United Kingdom: en-GB, English United States: en-US, Spanish: es-ES, Spanish (Mexico): es-MX, Persian: fa-IR, Finnish: fi-FI, French (Canada): fr-CA, French: fr-FR, Hebrew: he-IL, Hindi: hi-IN, Italian: it-IT, Japanese: ja-JP, Korean: ko-KR, Norwegian: nb-NO, Dutch: nl-NL, Polish: pl-PL, Portuguese: pt-BR, Portuguese (Portugal): pt-PT, Russian: ru-RU, Swedish: sv-SE, Thai: th-TH, Turkish: tr-TR, Chinese (Simplified): zh-Hans, Chinese (Cantonese, Traditional): zh-HK. | [optional] 
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

# **delete_language_model**
> delete_language_model(location, account_id, model_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Delete Language Model

Delete language model.

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
api_instance = videoindexer.LanguagesApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
model_id = 'model_id_example' # str | Format - guid. Model id
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account</b> and permission should be <b>Contributor</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Delete Language Model
    api_instance.delete_language_model(location, account_id, model_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
except ApiException as e:
    print("Exception when calling LanguagesApi->delete_language_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **model_id** | **str**| Format - guid. Model id | 
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

# **delete_language_model_file**
> delete_language_model_file(location, account_id, model_id, file_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Delete Language Model File

Delete language model file.

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
api_instance = videoindexer.LanguagesApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
model_id = 'model_id_example' # str | Format - guid. Model id
file_id = 'file_id_example' # str | Format - guid. File id
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account</b> and permission should be <b>Contributor</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Delete Language Model File
    api_instance.delete_language_model_file(location, account_id, model_id, file_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
except ApiException as e:
    print("Exception when calling LanguagesApi->delete_language_model_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **model_id** | **str**| Format - guid. Model id | 
 **file_id** | **str**| Format - guid. File id | 
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

# **download_language_model_file_content**
> object download_language_model_file_content(location, account_id, model_id, file_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Download Language Model File Content

Downlaod language model file content.

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
api_instance = videoindexer.LanguagesApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
model_id = 'model_id_example' # str | Format - guid. Model id
file_id = 'file_id_example' # str | Format - guid. File id
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account</b> and permission should be <b>Reader</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Download Language Model File Content
    api_response = api_instance.download_language_model_file_content(location, account_id, model_id, file_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguagesApi->download_language_model_file_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **model_id** | **str**| Format - guid. Model id | 
 **file_id** | **str**| Format - guid. File id | 
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

# **get_language_model**
> object get_language_model(location, account_id, model_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Get Language Model

Get language model.

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
api_instance = videoindexer.LanguagesApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
model_id = 'model_id_example' # str | Format - guid. Model id
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account</b> and permission should be <b>Reader</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Get Language Model
    api_response = api_instance.get_language_model(location, account_id, model_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguagesApi->get_language_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **model_id** | **str**| Format - guid. Model id | 
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

# **get_language_model_edits_history**
> object get_language_model_edits_history(location, account_id, model_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Get Language Model Edits History (PREVIEW)

This API is a preview API subject to preview terms available <a href=\"https://aka.ms/vi-api-preview-terms\" target=\"_blank\">here</a>. It’s not final and might change.<br/>Get language model edits history.

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
api_instance = videoindexer.LanguagesApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
model_id = 'model_id_example' # str | Format - guid. Model id
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account</b> and permission should be <b>Reader</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Get Language Model Edits History (PREVIEW)
    api_response = api_instance.get_language_model_edits_history(location, account_id, model_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguagesApi->get_language_model_edits_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **model_id** | **str**| Format - guid. Model id | 
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

# **get_language_model_file_data**
> object get_language_model_file_data(location, account_id, model_id, file_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Get Language Model File Data

Get language model file data and metadata.

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
api_instance = videoindexer.LanguagesApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
model_id = 'model_id_example' # str | Format - guid. Model id
file_id = 'file_id_example' # str | Format - guid. File id
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account</b> and permission should be <b>Reader</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Get Language Model File Data
    api_response = api_instance.get_language_model_file_data(location, account_id, model_id, file_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguagesApi->get_language_model_file_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **model_id** | **str**| Format - guid. Model id | 
 **file_id** | **str**| Format - guid. File id | 
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

# **get_language_models**
> object get_language_models(location, account_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Get Language Models

Get language models.

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
api_instance = videoindexer.LanguagesApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account</b> and permission should be <b>Reader</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Get Language Models
    api_response = api_instance.get_language_models(location, account_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguagesApi->get_language_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
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

# **train_language_model**
> object train_language_model(location, account_id, model_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Train Language Model

Train the language model based on the enabled files.

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
api_instance = videoindexer.LanguagesApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
model_id = 'model_id_example' # str | Format - guid. Model id
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account</b> and permission should be <b>Contributor</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Train Language Model
    api_response = api_instance.train_language_model(location, account_id, model_id, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguagesApi->train_language_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **model_id** | **str**| Format - guid. Model id | 
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

# **update_language_model**
> object update_language_model(location, account_id, model_id, model_name=model_name, enable=enable, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Update Language Model

Updates a language model.  There are two ways to upload files in the body using form-data. 1. Key will be the file name and value will be the file. 2. Key will be the file name and value will be a URL to a txt/vtt/srt/ttml file.

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
api_instance = videoindexer.LanguagesApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
model_id = 'model_id_example' # str | Format - guid. Model id
model_name = 'model_name_example' # str | New model name (optional)
enable = true # bool | Enable / Disable all files under the model (optional)
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account</b> and permission should be <b>Contributor</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Update Language Model
    api_response = api_instance.update_language_model(location, account_id, model_id, model_name=model_name, enable=enable, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguagesApi->update_language_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **model_id** | **str**| Format - guid. Model id | 
 **model_name** | **str**| New model name | [optional] 
 **enable** | **bool**| Enable / Disable all files under the model | [optional] 
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

# **update_language_model_file**
> object update_language_model_file(location, account_id, model_id, file_id, file_name=file_name, enable=enable, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Update Language Model file

Update a language model file name or state.

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
api_instance = videoindexer.LanguagesApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
model_id = 'model_id_example' # str | Format - guid. Model id
file_id = 'file_id_example' # str | Format - guid. File id
file_name = 'file_name_example' # str | Model name (optional)
enable = true # bool | Enable (optional)
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account</b> and permission should be <b>Contributor</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Update Language Model file
    api_response = api_instance.update_language_model_file(location, account_id, model_id, file_id, file_name=file_name, enable=enable, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguagesApi->update_language_model_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **model_id** | **str**| Format - guid. Model id | 
 **file_id** | **str**| Format - guid. File id | 
 **file_name** | **str**| Model name | [optional] 
 **enable** | **bool**| Enable | [optional] 
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

