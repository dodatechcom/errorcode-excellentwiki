---
title: "[Solution] Linux: disk-usb-error — USB disk error"
description: "Fix Linux disk-usb-error errors. USB disk error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["disk"]
weight: 6
---
# Linux: USB Storage Error

USB storage errors occur when USB-connected drives fail to initialize, mount, or maintain connection.

## Common Causes

- Insufficient power delivery over USB port (especially bus-powered drives)
- Faulty USB cable or damaged port
- USB controller driver issues (xhci, ehci)
- Drive using aggressive power management and not waking up
- Filesystem not cleanly unmounted causing corruption

## How to Fix

### 1. Check USB Device Detection

```bash
lsusb
sudo lsusb -t
sudo usb-devices
```

### 2. Check Kernel Messages

```bash
dmesg | grep -iE "usb|sd" | grep -iE "error|fail|reset" | tail -30
```

### 3. Disable USB Auto-Suspend

```bash
echo "N" | sudo tee /sys/module/usbcore/parameters/autosuspend
```

### 4. Reset USB Device

```bash
# Unbind and rebind 
echo "1-2" | sudo tee /sys/bus/usb/drivers/usb/unbind
echo "1-2" | sudo tee /sys/bus/usb/drivers/usb/bind
```

## Examples

```bash
$ dmesg | grep usb | tail -3
[ 5678.901] usb 3-2: new high-speed USB device number 5 using xhci_hcd
[ 5679.012] usb 3-2: device descriptor read/64, error -110
[ 5679.234] usb 3-2: device not accepting address 5, error -110
```
