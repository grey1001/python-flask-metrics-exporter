#!/bin/bash

CLUSTER_NAME=femi.abiwon
APP_LANGUAGE=python

CLUSTER_VERSION=$(cat .tool-versions | grep kubectl | cut -d" " -f2)

[ -z "$APP_LANGUAGE" ] && echo "Programming language for the app not defined, please fill it in settings.sh" && exit 1

[ -z "$CLUSTER_NAME" ] && echo "Cluster name is not defined, please fill it in settings.sh" && exit 1
