---
title: "[Solution] Systemd Unit Not Found"
description: "Fix systemd 'unit not found' error. Resolve missing service files and path issues."
tools: ["systemd"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Systemd Unit Not Found

A unit not found error means systemd cannot locate the service, socket, or timer file. The unit was either never installed, was removed, or its file is in a location systemd does not scan.

## Common Causes

- The unit file was deleted or never created
- The unit file is in a non-standard directory
- A typo in the unit name
- The unit was not properly installed with `systemctl enable`

## How to Fix

### Verify the Unit File Exists

```bash
ls /etc/systemd/system/<service-name>.service
ls /lib/systemd/system/<service-name>.service
```

### Reload systemd After Adding Unit Files

```bash
sudo systemctl daemon-reload
```

### Create the Unit File

```ini
# /etc/systemd/system/my-app.service
[Unit]
Description=My Application

[Service]
ExecStart=/usr/bin/my-app
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

### Enable and Start

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now my-app
```

### List All Available Units

```bash
systemctl list-unit-files | grep <partial-name>
```

## Examples

```bash
# Typo in service name
sudo systemctl start my-app
# Failed to start my-app.service: Unit my-app.service not found.
# Fix: check the exact unit name with systemctl list-unit-files

# Unit file not reloaded after creation
sudo systemctl start custom-service
# Unit custom-service.service not found.
# Fix: systemctl daemon-reload && systemctl start custom-service
```

## Related Errors

- [Already Active]({{< relref "/tools/systemd/already-active" >}}) — unit is already running
- [Service Failed]({{< relref "/tools/systemd/service-failed" >}}) — unit exists but failed to start
