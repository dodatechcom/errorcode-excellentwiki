---
title: "[Solution] Ansible Syntax Error — Fix Playbook Syntax"
description: "Fix Ansible playbook syntax errors. Identify YAML formatting mistakes, indentation issues, and module configuration errors with fixes."
---

## What This Error Means

Syntax errors prevent Ansible from parsing your playbook before any tasks execute. These errors are caught by the YAML parser or Ansible's syntax checker and are usually caused by formatting mistakes.

A typical error:

```
ERROR! Syntax Error while loading YAML.
  line 15, column 5, could not find expected ':'
```

Or:

```
ERROR! failed to combine variables, already defined variables have the
same name but different types: my_list
```

## Why It Happens

Syntax errors are caused by:

- **YAML indentation mistakes**: Inconsistent spacing or wrong indentation levels.
- **Missing colons**: Forgetting the `:` after dictionary keys.
- **Using tabs instead of spaces**: YAML requires spaces for indentation, never tabs.
- **Incorrect quoting**: Mismatched quotes around strings or values.
- **Module option errors**: Wrong parameter names or values for Ansible modules.
- **Jinja2 syntax errors**: Invalid template expressions inside `{{ }}` blocks.

## How to Fix It

**Step 1: Run the syntax check**

```bash
ansible-playbook site.yml --syntax-check
```

**Step 2: Validate YAML independently**

```bash
python -c "import yaml; yaml.safe_load(open('site.yml'))"
# Or use yamllint
yamllint site.yml
```

**Step 3: Fix common YAML issues**

```yaml
# WRONG - inconsistent indentation
- hosts: webservers
  tasks:
    - name: Install package
      ansible.builtin.apt:      # Must be indented under task
      name: nginx                # WRONG - same level as module name
      state: present

# CORRECT
- hosts: webservers
  tasks:
    - name: Install package
      ansible.builtin.apt:
        name: nginx
        state: present
```

**Step 4: Fix module parameter errors**

Check module documentation:

```bash
ansible-doc ansible.builtin.apt
```

**Step 5: Use yamllint in your CI pipeline**

```yaml
# .yamllint
---
extends: default
rules:
  indentation:
    spaces: 2
    indent-sequences: true
  line-length:
    max: 200
```

## Common Mistakes

- **Using tabs for indentation**: Always use spaces (2 spaces is the Ansible convention).
- **Wrong module parameter names**: Check `ansible-doc` for the exact parameter names.
- **Mixing YAML and Jinja2 syntax**: Ensure Jinja2 expressions are properly quoted.
- **Not validating before running**: Always run `--syntax-check` before executing playbooks.

## Related Pages

- [Ansible Undefined Variable](/tools/ansible/ansible-undefined-variable/) — Missing variable errors
- [Ansible Task Failed](/tools/ansible/ansible-task-failed/) — Runtime task failures
- [Terraform Validation Error](/tools/terraform/terraform-validation-error/) — Configuration validation
