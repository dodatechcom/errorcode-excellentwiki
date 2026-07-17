---
title: "[Solution] Ansible Undefined Variable Error — Fix Variables"
description: "Fix Ansible undefined variable errors. Resolve variable scope, defaults, and template rendering issues with practical solutions."
---

## What This Error Means

The `undefined variable` error occurs when Ansible encounters a variable reference in a playbook, role, or template that has not been defined anywhere in the variable hierarchy.

A typical error:

```
fatal: [host1]: FAILED! => {"msg": "The task includes an option with an
undefined variable. The error was: 'app_port' is undefined"}
```

## Why It Happens

Undefined variable errors arise from:

- **Variable not defined anywhere**: The variable is referenced but never set in any scope.
- **Wrong variable name**: Typo in the variable name or wrong casing (Ansible is case-sensitive).
- **Missing default values**: Variables expected from inventory or group_vars are missing.
- **Template rendering before facts are gathered**: Using `setup` module facts before gathering.
- **Role variable scope**: Variable defined in a role but referenced outside the role's scope.
- **Conditional based on missing variable**: `when:` clause referencing an undefined variable.

## How to Fix It

**Step 1: Use default filters for optional variables**

```yaml
- name: Start application
  ansible.builtin.service:
    name: myapp
    state: started
    port: "{{ app_port | default(8080) }}"
```

**Step 2: Define variables in group_vars or host_vars**

```yaml
# group_vars/webservers.yml
app_port: 8080
app_name: myapp
```

**Step 3: Check variable scope hierarchy**

Ansible resolves variables in this order (last wins):

1. Role defaults (`roles/x/defaults/main.yml`)
2. Inventory variables
3. Playbook `vars`
4. Role vars (`roles/x/vars/main.yml`)
5. Task-level `vars`
6. Extra vars (`-e`)

**Step 4: Validate variables before use**

```yaml
- name: Assert required variables are defined
  ansible.builtin.assert:
    that:
      - app_port is defined
      - app_name is defined
    fail_msg: "app_port and app_name must be defined"
```

**Step 5: Use `omit` for optional module parameters**

```yaml
- name: Configure application
  ansible.builtin.template:
    src: app.conf.j2
    dest: /etc/app/config.yml
    owner: "{{ app_user | default(omit) }}"
```

## Common Mistakes

- **Forgetting that Jinja2 is case-sensitive**: `{{ App_Port }}` and `{{ app_port }}` are different variables.
- **Not using `default` filter for optional variables**: Always use `| default()` for variables that might not be set.
- **Defining variables in the wrong scope**: Variables in `vars:` within a role are not accessible outside the role.
- **Missing `gather_facts: true`**: Facts-based variables require fact gathering to be enabled.

## Related Pages

- [Ansible Syntax Error](/tools/ansible/ansible-syntax-error/) — Playbook syntax issues
- [Ansible Task Failed](/tools/ansible/ansible-task-failed/) — Task execution failures
- [Terraform Validation Error](/tools/terraform/terraform-validation-error/) — Variable validation errors
