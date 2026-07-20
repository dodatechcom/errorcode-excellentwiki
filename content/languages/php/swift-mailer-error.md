---
title: "[Solution] SwiftMailer Transport Error Fix"
description: "Fix SwiftMailer transport errors. Check transport config, verify SMTP settings, handle attachment issues."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1117
---

# SwiftMailer Transport Error

SwiftMailer transport errors occur when the mail transport cannot connect, authenticate, or deliver emails. SwiftMailer (now deprecated in favor of Symfony Mailer) throws `TransportException` for connection and delivery failures. These errors typically stem from misconfigured SMTP settings or network issues.

## Common Causes

```php
<?php
// Cause 1: SMTP transport misconfigured
$transport = (new Swift_SmtpTransport('smtp.example.com', 587, 'tls'))
    ->setUsername('user@example.com')
    ->setPassword('wrong-password');

// Cause 2: Connection timeout
$transport = new Swift_SmtpTransport('smtp.example.com', 587, 'tls');
// Server unreachable or firewall blocking

// Cause 3: Invalid sender/recipient address
$message = (new Swift_Message())
    ->setFrom('invalid-email')  // Missing @
    ->setTo('invalid-recipient');

// Cause 4: Attachment file not found
$message->attach(
    Swift_Attachment::fromPath('/nonexistent/file.pdf')
);

// Cause 5: Memory limit exceeded with large attachments
$message->attach(
    Swift_Attachment::fromPath('/path/to/large-file.zip') // > memory_limit
);
```

## How to Fix

### Fix 1: Configure SMTP transport correctly

```php
<?php
require 'vendor/autoload.php';

// Create SMTP transport
$transport = (new Swift_SmtpTransport('smtp.gmail.com', 587, 'tls'))
    ->setUsername('your-email@gmail.com')
    ->setPassword('your-app-password');

// Create mailer
$mailer = new Swift_Mailer($transport);

// Create message
$message = (new Swift_Message('Subject'))
    ->setFrom('your-email@gmail.com', 'Your Name')
    ->setTo('recipient@example.com', 'Recipient Name')
    ->setBody('<h1>Hello</h1><p>This is HTML content.</p>', 'text/html')
    ->addPart('Plain text version', 'text/plain');

// Send
$result = $mailer->send($message);
if ($result) {
    echo "Email sent successfully\n";
} else {
    echo "Failed to send email\n";
}
```

### Fix 2: Test transport connection before sending

```php
<?php
// Verify SMTP connection
$transport = (new Swift_SmtpTransport('smtp.example.com', 587, 'tls'))
    ->setUsername('user@example.com')
    ->setPassword('password');

try {
    $transport->start();
    echo "Transport connected successfully\n";
    $transport->stop();
} catch (Swift_TransportException $e) {
    echo "Connection failed: {$e->getMessage()}\n";
}
```

### Fix 3: Handle large attachments properly

```php
<?php
// Check file size before attaching
$filePath = '/path/to/attachment.pdf';
$fileSize = filesize($filePath);

if ($fileSize === false) {
    throw new \RuntimeException("Cannot read file: $filePath");
}

$maxSize = 25 * 1024 * 1024; // 25MB
if ($fileSize > $maxSize) {
    throw new \RuntimeException("File too large: $fileSize bytes");
}

$message->attach(
    Swift_Attachment::fromPath($filePath)
        ->setFilename('document.pdf')
);
```

### Fix 4: Configure for different providers

```php
<?php
// Gmail
$transport = (new Swift_SmtpTransport('smtp.gmail.com', 587, 'tls'))
    ->setUsername('user@gmail.com')
    ->setPassword('app-password');

// Outlook
$transport = (new Swift_SmtpTransport('smtp.office365.com', 587, 'tls'))
    ->setUsername('user@outlook.com')
    ->setPassword('password');

// Amazon SES
$transport = (new Swift_SmtpTransport('email-smtp.us-east-1.amazonaws.com', 587, 'tls'))
    ->setUsername('SMTP_USERNAME')
    ->setPassword('SMTP_PASSWORD');

// Local development (Mailhog/Mailpit)
$transport = new Swift_SmtpTransport('127.0.0.1', 1025);
// No authentication needed for local dev
```

### Fix 5: Add error handling for delivery failures

```php
<?php
// Comprehensive error handling
$message = (new Swift_Message('Test'))
    ->setFrom('sender@example.com')
    ->setTo('recipient@example.com')
    ->setBody('Hello!');

try {
    $result = $mailer->send($message, $failedRecipients);

    if ($result === 0) {
        error_log("No recipients were accepted");
        if (!empty($failedRecipients)) {
            error_log("Failed recipients: " . implode(', ', $failedRecipients));
        }
    }
} catch (Swift_TransportException $e) {
    error_log("Transport error: {$e->getMessage()}");
} catch (Swift_RfcComplianceException $e) {
    error_log("RFC compliance error: {$e->getMessage()}");
}
```

## Examples

```php
<?php
// Complete SwiftMailer usage example

use Swift_SmtpTransport;
use Swift_Mailer;
use Swift_Message;
use Swift_Attachment;

// Setup
$transport = (new Swift_SmtpTransport('smtp.example.com', 587, 'tls'))
    ->setUsername('user@example.com')
    ->setPassword('password');

$mailer = new Swift_Mailer($transport);

// Create message with attachment
$message = (new Swift_Message('Monthly Report'))
    ->setFrom('reports@example.com', 'System')
    ->setTo('admin@example.com')
    ->setBody(
        '<h1>Monthly Report</h1><p>Please find attached.</p>',
        'text/html'
    )
    ->addPart('Monthly report attached.', 'text/plain');

// Attach file with validation
$reportPath = '/tmp/report-' . date('Y-m') . '.pdf';
if (file_exists($reportPath)) {
    $message->attach(Swift_Attachment::fromPath($reportPath));
}

// Send with error handling
try {
    $mailer->send($message);
    echo "Report sent successfully\n";
} catch (Swift_TransportException $e) {
    error_log("Failed to send report: {$e->getMessage()}");
}
```

## Related Errors

- [PHPMailer Error]({{< relref "/languages/php/phpmailer-error" >}}) — PHPMailer errors
- [Warning Mail Failed]({{< relref "/languages/php/warning-mail-failed" >}}) — native mail failure
- [Laravel Mail Error]({{< relref "/languages/php/laravel-mail-error" >}}) — Laravel mail issues
