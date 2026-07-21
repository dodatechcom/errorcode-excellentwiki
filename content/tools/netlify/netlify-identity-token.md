---
title: "[Solution] Netlify Identity Token Error"
description: "Fix Netlify Identity JWT token errors when authentication tokens are invalid or expired."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

# Netlify Identity Token Error

Netlify Identity returns invalid or expired JWT tokens.

```
Invalid token: token is expired or malformed
```

## Common Causes

- JWT token has expired
- Token was generated with wrong secret
- GoTrue service not responding
- Token header malformed
- Identity service not enabled for site

## How to Fix

### Check Token Validity

```bash
# Decode JWT payload
echo "eyJhbGci..." | cut -d'.' -f2 | base64 -d 2>/dev/null | jq .
```

### Refresh Expired Token

```javascript
const { user } = await netlifyIdentity.currentUser();
const token = await netlifyIdentity.gotrue.currentUser();
```

### Configure Identity in netlify.toml

```toml
[[headers]]
  for = "/.netlify/identity/*"
  [headers.values]
    Access-Control-Allow-Origin = "*"
```

### Enable Identity

```
1. Go to Site settings > Identity
2. Click "Enable Identity"
3. Configure Git Gateway if needed
```

### Use Access Token

```javascript
const response = await fetch(url, {
  headers: {
    Authorization: `Bearer ${netlifyIdentity.currentUser()?.token?.access_token}`
  }
});
```

### Check GoTrue Service

```bash
# Test GoTrue endpoint
curl https://your-site.netlify.app/.netlify/identity/health
```

## Examples

```javascript
// Handle token refresh
async function fetchWithAuth(url) {
  const user = netlifyIdentity.currentUser();
  if (!user) throw new Error("Not authenticated");
  
  const token = user.token?.access_token;
  if (!token) throw new Error("No token");
  
  return fetch(url, {
    headers: { Authorization: `Bearer ${token}` }
  });
}
```
