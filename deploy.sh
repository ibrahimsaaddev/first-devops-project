#!/bin/bash

echo "===== DEPLOYMENT STARTED ====="

git pull

source venv/bin/activate

pip install -r requirements.txt

sudo systemctl restart devops-app

sleep 2

sudo systemctl status devops-app --no-pager

curl http://127.0.0.1:8000/health

echo "===== DEPLOYMENT FINISHED ====="
