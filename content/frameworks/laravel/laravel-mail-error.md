---
title: "Swift_TransportException - mail send failed"
description: "Laravel throws Swift_TransportException when it cannot connect to the mail server to send an email"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Laravel's mailer (SwiftMailer/Mailer) cannot establish a connection to the configured SMTP server. It throws `Swift_TransportException` with connection refused or timeout details.

## Common Causes

- SMTP server host, port, or credentials are incorrect in `.env`
- SMTP server is down or unreachable from the application server
- Firewall blocking the SMTP port (typically 587 or 465)
- SSL/TLS certificate verification failure
- Authentication credentials expired or revoked

## How to Fix

1. Verify your mail configuration in `.env`:

```env
MAIL_MAILER=smtp
MAIL_HOST=smtp.mailtrap.io
MAIL_PORT=587
MAIL_USERNAME=your_username
MAIL_PASSWORD=your_password
MAIL_ENCRYPTION=tls
MAIL_FROM_ADDRESS="hello@example.com"
MAIL_FROM_NAME="${APP_NAME}"
```

2. Test the connection manually:

```php
use Illuminate\Support\Facades\Mail;

try {
    Mail::raw('Test email', function ($message) {
        $message->to('test@example.com')
                ->subject('Test');
    });
} catch (\Swift_TransportException $e) {
    Log::error('Mail failed: ' . $e->getMessage());
}
```

3. Use the `log` driver during development:

```env
MAIL_MAILER=log
```

## Examples

```php
// Swift_TransportException: Connection could not be established with host "smtp.example.com"
Mail::to('user@example.com')->send(new WelcomeEmail());
```

## Related Errors

- [Queue error]({{< relref "/frameworks/laravel/queue-error" >}})
- [Cache error]({{< relref "/frameworks/laravel/cache-error" >}})
