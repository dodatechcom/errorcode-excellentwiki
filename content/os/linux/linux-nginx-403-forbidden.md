---
title: "[Solution] Linux nginx 403 Forbidden — Permission Denied"
description: "Fix Linux nginx 403 Forbidden errors. Resolve file permission issues, directory indexing, and access denial problems."
platforms: ["linux"]
severities: ["warning"]
error-types: ["runtime-error"]
tags: ["nginx", "403", "forbidden", "permission", "access-denied"]
weight: 5
---

# Linux: nginx — 403 Forbidden — permission denied

The nginx `403 Forbidden` error means nginx understood the request but refused to authorize it. This is different from 401 (Unauthorized) — 403 means the server explicitly denies access regardless of authentication. Common causes include missing index files, directory permission issues, and misconfigured access rules.

## What This Error Means

nginx returns 403 when it cannot serve the requested resource. This happens when the nginx worker process (running as `www-data` or `nginx` user) lacks filesystem permissions to read the file, when no index file exists and directory listing is disabled, or when nginx configuration explicitly denies access via `deny` directives.

## Common Causes

- File or directory permissions do not allow nginx user to read
- No index file (index.html, index.php) in the directory
- `autoindex off` set and no index file present
- `deny all` directive in nginx configuration
- SELinux blocking nginx access to the directory
- `.htaccess` or auth configuration blocking access
- `root` directive pointing to wrong directory

## How to Fix

### 1. Check File Permissions

```bash
# Check what user nginx runs as
grep -E '^(user|worker_processes)' /etc/nginx/nginx.conf

# Check permissions on the web root
ls -la /var/www/html/

# Ensure nginx user can read the files
sudo chown -R www-data:www-data /var/www/html
sudo chmod -R 755 /var/www/html

# For specific files
sudo chmod 644 /var/www/html/index.html
```

### 2. Add an Index File

```bash
# If no index file exists and autoindex is off
ls /var/www/html/
# index.html is missing

# Create an index file
echo '<html><body>Hello</body></html>' | sudo tee /var/www/html/index.html
```

### 3. Fix nginx Configuration

```nginx
# /etc/nginx/sites-available/mysite.conf

server {
    listen 80;
    server_name example.com;
    root /var/www/html;

    # Ensure index directive is set
    index index.html index.htm index.php;

    # Enable directory listing (optional)
    autoindex on;

    # Remove any deny directives for the path
    location / {
        # deny all;  # REMOVE this line
        try_files $uri $uri/ =404;
    }
}
```

### 4. Fix SELinux (RHEL/CentOS/Fedora)

```bash
# Check if SELinux is blocking
sudo ausearch -m AVC -ts recent | grep nginx

# Restore context on web directory
sudo restorecon -Rv /var/www/html

# Allow nginx to serve content from a custom directory
sudo semanage fcontext -a -t httpd_sys_content_t '/srv/myapp(/.*)?'
sudo restorecon -Rv /srv/myapp

# Check booleans
sudo getsebool -a | grep httpd
```

### 5. Fix ownership for PHP Applications

```bash
# For WordPress, Drupal, etc.
sudo chown -R www-data:www-data /var/www/html

# Or use a more restrictive approach
sudo chown -R root:www-data /var/www/html
sudo find /var/www/html -type d -exec chmod 750 {} \;
sudo find /var/www/html -type f -exec chmod 640 {} \;
```

### 6. Check for .htaccess or Auth Config

```bash
# Look for auth configuration
grep -r 'auth_basic\|htpasswd\|deny' /etc/nginx/

# Check for .htaccess files (nginx does not read .htaccess)
find /var/www -name '.htaccess'

# If using auth, ensure the password file exists and is readable
ls -la /etc/nginx/.htpasswd
```

### 7. Test Configuration and Reload

```bash
# Test nginx configuration
sudo nginx -t

# Reload
sudo nginx -s reload
```

## Examples

```bash
$ curl -I http://example.com/
HTTP/1.1 403 Forbidden

$ ls -la /var/www/html/
total 12
drwxr-x--- 2 root root 4096 .  # Wrong: others have no access
-rw------- 1 root root  200 index.html  # Wrong: not world-readable

$ sudo chmod 755 /var/www/html
$ sudo chmod 644 /var/www/html/index.html
$ curl -I http://example.com/
HTTP/1.1 200 OK
```

```bash
# SELinux case
$ sudo ausearch -m AVC -ts recent | grep nginx
type=AVC msg=audit(...) : avc: denied { read } for ... scontext=system_u:system_r:httpd_t:s0
  tcontext=unconfined_u:object_r:default_t:s0 tclass=dir

$ sudo restorecon -Rv /var/www/html
$ curl -I http://example.com/
HTTP/1.1 200 OK
```

## Related Errors

- [nginx 502 bad gateway]({{< relref "/os/linux/linux-nginx-502-upstream" >}}) — Upstream errors
- [nginx 504 timeout]({{< relref "/os/linux/linux-nginx-504-timeout" >}}) — Upstream timeout
- [Permission denied]({{< relref "/os/linux/permission-denied10" >}}) — General permission issues
