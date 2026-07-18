---
title: "[Solution] Ansible Set Fact Variable Error Fix"
description: "Fix Ansible set_fact variable errors. Resolve variable setting, scope, and persistence issues in playbooks."
tools: ["ansible"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Ansible Set Fact Variable Error Fix

The `set_fact variable error` occurs when the `set_fact` module fails to create or update a variable due to scope issues, invalid values, or conflicts with existing variables.

## What This Error Means

`set_fact` creates host variables during playbook execution. When the variable name is invalid, the value causes an error, or the scope is incorrect, the module fails.

A typical error:

```
ERROR! Failed to set fact: invalid variable name
```

Or the fact is not accessible in the expected scope.

## Why It Happens

Common causes include:

- **Invalid variable name** — Using hyphens or special characters.
- **Variable scope confusion** — Fact not visible in expected context.
- **Cache issues** — Stale cached facts interfering.
- **Type conflicts** — Overwriting string with list or vice versa.
- **Jinja2 error in value** — Bad syntax in the value expression.

## How to Fix It

### Fix 1: Use valid variable names

```yaml
# WRONG: Invalid variable name
- ansible.builtin.set_fact:
    my-var: "value"  # Hyphens not allowed

# RIGHT: Use underscores
- ansible.builtin.set_fact:
    my_var: "value"
```

### Fix 2: Understand fact caching

```yaml
# RIGHT: Facts are per-host and persist across tasks
- name: Set database config
  ansible.builtin.set_fact:
    db_host: "localhost"
    db_port: 5432

# Later in same play or role
- name: Use the fact
  ansible.builtin.debug:
    msg: "Connecting to {{ db_host }}:{{ db_port }}"
```

### Fix 3: Set fact with complex values

```yaml
# RIGHT: Set complex data structures
- ansible.builtin.set_fact:
    app_config:
      database:
        host: "db.example.com"
        port: 5432
        name: "mydb"
      cache:
        ttl: 3600
```

### Fix 4: Clear cached facts

```yaml
# RIGHT: Clear facts when needed
- ansible.builtin.meta: clear_facts

# Or clear specific fact
- ansible.builtin.set_fact:
    my_var: "{{ omit }}"  # This does not actually unset
```

### Fix 5: Use set_fact for dynamic configuration

```yaml
# RIGHT: Dynamic configuration based on conditions
- ansible.builtin.set_fact:
    max_connections: "{{ 1000 if ansible_memtotal_mb > 4000 else 500 }}"
  when: ansible_memtotal_mb is defined
```

## Common Mistakes

- **Assuming facts persist across plays** — Facts are per-host, per-play by default.
- **Using set_fact in roles** — Facts set in roles are accessible in the same play.
- **Not using cacheable: yes** — Facts are not cached unless explicitly set.

## Related Pages

- [Ansible Lookup Error](ansible-lookup-error) — Lookup plugin issues
- [Ansible Filter Error](ansible-filter-error) — Jinja2 filter issues
- [Ansible Block Rescue Error](ansible-block-rescue) — Error handling issues
