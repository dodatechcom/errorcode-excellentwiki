---
title: "[Solution] CircleCI SSH Key Passphrase Error"
description: "Fix CircleCI SSH key passphrase errors when deploy keys with passphrases fail to authenticate during pipeline execution."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI SSH Key Passphrase Error

SSH key passphrase errors occur when an SSH key added to CircleCI is encrypted with a passphrase, but CircleCI does not support passphrased keys for deployment.

## Common Causes

- SSH key was generated with a passphrase
- Key was imported from another system with a passphrase
- CircleCI does not support encrypted private keys for deploy keys
- SSH agent is not loaded with the key

## How to Fix

### Solution 1: Remove the passphrase from the key

```bash
# Remove passphrase from existing key
ssh-keygen -p -f ~/.ssh/deploy_key
# Enter empty passphrase when prompted
```

### Solution 2: Generate a new key without passphrase

```bash
ssh-keygen -t rsa -b 4096 -f deploy_key -N ""
```

### Solution 3: Use ssh-agent in the job

```yaml
jobs:
  deploy:
    steps:
      - add_ssh_keys:
          fingerprints:
            - "aa:bb:cc:dd:ee:ff:00:11:22:33:44:55:66:77:88:99"
      - run:
          name: Deploy via SSH
          command: ssh deploy@server "cd /app && git pull"
```

## Examples

```
Error: Load key "deploy_key": incorrect passphrase
ERROR: SSH key authentication failed
```

## Prevent It

- Generate CI/CD SSH keys without passphrases
- Store passphrase-free keys securely in CircleCI
- Use `add_ssh_keys` step for automatic key loading
