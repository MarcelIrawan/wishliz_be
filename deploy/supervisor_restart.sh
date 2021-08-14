#!/usr/bin/env bash

set -e

PROJECT_BASE_PATH='/usr/local/apps/wishlist-api'

cp $PROJECT_BASE_PATH/deploy/supervisor_wishlist_api.conf /etc/supervisor/conf.d/wishlist_api.conf
supervisorctl reread
supervisorctl update
supervisorctl restart wishlist_api

echo 'DONE!! :D'