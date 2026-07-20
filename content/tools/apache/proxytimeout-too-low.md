---
title: "[Solution] Apache ProxyTimeout Too Low"
description: "The ProxyTimeout is set too low, causing premature connection closure."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The ProxyTimeout is set too low, causing premature connection closure.

## Common Causes

- Default ProxyTimeout of 60 seconds too short
- Backend takes longer than configured timeout
- Large file transfers need more time

## How to Fix

- Increase ProxyTimeout to match backend response time
- Set per-connection timeouts if needed
- Consider async processing for long operations

## Examples

```
['ProxyTimeout 300\n# Or per-location:\n<Location /api/>\n  ProxyTimeout 600\n</Location>']
```
