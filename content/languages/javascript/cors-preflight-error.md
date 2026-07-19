---
title: "[Solution] CORS Preflight Error — OPTIONS Request Failed Fix"
description: "Fix CORS preflight errors when browser OPTIONS request fails. Configure Access-Control-Allow-Headers and Methods."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# CORS Preflight Error

The browser sends an OPTIONS request before the actual request.

## Server Fix (Express)

```javascript
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
  res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  if (req.method === 'OPTIONS') return res.sendStatus(200);
  next();
});
```

## Or use the cors package

```bash
npm install cors
```

```javascript
const cors = require('cors');
app.use(cors());
```
