#!/usr/bin/env bash

source /vagrant/.venv/update-register/bin/activate
source environment-test.sh

py.test --cov application tests/ --cov-report=term --cov-report=html
