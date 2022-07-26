#!/bin/bash

set -e

TEMP_FILES="generated Operations.yaml Operations_fixed.yaml"

rm -rf ${TEMP_FILES} *.tar.gz *.whl

echo "# Download OpenAPI spec..."

curl -H 'Accept: application/vnd.oai.openapi' "https://viprod-apim.management.azure-api.net/subscriptions/000/resourceGroups/000/providers/Microsoft.ApiManagement/service/viprod-apim/apis/Operations?api-version=2019-12-01" > Operations.yaml

echo "# Fix spec..."

poetry run python ./fix_swagger.py Operations.yaml > Operations_fixed.yaml

echo "# Generate SDK..."

mkdir generated

docker run --user $(id -u):$(id -g) --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli-v3 generate -i /local/Operations_fixed.yaml -o /local/generated -l python -DpackageName=azure.videoindexer

echo "# Build SDK..."

cd generated
touch azure/__init__.py
python setup.py sdist
python setup.py bdist_wheel --universal

mv dist/*.tar.gz ..
mv dist/*.whl ..

echo "# Clean up..."

cd ..

if [ "$1" != "-k" ]
then
    rm -rf ${TEMP_FILES}
fi
