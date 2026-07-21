---
title: "[Solution] Git Clone Error"
description: "Fix Git clone errors when cloning repositories from remote servers fails."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
---

# Git Clone Error

Git clone fails to download or set up a repository.

```
fatal: repository not found
fatal: could not read from remote repository
```

## Common Causes

- Repository URL is incorrect
- Authentication required but not provided
- SSH key not configured
- Repository does not exist or was deleted
- Network connectivity issues

## How to Fix

### Verify Repository URL

```bash
# Test HTTPS URL
git ls-remote https://github.com/user/repo.git

# Test SSH URL
git ls-remote git@github.com:user/repo.git
```

### Configure Authentication

```bash
# HTTPS with token
git clone https://oauth2:TOKEN@github.com/user/repo.git

# SSH - add key
ssh-add ~/.ssh/id_rsa

# Test SSH connection
ssh -T git@github.com
```

### Clone Specific Branch

```bash
# Clone specific branch only
git clone -b main --single-branch https://github.com/user/repo.git

# Shallow clone for speed
git clone --depth 1 https://github.com/user/repo.git
```

### Fix Network Issues

```bash
# Increase timeout
git clone --config http.lowSpeedLimit=1000 \
          --config http.lowSpeedTime=60 \
          https://github.com/user/repo.git

# Use different protocol
git clone git://github.com/user/repo.git
```

## Examples

```bash
# Clone with specific directory name
git clone https://github.com/user/repo.git my-project

# Mirror clone
git clone --mirror https://github.com/user/repo.git

# Recursive clone with submodules
git clone --recurse-submodules https://github.com/user/repo.git
```
