#!/usr/bin/env bash

echo "Hello {{token}}"

curl --data "count=${1}" {{host}}{% url 'graphs:api:wordcount-list' %}  -H 'Authorization: Token {{token}}'