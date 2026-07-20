---
title: "[Solution] PHPMailer Sending Error Fix"
description: "Fix PHPMailer SMTP errors. Check SMTP configuration, verify server connection, handle authentication, use proper encoding."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1116
---

# PHPMailer Sending Error

PHPMailer errors occur when email sending fails due to SMTP connection issues, authentication failures, invalid recipient addresses, or misconfigured transport settings. These errors typically throw `phpmailerException` with detailed error messages.

## Common Causes

```php
<?php
// Cause 1: SMTP server unreachable
$mail->isSMTP();
$mail->Host = 'smtp.example.com'; // Server down or wrong hostname

// Cause 2: Authentication failure
$mail->Username = 'user@example.com';
$mail->Password = 'wrong-password';

// Cause 3: Invalid recipient address
$mail->addAddress('invalid-email'); // Missing @ or domain

// Cause 4: Missing SMTP configuration
$mail->isSMTP(); // Marked as SMTP but no Host set

// Cause 5: SSL/TLS configuration mismatch
$mail->SMTPSecure = PHPMailer::ENCRYPTION_SMTPS; // Port 465
$mail->Port = 587; // But port is for STARTTLS

// Cause 6: Attachment file doesn't exist
$mail->addAttachment('/path/to/file.pdf'); // File not found
```

## How to Fix

### Fix 1: Configure SMTP properly

```php
<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;
use PHPMailer\PHPMailer\Exception;

require 'vendor/autoload.php';

$mail = new PHPMailer(true);

try {
    // SMTP configuration
    $mail->isSMTP();
    $mail->Host       = 'smtp.gmail.com';
    $mail->SMTPAuth   = true;
    $mail->Username   = 'your-email@gmail.com';
    $mail->Password   = 'your-app-password';
    $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
    $mail->Port       = 587;

    // Recipients
    $mail->setFrom('from@example.com', 'Sender');
    $mail->addAddress('recipient@example.com', 'Recipient');

    // Content
    $mail->isHTML(true);
    $mail->Subject = 'Test Email';
    $mail->Body    = '<h1>Hello</h1><p>This is a test.</p>';

    $mail->send();
    echo 'Message sent successfully';
} catch (Exception $e) {
    echo "Message could not be sent.Mailer Error: {$mail->ErrorInfo}";
}
```

### Fix 2: Verify SMTP credentials and test connection

```php
<?php
// Test SMTP connection before sending
$mail = new PHPMailer(true);

$mail->isSMTP();
$mail->Host = 'smtp.example.com';
$mail->SMTPAuth = true;
$mail->Username = 'user@example.com';
$mail->Password = 'password';
$mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
$mail->Port = 587;

try {
    $mail->smtpConnect();
    echo "SMTP connection successful\n";
    $mail->smtpClose();
} catch (Exception $e) {
    echo "Connection failed: {$e->getMessage()}\n";
    // Debug: check credentials, firewall, DNS
}
```

### Fix 3: Validate email addresses before sending

```php
<?php
// Validate before adding recipients
function validateEmail(string $email): bool
{
    return filter_var($email, FILTER_VALIDATE_EMAIL) !== false;
}

$recipients = ['valid@example.com', 'invalid-email', 'another@domain.com'];

foreach ($recipients as $email) {
    if (validateEmail($email)) {
        $mail->addAddress($email);
    } else {
        error_log("Invalid email skipped: $email");
    }
}
```

### Fix 4: Handle attachments properly

```php
<?php
// Verify file exists before attaching
$filePath = '/path/to/attachment.pdf';

if (file_exists($filePath)) {
    $mail->addAttachment($filePath, 'document.pdf');
} else {
    error_log("Attachment not found: $filePath");
    // Optionally throw or skip
}

// For multiple attachments
$attachments = [
    '/path/to/file1.pdf' => 'Document1.pdf',
    '/path/to/file2.pdf' => 'Document2.pdf',
];

foreach ($attachments as $path => $name) {
    if (file_exists($path)) {
        $mail->addAttachment($path, $name);
    }
}
```

### Fix 5: Configure for different email providers

```php
<?php
// Gmail SMTP
$mail->Host     = 'smtp.gmail.com';
$mail->Port     = 587;
$mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;

// Outlook/Office365
$mail->Host     = 'smtp.office365.com';
$mail->Port     = 587;
$mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;

// Amazon SES
$mail->Host     = 'email-smtp.us-east-1.amazonaws.com';
$mail->Port     = 587;
$mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;

// Local Mailhog (development)
$mail->Host     = '127.0.0.1';
$mail->Port     = 1025;
$mail->SMTPAuth = false;
$mail->SMTPAutoTLS = false;
```

## Examples

```php
<?php
// Complete email sending example with error handling

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;
use PHPMailer\PHPMailer\Exception;

function sendEmail(array $config, string $to, string $subject, string $body): bool
{
    $mail = new PHPMailer(true);

    try {
        $mail->isSMTP();
        $mail->Host       = $config['host'];
        $mail->SMTPAuth   = true;
        $mail->Username   = $config['username'];
        $mail->Password   = $config['password'];
        $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
        $mail->Port       = $config['port'] ?? 587;

        $mail->setFrom($config['from'], $config['from_name']);
        $mail->addAddress($to);

        $mail->isHTML(true);
        $mail->Subject = $subject;
        $mail->Body    = $body;
        $mail->AltBody = strip_tags($body);

        $mail->send();
        return true;
    } catch (Exception $e) {
        error_log("PHPMailer error: {$mail->ErrorInfo}");
        return false;
    }
}
```

## Related Errors

- [SwiftMailer Error]({{< relref "/languages/php/swift-mailer-error" >}}) — alternative mailer
- [Warning Mail Failed]({{< relref "/languages/php/warning-mail-failed" >}}) — native mail() failure
- [Laravel Mail Error]({{< relref "/languages/php/laravel-mail-error" >}}) — Laravel mail issues
