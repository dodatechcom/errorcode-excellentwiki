---
title: "[Solution] Rails ActionController::InvalidAuthenticityToken Fix"
description: "Fix Rails CSRF token errors when form submissions fail authenticity token validation."
languages: ["ruby"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Rails ActionController::InvalidAuthenticityToken Fix

A Rails controller error occurs when a form submission or API request fails CSRF (Cross-Site Request Forgery) token validation.

## What This Error Means

Rails protects against CSRF attacks by requiring an authenticity token on non-GET requests. If the token is missing, invalid, or the session expired, the error fires.

## Common Causes

- Token missing from form submission
- Session expired before form submit
- AJAX request without CSRF token
- Token mismatch due to caching
- Using cookies session store with stale tokens

## How to Fix

### 1. Include CSRF token in forms

```erb
<!-- CORRECT: Use form helpers that include token -->
<%= form_with model: @user do |f| %>
  <%= f.text_field :name %>
  <%= f.submit %>
<% end %>
```

### 2. Add token to AJAX requests

```javascript
// CORRECT: Include token in fetch/XMLHttpRequest
const token = document.querySelector('meta[name="csrf-token"]').content;
fetch('/users', {
  method: 'POST',
  headers: {
    'X-CSRF-Token': token,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ user: { name: 'Alice' } })
});
```

### 3. Skip CSRF for API endpoints

```ruby
# CORRECT: Skip for API controllers
class Api::UsersController < ApplicationController
  skip_before_action :verify_authenticity_token
  # Or use null session
  protect_from_forgery with: :null_session
end
```

### 4. Handle expired sessions

```ruby
# CORRECT: Rescue CSRF errors
class ApplicationController < ActionController::Base
  rescue_from ActionController::InvalidAuthenticityToken do |exception|
    redirect_to root_path, alert: "Session expired. Please try again."
  end
end
```

## Related Errors

- [Rails Controller Error]({{< relref "/languages/ruby/rails-controller" >}}) — controller issues
- [Rails Routing Error](rails-routing-error) — route not found
- [Rails Template Error](rails-template-error) — missing templates
