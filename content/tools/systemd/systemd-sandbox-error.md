---
title: "[Solution] Systemd Sandbox or Namespace Error — How to Fix"
description: "Fix systemd sandbox and namespace errors by adjusting security directives, configuring namespace paths, resolving permission restrictions, and debugging chroot issues"
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
comments: true
---

# Systemd Sandbox or Namespace Error

This error means a systemd service failed because sandboxing or namespace isolation directives prevented it from accessing required resources. Systemd provides security features that restrict what a service can see and do on the system.

## Why It Happens

- `ProtectSystem=strict` prevents writing to `/etc`, `/usr`, or `/boot`
- `ProtectHome=true` blocks access to `/home`, `/root`, and `/run/user`
- `PrivateTmp=true` gives the service a private `/tmp` namespace
- `ReadOnlyPaths=` or `InaccessiblePaths=` block access to needed directories
- `NoNewPrivileges=true` prevents the service from gaining new privileges
- `ProtectKernelTunables=true` blocks writing to `/proc` and `/sys`
- `RestrictNamespaces=true` prevents creating new namespaces
- `AppArmor` or `SELinux` policies conflict with the service

## Common Error Messages

```
myapp.service: Failed to set up mount namespacing: No such file or directory
myapp.service: Failed at step NAMESPACE spawning /usr/bin/myapp: No such file or directory
```

```
myapp.service: Caught <SEGV>, core dumping.
```

```
myapp.service: Cannot open /etc/myapp/config: Permission denied
```

## How to Fix It

### 1. Identify the Sandbox Restriction

```bash
# Check the current unit file security settings
systemctl cat myapp.service | grep -E "Protect|Private|Restrict|ReadOnly|Inaccessible"

# Check if the service is being blocked by AppArmor
aa-status
journalctl -k | grep -i apparmor

# Check SELinux
getenforce
ausearch -m avc -ts recent
```

### 2. Relax Sandbox Directives

```ini
# In /etc/systemd/system/myapp.service
[Service]
# Allow writing to /etc and /usr
ProtectSystem=false

# Allow access to /home
ProtectHome=false

# Allow writing to /tmp (disable private tmp)
PrivateTmp=false

# Allow the service to create new namespaces
RestrictNamespaces=false

# Or selectively allow specific namespaces
RestrictNamespaces=false
```

### 3. Use ReadWritePaths Instead of Disabling Protection

```ini
# Keep ProtectSystem=strict but allow writing to specific paths
[Service]
ProtectSystem=strict
ReadWritePaths=/var/lib/myapp /var/log/myapp /etc/myapp

# Keep ProtectHome=true but allow specific home directories
ProtectHome=false
# Or use specific paths
BindPaths=/home/myapp:/home/myapp
```

### 4. Fix PrivateTmp Namespace Issues

```ini
# If the service needs to share /tmp with the host
[Service]
PrivateTmp=false

# Or bind-mount a shared directory
BindPaths=/var/shared-tmp:/tmp
```

### 5. Debug Namespace Failures

```bash
# Run the service with strace to see the failing syscall
sudo strace -f -e namespace /usr/bin/myapp 2>&1 | head -50

# Check available namespaces
ls /proc/self/ns/

# Test the unit file without sandboxing
# Temporarily comment out sandbox directives and restart
sudo systemctl daemon-reload
sudo systemctl restart myapp
```

### 6. Use TemporaryFile for Writable Locations

```ini
# Create a writable location within the sandbox
[Service]
ProtectSystem=strict
TemporaryFileSystem=/var/lib/myapp:mode=0755
StateDirectory=myapp
LogsDirectory=myapp
```

## Common Scenarios

- **Service needs to read /etc/ssl/certs**: `ProtectSystem=strict` blocks this. Add `ReadOnlyPaths=/etc/ssl/certs` to allow read access.
- **Service writes logs to /var/log**: `ProtectSystem=strict` blocks `/var`. Use `LogsDirectory=myapp` which creates `/var/log/myapp` automatically.
- **Docker-in-systemd**: A service that runs Docker needs access to `/var/lib/docker`. Add `ReadWritePaths=/var/lib/docker` and `ProtectSystem=full` instead of `strict`.

## Prevent It

- Test unit files with `systemd-analyze security` to see which directives are active
- Use `StateDirectory=`, `LogsDirectory=`, and `CacheDirectory=` instead of manually configuring writable paths
- Gradually increase security directives: start permissive and tighten over time

## Related Pages

- [Systemd Unit Failed](/tools/systemd/systemd-unit-failed)
- [Systemd Mount Error](/tools/systemd/systemd-mount-error)
- [Systemd Network Error](/tools/systemd/systemd-network-error)
