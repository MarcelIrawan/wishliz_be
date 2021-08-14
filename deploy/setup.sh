#!/usr/bin/env bash

set -e

# TODO: Set to URL of git repo.
PROJECT_GIT_URL='https://github.com/MarcelIrawan/wishliz_be.git'

PROJECT_BASE_PATH='/usr/local/apps/wishlist-api'

echo "Installing dependencies..."
apt-get update
apt-get install -y python3.9-dev sqlite python3.9-venv pipenv
apt install python3-pip

# Create project directory
mkdir -p $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH

cd $PROJECT_BASE_PATH
#pipenv --python /etc/python3.9
#pipenv install --deploy
#pipenv install uwsgi==2.0.18

# Create virtual environment
mkdir -p $PROJECT_BASE_PATH/env
python3.9 -m venv $PROJECT_BASE_PATH/env
pipenv lock -r > $PROJECT_BASE_PATH/requirements.txt

# Install python packages
$PROJECT_BASE_PATH/env/bin/pip install -r $PROJECT_BASE_PATH/requirements.txt
$PROJECT_BASE_PATH/env/bin/pip install uwsgi==2.0.18

# Run migrations and collectstatic
cd $PROJECT_BASE_PATH
$PROJECT_BASE_PATH/env/bin/python manage.py migrate
$PROJECT_BASE_PATH/env/bin/python manage.py collectstatic --noinput

# Configure supervisor
cp $PROJECT_BASE_PATH/deploy/supervisor_wishlist_api.conf /etc/supervisor/conf.d/wishlist_api.conf
supervisorctl reread
supervisorctl update
supervisorctl restart wishlist_api

# Configure nginx
cp $PROJECT_BASE_PATH/deploy/nginx_wishlist_api.conf /etc/nginx/sites-available/wishlist_api.conf
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/wishlist_api.conf /etc/nginx/sites-enabled/wishlist_api.conf
systemctl restart nginx.service

echo "DONE! :)"
