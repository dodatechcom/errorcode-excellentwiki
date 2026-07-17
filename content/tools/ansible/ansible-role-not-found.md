---
title: "[Solution] Ansible Role Not Found — Fix Collection Roles"
description: "Fix Ansible role not found errors. Resolve role paths, collection resolution, and Galaxy dependencies with practical solutions."
---

## What This Error Means

The `role not found` error occurs when Ansible cannot locate a role referenced in a playbook. This happens during playbook execution when the role path, collection, or Galaxy dependency is not properly configured.

A typical error:

```
ERROR! the role 'nginx' was not found in /roles:/etc/ansible/roles:~/.ansible/roles
```

Or:

```
ERROR! - unable to find role named 'company.webserver' found in collections
```

## Why It Happens

Role not found errors occur when:

- **Role not installed**: The role has not been downloaded from Galaxy or configured locally.
- **Wrong role name**: Typo in the role name or missing the collection namespace.
- **Incorrect roles_path**: The `roles_path` in `ansible.cfg` does not include the role location.
- **Missing collection**: The role is part of a collection that has not been installed.
- **Symlink or permission issues**: Role directory exists but is not accessible.

## How to Fix It

**Step 1: Install the role from Galaxy**

```bash
ansible-galaxy role install nginx
ansible-galaxy collection install community.general
```

**Step 2: Install from requirements file**

```yaml
# requirements.yml
roles:
  - name: nginx
    version: "3.1.0"
  - name: geerlingguy.docker
    version: "6.1.0"

collections:
  - name: community.general
    version: ">=5.0.0"
  - name: community.mysql
```

```bash
ansible-galaxy install -r requirements.yml
```

**Step 3: Verify roles_path configuration**

```ini
# ansible.cfg
[defaults]
roles_path = ./roles:/etc/ansible/roles:~/.ansible/roles
```

**Step 4: Use fully qualified collection names**

```yaml
- hosts: webservers
  roles:
    - role: nginx            # Galaxy role
    - role: company.webserver # Custom role with namespace
      vars:
        port: 80
```

**Step 5: Check role directory structure**

Ensure the role follows the expected directory layout:

```
roles/
  nginx/
    tasks/
      main.yml
    handlers/
      main.yml
    templates/
    files/
    vars/
      main.yml
    defaults/
      main.yml
    meta/
      main.yml
```

## Common Mistakes

- **Forgetting to install roles before running playbooks**: Always run `ansible-galaxy install -r requirements.yml` in your pipeline.
- **Using role names without collection namespaces**: FQCN format is required for collection roles.
- **Not specifying versions in requirements**: Pin versions to avoid breaking changes.
- **Mixing Galaxy and local roles without clear configuration**: Set `roles_path` explicitly in `ansible.cfg`.

## Related Pages

- [Ansible Syntax Error](/tools/ansible/ansible-syntax-error/) — Playbook formatting issues
- [Ansible Task Failed](/tools/ansible/ansible-task-failed/) — Runtime execution failures
- [Helm Chart Not Found](/tools/helm/helm-chart-not-found/) — Helm chart resolution errors
