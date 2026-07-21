---
title: "[Solution] macOS SSH Error -- SSH Connection Failed on Mac"
description: "Fix macOS SSH error when SSH connection to or from Mac fails. Resolve SSH authentication and connection issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS SSH Error -- SSH Connection Failed on Mac

SSH (Secure Shell) allows remote access to your Mac's command line. When SSH connections fail, you cannot remotely manage your Mac or transfer files securely.

## Common Causes
- Remote Login is not enabled in System Preferences
- SSH daemon configuration is incorrect
- Firewall is blocking SSH port 22
- SSH keys are not configured correctly
- Host key verification is failing

## How to Fix
1. Enable Remote Login in System Preferences > Sharing
2. Check the SSH daemon configuration in /etc/ssh/sshd_config
3. Check firewall settings for port 22
4. Verify SSH key permissions and configuration
5. Check the SSH host keys

```bash
# Enable Remote Login from terminal
sudo systemsetup -setremotelogin on

# Check SSH daemon status
sudo launchctl list | grep ssh

# Test SSH connection
ssh -v localhost
```

## Examples

```bash
# Check SSH host keys
ls -la /etc/ssh/ssh_host_*

# Check SSH configuration
cat /etc/ssh/sshd_config | grep -v "^#"
```

This error is common when Remote Login is not enabled, when SSH key permissions are incorrect, or when the firewall blocks port 22.
