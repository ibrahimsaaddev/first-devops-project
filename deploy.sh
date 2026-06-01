#!/bin/bash

echo "Starting deployment..."

sudo systemctl restart devops-app

echo "Application restarted."

sudo systemctl status devops-app --no-pager

echo "Deployment completed."
