---
title: "[Solution] Ansible Custom Filter Plugin Error"
description: "Fix Ansible custom Jinja2 filter plugin errors when custom filters fail to load or execute."
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

# Ansible Custom Filter Plugin Error

Ansible cannot load or execute a custom Jinja2 filter plugin.

```
ERROR! failed to typecast the filter: custom_filter
```

## Common Causes

- Filter plugin file has syntax errors
- Plugin class does not inherit from FilterModule
- Plugin directory not configured
- Missing Python module dependency
- Filter function signature is wrong

## How to Fix

### Create Correct Filter Plugin

```python
# filter_plugins/custom_filters.py
class FilterModule(object):
    def filters(self):
        return {
            'to_snake_case': self.to_snake_case,
            'dict_merge': self.dict_merge,
        }

    @staticmethod
    def to_snake_case(value):
        import re
        return re.sub(r'([A-Z])', r'_\1', value).lower().lstrip('_')

    @staticmethod
    def dict_merge(base, override):
        result = base.copy()
        result.update(override)
        return result
```

### Configure Filter Plugin Path

```ini
# ansible.cfg
[defaults]
filter_plugins = ./filter_plugins
```

### Verify Plugin Discovery

```bash
ansible-doc -t filter -l | grep custom
```

### Test Filter Manually

```bash
ansible -m debug -a "msg={{ 'helloWorld' | to_snake_case }}"
```

## Examples

```yaml
- name: Use custom filters
  hosts: localhost
  tasks:
    - name: Convert to snake case
      ansible.builtin.debug:
        msg: "{{ 'camelCaseVar' | to_snake_case }}"

    - name: Merge dictionaries
      ansible.builtin.debug:
        msg: "{{ base_dict | dict_merge(override_dict) }}"
```
