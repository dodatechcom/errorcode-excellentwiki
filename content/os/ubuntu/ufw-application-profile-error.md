---
title: "[Solution] Ubuntu Server: ufw-application-profile-error"
description: "Fix Ubuntu ufw-application-profile-error. UFW application profile not found or invalid."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# UFW Application Profile Error

UFW cannot find or parse an application profile.

## Common Causes
- Application profile file missing from /etc/ufw/applications.d/
- Profile syntax error
- Profile name does not match installed application
- Custom profile not loaded

## How to Fix
1. List available profiles
```bash
sudo ufw app list
```
2. Check profile files
```bash
ls /etc/ufw/applications.d/
cat /etc/ufw/applications.d/nginx
```
3. Create custom profile
```bash
sudo nano /etc/ufw/applications.d/myapp
[MyApp]
title=My Application
description=My custom app
ports=8080/tcp
```
4. Reload UFW
```bash
sudo ufw reload
```

## Examples
```bash
$ sudo ufw app list
Available applications:
  Nginx Full
  Nginx HTTP
  Nginx HTTPS
  OpenSSH

$ sudo ufw app info "Nginx Full"
Profile: Nginx Full
Title: Web Server (HTTP,HTTPS)
Ports: 80,443/tcp
```
