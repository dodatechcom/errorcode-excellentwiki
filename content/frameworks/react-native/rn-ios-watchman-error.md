---
title: "[Solution] React Native iOS Watchman Error"
description: "react-native iOS build fails because watchman service is not running or has incorrect file watcher limits on macOS"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The iOS watchman error occurs when the watchman file watching service is not running, is outdated, or has insufficient inotify/monitoring limits to track the React Native project files. Metro bundler requires watchman to detect changes for fast refresh.

## Common Causes

- Watchman not installed or removed by an OS update
- Watchman's persistent storage has become corrupted due to power loss
- File monitoring limit set too low for the number of files in node_modules
- Watchman can't watch the directory because of permissions or nested mounts
- Watchman version is older than required by Metro

## How to Fix

1. Reset watchman:

```bash
watchman watch-del-all
watchman shutdown-server
```

2. Increase file watcher limits:

```bash
# macOS
echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf
sysctl -p
```

3. Update or reinstall watchman:

```bash
brew uninstall watchman
brew install watchman
```

4. Start watchman if it has stopped:

```bash
launchctl load ~/Library/LaunchAgents/homebrew.mxcl.watchman.plist
```

## Examples

```bash
# Error: watchman can't figure out your path: No such file or directory
# Fix: remove .snap directory or files that break watchman
find . -name "*.swp" -delete

# Also clean node_modules and reinstall
rm -rf node_modules && npm cache clean --force && npm install
```

## Related Errors

- [Bundler Error]({{< relref "/frameworks/react-native/rn-bundler-error" >}})
