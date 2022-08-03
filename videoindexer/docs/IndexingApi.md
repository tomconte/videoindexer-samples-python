# videoindexer.IndexingApi

All URIs are relative to *https://api.videoindexer.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_video_index**](IndexingApi.md#get_video_index) | **GET** /{location}/Accounts/{accountId}/Videos/{videoId}/Index | Get Video Index
[**re_index_video**](IndexingApi.md#re_index_video) | **PUT** /{location}/Accounts/{accountId}/Videos/{videoId}/ReIndex | Re-Index Video
[**upload_video**](IndexingApi.md#upload_video) | **POST** /{location}/Accounts/{accountId}/Videos | Upload Video

# **get_video_index**
> object get_video_index(location, account_id, video_id, language=language, re_translate=re_translate, include_streaming_urls=include_streaming_urls, included_insights=included_insights, excluded_insights=excluded_insights, include_summarized_insights=include_summarized_insights, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Get Video Index

Get Video Index

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
api_instance = videoindexer.IndexingApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
video_id = 'video_id_example' # str | The video id
language = 'language_example' # str | The language to translate video insights. Supported languages: Afrikaans: af-ZA, Arabic (United Arab Emirates): ar-AE, Arabic Modern Standard (Bahrain): ar-BH, Arabic Egypt: ar-EG, Arabic (Israel): ar-IL, Arabic (Iraq): ar-IQ, Arabic (Jordan): ar-JO, Arabic (Kuwait): ar-KW, Arabic (Lebanon): ar-LB, Arabic (Oman): ar-OM, Arabic (Palestinian Authority): ar-PS, Arabic (Qatar): ar-QA, Arabic (Saudi Arabia): ar-SA, Arabic Syrian Arab Republic: ar-SY, Bulgarian: bg-BG, Bangla: bn-BD, Bosnian: bs-Latn, Catalan: ca-ES, Czech: cs-CZ, Danish: da-DK, German: de-DE, Greek: el-GR, English Australia: en-AU, Fijian: en-FJ, English United Kingdom: en-GB, English United States: en-US, Samoan: en-WS, Spanish: es-ES, Spanish (Mexico): es-MX, Estonian: et-EE, Persian: fa-IR, Finnish: fi-FI, Filipino: fil-PH, French (Canada): fr-CA, French: fr-FR, Haitian: fr-HT, Hebrew: he-IL, Hindi: hi-IN, Croatian: hr-HR, Hungarian: hu-HU, Indonesian: id-ID, Italian: it-IT, Japanese: ja-JP, Korean: ko-KR, Lithuanian: lt-LT, Latvian: lv-LV, Malagasy: mg-MG, Malay: ms-MY, Maltese: mt-MT, Norwegian: nb-NO, Dutch: nl-NL, Polish: pl-PL, Portuguese: pt-BR, Portuguese (Portugal): pt-PT, Romanian: ro-RO, Russian: ru-RU, Slovak: sk-SK, Slovenian: sl-SI, Serbian (Cyrillic): sr-Cyrl-RS, Serbian (Latin): sr-Latn-RS, Swedish: sv-SE, Kiswahili: sw-KE, Tamil: ta-IN, Thai: th-TH, Tongan: to-TO, Turkish: tr-TR, Ukrainian: uk-UA, Urdu: ur-PK, Vietnamese: vi-VN, Chinese (Simplified): zh-Hans, Chinese (Traditional): zh-Hant, Chinese (Cantonese, Traditional): zh-HK. (optional)
re_translate = false # bool | Indicates whether to re-translate the video and overwrite existing translation for the given language or leave existing translation. (optional) (default to false)
include_streaming_urls = true # bool | Indicates whether to include streaming urls in the video index. (optional) (default to true)
included_insights = 'included_insights_example' # str | Insights to include in the response. For example, to include only Transcript and Faces in the insights, pass the value 'Transcript,Faces'. Only array fields under the insights element are supported. An empty value will include all insights. (optional)
excluded_insights = 'excluded_insights_example' # str | Insights to exclude from the response. For example, to get all insights except Transcript and Faces, pass the value 'Transcript,Faces'. Only array fields under the insights element are supported. An empty value will exclude no insight. This query parameter cannot be provided if the 'includeInsights' parameter is provided. (optional)
include_summarized_insights = true # bool | Whether to include the deprecated SummarizedInsights field. It is recommended to pass 'false'. (optional) (default to true)
access_token = 'access_token_example' # str | Required for private videos<br>  Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account/Video</b> and permission should be <b>Reader</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Get Video Index
    api_response = api_instance.get_video_index(location, account_id, video_id, language=language, re_translate=re_translate, include_streaming_urls=include_streaming_urls, included_insights=included_insights, excluded_insights=excluded_insights, include_summarized_insights=include_summarized_insights, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexingApi->get_video_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **video_id** | **str**| The video id | 
 **language** | **str**| The language to translate video insights. Supported languages: Afrikaans: af-ZA, Arabic (United Arab Emirates): ar-AE, Arabic Modern Standard (Bahrain): ar-BH, Arabic Egypt: ar-EG, Arabic (Israel): ar-IL, Arabic (Iraq): ar-IQ, Arabic (Jordan): ar-JO, Arabic (Kuwait): ar-KW, Arabic (Lebanon): ar-LB, Arabic (Oman): ar-OM, Arabic (Palestinian Authority): ar-PS, Arabic (Qatar): ar-QA, Arabic (Saudi Arabia): ar-SA, Arabic Syrian Arab Republic: ar-SY, Bulgarian: bg-BG, Bangla: bn-BD, Bosnian: bs-Latn, Catalan: ca-ES, Czech: cs-CZ, Danish: da-DK, German: de-DE, Greek: el-GR, English Australia: en-AU, Fijian: en-FJ, English United Kingdom: en-GB, English United States: en-US, Samoan: en-WS, Spanish: es-ES, Spanish (Mexico): es-MX, Estonian: et-EE, Persian: fa-IR, Finnish: fi-FI, Filipino: fil-PH, French (Canada): fr-CA, French: fr-FR, Haitian: fr-HT, Hebrew: he-IL, Hindi: hi-IN, Croatian: hr-HR, Hungarian: hu-HU, Indonesian: id-ID, Italian: it-IT, Japanese: ja-JP, Korean: ko-KR, Lithuanian: lt-LT, Latvian: lv-LV, Malagasy: mg-MG, Malay: ms-MY, Maltese: mt-MT, Norwegian: nb-NO, Dutch: nl-NL, Polish: pl-PL, Portuguese: pt-BR, Portuguese (Portugal): pt-PT, Romanian: ro-RO, Russian: ru-RU, Slovak: sk-SK, Slovenian: sl-SI, Serbian (Cyrillic): sr-Cyrl-RS, Serbian (Latin): sr-Latn-RS, Swedish: sv-SE, Kiswahili: sw-KE, Tamil: ta-IN, Thai: th-TH, Tongan: to-TO, Turkish: tr-TR, Ukrainian: uk-UA, Urdu: ur-PK, Vietnamese: vi-VN, Chinese (Simplified): zh-Hans, Chinese (Traditional): zh-Hant, Chinese (Cantonese, Traditional): zh-HK. | [optional] 
 **re_translate** | **bool**| Indicates whether to re-translate the video and overwrite existing translation for the given language or leave existing translation. | [optional] [default to false]
 **include_streaming_urls** | **bool**| Indicates whether to include streaming urls in the video index. | [optional] [default to true]
 **included_insights** | **str**| Insights to include in the response. For example, to include only Transcript and Faces in the insights, pass the value &#x27;Transcript,Faces&#x27;. Only array fields under the insights element are supported. An empty value will include all insights. | [optional] 
 **excluded_insights** | **str**| Insights to exclude from the response. For example, to get all insights except Transcript and Faces, pass the value &#x27;Transcript,Faces&#x27;. Only array fields under the insights element are supported. An empty value will exclude no insight. This query parameter cannot be provided if the &#x27;includeInsights&#x27; parameter is provided. | [optional] 
 **include_summarized_insights** | **bool**| Whether to include the deprecated SummarizedInsights field. It is recommended to pass &#x27;false&#x27;. | [optional] [default to true]
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

# **re_index_video**
> re_index_video(location, account_id, video_id, indexing_preset=indexing_preset, streaming_preset=streaming_preset, callback_url=callback_url, source_language=source_language, send_success_email=send_success_email, linguistic_model_id=linguistic_model_id, person_model_id=person_model_id, animation_model_id=animation_model_id, priority=priority, brands_categories=brands_categories, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Re-Index Video

Re-index video

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
api_instance = videoindexer.IndexingApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
video_id = 'video_id_example' # str | The video id
indexing_preset = 'indexing_preset_example' # str | The indexing preset to use. Allowed values: Default / AudioOnly / VideoOnly / BasicAudio / Advanced / AdvancedAudio / AdvancedVideo (optional)
streaming_preset = 'streaming_preset_example' # str | The streaming preset to use. Allowed values: NoStreaming / Default / SingleBitrate / AdaptiveBitrate (optional)
callback_url = 'callback_url_example' # str | Format - uri. A url to send notifications to (POST). These are the supported notifications: 1. Video indexing completed:    2 additional query string parameters will be added to the url: id and state.     For example, if the callback url is 'https://test.com/notifyme?projectName=MyProject', the notification will be sent to 'https://test.com/notifyme?projectName=MyProject&id=12345abcde&state=Processed'.  2. A face was identified (after the face was trained in another video):    4 additional query string parameters will be added to the url: id, faceId, knownPersonId and personName.     For example, if the callback url is 'https://test.com/notifyme?projectName=MyProject', the notification will be sent to 'https://test.com/notifyme?projectName=MyProject&id=12345abcde&faceId=1234&knownPersonId=B689EC08-FAB6-497A-A727-DA7285DBD436&personName=JohnSmith'. (optional)
source_language = 'source_language_example' # str | The language of the video, to be used when generating the transcript: Auto-detect single language - 'auto', Auto-detect multi language (preview) - 'multi'.. Supported languages: Arabic (United Arab Emirates): ar-AE, Arabic Modern Standard (Bahrain): ar-BH, Arabic Egypt: ar-EG, Arabic (Israel): ar-IL, Arabic (Iraq): ar-IQ, Arabic (Jordan): ar-JO, Arabic (Kuwait): ar-KW, Arabic (Lebanon): ar-LB, Arabic (Oman): ar-OM, Arabic (Palestinian Authority): ar-PS, Arabic (Qatar): ar-QA, Arabic (Saudi Arabia): ar-SA, Arabic Syrian Arab Republic: ar-SY, Czech: cs-CZ, Danish: da-DK, German: de-DE, English Australia: en-AU, English United Kingdom: en-GB, English United States: en-US, Spanish: es-ES, Spanish (Mexico): es-MX, Persian: fa-IR, Finnish: fi-FI, French (Canada): fr-CA, French: fr-FR, Hebrew: he-IL, Hindi: hi-IN, Italian: it-IT, Japanese: ja-JP, Korean: ko-KR, Norwegian: nb-NO, Dutch: nl-NL, Polish: pl-PL, Portuguese: pt-BR, Portuguese (Portugal): pt-PT, Russian: ru-RU, Swedish: sv-SE, Thai: th-TH, Turkish: tr-TR, Chinese (Simplified): zh-Hans, Chinese (Cantonese, Traditional): zh-HK. (optional)
send_success_email = false # bool | Indicates whether to send a success mail once video was succesfully indexed (optional) (default to false)
linguistic_model_id = 'linguistic_model_id_example' # str | Linguistic model id as received by 'create linguistic model' call (optional)
person_model_id = 'person_model_id_example' # str | Faces will be identified against the provided person model. (optional)
animation_model_id = 'animation_model_id_example' # str | Animations will be identified against the provided animation model. (optional)
priority = 'priority_example' # str | Index priority, can be used in paid regions only. Allowed values: Low / Normal / High (optional)
brands_categories = 'brands_categories_example' # str | List of brands categories delimited by comma. Azure Video Indexer will only take these categories in to account when indexing. If not specified all brands will be used. (optional)
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account/Video</b> and permission should be <b>Contributor</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Re-Index Video
    api_instance.re_index_video(location, account_id, video_id, indexing_preset=indexing_preset, streaming_preset=streaming_preset, callback_url=callback_url, source_language=source_language, send_success_email=send_success_email, linguistic_model_id=linguistic_model_id, person_model_id=person_model_id, animation_model_id=animation_model_id, priority=priority, brands_categories=brands_categories, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
except ApiException as e:
    print("Exception when calling IndexingApi->re_index_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **video_id** | **str**| The video id | 
 **indexing_preset** | **str**| The indexing preset to use. Allowed values: Default / AudioOnly / VideoOnly / BasicAudio / Advanced / AdvancedAudio / AdvancedVideo | [optional] 
 **streaming_preset** | **str**| The streaming preset to use. Allowed values: NoStreaming / Default / SingleBitrate / AdaptiveBitrate | [optional] 
 **callback_url** | **str**| Format - uri. A url to send notifications to (POST). These are the supported notifications: 1. Video indexing completed:    2 additional query string parameters will be added to the url: id and state.     For example, if the callback url is &#x27;https://test.com/notifyme?projectName&#x3D;MyProject&#x27;, the notification will be sent to &#x27;https://test.com/notifyme?projectName&#x3D;MyProject&amp;id&#x3D;12345abcde&amp;state&#x3D;Processed&#x27;.  2. A face was identified (after the face was trained in another video):    4 additional query string parameters will be added to the url: id, faceId, knownPersonId and personName.     For example, if the callback url is &#x27;https://test.com/notifyme?projectName&#x3D;MyProject&#x27;, the notification will be sent to &#x27;https://test.com/notifyme?projectName&#x3D;MyProject&amp;id&#x3D;12345abcde&amp;faceId&#x3D;1234&amp;knownPersonId&#x3D;B689EC08-FAB6-497A-A727-DA7285DBD436&amp;personName&#x3D;JohnSmith&#x27;. | [optional] 
 **source_language** | **str**| The language of the video, to be used when generating the transcript: Auto-detect single language - &#x27;auto&#x27;, Auto-detect multi language (preview) - &#x27;multi&#x27;.. Supported languages: Arabic (United Arab Emirates): ar-AE, Arabic Modern Standard (Bahrain): ar-BH, Arabic Egypt: ar-EG, Arabic (Israel): ar-IL, Arabic (Iraq): ar-IQ, Arabic (Jordan): ar-JO, Arabic (Kuwait): ar-KW, Arabic (Lebanon): ar-LB, Arabic (Oman): ar-OM, Arabic (Palestinian Authority): ar-PS, Arabic (Qatar): ar-QA, Arabic (Saudi Arabia): ar-SA, Arabic Syrian Arab Republic: ar-SY, Czech: cs-CZ, Danish: da-DK, German: de-DE, English Australia: en-AU, English United Kingdom: en-GB, English United States: en-US, Spanish: es-ES, Spanish (Mexico): es-MX, Persian: fa-IR, Finnish: fi-FI, French (Canada): fr-CA, French: fr-FR, Hebrew: he-IL, Hindi: hi-IN, Italian: it-IT, Japanese: ja-JP, Korean: ko-KR, Norwegian: nb-NO, Dutch: nl-NL, Polish: pl-PL, Portuguese: pt-BR, Portuguese (Portugal): pt-PT, Russian: ru-RU, Swedish: sv-SE, Thai: th-TH, Turkish: tr-TR, Chinese (Simplified): zh-Hans, Chinese (Cantonese, Traditional): zh-HK. | [optional] 
 **send_success_email** | **bool**| Indicates whether to send a success mail once video was succesfully indexed | [optional] [default to false]
 **linguistic_model_id** | **str**| Linguistic model id as received by &#x27;create linguistic model&#x27; call | [optional] 
 **person_model_id** | **str**| Faces will be identified against the provided person model. | [optional] 
 **animation_model_id** | **str**| Animations will be identified against the provided animation model. | [optional] 
 **priority** | **str**| Index priority, can be used in paid regions only. Allowed values: Low / Normal / High | [optional] 
 **brands_categories** | **str**| List of brands categories delimited by comma. Azure Video Indexer will only take these categories in to account when indexing. If not specified all brands will be used. | [optional] 
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

# **upload_video**
> object upload_video(location, account_id, name=name, privacy=privacy, priority=priority, description=description, partition=partition, external_id=external_id, external_url=external_url, callback_url=callback_url, metadata=metadata, language=language, video_url=video_url, file_name=file_name, indexing_preset=indexing_preset, streaming_preset=streaming_preset, linguistic_model_id=linguistic_model_id, person_model_id=person_model_id, animation_model_id=animation_model_id, send_success_email=send_success_email, asset_id=asset_id, brands_categories=brands_categories, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)

Upload Video

Uploads the given video, starts indexing it and returns a new Video id.<br> The supported formats are listed  < a href = https://aka.ms/vi-supported-formats target=\"_blank\"> here</a>

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
api_instance = videoindexer.IndexingApi(videoindexer.ApiClient(configuration))
location = 'location_example' # str | Location indicates the Azure region to which the call should be routed<br> See more details <a href=https://aka.ms/vi-apiportal-location target=\"_blank\">here</a>
account_id = 'account_id_example' # str | Account ID is a globally unique identifier (GUID) for the account.<br> See more details <a href=https://aka.ms/vi-apiportal-useapi-accountId target=\"_blank\">here</a>
name = 'name_example' # str | The video name (optional)
privacy = 'Private' # str | The video privacy mode. Allowed values: Private / Public (optional) (default to Private)
priority = 'priority_example' # str | Index priority, can be used in paid regions only. Allowed values: Low / Normal / High (optional)
description = 'description_example' # str | The video description. (optional)
partition = 'partition_example' # str | A partition to partition videos by (used for searching a specific partition) (optional)
external_id = 'external_id_example' # str | An external id to associate with the video (can be searched for later). (optional)
external_url = 'external_url_example' # str | Format - uri. An external URL to associate with the video (can be retrieved later) (optional)
callback_url = 'callback_url_example' # str | Format - uri. A url to send notifications to (POST). These are the supported notifications: 1. Video indexing completed:    2 additional query string parameters will be added to the url: id and state.     For example, if the callback url is 'https://test.com/notifyme?projectName=MyProject', the notification will be sent to 'https://test.com/notifyme?projectName=MyProject&id=12345abcde&state=Processed'.  2. A face was identified (after the face was trained in another video):    4 additional query string parameters will be added to the url: id, faceId, knownPersonId and personName.     For example, if the callback url is 'https://test.com/notifyme?projectName=MyProject', the notification will be sent to 'https://test.com/notifyme?projectName=MyProject&id=12345abcde&faceId=1234&knownPersonId=B689EC08-FAB6-497A-A727-DA7285DBD436&personName=JohnSmith'. (optional)
metadata = 'metadata_example' # str | Metadata to associate with the video (will be returned in queries). (optional)
language = 'language_example' # str | The language of the video, to be used when generating the transcript: Auto-detect single language - 'auto', Auto-detect multi language (preview) - 'multi'.. Supported languages: Arabic (United Arab Emirates): ar-AE, Arabic Modern Standard (Bahrain): ar-BH, Arabic Egypt: ar-EG, Arabic (Israel): ar-IL, Arabic (Iraq): ar-IQ, Arabic (Jordan): ar-JO, Arabic (Kuwait): ar-KW, Arabic (Lebanon): ar-LB, Arabic (Oman): ar-OM, Arabic (Palestinian Authority): ar-PS, Arabic (Qatar): ar-QA, Arabic (Saudi Arabia): ar-SA, Arabic Syrian Arab Republic: ar-SY, Czech: cs-CZ, Danish: da-DK, German: de-DE, English Australia: en-AU, English United Kingdom: en-GB, English United States: en-US, Spanish: es-ES, Spanish (Mexico): es-MX, Persian: fa-IR, Finnish: fi-FI, French (Canada): fr-CA, French: fr-FR, Hebrew: he-IL, Hindi: hi-IN, Italian: it-IT, Japanese: ja-JP, Korean: ko-KR, Norwegian: nb-NO, Dutch: nl-NL, Polish: pl-PL, Portuguese: pt-BR, Portuguese (Portugal): pt-PT, Russian: ru-RU, Swedish: sv-SE, Thai: th-TH, Turkish: tr-TR, Chinese (Simplified): zh-Hans, Chinese (Cantonese, Traditional): zh-HK. (optional)
video_url = 'video_url_example' # str | Format - uri. A public url of the video/audio file (url encoded). It is recommended to use readonly urls (e.g. when using Azure Storage SAS urls). If not specified, the file should be passed as a multipart/form body content. (optional)
file_name = 'file_name_example' # str | The uploaded file name. (optional)
indexing_preset = 'Default' # str | The indexing preset to use. Allowed values: Default / AudioOnly / VideoOnly / BasicAudio / Advanced / AdvancedAudio / AdvancedVideo (optional) (default to Default)
streaming_preset = 'Default' # str | The streaming preset to use. Allowed values: NoStreaming / Default / SingleBitrate / AdaptiveBitrate (optional) (default to Default)
linguistic_model_id = 'linguistic_model_id_example' # str | Linguistic model id as received by 'create linguistic model' call (optional)
person_model_id = 'person_model_id_example' # str | Faces will be identified against the provided person model. (optional)
animation_model_id = 'animation_model_id_example' # str | Animations will be identified against the provided animation model. (optional)
send_success_email = false # bool | Indicates whether to send a success mail once video was succesfully indexed (optional) (default to false)
asset_id = 'asset_id_example' # str | Azure media services asset id. Used to index from existing assets in your connected Azure media services account. (Paid only) (optional)
brands_categories = 'brands_categories_example' # str | List of brands categories delimited by comma. Azure Video Indexer will only take these categories in to account when indexing. If not specified all brands will be used. (optional)
access_token = 'access_token_example' # str | Required. Should be given as parameter in URL query string or in Authorization header as Bearer token. Access token scope should be <b>Account</b> and permission should be <b>Contributor</b>.<br>  Note that Access tokens expire within 1 hour<br> See more details for <b>Classic Account</b> <a href=https://aka.ms/DocsObtainAccessToken target=\"_blank\">here</a>, for <b>ARM Account</b> <a href=https://aka.ms/vi-classic-access-token target=\"_blank\">here</a> (optional)
x_ms_client_request_id = 'x_ms_client_request_id_example' # str | Format - uuid. A globally unique identifier (GUID) for the request which can be sent by client for instrumentation purposes. The server makes sure all logs associated with handling the request can be linked to the client request id so a client can provide this request id in support tickets so support engineers could find the logs linked to this particular request, so avoid using the same request id for different requests, including in retry scenarios. (optional)

try:
    # Upload Video
    api_response = api_instance.upload_video(location, account_id, name=name, privacy=privacy, priority=priority, description=description, partition=partition, external_id=external_id, external_url=external_url, callback_url=callback_url, metadata=metadata, language=language, video_url=video_url, file_name=file_name, indexing_preset=indexing_preset, streaming_preset=streaming_preset, linguistic_model_id=linguistic_model_id, person_model_id=person_model_id, animation_model_id=animation_model_id, send_success_email=send_success_email, asset_id=asset_id, brands_categories=brands_categories, access_token=access_token, x_ms_client_request_id=x_ms_client_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexingApi->upload_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location indicates the Azure region to which the call should be routed&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-location target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **account_id** | **str**| Account ID is a globally unique identifier (GUID) for the account.&lt;br&gt; See more details &lt;a href&#x3D;https://aka.ms/vi-apiportal-useapi-accountId target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; | 
 **name** | **str**| The video name | [optional] 
 **privacy** | **str**| The video privacy mode. Allowed values: Private / Public | [optional] [default to Private]
 **priority** | **str**| Index priority, can be used in paid regions only. Allowed values: Low / Normal / High | [optional] 
 **description** | **str**| The video description. | [optional] 
 **partition** | **str**| A partition to partition videos by (used for searching a specific partition) | [optional] 
 **external_id** | **str**| An external id to associate with the video (can be searched for later). | [optional] 
 **external_url** | **str**| Format - uri. An external URL to associate with the video (can be retrieved later) | [optional] 
 **callback_url** | **str**| Format - uri. A url to send notifications to (POST). These are the supported notifications: 1. Video indexing completed:    2 additional query string parameters will be added to the url: id and state.     For example, if the callback url is &#x27;https://test.com/notifyme?projectName&#x3D;MyProject&#x27;, the notification will be sent to &#x27;https://test.com/notifyme?projectName&#x3D;MyProject&amp;id&#x3D;12345abcde&amp;state&#x3D;Processed&#x27;.  2. A face was identified (after the face was trained in another video):    4 additional query string parameters will be added to the url: id, faceId, knownPersonId and personName.     For example, if the callback url is &#x27;https://test.com/notifyme?projectName&#x3D;MyProject&#x27;, the notification will be sent to &#x27;https://test.com/notifyme?projectName&#x3D;MyProject&amp;id&#x3D;12345abcde&amp;faceId&#x3D;1234&amp;knownPersonId&#x3D;B689EC08-FAB6-497A-A727-DA7285DBD436&amp;personName&#x3D;JohnSmith&#x27;. | [optional] 
 **metadata** | **str**| Metadata to associate with the video (will be returned in queries). | [optional] 
 **language** | **str**| The language of the video, to be used when generating the transcript: Auto-detect single language - &#x27;auto&#x27;, Auto-detect multi language (preview) - &#x27;multi&#x27;.. Supported languages: Arabic (United Arab Emirates): ar-AE, Arabic Modern Standard (Bahrain): ar-BH, Arabic Egypt: ar-EG, Arabic (Israel): ar-IL, Arabic (Iraq): ar-IQ, Arabic (Jordan): ar-JO, Arabic (Kuwait): ar-KW, Arabic (Lebanon): ar-LB, Arabic (Oman): ar-OM, Arabic (Palestinian Authority): ar-PS, Arabic (Qatar): ar-QA, Arabic (Saudi Arabia): ar-SA, Arabic Syrian Arab Republic: ar-SY, Czech: cs-CZ, Danish: da-DK, German: de-DE, English Australia: en-AU, English United Kingdom: en-GB, English United States: en-US, Spanish: es-ES, Spanish (Mexico): es-MX, Persian: fa-IR, Finnish: fi-FI, French (Canada): fr-CA, French: fr-FR, Hebrew: he-IL, Hindi: hi-IN, Italian: it-IT, Japanese: ja-JP, Korean: ko-KR, Norwegian: nb-NO, Dutch: nl-NL, Polish: pl-PL, Portuguese: pt-BR, Portuguese (Portugal): pt-PT, Russian: ru-RU, Swedish: sv-SE, Thai: th-TH, Turkish: tr-TR, Chinese (Simplified): zh-Hans, Chinese (Cantonese, Traditional): zh-HK. | [optional] 
 **video_url** | **str**| Format - uri. A public url of the video/audio file (url encoded). It is recommended to use readonly urls (e.g. when using Azure Storage SAS urls). If not specified, the file should be passed as a multipart/form body content. | [optional] 
 **file_name** | **str**| The uploaded file name. | [optional] 
 **indexing_preset** | **str**| The indexing preset to use. Allowed values: Default / AudioOnly / VideoOnly / BasicAudio / Advanced / AdvancedAudio / AdvancedVideo | [optional] [default to Default]
 **streaming_preset** | **str**| The streaming preset to use. Allowed values: NoStreaming / Default / SingleBitrate / AdaptiveBitrate | [optional] [default to Default]
 **linguistic_model_id** | **str**| Linguistic model id as received by &#x27;create linguistic model&#x27; call | [optional] 
 **person_model_id** | **str**| Faces will be identified against the provided person model. | [optional] 
 **animation_model_id** | **str**| Animations will be identified against the provided animation model. | [optional] 
 **send_success_email** | **bool**| Indicates whether to send a success mail once video was succesfully indexed | [optional] [default to false]
 **asset_id** | **str**| Azure media services asset id. Used to index from existing assets in your connected Azure media services account. (Paid only) | [optional] 
 **brands_categories** | **str**| List of brands categories delimited by comma. Azure Video Indexer will only take these categories in to account when indexing. If not specified all brands will be used. | [optional] 
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

