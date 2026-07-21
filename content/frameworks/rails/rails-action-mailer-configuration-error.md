---
title: "[Solution] Rails Action Mailer Configuration Error"
description: "Fix Rails Action Mailer SMTP configuration errors. Resolve delivery method not set or SMTP connection failures."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when Action Mailer cannot send emails because the delivery method is not configured or SMTP settings are incorrect.

## Common Causes

- `config.action_mailer.delivery_method` not set in environment config
- SMTP host, port, or credentials are wrong in `config/environments`
- `default_url_options` not configured (required for mailer links)
- TLS/SSL settings mismatch with the SMTP server
- Gmail or provider blocks sign-in from less secure apps

## How to Fix

1. Configure SMTP in the environment file:

```ruby
# config/environments/production.rb
config.action_mailer.delivery_method = :smtp
config.action_mailer.smtp_settings = {
  address: 'smtp.gmail.com',
  port: 587,
  domain: 'example.com',
  user_name: ENV['SMTP_USERNAME'],
  password: ENV['SMTP_PASSWORD'],
  authentication: 'plain',
  enable_starttls_auto: true
}
```

2. Set default URL options for mailer links:

```ruby
config.action_mailer.default_url_options = { host: 'yourapp.com', protocol: 'https' }
```

3. Set a default from address:

```ruby
config.action_mailer.default_options = { from: 'no-reply@yourapp.com' }
```

4. Test the configuration:

```ruby
# rails console
ActionMailer::Base.smtp_settings
UserMailer.welcome(User.first).deliver_now
```

## Examples

```ruby
# Missing default_url_options causes error in mailer views
class UserMailer < ApplicationMailer
  def welcome(user)
    @user = user
    mail(to: user.email, subject: 'Welcome')
  end
end
# ActionView::Template::Error: Missing host to link to!
# Fix: add config.action_mailer.default_url_options = { host: 'localhost', port: 3000 }

# SMTP authentication failure
# Net::SMTPAuthenticationError: 535 5.7.8 Error: authentication failed
```
