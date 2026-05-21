#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────
# deploy-aws.sh  — Run this ON your AWS EC2 instance (Ubuntu 22/24)
#
# What it does:
#   1. Installs Docker + Docker Compose (if not present)
#   2. Pulls latest images from Docker Hub
#   3. Brings the stack up (replaces any running containers)
#
# Usage:
#   scp deploy-aws.sh docker-compose.yml ubuntu@<EC2-IP>:~/
#   ssh ubuntu@<EC2-IP>
#   export DOCKERHUB_USERNAME=yourname
#   chmod +x deploy-aws.sh && ./deploy-aws.sh
# ─────────────────────────────────────────────────────────────────
set -euo pipefail

: "${DOCKERHUB_USERNAME:?Set DOCKERHUB_USERNAME before running this script.}"

APP_DIR="$HOME/insurance-app"

# ── 1. Install Docker if missing ─────────────────────────────────
if ! command -v docker &>/dev/null; then
  echo "==> Installing Docker..."
  sudo apt-get update -y
  sudo apt-get install -y ca-certificates curl gnupg lsb-release
  sudo install -m 0755 -d /etc/apt/keyrings
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
    | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
  echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
    https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" \
    | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  sudo apt-get update -y
  sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
  sudo usermod -aG docker "$USER"
  echo "==> Docker installed. You may need to log out and back in for group changes."
else
  echo "==> Docker already installed: $(docker --version)"
fi

# ── 2. Install docker compose plugin if missing ──────────────────
if ! docker compose version &>/dev/null 2>&1; then
  echo "==> Installing docker compose plugin..."
  sudo apt-get install -y docker-compose-plugin
fi

# ── 3. Set up app directory ──────────────────────────────────────
mkdir -p "$APP_DIR"
cp docker-compose.yml "$APP_DIR/"

# ── 4. Pull latest images ────────────────────────────────────────
echo "==> Pulling images from Docker Hub..."
cd "$APP_DIR"
DOCKERHUB_USERNAME="$DOCKERHUB_USERNAME" docker compose pull

# ── 5. Bring the stack up ────────────────────────────────────────
echo "==> Starting containers..."
DOCKERHUB_USERNAME="$DOCKERHUB_USERNAME" docker compose up -d --remove-orphans

echo ""
echo "✅  Deployment complete!"
echo "   Frontend : http://$(curl -s http://checkip.amazonaws.com)"
echo "   Backend  : http://$(curl -s http://checkip.amazonaws.com):8000"
echo "   Health   : http://$(curl -s http://checkip.amazonaws.com):8000/health"
