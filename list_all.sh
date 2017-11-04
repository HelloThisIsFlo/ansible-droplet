#!/bin/bash

# Debug script. Requires `jq` installed (npm tool)

DO_TOKEN_FILE="/Users/floriankempenich/config-in-the-cloud/secrets/digitalocean-awesometeam/token"
DO_TOKEN=$(cat $DO_TOKEN_FILE)

RES=$(\
  curl \
  -s \
  -X GET \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DO_TOKEN" \
  "https://api.digitalocean.com/v2/droplets")

echo $RES | jq '.droplets[].name' -r
