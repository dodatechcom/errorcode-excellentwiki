---
title: "[Solution] Linux Wayland Compositor Error — Fix"
description: "Fix Linux Wayland compositor errors. Resolve display server crashes, compositor failures, and graphics driver issues."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["wayland", "compositor", "display", "graphics", "wlroots"]
weight: 5
---

# Linux: Wayland: compositor error

Wayland compositor errors occur when the Wayland display server fails to start or crashes. This prevents the graphical desktop session from loading.

## Common Causes

- GPU driver incompatibility with Wayland
- Missing or incompatible graphics drivers
- Compositor configuration errors
- Outdated kernel or mesa drivers
- NVIDIA proprietary driver issues (limited Wayland support)
- Environment variable conflicts with X11
- Missing Wayland protocols

## How to Fix

### 1. Check Compositor Status

```bash
# Check which compositor is running
echo $XDG_SESSION_TYPE
ps aux | grep -E 'gnome-shell|kwin|sway|river|hyprland'

# Check for compositor logs
journalctl --user -u gnome-shell 2>/dev/null
journalctl -u sway 2>/dev/null
```

### 2. Switch to X11 Session

```bash
# At the login screen, click the gear icon and select
# "Ubuntu on Xorg" or similar

# For GDM, disable Wayland permanently:
sudo sed -i 's/#WaylandEnable=false/WaylandEnable=false/' /etc/gdm3/custom.conf
```

### 3. Update Graphics Drivers

```bash
# Update mesa drivers
sudo apt install mesa-utils mesa-va-drivers
sudo dnf install mesa-dri-drivers

# For Intel
sudo apt install intel-media-va-driver

# For AMD
sudo apt install mesa-amdgpu-va-driver

# For NVIDIA (experimental Wayland support)
sudo apt install nvidia-driver-545
```

### 4. Use WLR_BACKEND Environment Variable (wlroots-based compositors)

```bash
# For Sway, Hyprland, etc., force a specific backend
export WLR_BACKEND=drm
export WLR_RENDERER=gl

# For NVIDIA with wlroots
export WLR_NO_HARDWARE_CURSORS=1
export QT_QPA_PLATFORM=wayland
export GDK_BACKEND=wayland
```

### 5. Check for Missing Wayland Protocols

```bash
# Install Wayland development packages
sudo apt install wayland-protocols libwayland-dev

# For wlroots-based compositors
sudo apt install libwlroots-dev
```

### 6. Fix NVIDIA Wayland Issues

```bash
# Check NVIDIA driver version
nvidia-smi

# For GNOME + NVIDIA, add these kernel parameters
# Edit /etc/default/grub:
# GRUB_CMDLINE_LINUX="nvidia_drm.modeset=1"

sudo update-grub
```

### 7. Check Compositor Configuration

```bash
# For Sway, check config
cat ~/.config/sway/config

# For Hyprland
cat ~/.config/hypr/hyprland.conf

# Check for syntax errors in config files
```

### 8. Fall Back to X11

```bash
# Install X11 session
sudo apt install gnome-session-xsession

# Select X11 from the login screen
# At the gear menu, choose "GNOME on Xorg"
```

## Examples

```bash
$ echo $XDG_SESSION_TYPE
wayland

$ journalctl -u sway --no-pager | tail -20
Jun 15 10:00:00 host sway[1234]: 00:00:00.001 [ERROR] Unable to create the WLR DRM backend
Jun 15 10:00:00 host sway[1234]: 00:00:00.001 [ERROR] Failed to open any DRM device

# GPU driver not available — check and install correct driver
```

## Related Errors

- [X11 display error]({{< relref "/os/linux/linux-x11-error" >}}) — X11 issues
- [Desktop environment error]({{< relref "/os/linux/linux-desktop-error" >}}) — DE startup failures
- [Kernel module error]({{< relref "/os/linux/linux-kernel-module-error" >}}) — GPU driver problems
