---
title: "[Solution] macOS Audio Output Error -- No Sound From Mac Speakers"
description: "Fix macOS audio output error when no sound comes from Mac speakers or headphones. Resolve audio output issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Audio Output Error -- No Sound From Mac Speakers

Audio output errors prevent sound from playing through the Mac's speakers, connected headphones, or external audio devices. The volume may show as working but no sound is produced.

## Common Causes
- Audio output device is not selected correctly
- Core Audio service has crashed
- Audio driver is corrupted or outdated
- Headphone jack has debris or a faulty connection
- Audio MIDI Setup has incorrect configuration

## How to Fix
1. Check the audio output device in System Preferences > Sound
2. Restart the Core Audio service
3. Check Audio MIDI Setup for correct configuration
4. Try a different audio output device
5. Reset the audio configuration

```bash
# Restart Core Audio
sudo launchctl stop com.apple.audio.coreaudiod
sudo launchctl start com.apple.audio.coreaudiod

# Check audio devices
system_profiler SPAudioDataType
```

## Examples

```bash
# Test audio output
say "Hello, this is a test"

# Open Audio MIDI Setup
open -a "Audio MIDI Setup"
```

This error is common when the wrong audio output device is selected, when Core Audio crashes, or when the Audio MIDI Setup has an incorrect configuration.
