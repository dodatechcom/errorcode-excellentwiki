---
title: "[Solution] macOS WindowServer Error -- WindowServer High CPU or Crashing"
description: "Fix macOS WindowServer error when WindowServer uses excessive CPU or crashes. Resolve WindowServer issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS WindowServer Error -- WindowServer High CPU or Crashing

WindowServer is the macOS process responsible for drawing and managing windows on the screen. When it uses excessive CPU or crashes, you may experience slow performance, graphical glitches, or a black screen.

## Common Causes
- Too many windows or animations consuming GPU resources
- Corrupted display preferences
- External display with unsupported resolution
- GPU driver issue causing rendering problems
- Multiple displays with different refresh rates

## How to Fix
1. Close unnecessary windows to reduce WindowServer load
2. Reduce display resolution or refresh rate
3. Reset display preferences
4. Disconnect external displays temporarily
5. Restart the Mac to clear the WindowServer state

```bash
# Check WindowServer CPU usage
top -o cpu -l 1 | grep WindowServer

# Reset display preferences
defaults delete com.apple.windowserver
```

## Examples

```bash
# Monitor WindowServer resource usage
sudo powermetrics --samplers gpu_power -i 2000 -n 5
```

This error is common when too many windows are open, when an external display has an unsupported resolution, or when GPU drivers have a bug with specific display configurations.
