---
title: "[Solution] Eclipse Git integration error"
description: "Git integration error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "eclipse"
tags: ["eclipse", "ide", "git", "egit", "version-control"]
severity: "error"
---

# Git integration error

## Error Message

```
An internal error occurred during: 'Fetching Changes'. org.eclipse.jgit.api.errors.TransportException: ssh://git@github.com/repository.git: Auth fail
```

## Common Causes

- SSH authentication credentials are incorrect or the SSH key is not configured in Eclipse.
- The EGit plugin cannot find the system SSH agent or the SSH key passphrase is not cached.
- Network proxy settings prevent Eclipse from reaching the Git remote repository.

## Solutions

### Solution 1: Configure SSH Credentials in Eclipse

Go to **Window > Preferences > General > Network Connections > SSH2** and configure the SSH key directory. Ensure your `id_rsa` or `id_ed25519` key is in the `~/.ssh/` directory. Also go to **Window > Preferences > General > Security > Secure Storage** and add your SSH passphrase.

```java
# Generate SSH key for GitHub
ssh-keygen -t ed25519 -C "your-email@example.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Verify SSH connection
ssh -T git@github.com
```

### Solution 2: Use HTTPS Instead of SSH

If SSH is problematic, switch to HTTPS authentication. In the Git repository's configuration, change the remote URL from SSH to HTTPS. Eclipse will prompt for your GitHub username and password or a personal access token when you push or pull.

```bash
# Change remote URL from SSH to HTTPS
git remote set-url origin https://github.com/user/repository.git

# Or clone with HTTPS initially
git clone https://github.com/user/repository.git

# Generate a personal access token at GitHub Settings > Developer Settings
```

## Prevention Tips

- Use **Window > Show View > Other > Git > Git Repositories** to manage Git repositories.
- Enable **Push and Fetch > Configure independent push and fetch** in remote configuration.
- Install the **EGit** update site for the latest Git integration features and bug fixes.

## Related Errors

- [svn-integration-error]({{< relref "/tools/eclipse/svn-integration-error" >}})
- [terminal-error]({{< relref "/tools/eclipse/terminal-error" >}})
- [workspace-corruption]({{< relref "/tools/eclipse/workspace-corruption" >}})
