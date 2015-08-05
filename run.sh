#!/usr/bin/env bash

#get the absolute path to the directory that this script is in
dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
cd $dir

source ./environment.sh

python run.py
