---
title: "[Solution] Ansible Jinja2 Macro Undefined"
description: "Fix Ansible errors when Jinja2 macros are not defined in templates"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible template references an undefined Jinja2 macro.

```
ERROR! Jinja2 Template Error: UndefinedError: 'my_macro' is undefined
```

## Common Causes

- Macro not defined in template
- Macro in wrong scope
- Typo in macro name
- Macro file not imported

## How to Fix

```yaml
# Define macro in template
# templates/config.j2
# {% macro server_block(name, port) %}
# server {
#     listen {{ port }};
#     server_name {{ name }};
# }
# {% endmacro %}

# Import macros from file
# templates/main.j2
# {% from 'macros/network.j2' import firewall_rule %}
# {{ firewall_rule('allow_http', 80, 'tcp') }}
```
