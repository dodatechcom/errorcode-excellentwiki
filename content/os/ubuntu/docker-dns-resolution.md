---
title: "Docker Container DNS Resolution Error"
description: "Containers cannot resolve DNS names or external hostnames"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Docker Container DNS Resolution Error

Containers cannot resolve DNS names or external hostnames

## Common Causes

- Docker daemon DNS configuration incorrect
- /etc/resolv.conf not properly copied to container
- Internal DNS server (127.0.0.11) not responding
- Network namespace isolation preventing DNS access

## How to Fix

1. Check container DNS: `docker exec <container> cat /etc/resolv.conf`
2. Configure DNS in daemon.json: `{"dns": ["8.8.8.8"]}`
3. Restart Docker daemon: `sudo systemctl restart docker`
4. Test DNS from container: `docker exec <container> nslookup google.com`

## Examples

```bash
# Check container DNS settings
docker exec mycontainer cat /etc/resolv.conf

# Test DNS resolution
docker exec mycontainer nslookup google.com

# Set custom DNS in /etc/docker/daemon.json
echo '{"dns": ["8.8.8.8", "8.8.4.4"]}' | sudo tee /etc/docker/daemon.json
sudo systemctl restart docker
```
