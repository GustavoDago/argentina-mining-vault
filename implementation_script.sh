#!/usr/bin/env bash
set -euo pipefail

# Navigate to repo root (assumes script is placed in repo root)
cd "$(dirname "$0")"

# 1. Fetch all updates from remote
git fetch --all

# 2. Ensure we are on main and pull latest changes
git checkout main
git pull origin main

# 3. Add any local modifications and commit
if git diff --quiet && git diff --cached --quiet; then
  echo "No changes to commit."
else
  git add .
  git commit -m "Consolidate changes from remote and local modifications"
fi

# 4. Delete merged branches locally (exclude main)
merged_branches=$(git branch --merged | grep -v "\*" | grep -v " main$" || true)
for branch in $merged_branches; do
  git branch -d "$branch" || echo "Failed to delete local branch $branch"
 done

# 5. Delete merged branches remotely
remote_merged=$(git branch -r --merged | grep -v "/main$" | sed 's#origin/##')
for branch in $remote_merged; do
  git push origin --delete "$branch" || echo "Failed to delete remote branch $branch"
 done

# 6. Push any remaining commits to remote
git push origin main

echo "Repository synchronization complete."
