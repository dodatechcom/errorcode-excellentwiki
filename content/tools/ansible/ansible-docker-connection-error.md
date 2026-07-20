---
title: "[Solution] Ansible Docker Connection Error"
description: "Resolve Ansible Docker connection plugin errors when managing containers"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible cannot connect to Docker daemon or containers using the Docker connection plugin.

```
FAILED! => "docker connection plugin failed to connect: Cannot connect to Docker daemon"
```

## Common Causes

- Docker daemon not running
- Current user not in docker group
- Docker socket permissions wrong
- Docker connection plugin not installed

## How to Fix

```bash
sudo systemctl start docker
sudo usermod -aG docker $USER
newgrp docker
ls -la /var/run/docker.sock
```

```yaml
[containers]
container1 ansible_connection=docker
```
