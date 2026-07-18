---
title: "[Solution] Systemd Unit Is Masked Error — How to Fix"
description: "Fix systemd masked unit errors by unmasking services, understanding why units are masked, and restoring proper unit file configurations"
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
comments: true
---

# Systemd Unit Is Masked Error

This error means the systemd unit you are trying to start, enable, or interact with is masked. A masked unit is completely disabled and cannot be started by any means, including manually or as a dependency of another unit.

## Why It Happens

- The unit was explicitly masked by an administrator or automated script
- Distribution package manager masked the unit during an upgrade
- A security hardening script masked unnecessary services
- The unit was masked to prevent conflicts with a replacement service
- An Ansible or Chef recipe masked the service and the configuration was not reverted
- The unit is masked as part of a minimal Docker container image

## Common Error Messages

```
Failed to start myapp.service: Unit myapp.service is masked.
```

```
Failed to enable myapp.service: Unit myapp.service is masked.
```

```
myapp.service is masked.
```

## How to Fix It

### 1. Check if the Unit Is Masked

```bash
# Check the unit status
systemctl status myapp.service

# Check if it is masked
systemctl is-enabled myapp.service
# Output: masked

# Check what it is masked to
ls -la /etc/systemd/system/myapp.service
# lrwxrwxrwx 1 root root 32 ... /dev/null
```

### 2. Unmask the Unit

```bash
# Unmask the service
sudo systemctl unmask myapp.service

# Verify it is no longer masked
systemctl is-enabled myapp.service

# Start the service
sudo systemctl start myapp.service

# Enable it to start at boot
sudo systemctl enable myapp.service
```

### 3. Unmask and Start in One Step

```bash
# Unmask, enable, and start
sudo systemctl unmask myapp.service && \
sudo systemctl enable myapp.service && \
sudo systemctl start myapp.service
```

### 4. Check All Masked Units

```bash
# List all masked units on the system
systemctl list-unit-files --state=masked

# Unmask multiple units at once
sudo systemctl unmask unit1.service unit2.service unit3.service
```

### 5. Restore Unit File if Symlink Was Deleted

```bash
# If the symlink points to /dev/null, recreate it
sudo rm /etc/systemd/system/myapp.service
sudo systemctl daemon-reload

# If the original unit file exists in /usr/lib/systemd/
ls /usr/lib/systemd/system/myapp.service

# Re-enable the unit
sudo systemctl enable myapp.service
sudo systemctl start myapp.service
```

## Common Scenarios

- **Security hardening**: A CIS benchmark script masked services like `telnet.socket` and `rsh.socket`. This is intentional and should not be reverted unless those services are needed.
- **Docker container**: Base images mask systemd units to reduce startup time. Use `systemctl unmask` in the container startup script if you need those services.
- **Upgrade masking**: A package upgrade masked an old version of a service. Unmask the new version after the upgrade completes.

## Prevent It

- Document which services are intentionally masked in your server build documentation
- Use Ansible or Puppet to ensure masked/unmasked state matches your desired configuration
- Run `systemctl list-unit-files --state=masked` periodically to audit masked units

## Related Pages

- [Systemd Unit Failed](/tools/systemd/systemd-unit-failed)
- [Systemd Dependency Cycle](/tools/systemd/systemd-dependency-cycle)
- [Systemd Log Error](/tools/systemd/systemd-log-error)
