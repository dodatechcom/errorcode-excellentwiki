---
title: "[Solution] lettre SMTP Error Fix"
description: "Fix lettre SMTP errors. Handle email sending, authentication, and transport configuration."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Lettre Error

Lettre errors occur when using the `lettre` crate for email — SMTP connection failures and address parsing errors.

## Common Causes

```rust
// Invalid email address
let from = "invalid".parse::<Address>()?; // ERROR: not an email

// SMTP connection failure
let mailer = SmtpTransport::builder_dangerous("wrong.host").build();
```

## How to Fix

1. **Parse email addresses correctly**

```rust
use lettre::message::Address;

let from: Address = "sender@example.com".parse()?;
let to: Address = "recipient@example.com".parse()?;
```

2. **Configure SMTP transport with TLS**

```rust
use lettre::{SmtpTransport, Transport};
use lettre::transport::smtp::authentication::Credentials;

let creds = Credentials::new("user".into(), "password".into());
let mailer = SmtpTransport::relay("smtp.example.com")?
    .credentials(creds)
    .build();
```

3. **Handle transport errors**

```rust
match mailer.send(&message) {
    Ok(_) => println!("Email sent!"),
    Err(e) => eprintln!("Failed to send: {}", e),
}
```

## Examples

```rust
use lettre::{Message, SmtpTransport, Transport};
use lettre::transport::smtp::authentication::Credentials;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let message = Message::builder()
        .from("sender@example.com".parse()?)
        .to("recipient@example.com".parse()?)
        .subject("Test Email")
        .body("Hello from Rust!".to_string())?;

    let creds = Credentials::new("user".into(), "pass".into());
    let mailer = SmtpTransport::relay("smtp.example.com")?
        .credentials(creds)
        .build();
    mailer.send(&message)?;
    println!("Email sent!");
    Ok(())
}
```

## Related Errors

- [Connection Refused]({{< relref "/languages/rust/connection-refused" >}}) — SMTP server
- [Native TLS Error]({{< relref "/languages/rust/native-tls-error" >}}) — TLS issues
- [IO Error]({{< relref "/languages/rust/io-error" >}}) — network I/O
