#!/bin/bash

if [ -z "$1" ]; then
  echo "Please provide a name for the Droplet"
  echo ""
  echo "    \`create_droplet.sh DROPLET_NAME\`"
  echo ""
  exit 1
fi


DROPLET_NAME=$1


# `cd` in ansible directory to get ansible config: `ansible.cfg` and `inventory` directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $SCRIPT_DIR

# Run "Create droplet" playbook
ansible-playbook ./playbooks/create-droplet-playbook.yml --extra-vars "droplet_name=$DROPLET_NAME"
