---
title: "[Solution] Django Email Sending Failed Error — How to Fix"
description: "Fix Django email sending errors. Resolve SMTP connection failures, email delivery, and email configuration issues."
frameworks: ["django"]
error-types": ["connection-error"]
severities: ["error"]
weight: 5
comments: true
---

A Django email sending failed error occurs when the application cannot connect to the SMTP server, authenticate, or deliver email messages. This affects password resets, notifications, and any automated email functionality.

## Why It Happens

Django uses Python's `smtplib` to send emails via SMTP. Errors occur when SMTP server settings are incorrect, authentication fails, the connection times out, TLS/SSL configuration is wrong, the sender address is rejected by the server, or when rate limits are exceeded.

## Common Error Messages

```
smtplib.SMTPAuthenticationError: (535, b'Authentication Failed')
```

```
ConnectionRefusedError: [Errno 111] Connection refused
```

```
smtplib.SMTPRecipientsRefused: {'user@example.com': (550, b'User unknown')}
```

```
OSError: [Errno 110] Connection timed out
```

## How to Fix It

### 1. Configure Email Settings Correctly

Set up email backend with proper SMTP parameters:

```python
# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'  # Use app password for Gmail
DEFAULT_FROM_EMAIL = 'MyApp <noreply@myapp.com>'
EMAIL_TIMEOUT = 30

# For local development
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

### 2. Test Email Sending

Verify email configuration with a test:

```python
# In Django shell
from django.core.mail import send_mail, send_mass_mail
from django.conf import settings

# Simple test
result = send_mail(
    subject='Test Email',
    message='This is a test email from Django.',
    from_email=settings.DEFAULT_FROM_EMAIL,
    recipient_list=['recipient@example.com'],
    fail_silently=False,
)
print(f"Emails sent: {result}")

# Test with HTML content
from django.core.mail import EmailMultiAlternatives

msg = EmailMultiAlternatives(
    subject='HTML Email',
    body='This is the plain text body.',
    from_email=settings.DEFAULT_FROM_EMAIL,
    to=['recipient@example.com'],
)
msg.attach_alternative(
    '<h1>HTML Email</h1><p>This is the HTML body.</p>',
    'text/html'
)
msg.send()
```

### 3. Handle Email Failures Gracefully

Add error handling for email operations:

```python
import logging
from django.core.mail import send_mail
from django.conf import settings

logger = logging.getLogger(__name__)

def send_notification_email(user, subject, message):
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False,
        )
        logger.info(f"Email sent to {user.email}: {subject}")
        return True
    except smtplib.SMTPAuthenticationError as e:
        logger.error(f"SMTP authentication failed: {e}")
        return False
    except smtplib.SMTPException as e:
        logger.error(f"SMTP error sending to {user.email}: {e}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error sending email: {e}")
        return False
```

### 4. Use Async Email for Performance

Send emails asynchronously to avoid blocking the request:

```python
# Option 1: Use Django's EmailMessage
from django.core.mail import EmailMultiAlternatives

def send_welcome_email(user):
    msg = EmailMultiAlternatives(
        subject='Welcome to MyApp',
        body=f'Hello {user.first_name}, welcome to MyApp!',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email],
    )
    msg.send(fail_silently=True)

# Option 2: Use Celery for async email
from celery import shared_task

@shared_task
def send_email_task(subject, message, recipient_list):
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=recipient_list,
    )

# Usage
send_email_task.delay(
    subject='Welcome',
    message='Hello!',
    recipient_list=[user.email],
)
```

## Common Scenarios

**Scenario 1: Gmail blocks login attempts.**
Gmail requires "App Passwords" for less secure apps. Generate an app password in your Google account settings and use it instead of your regular password.

**Scenario 2: Emails work in development but not production.**
Production servers may block outbound SMTP connections. Check firewall rules, use a transactional email service (SendGrid, Mailgun), or configure the server's mail relay.

**Scenario 3: Emails arrive in spam folder.**
Set up SPF, DKIM, and DMARC DNS records for your domain. Use a consistent `From` address and avoid spam trigger words in subjects.

## Prevent It

1. **Always use `fail_silently=False` in development** to catch email errors immediately. Switch to `fail_silently=True` only for non-critical notifications in production.

2. **Use a dedicated email service for production.** Services like SendGrid, Mailgun, or Amazon SES handle deliverability, rate limiting, and bounce management.

3. **Log all email attempts.** Keep a record of sent emails for debugging and compliance purposes.
