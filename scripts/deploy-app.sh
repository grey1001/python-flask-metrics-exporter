#!/bin/bash

# WARNING: You don't need to edit this file!

SCRIPT=`realpath $0`
SCRIPTPATH=`dirname "$SCRIPT"`

. "${SCRIPTPATH}/../settings.sh"
. "${SCRIPTPATH}/_library.sh"

set -eu

switch_k8s_context
apply_manifests app.yml "Deploying the app"
restart_rollout camunda-app
wait_for_app || log_fail "Couldn't wait for the app to start"
