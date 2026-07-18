---
title: "[Solution] Ansible Become Error — Fix Missing Sudo Password / Become Failed"
description: "Fix Ansible become errors when privilege escalation fails. Configure sudo passwords, NOPASSWD rules, and become method settings for task execution."
---

## What This Error Means

Ansible become errors occur when privilege escalation via sudo, su, or other methods fails. The task cannot execute with elevated privileges and exits with a permission denied error.

A typical error:

```
host1 | FAILED! => {
    "msg": "Missing sudo password"
}
```

Or:

```
host1 | FAILED! => {
    "changed": false,
    "msg": "Timeout (12) waiting for privilege escalation prompt: "
}
```

## Why It Happens

Become failures happen when:

- **sudo password is required but not provided**: The remote user requires a password for sudo.
- **Incorrect sudo password**: The become password does not match the remote system.
- **User is not in sudoers**: The remote user lacks sudo privileges.
- **sudo requires tty**: `requiretty` is set in sudoers but Ansible does not allocate a TTY.
- **Wrong become method**: The default sudo method does not work; su or pbrun may be needed.
- **Timeout during privilege escalation**: The sudo prompt was not detected in time.

## How to Fix It

**Step 1: Provide the become password**

```bash
ansible-playbook playbook.yml --ask-become-pass
```

Or set in variables:

```yaml
# group_vars/all.yml
ansible_become_password: "{{ vault_become_password }}"
```

**Step 2: Configure NOPASSWD in sudoers**

```bash
# On the managed host
echo "username ALL=(ALL) NOPASSWD: ALL" | sudo tee /etc/sudoers.d/ansible
```

**Step 3: Disable requiretty for Ansible**

```bash
# On the managed host
echo "Defaults:username !requiretty" | sudo tee /etc/sudoers.d/ansible-tty
```

**Step 4: Use a different become method**

```yaml
- name: Use su instead of sudo
  hosts: all
  vars:
    ansible_become_method: su
    ansible_become_user: root
  tasks:
    - command: whoami
```

**Step 5: Increase become timeout**

```ini
# ansible.cfg
[defaults]
timeout = 30
```

## Common Mistakes

- **Hardcoding become passwords in plaintext in playbooks**: Use Ansible Vault or environment variables.
- **Assuming all hosts have the same sudo configuration**: Group variables may vary per host group.
- **Not testing sudo manually on the target host**: Log in and run `sudo -k && sudo whoami` to verify.
- **Forgetting --ask-become-pass in automation scripts**: Always provide the password via env or vault.

## Related Pages

- [Ansible Permission Denied](/tools/ansible/ansible-permission-denied/) -- Authentication failures
- [Ansible SSH Timeout](/tools/ansible/ansible-ssh-timeout/) -- SSH connection issues
- [Ansible Vault Error](/tools/ansible/ansible-vault-error/) -- Vault encryption issues
