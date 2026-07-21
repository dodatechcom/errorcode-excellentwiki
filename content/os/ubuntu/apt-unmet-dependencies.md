---
title: "[Solution] Ubuntu Server: apt-unmet-dependencies"
description: "Fix Ubuntu apt-unmet-dependencies. APT has unmet dependencies preventing package installation."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Apt Unmet Dependencies

APT cannot install a package because required dependencies are not satisfied.

## Common Causes
- Missing required library or package
- Version conflict between packages
- Partially installed state from interrupted operation
- Third-party PPA providing incompatible versions

## How to Fix
1. Check broken dependencies
```bash
sudo apt -f install
apt-cache depends <package>
```
2. Review full dependency chain
```bash
apt-cache policy <package>
```
3. Allow changing held packages if needed
```bash
sudo apt-mark unhold <package>
sudo apt install <package>
```

## Examples
```bash
$ sudo apt install mysql-server
The following packages have unmet dependencies:
 mysql-server : Depends: mysql-server-8.0 but it is not going to be installed
E: Unable to correct problems, you have held broken packages.
```
