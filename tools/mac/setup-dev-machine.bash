#!/usr/bin/env bash

# terminate script as soon as any command inside it fails
set -e
# echo shell commands as they are executed
set -x

brew update
# setup python3
brew install python3 || brew upgrade python3
# upgrade pip
pip3 install -U pip

# install dependencies
pip3 install pocket-api
pip3 install -U pocket-api