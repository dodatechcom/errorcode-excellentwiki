---
title: "[Solution] Vagrant Box Add Timeout"
description: "Fix Vagrant box add timeout errors when downloading base boxes. Resolve network issues and download failures."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Vagrant Box Add Timeout

A Vagrant box add timeout occurs when the box download takes too long and the operation is terminated.

## Why This Happens

- Slow internet connection
- Large box file size
- Vagrant Cloud server issues
- Network proxy blocking the download
- Disk space exhaustion during extraction

## Common Error Messages

- `vagrant_box_add_timeout`
- `vagrant_box_download_timeout`
- `vagrant_box_extract_timeout`
- `vagrant_box_network_error`

## How to Fix It

### Solution 1: Increase Timeout

Set a longer timeout for box operations:

```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"
  config.vm.box_download_timeout = 600
end
```

### Solution 2: Use a Direct URL

Download the box manually and add from file:

```bash
wget -O box.box https://vagrantcloud.com/ubuntu/boxes/focal64/versions/20.04/providers/virtualbox.box
vagrant box add my-box box.box
```

### Solution 3: Check Disk Space

Ensure adequate disk space for download and extraction:

```bash
df -h
```

### Solution 4: Configure Proxy

If behind a proxy, configure Vagrant to use it:

```bash
export http_proxy=http://proxy.example.com:8080
export https_proxy=http://proxy.example.com:8080
vagrant box add ubuntu/focal64
```

## Common Scenarios

- **Timeout during download:** Check internet speed and proxy settings
- **Timeout during extraction:** Verify disk space availability
- **Intermittent timeouts:** Try a different mirror or CDN

## Prevent It

- Use local box files when possible
- Monitor disk space before adding boxes
- Configure appropriate timeouts in Vagrantfile
