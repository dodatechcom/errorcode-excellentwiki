---
title: "[Solution] Ansible Debug Output Too Verbose"
description: "Fix Ansible debug module output flooding console with too much information during playbook runs."
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Ansible Debug Output Too Verbose

The `ansible.builtin.debug` module outputs excessive data to the console, making playbook output hard to read.

```
ok: [host1] => {
    "msg": {
        "large_dict_key": "...very long output..."
    }
}
```

## Common Causes

- Printing entire registered variables
- Verbose mode enabled globally
- No output filtering applied
- Debug tasks left in production playbooks
- Large data structures dumped without truncation

## How to Fix

### Use verbosity Control

```yaml
- name: Debug output with verbosity
  ansible.builtin.debug:
    var: result.stdout
  verbosity: 1
# Only shows when running with -v
```

### Limit Output in Playbook

```yaml
- name: Show only relevant output
  ansible.builtin.debug:
    msg: "Task completed with rc={{ result.rc }}"
  when: result.rc != 0
```

### Control Verbosity at Runtime

```bash
# Normal output (no debug)
ansible-playbook site.yml

# Show debug messages (-v)
ansible-playbook site.yml -v

# Very verbose (-vvv)
ansible-playbook site.yml -vvv
```

### Use Callback for Selective Output

```yaml
# Hide debug output in summary
- name: Log to file instead of console
  ansible.builtin.copy:
    content: "{{ result | to_nice_json }}"
    dest: /var/log/ansible/debug-{{ ansible_date_time.iso8601 }}.json
  delegate_to: localhost
```

## Examples

```bash
# Use NO_COLOR to simplify output
export NO_COLOR=1
ansible-playbook site.yml

# Use yaml callback for cleaner output
export ANSIBLE_STDOUT_CALLBACK=yaml
ansible-playbook site.yml
```
