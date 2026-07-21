---
title: "[Solution] Netlify GraphQL API Error"
description: "Fix Netlify GraphQL API errors. Resolve GraphQL query issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

Netlify GraphQL API Error can prevent your application from working correctly.

## Common Causes

- Query syntax error
- Schema mismatch
- Permission denied
- Rate limited

## How to Fix

### Query API

```bash
curl -X POST https://api.netlify.com/api/v1/graphql \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  --data '{"query":"{ allSite { edges { node { name } } } }"}'
```

