---
title: "[Solution] Ansible Task Failed — Fix Non-Zero Return Code"
description: "Fix Ansible task failed with non-zero return code. Diagnose task failures, handle errors gracefully, and debug playbook execution."
---

## What This Error Means

The `Failed! => rc=1` or non-zero return code error means an Ansible task executed but the underlying command or module returned an error. The task ran to completion but the result was not successful.

A typical error:

```
host1 | FAILED! => {"changed": false, "msg": "Non-zero return code",
"stderr": "E: Unable to locate package nginx", "rc": 100}
```

## Why It Happens

Non-zero return code errors occur when:

- **Package not found**: The package manager cannot find the specified package name.
- **Service does not exist**: Attempting to manage a service that is not installed.
- **Command fails**: Shell or command module runs a command that returns an error.
- **File not found**: Copy or template module references a source file that does not exist.
- **Permission issues**: The remote user lacks permissions to perform the action.
- **Configuration error**: Module parameters are logically incorrect for the target system.

## How to Fix It

**Step 1: Read the full error output**

The `stderr` and `stdout` fields contain the actual error message. Focus on these, not just the Ansible message.

**Step 2: Use ignore_errors for expected failures**

```yaml
- name: Try to stop service (may not exist)
  ansible.builtin.service:
    name: old-service
    state: stopped
  ignore_errors: yes
  register: service_result
```

**Step 3: Use failed_when for custom failure detection**

```yaml
- name: Check if process is running
  ansible.builtin.command: pgrep myapp
  register: result
  failed_when: result.rc > 1
  changed_when: false
```

**Step 4: Debug tasks interactively**

```bash
# Run with extra verbosity
ansible-playbook site.yml -vvv

# Run specific tags
ansible-playbook site.yml --tags "debug"

# Step through with --step
ansible-playbook site.yml --step
```

**Step 5: Add error handling blocks**

```yaml
- block:
    - name: Deploy application
      ansible.builtin.command: /opt/deploy.sh
  rescue:
    - name: Rollback on failure
      ansible.builtin.command: /opt/rollback.sh
  always:
    - name: Send notification
      ansible.builtin.uri:
        url: "https://hooks.slack.com/services/xxx"
        method: POST
        body_format: json
        body:
          text: "Deployment completed (with errors if any)"
```

## Common Mistakes

- **Not reading the stderr output**: The actual error is in `stderr`, not the Ansible failure message.
- **Using `ignore_errors` blindly**: Only use it when failure is expected and acceptable.
- **Not registering task results**: Register results to use in conditionals and error handling.
- **Skipping error handling**: Always add `rescue` and `always` blocks for critical deployments.

## Related Pages

- [Ansible Syntax Error](/tools/ansible/ansible-syntax-error/) — Pre-execution syntax issues
- [Ansible Undefined Variable](/tools/ansible/ansible-undefined-variable/) — Variable errors
- [Terraform Apply Error](/tools/terraform/terraform-apply-error/) — Terraform execution failures
