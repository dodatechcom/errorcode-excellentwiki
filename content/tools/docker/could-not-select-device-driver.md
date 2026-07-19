---
title: "[Solution] Docker Could Not Select Device Driver — could not select device driver"
description: "Fix Docker device driver selection error. Configure GPU and device access for containers."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# could not select device driver "" with capabilities

This error occurs when Docker cannot find the required device driver for GPU or other hardware access. Common with NVIDIA GPU containers or other specialized hardware.

## Common Causes

- NVIDIA Container Toolkit not installed
- GPU driver not installed or outdated
- Docker not configured for GPU runtime
- Wrong device driver name specified
- Missing --privileged flag

## How to Fix

### Install NVIDIA Container Toolkit

```bash
# Add repository
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list |   sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' |   sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

# Install
sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit

# Configure Docker
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```

### Use --gpus Flag

```bash
docker run --gpus all nvidia/cuda:11.0-base nvidia-smi
```

### Check GPU Availability

```bash
nvidia-smi
```

### Use Privileged Mode

```bash
docker run --privileged --device /dev/nvidia0 my-image
```

### Specify Device Driver

```bash
docker run --device-driver nvidia --gpus all my-image
```

## Examples

```bash
# Example 1: Check NVIDIA toolkit
nvidia-smi
# Shows GPU info if installed

# Example 2: Run GPU container
docker run --gpus all nvidia/cuda:11.0-base nvidia-smi

# Example 3: Install toolkit
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```

## Related Errors

- [Docker out of memory]({{< relref "/tools/docker/docker-out-of-memory" >}}) — related error
- [Docker exec error]({{< relref "/tools/docker/docker-exec-error" >}}) — related error
