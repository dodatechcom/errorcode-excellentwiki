---
title: "[Solution] Ruby ActionMailer::DeliveryError Fix"
description: "Fix ActionMailer::DeliveryError in Rails. Learn why email delivery fails and how to configure mailer settings."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["actionmailer", "delivery", "email", "rails", "ruby"]
weight: 5
---

## What This Error Means

An `ActionMailer::DeliveryError` is raised when Rails cannot deliver an email. This can happen due to SMTP configuration issues, network problems, or invalid recipient addresses.

## Common Causes

- SMTP server unreachable or misconfigured
- Invalid email address in recipient
- Authentication failure with SMTP server
- Email size exceeds server limits

## How to Fix

```ruby
# WRONG: Not configuring SMTP
# config/environments/production.rb
config.action_mailer.delivery_method = :smtp

# CORRECT: Configure SMTP settings
config.action_mailer.delivery_method = :smtp
config.action_mailer.smtp_settings = {
  address: 'smtp.gmail.com',
  port: 587,
  user_name: ENV['SMTP_USERNAME'],
  password: ENV['SMTP_PASSWORD'],
  authentication: 'plain',
  enable_starttls_auto: true
}
```

```ruby
# WRONG: Invalid recipient email
UserMailer.welcome("not-an-email").deliver_now  # DeliveryError

# CORRECT: Validate email before sending
def send_welcome(user)
  if user.email.match?(/\A[\w+\-.]+@[a-z\d\-.]+\.[a-z]+\z/i)
    UserMailer.welcome(user).deliver_now
  else
    Rails.logger.error "Invalid email: #{user.email}"
  end
end
```

```ruby
# WRONG: Not handling delivery failures
UserMailer.welcome(user).deliver_now  # May raise DeliveryError

# CORRECT: Rescue delivery errors
begin
  UserMailer.welcome(user).deliver_now
rescue ActionMailer::DeliveryError => e
  Rails.logger.error "Email delivery failed: #{e.message}"
end
```

## Examples

```ruby
# Example 1: Test mailer configuration
rails console
ActionMailer::Base.smtp_settings

# Example 2: Use letter_opener in development
config.action_mailer.delivery_method = :letter_opener

# Example 3: Check email before sending
user.valid_email?  # Custom validation
```

## Related Errors

- [ActionController::RoutingError](rails-routing) — route not found
- [ActionController::InvalidAuthenticityToken](rails-controller) — CSRF token invalid
- [ActionView::MissingTemplate](rails-template) — template not found
