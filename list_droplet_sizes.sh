#!/bin/bash

# Debug script. Requires `jq` installed (npm tool)

DO_TOKEN_FILE="$HOME/config-in-the-cloud/secrets/digitalocean/token"
DO_TOKEN=$(cat $DO_TOKEN_FILE)

RES=$(\
  curl \
  -s \
  -X GET \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DO_TOKEN" \
  "https://api.digitalocean.com/v2/sizes")

echo $RES | jq '.sizes[] | {slug: .slug, vcpus: .vcpus, hourly: .price_hourly, monthly: .price_monthly}'
