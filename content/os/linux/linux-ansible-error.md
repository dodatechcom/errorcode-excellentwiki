---
title: "[Solution] Linux ansible Playbook Error — Fix"
description: "Fix Linux 'ansible: playbook error' and Ansible failures. Resolve SSH connectivity, module errors, and playbook execution issues."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["ansible", "playbook-error", "automation", "configuration-management", "ssh", "module"]
weight: 5
---

# Linux: ansible: playbook error

The `ansible: playbook error` message means Ansible encountered a problem during playbook execution. This can happen at various stages: SSH connectivity to managed hosts, module execution failures, variable resolution errors, or YAML syntax issues. Playbook errors are displayed with line numbers and failed task details.

## What This Error Means

Ansible automates configuration management by connecting to remote hosts via SSH and executing modules. A playbook error means one or more tasks failed during execution. The error output includes the task name, the module that failed, the error message, and often suggested fixes. Understanding the error type helps identify whether the issue is connectivity, permissions, or logic-related.

## Common Causes

- SSH connectivity issues to managed hosts
- Python not installed on remote host
- Module-specific errors (missing packages, invalid parameters)
- YAML syntax errors in playbook
- Variable undefined or incorrect
- Permission issues on remote host
- Ansible version incompatibility with modules
- Connection timeout on slow networks

## How to Fix

### 1. Check Ansible Connectivity

```bash
# Test connection to all hosts
ansible all -m ping

# Test specific host
ansible webserver -m ping

# Check inventory
ansible-inventory --list

# Check SSH connectivity manually
ssh user@remote-host echo "Connection OK"
```

### 2. Enable Verbose Output

```bash
# Run playbook with increasing verbosity
ansible-playbook site.yml -v
ansible-playbook site.yml -vv
ansible-playbook site.yml -vvv
ansible-playbook site.yml -vvvv    # Maximum debug output

# Check specific task
ansible-playbook site.yml --step
```

### 3. Check YAML Syntax

```bash
# Validate YAML syntax
ansible-lint site.yml

# Or use yamllint
yamllint site.yml

# Check for common mistakes:
# - Inconsistent indentation (use 2 spaces)
# - Missing colons after keys
# - Incorrect variable syntax
```

### 4. Fix SSH and Python Issues

```bash
# Ensure Python is installed on remote
ansible webserver -m ping -u user --ask-pass

# Check Python version on remote
ansible webserver -m shell -a "python3 --version"

# Use correct Python path
ansible webserver -m ping -e "ansible_python_interpreter=/usr/bin/python3"

# Fix SSH key permissions
chmod 600 ~/.ssh/id_rsa
chmod 700 ~/.ssh
```

### 5. Check Ansible Version

```bash
# Check Ansible version
ansible --version

# Check module compatibility
ansible-doc <module-name>

# Update Ansible
pip install --upgrade ansible
# Or
sudo apt install --reinstall ansible
```

### 6. Debug Playbook Execution

```bash
# Check syntax only
ansible-playbook site.yml --syntax-check

# Dry run (check mode)
ansible-playbook site.yml --check

# List tasks
ansible-playbook site.yml --list-tasks

# Start from specific task
ansible-playbook site.yml --start-at-task="Install nginx"

# Limit to specific hosts
ansible-playbook site.yml --limit webserver1
```

### 7. Fix Module-Specific Errors

```bash
# Check module documentation
ansible-doc apt
ansible-doc yum

# Check if required packages are available
ansible webserver -m shell -a "apt list --installed | grep nginx"

# Use become for privileged operations
ansible-playbook site.yml --become --become-method sudo
```

## Examples

```bash
$ ansible-playbook site.yml
PLAY [all] *************************************************************

TASK [Gathering Facts] *************************************************
fatal: [webserver1]: UNREACHABLE! => {"changed": false, "msg": "Failed to connect to the host via ssh: Connection refused"}

# Fix: ensure SSH is running on webserver1
$ ansible-playbook site.yml -vvv
# Shows: "ssh: connect to host 192.168.1.100 port 22: Connection refused"

$ ansible-playbook site.yml
TASK [Install nginx] ***************************************************
fatal: [webserver1]: FAILED! => {"changed": false, "msg": "E: Unable to locate package nginx"}

# Fix: update apt cache first
# Add - apt: update_cache=yes before install task
```

## Related Errors

- [SSH connection refused]({{< relref "/os/linux/linux-ssh-connection-refused-v2" >}}) — SSH connectivity issues
- [SSH permission denied]({{< relref "/os/linux/linux-ssh-permission-denied" >}}) — SSH authentication failures
- [Terraform provider error]({{< relref "/os/linux/linux-terraform-error" >}}) — Infrastructure automation issues
