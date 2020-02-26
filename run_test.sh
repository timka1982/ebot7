#!/usr/bin/env bash

image_id=$(docker build -q . | awk -F':' '{print $2}')
docker run $image_id python -m unittest discover -s python-coding-challenge-test -p "*test*.py"
