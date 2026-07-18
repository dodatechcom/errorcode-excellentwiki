---
title: "[Solution] macOS App Extension Error — Today Widget or Share Extension Not Working"
description: "Fix macOS app extension error: Today widget not loading, Share extension missing, app extension crashes, extension not appearing."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 215
---

# App Extension Error — Today Widget or Share Extension Not Working

Fix macOS app extension error: Today widget not loading, Share extension missing, app extension crashes, extension not appearing.

## Common Causes

- App extension not properly registered with system
- Extension process crashed during initialization
- Extension entitlements missing required capabilities
- System UI cache preventing extensions from loading

## How to Fix

### 1. Check App Extensions

```bash
# System Settings → Privacy & Security → Extensions → Review available extensions
# Or:pluginkit -m -v -i com.apple.appextension
```

### 2. Re-register Extensions

```bash
pluginkit -e reset
# Restart Mac to re-register all extensions
```

### 3. Reinstall App

```bash
# Delete and reinstall app to re-register its extensions
```

### 4. Check Extension Logs

```bash
log show --predicate 'process == "pluginkitd"' --last 1h | head -20
```

## Common Scenarios

This error commonly occurs when:

- Today widget shows blank or loading spinner indefinitely
- Share menu does not show app's share extension
- Extension appears in settings but does not function
- Extension crashes immediately when activated

## Prevent It

- Restart Mac to re-register crashed extensions
- Reinstall app if its extensions stop working
- Keep macOS updated for extension framework compatibility
- Check extension logs in Console for crash details
