---
title: "[Solution] Ubuntu Server: apt-no-installable-candidate"
description: "Fix Ubuntu apt-no-installable-candidate. No installable candidate found for requested package."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Apt No Installable Candidate

APT cannot find a package candidate that satisfies the requested installation.

## Common Causes
- Package name is misspelled
- Required repository is not enabled
- Package removed from Ubuntu repositories
- Package exists only in universe or multiverse
- PPA providing the package not added

## How to Fix
1. Search for the correct package name
```bash
apt-cache search <partial-name>
```
2. Enable universe repository
```bash
sudo add-apt-repository universe
sudo apt update
```
3. Add required PPA
```bash
sudo add-apt-repository ppa:<owner>/<repo>
sudo apt update
```

## Examples
```bash
$ sudo apt install docker-ce
E: Package 'docker-ce' has no installable candidate

$ apt-cache search docker-ce
docker-ce-cli - Docker CLI
docker-ce - Docker Community Edition
```
