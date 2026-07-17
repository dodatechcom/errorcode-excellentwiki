---
title: "Mail transport error"
description: "Laravel throws TransportException when the mailer cannot connect to or send through the configured mail transport"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Laravel cannot send an email through the configured mail transport. It is typically thrown as `Symfony\Component\Mailer\Exception\TransportException` when the SMTP server is unreachable or credentials are invalid.

## Common Causes

- SMTP server host or port is incorrect
- Invalid SMTP username or password
- SSL/TLS encryption mismatch
- SMTP server connection timeout
- Mailgun or Postmark API key is invalid

## How to Fix

1. Verify your mail configuration in `.env`:

```
MAIL_MAILER=smtp
MAIL_HOST=smtp.mailtrap.io
MAIL_PORT=587
MAIL_USERNAME=your_username
MAIL_PASSWORD=your_password
MAIL_ENCRYPTION=tls
MAIL_FROM_ADDRESS="hello@example.com"
MAIL_FROM_NAME="${APP_NAME}"
```

2. Test the SMTP connection before sending:

```php
use Illuminate\Support\Facades\Mail;
use Symfony\Component\Mailer\Exception\TransportException;

try {
    Mail::raw('Test email', function ($message) {
        $message->to('test@example.com')
                ->subject('Test');
    });
} catch (TransportException $e) {
    Log::error('Mail failed: ' . $e->getMessage());
}
```

3. Use a queue to prevent blocking the request:

```php
use App\Mail\WelcomeMail;

dispatch(function () use ($user) {
    Mail::to($user->email)->send(new WelcomeMail($user));
});
```

4. Configure a fallback mail driver:

```php
// config/mail.php
'mailers' => [
    'smtp' => [
        'transport' => 'smtp',
        // ...
    ],
    'log' => [
        'transport' => 'log',
        'channel' => 'mail',
    ],
],
```

## Examples

```php
// Sending with explicit transport failure handling
try {
    Mail::to('user@example.com')->send(new InvoiceMail($invoice));
} catch (TransportException $e) {
    Log::error('Could not send invoice email: ' . $e->getMessage());
    // Store for retry or notify admin
}
```

## Related Errors

- [Queue worker connection error]({{< relref "/frameworks/laravel/laravel-queue-error-v2" >}})
- [File not found in Laravel]({{< relref "/frameworks/laravel/laravel-file-not-found-v2" >}})
