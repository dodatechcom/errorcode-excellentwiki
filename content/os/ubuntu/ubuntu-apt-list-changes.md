---
title: "APT List-Changes Display Error"
description: "apt-list-changes fails to display changelog during package upgrade"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# APT List-Changes Display Error

apt-list-changes fails to display changelog during package upgrade

## Common Causes

- apt-list-changes not installed
- Changelog URL unreachable or incorrect
- Terminal does not support pager for changelog display
- Package version not found in changelog database

## How to Fix

1. Install apt-list-changes: `sudo apt-get install apt-list-changes`
2. Skip changelog: `apt-list-changes --help` or set NEVER
3. Check configuration: `cat /etc/apt/listchanges.conf`
4. Update apt: `sudo apt-get update`

## Examples

```bash
# Install apt-list-changes
sudo apt-get install apt-list-changes

# Skip changelog prompts
sudo apt-get -o APT::List::Changes::Enable=0 upgrade
```
