---
title: "[Solution] Ansible Vars Prompt Not Allowed"
description: "Fix Ansible vars_prompt restrictions in certain contexts"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible vars_prompt is used in an invalid context.

```
ERROR! vars_prompt is not allowed in a pre_tasks or role context
```

## Common Causes

- vars_prompt used in pre_tasks instead of play level
- vars_prompt used inside a role
- vars_prompt in imported play

## How to Fix

```yaml
# CORRECT: vars_prompt at play level
- name: Deploy with confirmation
  hosts: all
  vars_prompt:
    - name: deploy_env
      prompt: "Enter target environment"
      default: dev
      private: false
  tasks:
    - name: Deploy
      ansible.builtin.debug:
        msg: "Deploying to {{ deploy_env }}"
```

# Use --extra-vars instead:
# ansible-playbook deploy.yml --extra-vars \"deploy_env=prod\"" 
