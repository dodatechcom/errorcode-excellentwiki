---
title: "[Solution] Linux SELinux 'denied { read }' — Permission Fix"
description: "Fix Linux SELinux 'denied' errors. Set correct SELinux contexts, use audit2allow, and resolve security policy denials."
platforms: ["linux"]
severities: ["error"]
error-types: ["system-error"]
tags: ["selinux", "denied", "security", "context", "audit2allow"]
weight: 5
---

# Linux: SELinux: denied { read } for pid

The `SELinux: denied { read } for pid ...` error means SELinux (Security-Enhanced Linux) has blocked a process from performing an operation. Even though standard Unix permissions may allow the action, SELinux enforces mandatory access controls based on security contexts. This is common on RHEL, CentOS, Fedora, and other SELinux-enabled distributions.

## Common Causes

- Incorrect SELinux file context for a file or directory
- Process running in the wrong SELinux domain
- Custom application not covered by existing SELinux policies
- Restored files from backup without proper SELinux labels
- Moved files to a non-standard location (e.g., serving web files from `/home`)

## How to Fix

### 1. Check SELinux Status

```bash
# Check if SELinux is enabled
getenforce

# View detailed status
sestatus

# View current mode
cat /etc/selinux/config
```

### 2. Read the Audit Log

SELinux denials are logged in `/var/log/audit/audit.log`:

```bash
# Find recent SELinux denials
sudo ausearch -m AVC --start recent

# Or search directly
sudo grep "denied" /var/log/audit/audit.log | tail -20

# Use audit2why to understand why access was denied
sudo ausearch -m AVC -ts recent | audit2why
```

### 3. Set Correct File Context

```bash
# Check the context of a file
ls -Z /path/to/file

# Set the correct context for web content
sudo semanage fcontext -a -t httpd_sys_content_t "/var/www(/.*)?"
sudo restorecon -Rv /var/www

# Set context for a custom directory
sudo semanage fcontext -a -t httpd_sys_content_t "/srv/web(/.*)?"
sudo restorecon -Rv /srv/web

# Set context for writable web content
sudo semanage fcontext -a -t httpd_sys_rw_content_t "/var/www/html/uploads(/.*)?"
sudo restorecon -Rv /var/www/html/uploads
```

### 4. Use audit2allow to Generate Policy

If the denial is legitimate and you need to allow it:

```bash
# Generate a policy module from denials
sudo ausearch -m AVC -ts recent | audit2allow -M mypolicy

# Review the generated policy
cat mypolicy.te

# Install the policy
sudo semodule -i mypolicy.pp
```

### 5. Temporarily Set Permissive Mode

For testing only — **not recommended for production**:

```bash
# Set permissive mode (logs denials but doesn't block)
sudo setenforce 0

# Set enforcing mode back
sudo setenforce 1

# Make permanent in config
sudo sed -i 's/SELINUX=enforcing/SELINUX=permissive/' /etc/selinux/config
```

### 6. Use Boolean Flags for Common Adjustments

```bash
# List all booleans
getsebool -a | grep httpd

# Allow httpd to connect to the network
sudo setsebool -P httpd_can_network_connect 1

# Allow httpd to send mail
sudo setsebool -P httpd_can_sendmail 1

# Allow home directories to be served
sudo setsebool -P httpd_enable_homedirs 1
```

### 7. Fix Context After Copying or Moving Files

```bash
# Files inherit parent directory context when copied
# Use -Z to set context when copying
cp -Z /etc/myapp.conf /etc/myapp.conf.bak

# Restore default context for a path
sudo restorecon -Rv /path/to/directory

# View what restorecon would change (dry run)
sudo restorecon -nv /path/to/directory
```

## Examples

```bash
$ sudo grep "denied" /var/log/audit/audit.log | tail -5
type=AVC msg=audit(1234567890.123:456): avc:  denied  { read } for  pid=1234 comm="nginx" name="index.html" dev="sda1" ino=78901 scontext=system_u:system_r:httpd_t:s0 tcontext=unconfined_u:object_r:user_home_t:s0 tclass=file

$ sudo ausearch -m AVC -ts recent | audit2why
type=AVC msg=audit(...): avc:  denied  { read } for ...
    Was caused by:
        Missing boolean allow_httpd_read_user_content
        Set boolean allow_httpd_read_user_content to true.

$ sudo setsebool -P httpd_read_user_content 1
$ sudo grep "denied" /var/log/audit/audit.log | tail -5
# No new denials
```

## Related Errors

- [Permission denied]({{< relref "/os/linux/permission-denied10" >}}) — Unix permission issues
- [iptables errors]({{< relref "/os/linux/iptables-error" >}}) — Firewall rule issues
- [Connection refused]({{< relref "/os/linux/connection-refused7" >}}) — SELinux blocking network access
