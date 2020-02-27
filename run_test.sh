#!/usr/bin/env bash

image_id=$(docker build -q . | awk -F':' '{print $2}')
docker run $image_id python python-coding-challenge-test/test_suite.py
