---
title: "[Solution] macOS Bluetooth Audio Error — Audio Stuttering or Cutting Out"
description: "Fix macOS Bluetooth audio error: audio stuttering over Bluetooth, AirPods cutting out, Bluetooth speaker disconnects during playback."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 172
---

# Bluetooth Audio Error — Audio Stuttering or Cutting Out

Fix macOS Bluetooth audio error: audio stuttering over Bluetooth, AirPods cutting out, Bluetooth speaker disconnects during playback.

## Common Causes

- Bluetooth bandwidth interference from too many connected devices
- Audio codec quality settings causing latency or dropouts
- Low Bluetooth signal strength due to distance or obstacles
- Bluetooth audio device battery low causing unstable connection

## How to Fix

### 1. Check Bluetooth Audio Device Status

```bash
system_profiler SPBluetoothDataType | grep -A 10 'Connected: Yes'
# Check device battery level in Bluetooth settings
```

### 2. Reduce Bluetooth Interference

```bash
# Disconnect unused Bluetooth devices → Keep only audio device connected
```

### 3. Change Audio Codec Quality

```bash
# System Settings → Sound → Output → Select Bluetooth device → Adjust quality settings
```

### 4. Reset Bluetooth Connection

```bash
# System Settings → Bluetooth → Disconnect → Reconnect
# Or forget device and pair again
```

## Common Scenarios

This error commonly occurs when:

- Audio cuts out every few seconds when using Bluetooth headphones
- AirPods connection drops during music playback or phone calls
- Bluetooth speaker crackles and loses connection intermittently
- Bluetooth audio works but with noticeable delay or echo

## Prevent It

- Keep Bluetooth audio device within 30 feet of Mac
- Reduce number of simultaneously connected Bluetooth devices
- Keep Bluetooth audio device firmware updated
- Use 5GHz WiFi to reduce Bluetooth/WiFi interference
