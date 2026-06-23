#!/bin/bash

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Installing PixelWise deployment timer..."

sudo cp "$SCRIPT_DIR/deploy/systemd/pixelwise-deploy.service" \
    /etc/systemd/system/

sudo cp "$SCRIPT_DIR/deploy/systemd/pixelwise-deploy.timer" \
    /etc/systemd/system/

sudo systemctl daemon-reload
sudo systemctl enable pixelwise-deploy.timer

echo "Setup completed."
