---
title: "[Solution] Rails CSRF Error — How to Fix"
description: "Fix Rails CSRF token errors. Resolve CSRF verification failures, missing tokens, and cross-site request issues."
frameworks: ["rails"]
error-types: ["security-error"]
severities: ["error"]
weight: 5
comments: true
---

A Rails CSRF error occurs when the Cross-Site Request Forgery token is missing, invalid, or does not match the session.

## Why It Happens

CSRF errors happen when tokens are absent from AJAX requests, the cookie is not set, middleware order is incorrect, or the origin check fails.

## Common Error Messages

```
CSRF verification failed. Request aborted.
```

```
CSRF token missing or incorrect.
```

```
CSRF cookie not set.
```

```
Origin checking failed - does not match TrustedOrigins.
```

## How to Fix It

### 1. Add CSRF Token to Templates

Include the CSRF token in all forms.

```erb
<%= form_with model: @user do |f| %>
  <%= f.text_field :name %>
  <%= f.submit %>
<% end %>
<%= csrf_meta_tags %>
```

### 2. Include Token in AJAX Requests

Read the CSRF cookie for headers.

```javascript
const csrfToken = document.querySelector('meta[name="csrf-token"]').content;
fetch('/users', {
  method: 'POST',
  headers: { 'X-CSRF-Token': csrfToken, 'Content-Type': 'application/json' },
  body: JSON.stringify({ user: { name: 'John' } })
});
```

### 3. Exempt API Views

Exempt views using token-based auth.

```ruby
class Api::UsersController < ApplicationController
  skip_before_action :verify_authenticity_token
  before_action :authenticate_api_user!
end
```

### 4. Configure Trusted Origins

Add domains to the trusted list.

```ruby
CSRF_TRUSTED_ORIGINS = ['https://example.com', 'https://app.example.com']
```

## Common Scenarios

**Scenario 1: AJAX POST returns 403 Forbidden.**
Include CSRF token in request headers.

**Scenario 2: CSRF cookie not set error.**
Ensure SessionMiddleware is before CsrfViewMiddleware.

**Scenario 3: Cross-origin form fails.**
Add origin to CSRF_TRUSTED_ORIGINS.

## Prevent It

1. **Always include CSRF tokens.**
Use `form_with` which includes tokens.

2. **Never disable CSRF globally.**
Only exempt specific API actions.

3. **Test CSRF protection.**
Verify POST without tokens is rejected.

