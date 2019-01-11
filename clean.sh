#!/bin/bash

rm -rf ./build
rm -rf ./dist
rm -rf ./ansible_droplet.egg-info
pipenv run pip uninstall -y ansible-droplet
