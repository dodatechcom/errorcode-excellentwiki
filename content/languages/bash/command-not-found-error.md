---
title: "[Solution] Bash Command Not Found Error"
description: "Fix 'bash: command not found' when a command is not installed, not in PATH, or misspelled."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "bash"
tags: ["bash", "shell", "command", "path", "not-found", "installation"]
severity: "error"
---

# Command Not Found

## Error Message

```
bash: command-name: command not found
```

## Common Causes

- The command is not installed on the system
- The command is installed but not in the `PATH` environment variable
- The command name is misspelled
- The script uses a shebang (`#!`) pointing to a non-existent interpreter

## Solutions

### Solution 1: Install the Missing Command

Use your system's package manager to install the missing program. Check which package provides the command before installing.

```bash
# Check if a command exists
which docker
type docker

# Install on Ubuntu/Debian
sudo apt update && sudo apt install docker.io

# Install on CentOS/RHEL
sudo yum install docker

# Install on macOS with Homebrew
brew install docker 
```

### Solution 2: Add the Command's Directory to PATH

If the program is installed but not found, its directory may not be in PATH. Add it temporarily or permanently.

```bash
# Find where the command is located
find / -name "mycommand" 2>/dev/null

# Temporarily add to PATH
export PATH=$PATH:/opt/myapp/bin

# Permanently add to ~/.bashrc
echo 'export PATH=$PATH:/opt/myapp/bin' >> ~/.bashrc
source ~/.bashrc

# Verify the path was added
echo $PATH 
```

## Prevention Tips

- Use `which` or `type` to check if a command is installed
- Check PATH with `echo $PATH` and look for the command's directory
- Use full paths for system scripts that run via cron or systemd

## Related Errors

- [Permission Denied]({< relref "/languages/bash/permission-denied" >})
- [No Such File]({< relref "/languages/bash/no-such-file" >})
