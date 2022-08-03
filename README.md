# Azure Video Indexer Python samples

This repository contains some examples showing how to access the REST API of [Azure Video Indexer](https://docs.microsoft.com/en-us/azure/azure-video-indexer/) from Python.

The dependencies are managed using [Poetry](https://python-poetry.org/), you should also install this tool on your machine.

## Use the examples

To use the samples, first install the dependencies using Poetry. You don't need to build the SDK, the samples will use the SDK included in the repository.

```sh
poetry install
```

The examples rely on a small helper library to retrieve an AVAM access token. This libray uses the `DefaultAzureCredential` class in the [azure-identity](https://docs.microsoft.com/en-us/python/api/overview/azure/identity-readme?view=azure-python) library to authenticate with Azure Active Directory. This class can use a number of different schemes to determine the identity to use for authentication: environment variables, user/system assigned managed identities, etc.

For example, if you want to use a Service Principal to authenticate, you can define the following environment variables:

```sh
export AZURE_CLIENT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
export AZURE_CLIENT_SECRET=123random456string
export AZURE_TENANT_ID=yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy
```

If you are logged in using the Azure CLI tool, `DefaultAzureCredential` will use your current credentials.

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

## Generate the SDK

Here are the steps you can follow if you want to re-generate the SDK for any reason.

The SDK is generated using a [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) Docker image, so you should have Docker installed and runnning on your machine.

You can generate the SDK in the `scripts` directory:

```sh
cd scripts
poetry install
poetry run bash build_sdk.sh
```

The SDK is generated in the `videoindexer` directory. If you want to use it in the samples, you will have to move it into place (one directory up).
