---
title: "[Solution] Linux crontab Installation Error — Fix"
description: "Fix Linux 'crontab: installation error' and cron job failures. Debug cron syntax, permissions, and scheduled task issues."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["crontab", "installation-error", "cron", "scheduled-task", "crontab-edit"]
weight: 5
---

# Linux: crontab: installation error

The `crontab: installation error` message means the crontab command failed to save or install a new crontab file. This typically happens when the crontab directory is full, permissions are wrong, or the cron daemon has issues reading the spool directory.

## What This Error Means

When you run `crontab -e`, the edited crontab is saved to `/var/spool/cron/crontabs/` (Debian/Ubuntu) or `/var/spool/cron/` (RHEL/CentOS). The cron daemon (`cron` or `crond`) watches this directory and loads new crontabs on changes. An "installation error" means the temporary file couldn't be moved to the spool directory, or cron couldn't read it.

## Common Causes

- Crontab spool directory missing or has wrong permissions
- Disk full preventing crontab save
- Cron daemon not running
- Crontab syntax errors (some versions reject invalid entries)
- User's crontab file has wrong ownership
- Maximum crontab size exceeded
- Cron deny file (`/etc/cron.deny`) blocking the user

## How to Fix

### 1. Check Crontab Spool Directory

```bash
# Debian/Ubuntu
ls -la /var/spool/cron/crontabs/

# RHEL/CentOS/Fedora
ls -la /var/spool/cron/

# Ensure correct permissions
sudo chmod 1730 /var/spool/cron/crontabs/    # Debian/Ubuntu
sudo chmod 700 /var/spool/cron/              # RHEL/CentOS
```

### 2. Check Disk Space

```bash
# Check available disk space
df -h

# Check inode usage
df -i

# If full, free up space
sudo journalctl --vacuum-size=100M
sudo apt clean
```

### 3. Verify Cron Daemon Is Running

```bash
# Check cron status
sudo systemctl status cron      # Debian/Ubuntu
sudo systemctl status crond     # RHEL/CentOS/Fedora

# Start cron if not running
sudo systemctl start cron
sudo systemctl enable cron
```

### 4. Check Cron Deny/Allow Files

```bash
# Check if user is in cron.deny
cat /etc/cron.deny
grep username /etc/cron.deny

# Remove user from deny list
sudo sed -i '/username/d' /etc/cron.deny

# Or add user to cron.allow
echo "username" | sudo tee -a /etc/cron.allow
```

### 5. Fix Crontab Syntax

```bash
# Edit the crontab
crontab -e

# View current crontab
crontab -l

# Common syntax mistakes:
# - Using tabs instead of spaces
# - Missing command path
# - Invalid time values
# - Unclosed quotes
```

Correct cron format:

```
# ┌───── minute (0-59)
# │ ┌───── hour (0-23)
# │ │ ┌───── day of month (1-31)
# │ │ │ ┌───── month (1-12)
# │ │ │ │ ┌───── day of week (0-7, 0 and 7 = Sunday)
# │ │ │ │ │
  * * * * *  command_to_execute
```

### 6. Fix Crontab File Permissions

```bash
# Check existing crontab file
ls -la /var/spool/cron/crontabs/username

# Fix ownership
sudo chown username:crontab /var/spool/cron/crontabs/username

# Fix permissions
sudo chmod 600 /var/spool/cron/crontabs/username
```

### 7. Manually Install a Crontab

```bash
# Create crontab from a file
crontab /path/to/crontabfile

# Or pipe it in
echo "*/5 * * * * /path/to/script.sh" | crontab -

# Verify installation
crontab -l
```

## Examples

```bash
$ crontab -e
crontab: installation error

$ ls -la /var/spool/cron/crontabs/
ls: cannot access '/var/spool/cron/crontabs/': No such file or directory

$ sudo mkdir -p /var/spool/cron/crontabs
$ sudo chmod 1730 /var/spool/cron/crontabs

$ crontab -e
# Now works — editor opens

$ crontab -l
*/5 * * * * /home/user/scripts/backup.sh
```

```bash
$ crontab -e
crontab: installation error

$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        20G   20G     0 100% /

# Disk is full — free space
$ sudo apt clean
$ sudo journalctl --vacuum-size=50M

$ crontab -e
# Now works
```

## Related Errors

- [CRON CMD failed]({{< relref "/os/linux/cron-error" >}}) — Cron job execution failures
- [No space left on device]({{< relref "/os/linux/no-space-left" >}}) — Disk full preventing saves
- [Permission denied]({{< relref "/os/linux/connection-refused7" >}}) — File permission issues
