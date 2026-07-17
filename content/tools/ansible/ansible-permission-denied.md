---
title: "[Solution] Ansible Permission Denied Error — Fix SSH Auth"
description: "Fix Ansible permission denied SSH errors. Resolve public key and password authentication issues with step-by-step solutions."
---

## What This Error Means

The `Permission denied (publickey,password)` error means SSH rejected the authentication attempt. Ansible connected to the SSH port but the remote host refused the credentials or SSH key provided.

A typical error:

```
host1 | FAILED! => {"msg": "Data could not be sent to remote host
\"192.168.1.10\". Make sure this host can be reached over ssh:
Permission denied (publickey,password)."}
```

## Why It Happens

Permission denied errors occur when:

- **Wrong SSH key**: The private key does not match any authorized key on the target.
- **Incorrect username**: The configured `ansible_user` is not valid on the remote host.
- **SSH key permissions**: The private key file has overly permissive permissions (must be 600 or 400).
- **Password authentication disabled**: The target only accepts key-based auth but no valid key is configured.
- **SELinux context**: SELinux blocking SSH key access on the target host.
- **authorized_keys missing**: The target user has no authorized keys configured.

## How to Fix It

**Step 1: Test SSH authentication manually**

```bash
ssh -i ~/.ssh/id_rsa user@192.168.1.10 -v
```

**Step 2: Fix SSH key permissions**

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_rsa
chmod 644 ~/.ssh/id_rsa.pub
```

**Step 3: Copy the public key to the target**

```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub user@192.168.1.10
```

**Step 4: Configure the correct user in inventory**

```ini
[webservers]
web1 ansible_host=192.168.1.10 ansible_user=deploy ansible_ssh_private_key_file=~/.ssh/deploy_key
```

**Step 5: Check authorized_keys on the target**

```bash
# On the remote host
cat /home/user/.ssh/authorized_keys
ls -la /home/user/.ssh/
```

**Step 6: Configure SSH key usage in ansible.cfg**

```ini
[defaults]
private_key_file = ~/.ssh/deploy_key
remote_user = deploy

[ssh_connection]
ssh_args = -o IdentitiesOnly=yes
```

## Common Mistakes

- **Private key permissions too open**: SSH refuses to use keys with permissions wider than 600.
- **Mixing keys for different hosts**: Use separate key files per environment or host group.
- **Not testing SSH before running Ansible**: Always verify SSH works manually first.
- **Forgetting `ansible_ssh_private_key_file`**: When using non-default keys, specify the path in inventory.

## Related Pages

- [Ansible Connection Refused](/tools/ansible/ansible-connection-refused/) — SSH port not accessible
- [Ansible Unreachable Host](/tools/ansible/ansible-unreachable-host/) — Network reachability issues
- [Kubectl Permission Error](/tools/kubectl/kubectl-permission-error/) — Kubernetes RBAC errors
