#!/bin/bash

# WARNING: You don't need to edit this file!

# Deletes a kind cluster and its registry

SCRIPT=`realpath $0`
SCRIPTPATH=`dirname "$SCRIPT"`

. "${SCRIPTPATH}/../settings.sh"
. "${SCRIPTPATH}/_library.sh"

make -C "app-${APP_LANGUAGE}" run 
