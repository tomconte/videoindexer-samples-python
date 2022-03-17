#!/bin/bash

TEMP_FILES="generated Operations.yaml Operations_fixed.yaml"

rm -rf ${TEMP_FILES} *.tar.gz

echo "# Download OpenAPI spec..."

curl -H 'Accept: application/vnd.oai.openapi' "https://viprod-apim.management.azure-api.net/subscriptions/000/resourceGroups/000/providers/Microsoft.ApiManagement/service/viprod-apim/apis/Operations?api-version=2019-12-01" > Operations.yaml

echo "# Fix spec..."

python ./fix_swagger.py Operations.yaml > Operations_fixed.yaml

echo "# Generate SDK..."

mkdir generated

docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli-v3 generate -i /local/Operations.yaml -o /local/generated -l python -DpackageName=azure.videoindexer

echo "# Build SDK..."

cd generated
touch azure/__init__.py
python setup.py sdist

mv dist/azure.videoindexer-*.tar.gz ..

echo "# Clean up..."

cd ..
rm -rf ${TEMP_FILES}
