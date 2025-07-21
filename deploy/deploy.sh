#!/bin/bash
cd ~/projects/smart-stock

# Venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Migrations va collectstatic
export $(cat .env | xargs)
python manage.py migrate
python manage.py collectstatic --noinput

# Gunicorn restart
sudo systemctl restart smart-stock.service
