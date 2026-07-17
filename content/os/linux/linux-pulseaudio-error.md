---
title: "[Solution] Linux PulseAudio Connection Refused — Fix"
description: "Fix Linux PulseAudio 'connection refused' errors. Resolve audio server issues, restart PulseAudio, and fix sound output problems."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Linux: PulseAudio: connection refused

The `PulseAudio: connection refused` error means the PulseAudio sound server is not running or is not accepting connections. Applications that try to play sound will fail or produce no audio output.

## Common Causes

- PulseAudio daemon crashed or not running
- User PulseAudio instance not started
- ALSA configuration conflicts
- Multiple PulseAudio instances conflicting
- Permission issues with audio devices
- Corrupted PulseAudio configuration
- PulseAudio module loading failure

## How to Fix

### 1. Start or Restart PulseAudio

```bash
# Start PulseAudio for the current user
pulseaudio --start

# Restart PulseAudio
pulseaudio -k
pulseaudio --start

# Check if PulseAudio is running
pactl info
```

### 2. Check PulseAudio Status

```bash
# List PulseAudio modules
pactl list modules short

# List audio sinks
pactl list sinks short

# List audio sources
pactl list sources short

# Set default sink
pactl set-default-sink <sink-name>
```

### 3. Kill and Restart PulseAudio Automatically

```bash
# Kill PulseAudio (systemd will restart it)
systemctl --user stop pulseaudio.service
systemctl --user stop pulseaudio.socket

# Restart
systemctl --user start pulseaudio.service

# Or kill and let it auto-restart
pulseaudio -k
sleep 2
pulseaudio --start
```

### 4. Check ALSA Configuration

```bash
# Check ALSA devices
aplay -l
arecord -l

# Test ALSA directly
speaker-test -t sine -f 440 -l 1

# If ALSA works but PulseAudio doesn't, the issue is in PulseAudio
```

### 5. Reset PulseAudio Configuration

```bash
# Move the configuration aside
mv ~/.config/pulse ~/.config/pulse.backup
mv ~/.pulse ~/.pulse.backup

# Restart PulseAudio
pulseaudio -k
pulseaudio --start
```

### 6. Check for Multiple PulseAudio Instances

```bash
# Check running PulseAudio processes
ps aux | grep pulse

# Kill all instances
killall pulseaudio
pulseaudio --start
```

### 7. Fix Permission Issues

```bash
# Add user to the audio group
sudo usermod -a -G audio $USER

# Log out and back in for group changes to take effect
```

### 8. Reinstall PulseAudio

```bash
# Debian/Ubuntu
sudo apt install --reinstall pulseaudio pulseaudio-utils

# Fedora/RHEL
sudo dnf reinstall pulseaudio
```

## Examples

```bash
$ pactl info
Connection failure: Connection refused
pa_context_connect() failed: Connection refused

$ pulseaudio --start
$ pactl info
Server String: /run/user/1000/pulse/native
Library Protocol Version: 34
Server Protocol Version: 34
Is Local: yes
Client Index: 0
Tile Size: 65472
User Name: user
Host Name: hostname
Server Name: pulseaudio
Server Version: 16.1
Default Sample Specification: s16le 2ch 44100Hz
Default Sink: alsa_output.pci-0000_00_1f.3.analog-stereo
Default Source: alsa_input.pci-0000_00_1f.3.analog-stereo
```

## Related Errors

- [ALSA device not found]({{< relref "/os/linux/linux-alsa-error" >}}) — Hardware audio issues
- [Kernel module error]({{< relref "/os/linux/linux-kernel-module-error" >}}) — Audio driver problems
- [Permission denied]({{< relref "/os/linux/permission-denied10" >}}) — Group/permission issues
