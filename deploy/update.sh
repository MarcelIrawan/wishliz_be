#!/usr/bin/env bash

set -e

PROJECT_BASE_PATH='/usr/local/apps/wishlist-api'

git pull
pipenv lock -r > $PROJECT_BASE_PATH/requirements.txt
$PROJECT_BASE_PATH/env/bin/pip install -r $PROJECT_BASE_PATH/requirements.txt
$PROJECT_BASE_PATH/env/bin/python manage.py migrate
$PROJECT_BASE_PATH/env/bin/python manage.py collectstatic --noinput
supervisorctl restart wishlist_api

echo "DONE! :)"
