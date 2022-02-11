# Azure Video Analyzer for Media Python samples

This repository contains some examples of Python scripts accessing Azure Video Analyzer for Media (née Video Indexer).

The examples use an SDK generated using [Swagger Codegen](https://github.com/swagger-api/swagger-codegen). You should first install the `swagger-codegen` tool, and then follow the next steps to generate the SDK.

## Generate the SDK

First download the AVAM OpenAPI spec:

```sh
curl -H 'Accept: application/vnd.oai.openapi' "https://viprod-apim.management.azure-api.net/subscriptions/000/resourceGroups/000/providers/Microsoft.ApiManagement/service/viprod-apim/apis/Operations?api-version=2019-12-01" > Operations.yaml
```

You can find this URL on the [API Portal for AVAM](https://api-portal.videoindexer.ai/api-details#api=Operations).

You can then generate the SDK:

```sh
mkdir sdk
cd sdk
swagger-codegen generate -i ../Operations.yaml -l python -DpackageName=azure.videoindexer
```

I decided to name the package `azure.videoindexer` rather than `azure.videoanalyzerformedia` for brevity purposes :-)

Once the SDK is generated, you can install it in "edit" mode with `pip`, so you can use it in your scripts:

```sh
pip install -e sdk
```

## Use the examples

The examples rely on a small helper library to retrieve an AVAM access token. This libray uses the `DefaultAzureCredential` class in the [azure-identity](https://docs.microsoft.com/en-us/python/api/overview/azure/identity-readme?view=azure-python) library to authenticate with Azure Active Directory. This class can use a number of different schemes to determine the identity to use for authentication: environment variables, user/system assigned managed identities, etc.

For example, if you want to use a Service Principal to authenticate, you can define the following environment variables:

```sh
export AZURE_CLIENT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
export AZURE_CLIENT_SECRET=123random456string
export AZURE_TENANT_ID=yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy
```

In addition, to access the AVAM API, the following environment variables will be used:

```sh
export AVAM_SUBSCRIPTION=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
export AVAM_RESOURCE_GROUP=foo
export AVAM_ACCOUNT_ID=yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy
export AVAM_ACCOUNT_NAME=bar
export AVAM_LOCATION=eastus
```

- `AVAM_SUBSCRIPTION` is the Azure subscription ID where the AVAM account was created.
- `AVAM_RESOURCE_GROUP` is the name of the Resource Group where the AVAM account was created.
- `AVAM_ACCOUNT_ID` is the AVAM account ID, it can be found for example on the AVAM resource "Overview" page in the portal.
- `AVAM_ACCOUNT_NAME` is the AVAM account name, as specified when it was created.
- `AVAM_LOCATION` is the datacenter location of the AVAM account.

You can then run an example:

```sh
python list_videos.py
```
