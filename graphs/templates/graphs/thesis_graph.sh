#!/usr/bin/env bash

curl --data "count=${1}" {{host}}{% url 'graphs:api:wordcount-list' %}  -H 'Authorization: Token {{token}}'