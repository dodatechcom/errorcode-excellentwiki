---
title: "[Solution] Rails ActionMailer::DeliveryError Fix"
description: "Fix Rails mailer delivery errors when email fails to send."
languages: ["ruby"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["ActionMailer", "delivery", "email", "smtp", "rails", "ruby"]
weight: 5
---

# Rails ActionMailer::DeliveryError Fix

A Rails mailer error occurs when an email fails to send due to SMTP issues, configuration errors, or network problems.

## What This Error Means

ActionMailer sends emails through SMTP or other delivery methods. `DeliveryError` occurs when the SMTP server rejects the message, credentials are wrong, or the connection fails.

## Common Causes

- Wrong SMTP server configuration
- Invalid credentials
- Connection timeout
- Email rejected by server (spam, policy)
- Missing required headers

## How to Fix

### 1. Check SMTP configuration

```ruby
# CORRECT: config/environments/production.rb
config.action_mailer.delivery_method = :smtp
config.action_mailer.smtp_settings = {
  address:              'smtp.gmail.com',
  port:                 587,
  domain:               'example.com',
  user_name:            ENV['SMTP_USERNAME'],
  password:             ENV['SMTP_PASSWORD'],
  authentication:       'plain',
  enable_starttls_auto: true
}
```

### 2. Test mailer in console

```ruby
# CORRECT: Test email delivery
UserMailer.welcome(User.first).deliver_now
# Check Rails logs for SMTP errors
```

### 3. Handle delivery errors

```ruby
# CORRECT: Rescue delivery errors
class UserMailer < ApplicationMailer
  def welcome(user)
    @user = user
    mail(to: @user.email, subject: "Welcome!")
  rescue Net::SMTPAuthenticationError => e
    Rails.logger.error "SMTP auth failed: #{e.message}"
  rescue Net::SMTPFatalError => e
    Rails.logger.error "SMTP error: #{e.message}"
  end
end
```

### 4. Use letter_opener for development

```ruby
# CORRECT: Development email preview
# config/environments/development.rb
config.action_mailer.delivery_method = :letter_opener
config.action_mailer.raise_delivery_errors = true
```

## Related Errors

- [Rails Template Error](rails-template-error) — missing templates
- [Rails Controller Error](rails-controller-error) — controller issues
- [Rails Routing Error](rails-routing-error) — route not found
