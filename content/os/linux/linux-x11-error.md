---
title: "[Solution] Linux X11 Display Error — Fix"
description: "Fix Linux X11 'display error' and 'cannot open display' issues. Resolve X server, DISPLAY variable, and display permission problems."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Linux: X11: display error

X11 display errors occur when an application cannot connect to the X server. The typical error is `cannot open display: :0` or `Error: Can't open display`.

## Common Causes

- DISPLAY environment variable not set
- X server not running
- X server permissions (xhost) blocking client
- SSH X11 forwarding not configured
- Wayland compositor running (not X11)
- X server crashed or frozen
- Missing X11 socket (/tmp/.X11-unix)
- Access control list (xauth) issues

## How to Fix

### 1. Check DISPLAY Variable

```bash
# Check the DISPLAY variable
echo $DISPLAY

# Set it if empty
export DISPLAY=:0

# For remote sessions
export DISPLAY=:10.0
```

### 2. Check X Server Status

```bash
# Check X server processes
ps aux | grep -E 'Xorg|X :'

# Check X socket
ls -la /tmp/.X11-unix/

# Check if X server is accessible
xdpyinfo
```

### 3. Grant X Server Permissions

```bash
# Allow all local connections (temporarily)
xhost +local:

# Allow a specific user
xhost +SI:localuser:username

# Allow remote host
xhost +192.168.1.100

# For containers/root (careful)
xhost +local:root
```

### 4. Fix X11 Forwarding (SSH)

```bash
# On the client, use -X or -Y
ssh -X user@remote
ssh -Y user@remote    # Trusted forwarding

# On the server, ensure X11Forwarding is enabled
sudo grep X11Forwarding /etc/ssh/sshd_config
# Should be: X11Forwarding yes

# Also install xauth on the server
sudo apt install xauth
```

### 5. Fix xauth Issues

```bash
# Check MIT-MAGIC-COOKIE
xauth list

# Add a cookie if missing
xauth add :0 . $(mcookie)

# For SSH, forward the cookie
xauth merge ~/.Xauthority
```

### 6. Check Wayland vs X11

```bash
# Check if running Wayland
echo $XDG_SESSION_TYPE

# Force X11 session
# At the login screen, select "Ubuntu on Xorg"
# Or edit /etc/gdm3/custom.conf and uncomment:
# WaylandEnable=false
```

### 7. Restart X Server

```bash
# Switch to a different TTY and restart
# Press Ctrl+Alt+F2, log in, then:
sudo systemctl restart display-manager

# Or for specific display managers
sudo systemctl restart gdm3    # GNOME
sudo systemctl restart lightdm  # LightDM
sudo systemctl restart sddm    # KDE
```

### 8. Set DISPLAY for Applications

```bash
# Run a single application with a specific display
DISPLAY=:0 firefox

# Or export permanently
echo 'export DISPLAY=:0' >> ~/.bashrc
```

## Examples

```bash
$ echo $DISPLAY
:0

$ xdpyinfo | grep -E 'name|version|vendor'
name of display:    :0
version number:    11.0
vendor vendor:     The X.Org Foundation

# Working correctly

$ ssh -X user@remote
$ echo $DISPLAY
localhost:10.0

$ xclock
# X11 forwarding working
```

## Related Errors

- [Wayland compositor error]({{< relref "/os/linux/linux-wayland-error" >}}) — Wayland display issues
- [Desktop environment error]({{< relref "/os/linux/linux-desktop-error" >}}) — DE startup failures
- [Permission denied]({{< relref "/os/linux/permission-denied10" >}}) — xauth/cookie denials
