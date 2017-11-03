#!/bin/bash

if [ -z "$1" ]; then
  echo "Please provide a name for the Droplet"
  echo ""
  echo "    \`create_droplet.sh DROPLET_NAME (DROPLET_SPEC_NAME)\`"
  echo ""
  exit 1
fi


DROPLET_NAME=$1
if [ -z "$2" ]; then
  SPEC_NAME=micro
else
  SPEC_NAME=$2
fi



# `cd` in ansible directory to get ansible config: `ansible.cfg` and `inventory` directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $SCRIPT_DIR/ansible

# Run "Create droplet" playbook
ansible-playbook \
    ./create-droplet-playbook.yml \
    --extra-vars "droplet_name=$DROPLET_NAME droplet_spec_name=$SPEC_NAME"
