#!/bin/sh

echo Updating backend image
docker pull essamgouda97/ayd_backend:latest

echo Updating frontend image
docker pull essamgouda97/ayd_frontend:latest

echo Updating is_dead microservice image
docker pull essamgouda97/ayd_is_dead_ms:latest

echo Updating sequence_runner microservice image
docker pull essamgouda97/ayd_sequence_runner_ms:latest
