#!/bin/bash


echo "Hyper Library Dynamic Integration Technology";

echo "HLEngine updates 2020";
gnome-terminal -e './launcher.sh &'


set -e

local_branch=$(git rev-parse --symbolic-full-name --abbrev-ref HEAD)
remote_branch=$(git rev-parse --abbrev-ref --symbolic-full-name @{u})
remote=$(git config branch.$local_branch.remote)

echo "Fetching from $remote..."
git fetch $remote

if git merge-base --is-ancestor $remote_branch HEAD; then
    echo 'Already up-to-date'
    exit 0
fi

if git merge-base --is-ancestor HEAD $remote_branch; then
    echo 'Fast-forward possible. Merging...'
    git merge --ff-only --stat $remote_branch
    echo "Reboot HLEngine to reflect updates";
else
    echo 'Fast-forward not possible. Rebasing...'
    git rebase --preserve-merges --stat $remote_branch
    echo "Couldn't Update";
    echo "Please Download HLEngine 2020 newer version Manually";
fi
