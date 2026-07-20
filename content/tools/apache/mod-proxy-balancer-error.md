---
title: "[Solution] Apache mod_proxy_balancer Error"
description: "The proxy balancer module encounters an error managing backend members."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The proxy balancer module encounters an error managing backend members.

## Common Causes

- BalancerMember not configured or unreachable
- lbmethod not specified or module not loaded
- Health check URL returning errors
- BalancerMember max_fails too low

## How to Fix

- Ensure all BalancerMember backends are running
- Load required modules: mod_proxy_balancer, mod_lbmethod_byrequests
- Set max_fails and failtimeout appropriately

## Examples

```
['<Proxy balancer://mycluster>\n  BalancerMember http://backend1:8080\n  BalancerMember http://backend2:8080\n  ProxySet lbmethod=byrequests\n</Proxy>']
```
