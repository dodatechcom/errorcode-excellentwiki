---
title: "[Solution] VS Code WSL connection failed"
description: "Fix VS Code WSL integration errors. Resolve issues when VS Code cannot connect to Windows Subsystem for Linux."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "vscode"
tags: ["vscode", "ide", "remote", "wsl", "windows"]
severity: "error"
---

# WSL connection failed

## Error Message

```
WSL connection failed: Unable to connect to WSL 2 instance. Error: WSL is not enabled. Enable Windows Subsystem for Linux in Windows Features.
```

## Common Causes

- WSL 2 is not enabled in Windows Features
- WSL distribution is not installed or has been corrupted
- Windows and WSL have incompatible network configurations
- VS Code WSL extension is missing or outdated

## Solutions

### Solution 1: Enable WSL 2

Enable Windows Subsystem for Linux and Virtual Machine Platform features through PowerShell.

```
wsl --set-default-version 2 && wsl --update
```

### Solution 2: Reinstall WSL Distribution

Uninstall and reinstall the WSL distribution to fix corruption issues.

```
wsl --unregister Ubuntu && wsl --install Ubuntu
```

### Solution 3: Open Folder in WSL

Use the Remote-WSL extension to open your project folder directly inside the WSL environment.

```
code --command 'remote-wsl.newWindow'
```

## Prevention Tips

- Keep WSL kernel updated using 'wsl --update'
- Use WSL 2 for better performance and Docker compatibility
- Store project files inside the WSL filesystem for faster access

## Related Errors

- [Failed to connect to remote host]({{< relref "/tools/vscode/remote-ssh-error" >}})
- [Failed to attach to container]({{< relref "/tools/vscode/remote-container-error" >}})
- [Remote development error]({{< relref "/tools/vscode/remote-development-error" >}})
