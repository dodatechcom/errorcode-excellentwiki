---
title: "[Solution] Ansible Template Error — Fix Undefined Variable in Template"
description: "Fix Ansible template errors when Jinja2 templates contain undefined variables. Resolve missing variables, incorrect references, and template syntax issues."
---

## What This Error Means

Ansible template errors occur when a Jinja2 template file contains a reference to an undefined variable or has invalid template syntax. Ansible raises an error before or during file creation.

A typical error:

```
fatal: [host1]: FAILED! => {
    "msg": "The task includes an option with an undefined variable.
    The error was: 'my_variable' is undefined"
}
```

Or:

```
fatal: [host1]: FAILED! => {
    "msg": "AnsibleUndefinedVariable: 'hostvars' is undefined"
}
```

## Why It Happens

Template errors happen when:

- **Variable is not defined**: The referenced variable is not set in vars, group_vars, host_vars, or facts.
- **Typo in variable name**: The template references a variable name that does not match the defined one.
- **Scoping issue**: The variable is defined but not accessible in the current context.
- **Filter or function does not exist**: Using a Jinja2 filter that is not available.
- **Missing fact for hostvars reference**: Accessing facts from a host that has not been gathered yet.
- **Incorrect template syntax**: Missing braces, unbalanced tags, or invalid Jinja2 expressions.

## How to Fix It

**Step 1: Enable debug output**

```bash
ansible-playbook playbook.yml -vvv
```

**Step 2: Use default values for optional variables**

```yaml
- name: Template with defaults
  template:
    src: config.j2
    dest: /etc/app/config
  vars:
    my_variable: "{{ my_variable | default('fallback') }}"
```

**Step 3: Validate variables with assert**

```yaml
- name: Verify required variables
  assert:
    that:
      - my_variable is defined
      - other_var is defined
```

**Step 4: Check variable precedence**

```bash
ansible-inventory --host host1 --export | grep my_variable
ansible host1 -m debug -a "var=my_variable"
```

**Step 5: Use Jinja2 strict mode in templates**

```yaml
- template:
    src: config.j2
    dest: /etc/app/config
  vars:
    _strict: true
```

## Common Mistakes

- **Not defining variables that templates expect**: Always define a default value in defaults/main.yml for roles.
- **Referencing hostvars without ensuring facts are gathered**: Set `gather_facts: true` or use `delegate_to`.
- **Typos in variable names that are hard to spot**: Use YAML linting to catch syntax errors.
- **Assuming group_vars are always loaded**: Verify the host is in the expected inventory group.

## Related Pages

- [Ansible Undefined Variable](/tools/ansible/ansible-undefined-variable/) -- Variable errors
- [Ansible Syntax Error](/tools/ansible/ansible-syntax-error/) -- Playbook syntax issues
- [Ansible Task Failed](/tools/ansible/ansible-task-failed/) -- Task execution failures
