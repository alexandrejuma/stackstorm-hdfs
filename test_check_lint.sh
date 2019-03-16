#!/bin/bash

PACK_DIR=/opt/stackstorm/packs/webhdfs/

echo "################# st2-check-validate-json-file #################"
find $PACK_DIR -name "*json" -exec st2-check-validate-json-file {} \;

echo "################# st2-check-validate-yaml-file #################"
find $PACK_DIR -name "*yaml" -exec st2-check-validate-yaml-file {} \;

echo "################# st2-check-validate-pack-metadata-exists #################"
st2-check-validate-pack-metadata-exists $PACK_DIR

echo "################# st2-check-print-pack-tests-coverage #################"
st2-check-print-pack-tests-coverage $PACK_DIR

