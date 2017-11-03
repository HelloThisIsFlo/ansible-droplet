#!/bin/bash

# `cd` in ansible directory to get ansible config: `ansible.cfg` and `inventory` directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $SCRIPT_DIR/ansible

DEFAULT_CFG="digitalocean_token_location: \"{{  ansible_env.HOME }}/config-in-the-cloud/secrets/digitalocean-awesometeam/token\""

echo $DEFAULT_CFG > group_vars/all

echo "Created file \`all\` in \`ansible/group_vars/\`"
