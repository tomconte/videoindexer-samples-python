#!/bin/bash

set -e

# Defaults
opt_keep=false
opt_build=false

while getopts "kn" opt
do
    case $opt in
        k)
            opt_keep=true
            ;;
        b)
            opt_build=true
            ;;
    esac
done

TEMP_FILES="Operations.yaml Operations_fixed.yaml"

# Delete any existing files
rm -rf ${TEMP_FILES} *.tar.gz *.whl

echo "# Download OpenAPI spec..."

curl -H 'Accept: application/vnd.oai.openapi' "https://viprod-apim.management.azure-api.net/subscriptions/000/resourceGroups/000/providers/Microsoft.ApiManagement/service/viprod-apim/apis/Operations?api-version=2019-12-01" > Operations.yaml

echo "# Fix spec..."

poetry run python ./fix_swagger.py Operations.yaml > Operations_fixed.yaml

echo "# Generate SDK..."

mkdir videoindexer

#docker run --user $(id -u):$(id -g) --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli-v3 generate -i /local/Operations_fixed.yaml -o /local/videoindexer -l python -DpackageName=videoindexer
docker run --user $(id -u):$(id -g) --rm -v ${PWD}:/local parsertongue/swagger-codegen-cli:3.0.32 generate -i /local/Operations_fixed.yaml -o /local/videoindexer -l python -DpackageName=videoindexer

if [ "$opt_build" = true ]
then
    echo "# Build SDK..."

    cd generated
    touch azure/__init__.py
    python setup.py sdist
    python setup.py bdist_wheel --universal

    mv dist/*.tar.gz ..
    mv dist/*.whl ..
    cd ..
fi

if [ "$opt_keep" = false ]
then
    echo "# Clean up..."
    rm -rf ${TEMP_FILES}
fi
