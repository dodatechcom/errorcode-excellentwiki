---
title: "Solved JavaScript nodemailer Error — How to Fix"
date: 2026-03-20T14:35:10+00:00
description: "Learn how to resolve JavaScript nodemailer email sending, SMTP, and transport errors."
categories: ["javascript"]
keywords: ["nodemailer error", "email error", "smtp error", "nodemailer transport", "mail error"]
error_types: ["runtime"]
severities: ["error"]
languages: ["javascript"]
weight: 5
comments: true
---

## Why It Happens

nodemailer errors occur when the email library encounters SMTP connection failures, authentication issues, or message formatting problems. Email delivery is sensitive to DNS, network, and server configuration.

Common causes include:
- SMTP server authentication failures
- Invalid email address format
- Attachment size exceeding server limits
- DNS resolution failures for mail server
- TLS/SSL certificate verification errors

## Common Error Messages

```
Error: Invalid login: Authentication failed
```

```
Error: Connection timeout
```

```
Error: Envelope address format incorrect
```

## How to Fix It

### 1. Configure nodemailer Transport

Set up email transport with proper SMTP settings.

```javascript
import nodemailer from "nodemailer";

// SMTP transport
const transporter = nodemailer.createTransport({
  host: process.env.SMTP_HOST || "smtp.gmail.com",
  port: parseInt(process.env.SMTP_PORT) || 587,
  secure: false, // true for 465, false for other ports
  auth: {
    user: process.env.SMTP_USER,
    pass: process.env.SMTP_PASS
  },
  tls: {
    rejectUnauthorized: true
  },
  connectionTimeout: 10000,
  greetingTimeout: 10000,
  socketTimeout: 10000
});

// Verify connection
async function verifyTransport() {
  try {
    await transporter.verify();
    console.log("SMTP connection verified");
    return true;
  } catch (error) {
    console.error("SMTP verification failed:", error.message);
    return false;
  }
}

// Send email
async function sendEmail(to, subject, html) {
  try {
    const info = await transporter.sendMail({
      from: `"MyApp" <${process.env.SMTP_FROM || process.env.SMTP_USER}>`,
      to,
      subject,
      html,
      text: html.replace(/<[^>]*>/g, ""), // Plain text fallback
      headers: {
        "X-Priority": "1",
        "X-MSMail-Priority": "High"
      }
    });
    
    console.log("Message sent:", info.messageId);
    return info;
  } catch (error) {
    console.error("Email send failed:", error.message);
    throw error;
  }
}
```

### 2. Handle Attachments

Send emails with file attachments.

```javascript
import nodemailer from "nodemailer";

async function sendEmailWithAttachment(to, subject, html, filePaths = []) {
  const attachments = filePaths.map(path => ({
    filename: path.split("/").pop(),
    path
  }));
  
  return transporter.sendMail({
    from: process.env.SMTP_FROM,
    to,
    subject,
    html,
    attachments
  });
}

// Inline images
async function sendRichEmail(to, subject, html, imageUrl) {
  return transporter.sendMail({
    from: process.env.SMTP_FROM,
    to,
    subject,
    html,
    alternatives: [{
      contentType: "text/html",
      content: html
    }],
    attachments: [{
      filename: "image.png",
      path: imageUrl,
      cid: "unique@image" // Same CID in img src
    }]
  });
}

// Stream attachment
import fs from "fs";

async function sendWithStreamAttachment(to, subject, stream, filename) {
  return transporter.sendMail({
    from: process.env.SMTP_FROM,
    to,
    subject,
    text: "Please see attached file",
    attachments: [{
      filename,
      content: stream
    }]
  });
}
```

### 3. Use Multiple Transports

Configure failover and testing transports.

```javascript
import nodemailer from "nodemailer";

// Primary SMTP
const primaryTransport = nodemailer.createTransport({
  host: "smtp.company.com",
  port: 587,
  auth: { user: "user", pass: "pass" }
});

// Backup SMTP
const backupTransport = nodemailer.createTransport({
  host: "smtp-backup.company.com",
  port: 587,
  auth: { user: "user", pass: "pass" }
});

// Development transport (logs to console)
const testTransport = nodemailer.createTransport({
  jsonTransport: true
});

// Send with fallback
async function sendWithFallback(mailOptions) {
  try {
    return await primaryTransport.sendMail(mailOptions);
  } catch (primaryError) {
    console.error("Primary transport failed:", primaryError.message);
    
    try {
      return await backupTransport.sendMail(mailOptions);
    } catch (backupError) {
      console.error("Backup transport also failed:", backupError.message);
      throw new Error("All email transports failed");
    }
  }
}

// Development mode
async function sendEmail(to, subject, html) {
  const transport = process.env.NODE_ENV === "production" 
    ? primaryTransport 
    : testTransport;
  
  return transport.sendMail({
    from: "dev@example.com",
    to,
    subject,
    html
  });
}
```

## Common Scenarios

### Scenario 1: Transactional Emails

Send welcome emails, password resets, etc.:

```javascript
import nodemailer from "nodemailer";

const templates = {
  welcome: (name) => `
    <h1>Welcome, ${name}!</h1>
    <p>Thank you for joining our platform.</p>
  `,
  
  resetPassword: (token) => `
    <h1>Password Reset</h1>
    <p>Click <a href="https://app.com/reset?token=${token}">here</a> to reset your password.</p>
    <p>This link expires in 1 hour.</p>
  `
};

async function sendWelcomeEmail(user) {
  return transporter.sendMail({
    from: "welcome@myapp.com",
    to: user.email,
    subject: "Welcome to MyApp!",
    html: templates.welcome(user.name)
  });
}

async function sendPasswordReset(user, token) {
  return transporter.sendMail({
    from: "security@myapp.com",
    to: user.email,
    subject: "Password Reset Request",
    html: templates.resetPassword(token)
  });
}
```

## Prevent It

- Always verify SMTP connection before sending emails in production
- Use `secure: true` (port 465) for encrypted connections
- Implement retry logic for temporary SMTP failures
- Set appropriate timeouts to handle slow SMTP servers
- Test email sending with Ethereal (https://ethereal.email) during development