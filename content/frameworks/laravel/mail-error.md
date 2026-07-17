---
title: "Mail send failed"
description: "Laravel throws Swift_TransportException or ConnectionException when sending email fails"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Laravel cannot send an email due to SMTP connection failures, authentication issues, or the mail server rejecting the message.

## Common Causes

- SMTP server credentials are incorrect or expired
- SMTP host/port is unreachable
- Email exceeds attachment size limits
- Mail queue driver is not running for queued emails

## How to Fix

1. Configure mail settings in `.env`:

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

2. Test the SMTP connection:

```php
use Illuminate\Support\Facades\Mail;

Mail::raw('Test email', function ($message) {
    $message->to('test@example.com')
            ->subject('Test');
});

// Or use Tinker
php artisan tinker
>>> Mail::raw('Hello', fn($m) => $m->to('test@test.com')->subject('Test'))
```

3. Queue emails to avoid blocking the request:

```php
// In a Mailable
class WelcomeMail extends Mailable
{
    public $queue = 'emails';

    public function build()
    {
        return $this->view('emails.welcome');
    }
}

// Send queued
Mail::to($user)->queue(new WelcomeMail($user));
```

4. Handle mail errors gracefully:

```php
try {
    Mail::to($user)->send(new WelcomeMail($user));
} catch (\Exception $e) {
    \Log::error("Mail failed: {$e->getMessage()}");
    // Fallback: log or retry later
}
```

## Examples

```php
Mail::to('user@example.com')->send(new OrderShipped($order));
```

```text
Swift_TransportException: Connection could not be established with host smtp.mailtrap.io
```

## Related Errors

- [Queue job failed]({{< relref "/frameworks/laravel/queue-error" >}})
