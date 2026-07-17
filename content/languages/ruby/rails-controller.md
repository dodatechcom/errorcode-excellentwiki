---
title: "[Solution] Ruby ActionController::InvalidAuthenticityToken Fix"
description: "Fix ActionController::InvalidAuthenticityToken in Rails. Learn why CSRF protection fails and how to handle authenticity tokens."
languages: ["ruby"]
severities: ["error"]
error-types: ["security-error"]
tags: ["actioncontroller", "csrf", "authenticity-token", "rails", "ruby"]
weight: 5
---

## What This Error Means

An `ActionController::InvalidAuthenticityToken` is raised when Rails detects a request with an invalid or missing CSRF authenticity token. This is a security feature to prevent cross-site request forgery attacks.

## Common Causes

- Missing authenticity token in form
- Session expired or cookie changed
- API request without CSRF skip
- Token mismatch between client and server

## How to Fix

```ruby
# WRONG: Form without authenticity token
# In ERB: <form action="/posts" method="post">

# CORRECT: Include authenticity token
# In ERB: <%= form_with model: @post do |f| %>
# Automatically includes authenticity_token
```

```ruby
# WRONG: API request hitting CSRF protection
class ApiController < ApplicationController
  def create
    # ActionController::InvalidAuthenticityToken
  end
end

# CORRECT: Skip CSRF for API controllers
class ApiController < ApplicationController
  skip_before_action :verify_authenticity_token
  def create
    # OK
  end
end
```

```ruby
# WRONG: Not handling token in JavaScript
# fetch('/posts', { method: 'POST', body: data })

# CORRECT: Include token in JavaScript requests
fetch('/posts', {
  method: 'POST',
  headers: {
    'X-CSRF-Token': document.querySelector('meta[name="csrf-token"]').content
  },
  body: data
})
```

## Examples

```ruby
# Example 1: Check token in controller
class ApplicationController < ActionController::Base
  protect_from_forgery with: :exception
end

# Example 2: Custom handling
class ApplicationController < ActionController::Base
  protect_from_forgery with: :null_session
end

# Example 3: Token in view
<%= tag.meta name: "csrf-token", content: form_authenticity_token %>
```

## Related Errors

- [ActionController::RoutingError](rails-routing) — route not found
- [ActionView::MissingTemplate](rails-template) — template not found
- [ActionMailer::DeliveryError](rails-mailer) — email delivery failed
