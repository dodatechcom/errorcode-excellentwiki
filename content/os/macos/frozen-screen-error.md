---
title: "[Solution] macOS Frozen Screen Error — Display Static and Unresponsive"
description: "Fix macOS frozen screen: display is static, trackpad and keyboard do not respond, requires hard reset to recover."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 104
---

# Frozen Screen Error — Display Static and Unresponsive

Fix macOS frozen screen: display is static, trackpad and keyboard do not respond, requires hard reset to recover.

## Common Causes

- Graphics driver crash leaving display in frozen state
- Kernel panic occurring but display not updating to show it
- Corrupted window server preventing UI updates
- Hardware failure in GPU or display controller

## How to Fix

### 1. Force Restart and Check System State

```bash
ls -lt /Library/Logs/DiagnosticReports/ | head -10
log show --predicate 'eventMessage contains "shutdown"' --last 24h | head -10
```

### 2. Test with External Display

```bash
system_profiler SPDisplaysDataType
# Connect external display via Thunderbolt or HDMI
```

### 3. Reset Graphics Driver

```bash
# Hold Option+Command+P+R for 20s to reset NVRAM
defaults delete com.apple.windowserver.plist
```

### 4. Check for Hardware Issues

```bash
# Run Apple Diagnostics: restart and hold D
log show --predicate 'subsystem == "com.apple.gpu"' --last 1h
```

## Common Scenarios

This error commonly occurs when:

- Screen freezes but cursor still moves but cannot click
- Display becomes completely static after waking from sleep
- Frozen screen occurs during graphically intensive applications
- External display connected when screen freeze occurred

## Prevent It

- Keep graphics drivers updated through macOS software updates
- Avoid running too many GPU-intensive apps simultaneously
- Ensure adequate ventilation to prevent GPU overheating
- Test with external display periodically to catch hardware issues
