#!/bin/bash

# Exit on error
set -e

# Stash local changes
git stash
# Update repo
git pull
# Restore local changes
git stash pop

# Restart service
systemctl --user restart transit-display
