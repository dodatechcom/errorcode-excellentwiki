---
title: "[Solution] Cloudflare Durable Object Alarm Error"
description: "Fix Cloudflare Durable Object alarm errors. Resolve alarm scheduling issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Durable Object Alarm Error can prevent your application from working correctly.

## Common Causes

- Alarm not implemented in class
- Alarm already scheduled
- Clock drift
- Storage exceeded

## How to Fix

### Implement Alarm

```javascript
export class MyDurableObject {
  async alarm() {
    await this.processScheduledTask();
    await this.state.storage.setAlarm(Date.now() + 60000);
  }
}
```

