---
title: "[Solution] Nginx Auth Basic User File Error"
description: "The htpasswd file referenced by auth_basic_user_file cannot be read or is malformed."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The htpasswd file referenced by auth_basic_user_file cannot be read or is malformed.

## Common Causes

- **File does not exist**
- **Incorrect permissions**
- **Malformed htpasswd entries**
- **Wrong path**

## How to Fix

1. Create: `htpasswd -c /etc/nginx/.htpasswd admin`
2. Permissions: `chown root:www-data /etc/nginx/.htpasswd; chmod 640 /etc/nginx/.htpasswd`
3. Verify: `sudo -u www-data cat /etc/nginx/.htpasswd`
4. Validate: `sudo nginx -t`

## Examples

**Config:**
```nginx
location /admin/ {
    auth_basic "Restricted Area";
    auth_basic_user_file /etc/nginx/.htpasswd;
    proxy_pass http://backend;
}
```
**Create:**
```bash
sudo apt install apache2-utils
sudo htpasswd -c /etc/nginx/.htpasswd admin
```