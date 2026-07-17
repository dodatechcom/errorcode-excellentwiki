---
title: "[Solution] Brew Cask Error — Fix Homebrew Cask Installation Failures"
description: "Fix Homebrew cask errors when brew install --cask fails to download or install a cask. Resolve checksum mismatches, Gatekeeper blocks, and app conflicts."
tools: ["brew"]
error-types: ["cask-error"]
severities: ["error"]
weight: 5
---

This error means `brew install --cask` failed to download, verify, or install a macOS application. Casks install pre-built `.app` bundles, `.dmg` files, or `.pkg` installers, and each step can fail differently.

## What This Error Means

Homebrew casks download a specific version of an application from the developer's server, verify its checksum, and install it to `/Applications`. When this fails:

```
Error: Cask 'firefox' is unavailable: No cask with this name exists
```

Or:

```
Error: Download failed on Cask 'visual-studio-code' with message:
  Download failed: SHA256 mismatch
```

Or:

```
Error: It seems there is already an App at '/Applications/Slack.app'
```

## Why It Happens

- The cask URL has changed and Homebrew's formula is outdated
- The developer released a new version but Homebrew has not updated the checksum yet
- A previous install left the application in `/Applications` and the new install detects a conflict
- The developer's download server is down or rate-limiting
- Gatekeeper or macOS security blocks the unsigned or quarantined application
- The cask was removed from Homebrew

## How to Fix It

### Update Homebrew

```bash
brew update
brew upgrade
```

### Force Reinstall the Cask

```bash
brew reinstall --cask <cask-name>
```

### Remove Existing Application First

```bash
brew uninstall --cask <cask-name>
rm -rf /Applications/<AppName>.app
brew install --cask <cask-name>
```

### Force Overwrite Existing App

```bash
brew install --cask --force <cask-name>
```

### Skip Checksum Verification (Temporary)

When checksums are outdated:

```bash
brew install --cask --no-quarantine <cask-name>
```

### Check if the Cask Exists

```bash
brew search <partial-name>
brew info --cask <cask-name>
```

### Fix Gatekeeper Issues

```bash
sudo xattr -rd com.apple.quarantine /Applications/<AppName>.app
```

## Common Mistakes

- Running `brew install --cask` without `brew update` first
- Forgetting to remove the existing application before reinstalling
- Using `--no-quarantine` permanently instead of waiting for a formula update
- Not checking if the cask name is correct (case-sensitive)
- Installing casks in a CI pipeline without accepting license agreements first

## Related Pages

- [Brew Install Error]({{< relref "/tools/brew/brew-install-error" >}}) -- formula installation failures
- [Brew Permission Error]({{< relref "/tools/brew/brew-permission-error" >}}) -- permission issues
- [Brew Tap Error]({{< relref "/tools/brew/brew-tap-error" >}}) -- tap repository errors
