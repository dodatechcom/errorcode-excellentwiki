---
title: "[Solution] macOS Mail Error -- Apple Mail Cannot Send or Receive"
description: "Fix macOS Mail error when Apple Mail cannot send or receive emails. Resolve Mail app connection and sync issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Mail Error -- Apple Mail Cannot Send or Receive

Apple Mail errors can prevent sending or receiving emails, show connection timeouts, or display authentication failures. These errors are often related to email server settings or account configuration.

## Common Causes
- Email account password has changed and Mail is using the old one
- SMTP or IMAP server settings are incorrect
- SSL certificate for the email server is not trusted
- Email account has been locked by the provider
- Mailbox is full on the email server

## How to Fix
1. Update the email account password in Mail preferences
2. Verify SMTP and IMAP server settings
3. Check that the email server's SSL certificate is trusted
4. Contact the email provider to check account status
5. Rebuild the mailbox to fix sync issues

```bash
# Check Mail app logs
log show --predicate 'process == "Mail"' --last 10m

# Rebuild mailbox
# Mail > Mailbox > Rebuild
```

## Examples

```bash
# Test SMTP connectivity from terminal
nc -zv smtp.gmail.com 587

# Test IMAP connectivity
nc -zv imap.gmail.com 993
```

This error is common after changing an email password without updating Mail settings, when the email provider changes their server configuration, or when an SSL certificate expires.
