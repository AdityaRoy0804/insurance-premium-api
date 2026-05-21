#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────
# build-and-push.sh
# Builds both Docker images and pushes them to Docker Hub.
# Usage:
#   export DOCKERHUB_USERNAME=yourname
#   export DOCKERHUB_PASSWORD=yourtoken   # optional – skipped if already logged in
#   chmod +x build-and-push.sh && ./build-and-push.sh
# ─────────────────────────────────────────────────────────────────
set -euo pipefail

: "${DOCKERHUB_USERNAME:?Set DOCKERHUB_USERNAME first.}"

BACKEND_IMAGE="$DOCKERHUB_USERNAME/insurance-backend:latest"
FRONTEND_IMAGE="$DOCKERHUB_USERNAME/insurance-frontend:latest"

echo "==> Logging in to Docker Hub..."
if [[ -n "${DOCKERHUB_PASSWORD:-}" ]]; then
  echo "$DOCKERHUB_PASSWORD" | docker login -u "$DOCKERHUB_USERNAME" --password-stdin
else
  docker login -u "$DOCKERHUB_USERNAME"
fi

echo ""
echo "==> Building backend image: $BACKEND_IMAGE"
docker build -f Dockerfile.backend -t "$BACKEND_IMAGE" .

echo ""
echo "==> Building frontend image: $FRONTEND_IMAGE"
docker build -f Dockerfile.frontend -t "$FRONTEND_IMAGE" .

echo ""
echo "==> Pushing backend..."
docker push "$BACKEND_IMAGE"

echo ""
echo "==> Pushing frontend..."
docker push "$FRONTEND_IMAGE"

echo ""
echo "✅  Done! Images pushed:"
echo "    $BACKEND_IMAGE"
echo "    $FRONTEND_IMAGE"
