---
title: "[Solution] Linux: selinux-file-context-error -- file context relabel failure"
description: "Fix Linux SELinux file context errors. File context relabel failure causing access issues."
os: ["linux"]
error-types: ["selinux-error"]
severities: ["error"]
---

# Linux: SELinux File Context Error

SELinux file context errors occur when files have incorrect security labels.

## Common Causes

- Files copied without preserving SELinux context
- Manual relabeling skipped after policy change
- restorecon not applied after file creation
- Custom directory missing from file_contexts
- Container volume without label support

## How to Fix

### 1. Check File Context

```bash
ls -Z /var/www/html/
matchpathcon /var/www/html/index.html
semanage fcontext -l | grep "/var/www"
```

### 2. Apply Correct Context

```bash
sudo semanage fcontext -a -t httpd_sys_content_t "/var/www/html(/.*)?"
sudo restorecon -Rv /var/www/html/
```

### 3. Full System Relabel

```bash
sudo touch /.autorelabel
sudo reboot
```

## Examples

```bash
$ ls -Z /var/www/html/
system_u:object_r:default_t:s0    index.html
# Should be httpd_sys_content_t
$ sudo restorecon -Rv /var/www/html/
restorecon reset /var/www/html/index.html system_u:object_r:httpd_sys_content_t:s0
```
