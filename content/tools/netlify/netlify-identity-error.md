---
title: "[Solution] Netlify Identity Authentication Failed Error — How to Fix"
description: "Fix Netlify Identity authentication failures. Resolve login errors, JWT issues, and Identity service configuration problems."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
weight: 1
comments: true
---

A Netlify Identity authentication failed error occurs when users cannot log in, register, or authenticate using Netlify Identity. The Identity service provides user management with JWT-based authentication.

## What This Error Means

Netlify Identity is a built-in user management service that handles registration, login, and JWT token generation. When authentication fails, it can be due to service misconfiguration, token validation errors, or client-side integration issues. Identity uses GoTrue under the hood for authentication operations.

## Why It Happens

- Netlify Identity is not enabled in the site settings
- The Identity JWT is not being validated correctly
- The `gotrue` endpoint URL is incorrect
- The user has not confirmed their email address
- The JWT has expired and is not being refreshed
- External authentication providers (GitHub, Google) are not configured
- The Identity service is hitting rate limits
- The JWT secret was regenerated, invalidating existing tokens
- The Identity service is disabled for the specific site

## Common Error Messages

- `Invalid login credentials` — Email or password is incorrect
- `Email not confirmed` — User has not clicked the confirmation link
- `JWT validation failed` — The token is invalid or expired
- `Identity not enabled` — Netlify Identity is not turned on for this site
- `User not found` — The email address is not registered
- `Token has expired` — The JWT TTL has been exceeded

## How to Fix It

### Enable Netlify Identity

```bash
# In Netlify Dashboard:
# Site Settings > Identity > Enable Identity

# Or via API
curl -X PATCH "https://api.netlify.com/api/v1/sites/SITE_ID" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
    "identity": {
      "enabled": true
    }
  }'
```

### Configure Identity Settings

```toml
# netlify.toml — Identity configuration
[build]
  command = "npm run build"

# Identity settings via dashboard:
# - Registration: Open / Invite only / Disabled
# - External providers: GitHub, Google, etc.
# - JWT expiry: 1 hour (default) to 30 days
# - Roles: Set default roles for new users
```

### Integrate Identity with Your App

```javascript
// Initialize the Identity client
import netlifyIdentity from 'netlify-identity-widget';

// Mount the widget
netlifyIdentity.init({
  container: '#netlify-modal',
  locale: 'en',
});

// Handle login
netlifyIdentity.on('login', (user) => {
  console.log('Logged in:', user.email);
  console.log('JWT:', user.token.access_token);

  // Store the JWT for API calls
  localStorage.setItem('auth-token', user.token.access_token);
});

// Handle logout
netlifyIdentity.on('logout', () => {
  console.log('Logged out');
  localStorage.removeItem('auth-token');
});

// Open the login dialog
function openLogin() {
  netlifyIdentity.open();
}
```

### Validate JWT Tokens

```javascript
// Validate the JWT in your API or edge function
const jwt = require('jsonwebtoken');

function validateToken(token) {
  try {
    // Netlify Identity uses a specific JWT secret
    // You can find it in: Dashboard > Identity > Settings > JWT Secret
    const decoded = jwt.verify(token, process.env.JWT_SECRET);

    return {
      valid: true,
      user: {
        email: decoded.email,
        roles: decoded.app_metadata?.roles || [],
        id: decoded.sub,
      },
    };
  } catch (err) {
    console.error('JWT validation failed:', err.message);
    return { valid: false, error: err.message };
  }
}
```

### Auto-Confirm Users for Development

```bash
# In Netlify Dashboard:
# Identity > Settings > Registration > Allow new registrations

# For development, enable auto-confirm:
# Identity > Settings > External providers > Git Gateway

# Or disable email confirmation entirely (dev only)
# This allows users to log in without confirming their email
```

### Manage User Roles

```javascript
// Assign roles to users via API
async function assignRole(userId, role) {
  const response = await fetch(
    `https://your-site.netlify.app/.netlify/functions/identity/admin/users/${userId}`,
    {
      method: 'PUT',
      headers: {
        'Authorization': `Bearer ${adminToken}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        app_metadata: {
          roles: [role],
        },
      }),
    }
  );

  return response.json();
}

// Check user roles in middleware
function isAdmin(user) {
  return user.app_metadata?.roles?.includes('admin') || false;
}
```

## Common Scenarios

- **Email confirmation required:** A new user registers but never clicks the confirmation email link. They cannot log in until their email is confirmed.
- **JWT expired:** The user's JWT token expired after 1 hour (default) but the app does not handle token refresh, causing API calls to fail.
- **Provider misconfigured:** GitHub OAuth is enabled in Identity but the OAuth App credentials are incorrect, causing the redirect to fail.

## Prevent It

1. Configure Identity settings (registration mode, JWT expiry, external providers) before launching to production
2. Implement JWT refresh logic in your application to handle token expiration gracefully
3. Use Netlify's invite-only mode for internal tools to prevent unauthorized registration

## Related Pages

- [Netlify Form Error]({{< relref "/tools/netlify/netlify-form-error" >}}) — Form submission issues
- [Netlify Identity Error]({{< relref "/tools/netlify/netlify-identity-error" >}}) — Identity service error
