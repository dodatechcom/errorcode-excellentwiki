---
title: "[Solution] Ansible Assert Error — Fix Assertion Failed in Task"
description: "Fix Ansible assert errors when validation conditions fail. Create effective assertions for idempotency and guard clauses in Ansible playbooks."
---

## What This Error Means

Ansible assert errors occur when the `assert` module evaluates a condition that returns false. Assertions are used to validate preconditions, postconditions, and assumptions in playbooks.

A typical error:

```
fatal: [host1]: FAILED! => {
    "assertion": "my_variable is defined",
    "changed": false,
    "evaluated_to": false,
    "msg": "Required variable my_variable is not defined"
}
```

Or:

```
fatal: [host1]: FAILED! => {
    "assertion": "my_service_state == 'running'",
    "changed": false,
    "evaluated_to": false,
    "msg": "Service is not running after restart attempt"
}
```

## Why It Happens

Assert failures happen when:

- **Precondition not met**: A required variable, file, or service state is not as expected.
- **Validation check fails**: A postcondition after a task does not hold true.
- **Incorrect assertion logic**: The Jinja2 expression in `that` is incorrectly formulated.
- **Missing variable definition**: The assertion references an undefined variable.
- **Wrong data type**: Comparing a string to an integer or list vs dict.
- **Timing issues**: Asserting a condition that has not stabilized yet.

## How to Fix It

**Step 1: Check the assertion condition**

```yaml
- name: Verify the assertion condition
  debug:
    msg: "{{ my_variable }}"
```

**Step 2: Use multiple assertions with meaningful messages**

```yaml
- name: Validate prerequisites
  assert:
    that:
      - required_var is defined
      - required_var is string
      - required_var | length > 0
    fail_msg: "required_var must be a non-empty string"
    success_msg: "required_var is valid"
```

**Step 3: Split complex conditions**

```yaml
- name: Check service is running
  assert:
    that:
      - service_status.state == 'running'
      - service_status.status == 'enabled'
```

**Step 4: Use quiet mode for optional checks**

```yaml
- name: Optional assertion
  assert:
    that:
      - optional_var is defined
    quiet: true
```

**Step 5: Add retries for timing-sensitive assertions**

```yaml
- name: Wait for condition
  assert:
    that: lookup('file', '/tmp/ready_flag') == 'ready'
  retries: 5
  delay: 10
```

## Common Mistakes

- **Asserting conditions with undefined variables**: Always use `is defined` checks first.
- **Using assert for control flow instead of `when`**: Use `when` for conditional task execution.
- **Not providing meaningful fail messages**: Always set `fail_msg` for debugging.
- **Asserting on data that has not been gathered yet**: Ensure facts are collected before assertions.

## Related Pages

- [Ansible Task Failed](/tools/ansible/ansible-task-failed/) -- Task execution failures
- [Ansible Undefined Variable](/tools/ansible/ansible-undefined-variable/) -- Variable errors
- [Ansible Syntax Error](/tools/ansible/ansible-syntax-error/) -- Playbook syntax issues
