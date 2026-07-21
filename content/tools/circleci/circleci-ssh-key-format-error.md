---
title: "[Solution] CircleCI SSH Key Format Error"
description: "Fix CircleCI SSH key format errors when deploy keys or SSH credentials are not in the correct format for the executor."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI SSH Key Format Error

SSH key format errors occur when the SSH key provided to CircleCI is not in the expected PEM format or is encrypted with an unsupported passphrase.

## Common Causes

- SSH key is in OpenSSH format instead of PEM
- Key was generated with an unsupported algorithm (Ed25519 not supported in some contexts)
- Private key includes a passphrase that was not provided
- Key file has incorrect line endings (CRLF instead of LF)

## How to Fix

### Solution 1: Convert key to PEM format

```bash
# Convert OpenSSH key to PEM
ssh-keygen -p -m PEM -f ~/.ssh/deploy_key

# Or generate a new RSA key
ssh-keygen -t rsa -b 4096 -f deploy_key -N ""
```

### Solution 2: Add the key in project settings

Navigate to **Project Settings > SSH Keys** and add the private key. Use the **Add Deploy Key** section for read-only keys.

### Solution 3: Configure in config.yml

```yaml
jobs:
  deploy:
    steps:
      - add_ssh_keys:
          fingerprints:
            - "aa:bb:cc:dd:ee:ff:00:11:22:33:44:55:66:77:88:99"
```

## Examples

```
ERROR: Error loading SSH key: invalid format
ERROR: Key is not in PEM format
```

## Prevent It

- Generate RSA 4096-bit keys for deploy keys
- Remove passphrases from CI/CD SSH keys
- Verify key format with `ssh-keygen -l -f key_file`
