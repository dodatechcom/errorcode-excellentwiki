---
title: "[Solution] Brew Update Error — Fix brew update Failures"
description: "Fix Homebrew update errors when brew update fails to fetch or merge the latest formula changes. Reset the Homebrew git repository and fix dirty working states."
tools: ["brew"]
error-types: ["update-error"]
severities: ["error"]
weight: 5
---

This error means `brew update` failed to fetch the latest formula definitions from Homebrew's repositories or could not merge them into your local copy. The update aborts and your formula list remains outdated.

## What This Error Means

`brew update` pulls from the Homebrew core and homebrew-cask git repositories. When the pull fails or the merge has conflicts, you see:

```
Error: Failed to tap: homebrew/core
```

Or:

```
fatal: refusing to merge unrelated histories
```

Or:

```
error: Your local changes to the following files would be overwritten
```

## Why It Happens

- A previous `brew update` was interrupted, leaving the git state dirty
- You manually edited formula files in `/usr/local/Homebrew/Library/`
- The Homebrew installation was moved or copied instead of installed properly
- Git is not installed or not working correctly on the system
- A network error prevented the fetch from completing
- macOS Xcode Command Line Tools git is outdated

## How to Fix It

### Reset the Homebrew Repository

```bash
cd /usr/local/Homebrew/Library
git status
git reset --hard origin/master
brew update
```

On Apple Silicon:

```bash
cd /opt/homebrew/Library
git status
git reset --hard origin/master
brew update
```

### Re-fetch and Force Reset

```bash
cd /usr/local/Homebrew/Library
git fetch origin
git reset --hard origin/master
cd /usr/local
git reset --hard origin/master
brew update
```

### Remove and Reinstall Homebrew

As a last resort:

```bash
rm -rf /usr/local/Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Check Git Is Working

```bash
git --version
```

If git is missing:

```bash
xcode-select --install
```

### Fix Dirty Working Directory

```bash
cd /usr/local/Homebrew/Library
git stash
git pull
git stash pop
```

### Use HOMEBREW_NO_INSTALL_CLEANUP

Sometimes cleanup during update causes failures:

```bash
HOMEBREW_NO_INSTALL_CLEANUP=1 brew update
```

## Common Mistakes

- Editing files inside `/usr/local/Homebrew/Library/` directly
- Running `brew update` in a script without checking if git is installed
- Using `sudo brew update` which corrupts file ownership
- Not checking `git status` inside the Homebrew directory before resetting

## Related Pages

- [Brew Permission Error]({{< relref "/tools/brew/brew-permission-error" >}}) -- permission issues
- [Brew Install Error]({{< relref "/tools/brew/brew-install-error" >}}) -- formula installation failures
- [Brew Tap Error]({{< relref "/tools/brew/brew-tap-error" >}}) -- tap repository errors
