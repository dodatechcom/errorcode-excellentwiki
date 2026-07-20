---
title: "[Solution] Apache BalancerMember Not Configured"
description: "The proxy balancer has no valid backend members defined."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The proxy balancer has no valid backend members defined.

## Common Causes

- No BalancerMember directives in Proxy block
- All BalancerMember backends are down
- BalancerMember URLs are invalid
- Missing mod_proxy_balancer module

## How to Fix

- Add BalancerMember directives with valid backend URLs
- Ensure backend servers are running
- Load mod_proxy_balancer module

## Examples

```
['<Proxy balancer://cluster>\n  BalancerMember http://backend1:8080\n  BalancerMember http://backend2:8080\n</Proxy>']
```
