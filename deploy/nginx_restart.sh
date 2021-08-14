#!/usr/bin/env bash

set -e

PROJECT_BASE_PATH='/usr/local/apps/wishlist-api'

cp $PROJECT_BASE_PATH/deploy/nginx_wishlist_api.conf /etc/nginx/sites-available/wishlist_api.conf
systemctl restart nginx.service

echo "DONE! :)"