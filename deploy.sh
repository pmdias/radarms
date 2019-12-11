#!/usr/bin/env bash

STACK_NAME=$1
COMPOSE_FILE=$2
ENVIRONMENT_FILE=$3

set -o allexport
source $ENVIRONMENT_FILE
set +o allexport

docker stack deploy --compose-file $COMPOSE_FILE $STACK_NAME
