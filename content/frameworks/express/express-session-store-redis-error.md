---
title: "[Solution] Express Session Store Redis Error"
description: "Redis session store failing."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Redis session store failing.

## Common Causes

Wrong client.

## How to Fix

Configure correctly.

## Example

```javascript
const RedisStore = require('connect-redis').default;
app.use(session({ store: new RedisStore({ client: redisClient }) }));
```
