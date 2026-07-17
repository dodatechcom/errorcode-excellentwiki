---
title: "[Solution] Linux Kernel Panic — GPU Driver Error"
description: "Fix Linux kernel panic caused by GPU driver errors. Resolve display driver crashes, Nouveau/NVIDIA/AMD kernel panics, and GPU hangs."
platforms: ["linux"]
severities: ["error"]
error-types: ["system-error"]
tags: ["kernel-panic", "gpu", "driver", "nvidia", "amdgpu", "nouveau", "display"]
weight: 5
---

# Linux: Kernel panic — GPU driver error

The `kernel panic — not syncing` caused by a GPU driver error (e.g., `GPU has fallen off the bus`, `Nouveau: trap: gr fault`, `amdgpu: GPU reset`) means the graphics driver encountered an unrecoverable hardware or firmware error and the kernel could not safely continue execution.

## What This Error Means

GPU drivers operate in kernel space and have direct access to hardware. When the GPU hangs, crashes, or enters an unrecoverable state, the driver triggers a kernel panic because the system state is potentially corrupted. This is common with NVIDIA proprietary drivers, Nouveau, AMDGPU, and Intel i915 under heavy GPU load or with driver bugs.

## Common Causes

- GPU hardware failure or overheating
- Incompatible or buggy GPU driver version
- GPU firmware (VBIOS) corruption or incompatibility
- Power supply insufficient for GPU under load
- Xorg/Wayland compositor triggering driver bugs
- CUDA/OpenCL compute workload exceeding GPU capabilities
- PCIe link instability or poor GPU seating

## How to Fix

### 1. Check Kernel Logs for GPU Errors

```bash
# Look for GPU-related errors
sudo dmesg | grep -i -E 'gpu|nvidia|nouveau|amdgpu|i915|drm'

# Check for hardware errors
sudo dmesg | grep -i 'mce\|hardware error\|trap'

# Check Xorg logs
sudo cat /var/log/Xorg.0.log | grep -i -E 'EE|error|fail'
```

### 2. Update or Downgrade GPU Driver

```bash
# Check current driver
lspci -k | grep -A3 'VGA\|3D'

# For NVIDIA proprietary driver
sudo apt install nvidia-driver-535    # or latest stable
sudo apt remove --purge nvidia-*
sudo apt install nvidia-driver-470    # try older if new causes issues

# For NVIDIA open-source (Nouveau)
sudo apt install xserver-xorg-video-nouveau

# For AMD
sudo apt install firmware-amd-graphics
sudo apt install xserver-xorg-video-amdgpu
```

### 3. Set Kernel Parameters for Stability

```bash
# Edit GRUB defaults
sudo nano /etc/default/grub

# Add to GRUB_CMDLINE_LINUX:
# nomodeset            - Disable kernel mode setting (debugging)
# nouveau.modeset=0    - Disable Nouveau
# nvidia-drm.modeset=1 - Enable NVIDIA DRM
# amdgpu.ppfeaturemask=0xffffffff - Unlock AMD power features

# Apply changes
sudo update-grub
sudo reboot
```

### 4. Fix Power Supply Issues

```bash
# Check GPU power draw (if supported by driver)
cat /sys/class/drm/card0/device/power_dpm_state

# Monitor GPU temperature
nvidia-smi                          # NVIDIA
cat /sys/class/drm/card0/device/hwmon/hwmon*/temp1_input  # AMD

# Check PSU wattage meets GPU requirements
# High-end GPUs may need 650W+ PSU
```

### 5. Reset GPU Without Reboot

```bash
# For NVIDIA GPUs
sudo nvidia-smi --gpu-reset

# For AMD GPUs (requires specific support)
echo 1 | sudo tee /sys/class/drm/card0/device/pp_dpm_reset

# Reload the driver module
sudo modprobe -r amdgpu
sudo modprobe amdgpu
```

### 6. Use Safe Graphics Mode

```bash
# Boot into recovery mode from GRUB
# Select 'Advanced options' -> 'Recovery mode'

# Or add nomodeset to GRUB
sudo nano /etc/default/grub
# Add: GRUB_CMDLINE_LINUX="nomodeset"
sudo update-grub

# Once in GUI, reinstall correct driver
```

## Examples

```bash
$ sudo dmesg | grep -i gpu
[  123.456] NVRM: GPU at PCI:0000:01:00; GPU uuid: ...
[  123.789] NVRM: GPU 0000:01:00.0000: Has fallen off the bus
[  123.789] NVRM: RmInitAdapter failed! (0x62:0xffffffff:1089)
[  123.789] NVRM: os_pci_init_handle: invalid PCI handle
[  123.790] Kernel panic - not syncing: Attempted to kill init!

$ lspci -k | grep -A3 'VGA'
01:00.0 VGA compatible controller: NVIDIA Corporation GA106
        Kernel driver in use: nvidia

# Fix: update NVIDIA driver and check GPU seating
$ sudo apt install --reinstall nvidia-driver-535
$ sudo reboot
```

## Related Errors

- [Kernel panic]({{< relref "/os/linux/linux-kernel-panic" >}}) — General kernel panic
- [Kernel oops]({{< relref "/os/linux/linux-kernel-oops" >}}) — Kernel bugs
- [Kernel tainted]({{< relref "/os/linux/linux-kernel-tainted" >}}) — Tainted kernel warnings
