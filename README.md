# Azure Video Analyzer for Media Python samples

This repository contains some examples showing how to access from Python the REST API of [Azure Video Analyzer for Media](https://docs.microsoft.com/en-us/azure/azure-video-analyzer/video-analyzer-for-media-docs/) (née Video Indexer, a.k.a. "AVAM").

The examples use an SDK generated using [Swagger Codegen](https://github.com/swagger-api/swagger-codegen). You should first install the `swagger-codegen` tool, and then follow the next steps to generate the SDK.

The dependencies are managed using [Poetry](https://python-poetry.org/), you should also install this tool on your machine.

## Generate the SDK

You can generate and build the SDK using the script provided:

```sh
cd sdk
poetry install
poetry run bash build_sdk.sh
```

I decided to name the package `azure.videoindexer` rather than `azure.videoanalyzerformedia` for brevity purposes :-)

## Install dependencies

Once the SDK is generated, it will be installed using Poetry, along with the other dependencies.

```sh
poetry install
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
poetry run python list_videos.py
```

## List of examples

- `list_videos.py`: list the names of all videos (limited to 1000 entries).
- `download_all_thumbnails.py`: download all keyframe thumbnails for all videos (limited to 100 entries).
- `download_all_insights.py`: download insights JSON document for all videos (limited to 100 entries).
