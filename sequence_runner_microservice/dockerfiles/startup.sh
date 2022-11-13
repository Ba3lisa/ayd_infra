#!/bin/sh

echo Running startup script: $STARTUP_SH
echo Moving to $WORKING_DIR
cd $WORKING_DIR

# TODO run django server on startup
tail -f /dev/null
