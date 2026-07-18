---
title: "[Solution] Ansible Collection Not Found Version Mismatch Error Fix"
description: "Fix Ansible collection not found and version mismatch errors. Install, update, and manage Ansible Galaxy collections."
tools: ["ansible"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Ansible Collection Not Found Version Mismatch Error Fix

The `collection not found` or `version mismatch` error occurs when an Ansible playbook references a collection that is not installed, or the installed version does not meet requirements.

## What This Error Means

Ansible collections are packages of modules, plugins, and roles. When a required collection is missing or the wrong version is installed, the playbook fails to load the necessary components.

A typical error:

```
ERROR! couldn't resolve module/community.general
```

Or:

```
ERROR! Collection community.general requires ansible>=2.12
```

## Why It Happens

Common causes include:

- **Collection not installed** — First time using a community collection.
- **Wrong version** — Installed version does not meet minimum requirements.
- **Galaxy server unreachable** — Cannot download collection.
- **Requirements file missing** — Not specifying required collections.
- **Namespace issues** — Wrong collection namespace.
- **Ansible version too old** — Collection requires newer Ansible.

## How to Fix It

### Fix 1: Install missing collections

```bash
# RIGHT: Install collection from Galaxy
ansible-galaxy collection install community.general

# Install from specific version
ansible-galaxy collection install community.general:>=4.0.0

# Install from requirements file
ansible-galaxy collection install -r requirements.yml
```

### Fix 2: Create requirements.yml

```yaml
# requirements.yml
collections:
  - name: community.general
    version: ">=4.0.0"
  - name: community.mysql
    version: "3.0.0"
  - name: ansible.posix
    version: "*"
```

### Fix 3: Check installed collections

```bash
# RIGHT: List installed collections
ansible-galaxy collection list

# Check specific collection
ansible-galaxy collection info community.general
```

### Fix 4: Update collections

```bash
# RIGHT: Update all collections
ansible-galaxy collection install -r requirements.yml --upgrade

# Update specific collection
ansible-galaxy collection install community.general --upgrade
```

### Fix 5: Use collections in playbooks

```yaml
# RIGHT: Use fully qualified collection names
- name: Deploy app
  community.general.copy:
    src: app.zip
    dest: /opt/app/

# Or use collections directive
- hosts: webservers
  collections:
    - community.general
    - community.mysql
  tasks:
    - name: Copy file
      copy:
        src: app.zip
        dest: /opt/app/
```

## Common Mistakes

- **Forgetting to install collections** — Always check with `ansible-galaxy collection list`.
- **Not pinning collection versions** — Use specific versions for reproducibility.
- **Assuming built-in modules cover all needs** — Many tasks need community collections.

## Related Pages

- [Ansible Connection Refused](ansible-connection-refused) — Connection issues
- [Ansible Filter Error](ansible-filter-error) — Jinja2 filter issues
- [Ansible Lookup Error](ansible-lookup-error) — Lookup plugin issues
