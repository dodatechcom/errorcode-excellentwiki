---
title: "[Solution] Linux ALSA Device Not Found — Sound Fix"
description: "Fix Linux ALSA 'device not found' errors. Detect sound cards, load audio modules, and restore audio output."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Linux: ALSA: device not found

The `ALSA: device not found` error means the Advanced Linux Sound Architecture cannot detect or access a sound card. No audio input or output devices are available.

## Common Causes

- Sound card driver not loaded
- Kernel module for audio hardware missing
- Sound card muted or disconnected
- BIOS/UEFI audio disabled
- ALSA configuration corrupted
- HDMI/DP audio not detected (GPU audio)
- USB audio device not recognized

## How to Fix

### 1. List ALSA Devices

```bash
# List sound cards
cat /proc/asound/cards
aplay -l
arecord -l

# List ALSA control devices
amixer
```

### 2. Detect and Load Audio Modules

```bash
# Probe ALSA for devices
sudo alsa force-reload

# Load common sound modules
sudo modprobe snd
sudo modprobe snd-hda-intel
sudo modprobe snd-usb-audio
sudo modprobe snd-hdmi-lpe-audio

# Check loaded modules
lsmod | grep snd
```

### 3. Unmute and Set Volume

```bash
# Open alsamixer
alsamixer

# Use arrow keys to navigate
# Press 'm' to unmute channels
# Press up arrow to increase volume

# Or from command line
amixer set Master unmute
amixer set Master 80%
amixer set PCM unmute
amixer set PCM 80%
```

### 4. Fix ALSA Configuration

```bash
# Backup current config
sudo cp /etc/asound.conf /etc/asound.conf.backup 2>/dev/null
cp ~/.asoundrc ~/.asoundrc.backup 2>/dev/null

# Set default sound card
sudo nano /etc/asound.conf
```

```
defaults.pcm.card 0
defaults.ctl.card 0
```

### 5. Check BIOS/UEFI Settings

```bash
# On some systems, audio may be disabled in firmware
# Reboot and enter BIOS/UEFI setup
# Look for: "Audio", "Onboard Audio", "HD Audio"
# Ensure it's enabled
```

### 6. Check USB Audio Devices

```bash
# List USB devices
lsusb | grep -i audio

# Check dmesg for USB audio detection
dmesg | grep -i audio
dmesg | grep -i "usb.*audio"

# For USB audio, ensure the module is loaded
sudo modprobe snd-usb-audio
```

### 7. Reinstall ALSA

```bash
# Debian/Ubuntu
sudo apt install --reinstall alsa-base alsa-utils
sudo alsa force-reload

# Fedora/RHEL
sudo dnf reinstall alsa-lib alsa-utils
```

## Examples

```bash
$ aplay -l
aplay: device_list:274: no soundcards found...

$ cat /proc/asound/cards
--- no soundcards ---

$ sudo modprobe snd-hda-intel
$ aplay -l
**** List of PLAYBACK Hardware Devices ****
card 0: PCH [HDA Intel PCH], device 0: ALC892 Analog [ALC892 Analog]
  Subdevices: 1/1
  Subdevice #0: subdevice #0

$ speaker-test -t sine -f 440
# Sound heard!
```

## Related Errors

- [PulseAudio error]({{< relref "/os/linux/linux-pulseaudio-error" >}}) — Sound server issues
- [Kernel module error]({{< relref "/os/linux/linux-kernel-module-error" >}}) — Driver problems
- [Kernel Oops]({{< relref "/os/linux/linux-kernel-oops" >}}) — Audio driver crash
