#!/bin/bash

# `cd` in ansible directory to get ansible config: `ansible.cfg` and `inventory` directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $SCRIPT_DIR/ansible

DEFAULT_CFG='
ssh_pub_key_name_on_digitalocean: "Main SSH Key"
ssh_pub_key_to_load_on_droplet_location: "{{ ansible_env.HOME }}/.ssh/id_rsa.pub"

digitalocean_token_location: "{{ ansible_env.HOME }}/config-in-the-cloud/secrets/digitalocean-awesometeam/token"
'

echo "$DEFAULT_CFG" > group_vars/all

echo "Created file \`all\` in \`ansible/group_vars/\`"
