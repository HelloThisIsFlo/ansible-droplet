#!/bin/bash

function generate_default_config {
    DEFAULT_CFG='
ssh_pub_key_name_on_digitalocean: "Main SSH Key"
ssh_pub_key_to_load_on_droplet_location: "{{ ansible_env.HOME }}/.ssh/id_rsa.pub"

digitalocean_token_location: "{{ ansible_env.HOME }}/config-in-the-cloud/secrets/digitalocean-awesometeam/token"
'

    echo "$DEFAULT_CFG" > group_vars/all
}

function install_requirements {
    ansible-galaxy install -r requirements.yml -p ./external-roles
}

echo "##############################"
echo "##                          ##"
echo "## Performing initial setup ##"
echo "##                          ##"
echo "##############################"
echo

# `cd` in ansible directory to get ansible config: `ansible.cfg` and `inventory` directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $SCRIPT_DIR/ansible

generate_default_config
echo "Created file \`all\` in \`ansible/group_vars/\`"

install_requirements
echo "Installed requirements"
