---
title: "[Solution] Express Session Mongo Error"
description: "Mongo session store failing."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Mongo session store failing.

## Common Causes

Wrong config.

## How to Fix

Configure correctly.

## Example

```javascript
const MongoStore = require('connect-mongo');
app.use(session({ store: MongoStore.create({ mongoUrl: 'mongodb://...' }) }));
```
