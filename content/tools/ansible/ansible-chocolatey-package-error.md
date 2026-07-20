---
title: "[Solution] Ansible Chocolatey Package Error"
description: "Fix Ansible Chocolatey package manager errors on Windows"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible Chocolatey module fails to manage packages.

```
FAILED! => "choco install failed: The package was not found"
```

## Common Causes

- Package name incorrect
- Chocolatey not installed
- Package not in Chocolatey repository

## How to Fix

```yaml
# Install Chocolatey first
- name: Install Chocolatey
  ansible.windows.win_shell: >
    Set-ExecutionPolicy Bypass -Scope Process -Force;
    iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Install packages
- name: Install packages via Chocolatey
  community.windows.win_chocolatey:
    name:
      - googlechrome
      - notepadplusplus
      - vscode
    state: present
```
