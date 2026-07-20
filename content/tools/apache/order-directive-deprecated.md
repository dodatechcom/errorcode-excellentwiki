---
title: "[Solution] Apache Order Directive Deprecated"
description: "The Order directive from Apache 2.2 is deprecated and may not work as expected."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The Order directive from Apache 2.2 is deprecated and may not work as expected.

## Common Causes

- Using Order allow,deny from Apache 2.2 configuration
- Mixing Order and Require directives
- Legacy configuration not updated for Apache 2.4

## How to Fix

- Replace Order/Allow/Deny with Require directives
- Use Require all granted instead of Order allow,deny
- Consult the Apache 2.4 migration guide

## Examples

```
['# Old (deprecated)\nOrder allow,deny\nAllow from all\n# New\nRequire all granted']
```
