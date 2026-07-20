---
title: "[Solution] PHP Warning: mail() — SMTP Server Response / Mail Sending Failed"
description: "Fix PHP Warning: mail() SMTP server response error. Check SMTP configuration, verify mail settings, test mail server connectivity."
languages: ["php"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 10
---

# PHP Warning: mail() — SMTP Server Response / Mail Sending Failed

This warning occurs when PHP's `mail()` function fails to send an email through the configured SMTP server. The message was handed off to the mail transfer agent (MTA) but the server rejected it or could not deliver it.

## Common Causes

```php
<?php
// Example 1: mail() with no SMTP configuration
$result = mail("user@example.com", "Subject", "Body");
// Warning: mail(): SMTP server response: 550 5.1.1 User unknown
```

```php
<?php
// Example 2: Invalid sender address
ini_set("sendmail_path", "/usr/sbin/sendmail -t -f invalid-email");
mail("user@example.com", "Subject", "Body");
// Warning: mail(): SMTP server response: 553 Sender address rejected
```

```php
<?php
// Example 3: SMTP server not running
// When using SMTP directly instead of sendmail
mail("user@example.com", "Subject", "Body");
// Warning: mail(): SMTP server connection failed
```

```php
<?php
// Example 4: Missing From header
$headers = "From: \r\n"; // Empty From header
mail("user@example.com", "Subject", "Body", $headers);
// Warning: mail(): SMTP server response: 553 Mail from not allowed
```

```php
<?php
// Example 5: Message too large for server limits
$hugeBody = str_repeat("A", 10 * 1024 * 1024); // 10MB body
mail("user@example.com", "Subject", $hugeBody);
// Warning: mail(): Message size exceeds server limit
```

## How to Fix

### Fix 1: Configure sendmail_path Correctly

Ensure PHP knows where to find the mail transfer agent.

```ini
; php.ini
sendmail_path = /usr/sbin/sendmail -t -i
```

```php
<?php
// Verify configuration at runtime
$sendmailPath = ini_get("sendmail_path");
if (empty($sendmailPath)) {
    throw new \RuntimeException("sendmail_path is not configured in php.ini");
}
```

### Fix 2: Set a Valid From Address

Always provide a valid sender address in the headers.

```php
<?php
$to = "recipient@example.com";
$subject = "Welcome";
$message = "Hello!";
$headers = "From: noreply@excellentwiki.com\r\n";
$headers .= "Reply-To: support@excellentwiki.com\r\n";
$headers .= "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

$result = mail($to, $subject, $message, $headers);
if (!$result) {
    error_log("Mail failed to send to {$to}");
}
```

### Fix 3: Use PHPMailer or Symfony Mailer for SMTP

For reliable email delivery, use a library that supports SMTP authentication.

```php
<?php
use PHPMailer\PHPMailer\PHPMailer;

$mail = new PHPMailer(true);
$mail->isSMTP();
$mail->Host = "smtp.example.com";
$mail->SMTPAuth = true;
$mail->Username = "user@example.com";
$mail->Password = "secure_password";
$mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
$mail->Port = 587;

$mail->setFrom("noreply@example.com", "My App");
$mail->addAddress("recipient@example.com");
$mail->Subject = "Welcome";
$mail->Body = "Hello!";

$mail->send();
```

### Fix 4: Test Mail Server Connectivity

Verify the mail server is reachable before attempting to send.

```php
<?php
function testSmtpConnection(string $host, int $port, int $timeout = 5): bool {
    $fp = @fsockopen($host, $port, $errno, $errstr, $timeout);
    if ($fp === false) {
        error_log("SMTP connection failed: {$host}:{$port} — {$errstr} ({$errno})");
        return false;
    }
    fclose($fp);
    return true;
}

if (!testSmtpConnection("smtp.example.com", 587)) {
    throw new \RuntimeException("SMTP server unreachable");
}
```

## Examples

```php
<?php
// Complete mail sending with error handling
function sendEmail(string $to, string $subject, string $body, array $attachments = []): bool {
    $headers = [
        "From: noreply@excellentwiki.com",
        "Reply-To: support@excellentwiki.com",
        "MIME-Version: 1.0",
        "Content-Type: text/plain; charset=UTF-8",
        "X-Mailer: PHP/" . phpversion(),
    ];

    $headerString = implode("\r\n", $headers);

    // Validate email format
    if (!filter_var($to, FILTER_VALIDATE_EMAIL)) {
        throw new \InvalidArgumentException("Invalid email address: {$to}");
    }

    $result = @mail($to, $subject, $body, $headerString);

    if (!$result) {
        $error = error_get_last();
        error_log("Mail failed: " . ($error["message"] ?? "Unknown error"));
        return false;
    }

    return true;
}

sendEmail("user@example.com", "Welcome", "Hello from ExcellentWiki!");
```

## Related Errors

- [PHP Warning: Headers Already Sent](/languages/php/warning-headers-sent-already)
- [PHP Swift Mailer Error](/languages/php/swift-mailer-error)
- [PHPMailer Error](/languages/php/phpmailer-error)
