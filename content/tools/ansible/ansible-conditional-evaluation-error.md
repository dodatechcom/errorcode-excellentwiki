---
title: "[Solution] Ansible Conditional Evaluation Error"
description: "Fix Ansible conditional evaluation errors when when clauses evaluate incorrectly or throw exceptions."
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

# Ansible Conditional Evaluation Error

Ansible fails to evaluate a conditional expression in a `when` clause.

```
ERROR! The conditional check 'result.stdout' failed.
The error was: Conditional is not a boolean
```

## Common Causes

- Variable is undefined or None
- Comparing incompatible types
- Incorrect Jinja2 syntax in the condition
- Register variable structure does not match expectation
- Missing quotes around string comparisons

## How to Fix

### Use Defined Check

```yaml
- name: Safe conditional check
  ansible.builtin.debug:
    msg: "Variable is set"
  when: my_variable is defined and my_variable | length > 0
```

### Handle None Values

```yaml
- name: Run only if previous task succeeded
  ansible.builtin.debug:
    msg: "Previous task changed something"
  when: result is defined and result.changed is defined and result.changed
```

### Compare Types Correctly

```yaml
# Wrong - comparing string to integer
- name: Bad comparison
  ansible.builtin.debug:
    msg: "Match found"
  when: result.rc == "0"

# Right - compare same types
- name: Correct comparison
  ansible.builtin.debug:
    msg: "Match found"
  when: result.rc == 0
```

### Use Default Filter

```yaml
- name: Use default value in conditional
  ansible.builtin.debug:
    msg: "Value exists"
  when: (result.stdout | default("")) | length > 0
```

## Examples

```yaml
- name: Complex conditional
  ansible.builtin.debug:
    msg: "All conditions met"
  when:
    - result is defined
    - result.rc is defined
    - result.rc == 0
    - result.stdout | default("") | length > 0
```
