---
title: "[Solution] Ansible Jinja2 Block Not Closed"
description: "Fix Ansible Jinja2 template block closure errors"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible template has an unclosed Jinja2 block.

```
ERROR! Jinja2 Template Error: Block 'if' not closed
```

## Common Causes

- Missing {% endif %}
- Missing {% endfor %}
- Missing {% endblock %}
- Nested blocks without proper closure

## How to Fix

```yaml
# All blocks must be properly closed
# CORRECT:
# {% if condition %}
# Do something
# {% endif %}

# Nested blocks
# {% for server in servers %}
#   {% if server.enabled %}
#     server {{ server.name }};
#   {% endif %}
# {% endfor %}
```
