---
title: "[Solution] PHP LARAVEL_MAIL_ERROR — Email Sending Failed"
description: "Fix PHP LARAVEL_MAIL_ERROR by checking mail config, verifying SMTP settings, handling queue failures, and testing mail driver. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 127
---

# PHP LARAVEL_MAIL_ERROR — Email Sending Failed

An email sending operation failed in Laravel. This error occurs when mail configuration is incorrect, SMTP settings are wrong, or the mail driver is unavailable.

## Common Causes

```php
// Wrong SMTP credentials
// config/mail.php
'mailers' => [
    'smtp' => [
        'host' => env('MAIL_HOST', 'smtp.mailtrap.io'),
        'port' => env('MAIL_PORT', 587),
        'encryption' => env('MAIL_ENCRYPTION', 'tls'),
        'username' => env('MAIL_USERNAME'), // null or wrong
        'password' => env('MAIL_PASSWORD'), // null or wrong
    ],
],
```

```php
// Mail driver not configured
MAIL_DRIVER=log // but trying to send via SMTP
```

```php
// Invalid email address
Mail::to('invalid-email')->send($email); // missing @
```

```php
// Email exceeds size limit
// Attachment too large for SMTP server
$email->attach('/path/to/large-file.zip'); // 50MB file
```

```php
// Queue driver not available
Mail::to($user)->queue(new WelcomeMail($user));
// But QUEUE_CONNECTION=sync with no queue worker running
```

## How to Fix

### Fix 1: Configure Mail Settings

```env
# .env file
MAIL_MAILER=smtp
MAIL_HOST=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_ENCRYPTION=tls
MAIL_FROM_ADDRESS="your-email@gmail.com"
MAIL_FROM_NAME="${APP_NAME}"
```

```php
// config/mail.php
'mailers' => [
    'smtp' => [
        'transport' => 'smtp',
        'host' => env('MAIL_HOST', 'smtp.gmail.com'),
        'port' => env('MAIL_PORT', 587),
        'encryption' => env('MAIL_ENCRYPTION', 'tls'),
        'username' => env('MAIL_USERNAME'),
        'password' => env('MAIL_PASSWORD'),
        'timeout' => null,
        'local_domain' => env('MAIL_EHLO_DOMAIN', parse_url(env('APP_URL', 'http://localhost'), PHP_URL_HOST)),
    ],

    'ses' => [
        'transport' => 'ses',
    ],

    'mailgun' => [
        'transport' => 'mailgun',
    ],

    'postmark' => [
        'transport' => 'postmark',
    ],

    'sendmail' => [
        'transport' => 'sendmail',
        'path' => env('MAIL_SENDMAIL_PATH', '/usr/sbin/sendmail -bs -i'),
    ],

    'log' => [
        'transport' => 'log',
        'channel' => env('MAIL_LOG_CHANNEL'),
    ],
],
```

### Fix 2: Test Mail Configuration

```bash
# Test mail sending
php artisan tinker

# In Tinker
Mail::raw('Test email', function ($message) {
    $message->to('test@example.com')
            ->subject('Test Email');
});

# Or with mailable
$user = App\Models\User::first();
Mail::to($user)->send(new App\Mail\WelcomeMail($user));

# Check mail queue
php artisan mail:send

# Verify SMTP connection
php artisan tinker
>>> config('mail.mailers.smtp')
```

### Fix 3: Create Proper Mailable

```php
// app/Mail/WelcomeMail.php
namespace App\Mail;

use App\Models\User;
use Illuminate\Bus\Queueable;
use Illuminate\Mail\Mailable;
use Illuminate\Mail\Mailables\Content;
use Illuminate\Mail\Mailables\Envelope;
use Illuminate\Queue\SerializesModels;

class WelcomeMail extends Mailable
{
    use Queueable, SerializesModels;

    public function __construct(
        public User $user,
    ) {}

    public function envelope(): Envelope
    {
        return new Envelope(
            subject: "Welcome {$this->user->name}!",
            from: config('mail.from.address'),
        );
    }

    public function content(): Content
    {
        return new Content(
            markdown: 'emails.welcome',
            with: [
                'loginUrl' => url('/login'),
            ],
        );
    }

    public function attachments(): array
    {
        return [];
    }
}

// In controller
Mail::to($user->email)->send(new WelcomeMail($user));
```

### Fix 4: Handle Queue Failures

```php
// Queue mail instead of sending immediately
Mail::to($user)->queue(new WelcomeMail($user));

// With delay
Mail::to($user)->later(60, new WelcomeMail($user));

// With specific queue
Mail::to($user)->queue(new WelcomeMail($user), ['queue' => 'emails']);

// Check failed jobs
php artisan queue:failed

// Retry failed job
php artisan queue:retry {job-id}

// Retry all failed jobs
php artisan queue:retry all

// Clear failed jobs
php artisan queue:flush
```

```php
// Handle mail sending errors
use Illuminate\Support\Facades\Mail;
use Illuminate\Mail\MailingException;

try {
    Mail::to($user->email)->send(new WelcomeMail($user));
} catch (MailingException $e) {
    Log::error("Mail failed: {$e->getMessage()}");
    // Fallback: try different driver
    config(['mail.mailers.smtp.host' => 'smtp.backup.com']);
    Mail::to($user->email)->send(new WelcomeMail($user));
}
```

## Examples

```php
// Complete mail example
class NotificationController extends Controller
{
    public function sendWelcome(User $user)
    {
        try {
            Mail::to($user->email)->send(new WelcomeMail($user));

            return response()->json(['message' => 'Email sent successfully']);
        } catch (\Exception $e) {
            Log::error("Failed to send email to {$user->email}: {$e->getMessage()}");
            return response()->json(['error' => 'Failed to send email'], 500);
        }
    }

    public function sendBulk()
    {
        $users = User::where('subscribed', true)->get();

        foreach ($users as $user) {
            Mail::to($user->email)
                ->queue(new NewsletterMail($user));
        }

        return response()->json(['message' => 'Emails queued']);
    }

    public function sendWithAttachment(Order $order)
    {
        $invoice = $this->generateInvoice($order);

        Mail::to($order->user->email)
            ->send(new InvoiceMail($order, $invoice));
    }
}
```

```blade
{{-- resources/views/emails/welcome.blade.php --}}
<x-mail::message>
# Welcome, {{ $user->name }}!

Thank you for joining {{ config('app.name') }}.

Your account has been created successfully.

<x-mail::button :url="$loginUrl">
Login to Your Account
</x-mail::button>

Thanks,<br>
{{ config('app.name') }}
</x-mail::message>
```

## Related Errors

- [Swift Mailer Error](/languages/php/swift-mailer-error)
- [PHPMailer Error](/languages/php/phpmailer-error)
- [Curl Connection Error](/languages/php/curl-connection-error)
- [Symfony Messenger Error](/languages/php/symfony-messenger-error)
