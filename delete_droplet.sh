#!/bin/bash

if [ -z "$1" ]; then
  echo "Please provide a name for the Droplet"
  echo ""
  echo "    \`delete_droplet.sh DROPLET_NAME\`"
  echo ""
  exit 1
fi


DROPLET_NAME=$1


# `cd` in ansible directory to get ansible config: `ansible.cfg` and `inventory` directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $SCRIPT_DIR

# Create python virtual environment
ansible-playbook ./playbooks/init-playbook.yml

# Run "Create droplet" playbook
ansible-playbook ./playbooks/delete-droplet-playbook.yml --extra-vars "droplet_name=$DROPLET_NAME"

