---
title: "[Solution] chacha20poly1305 Decrypt Error Fix"
description: "Fix chacha20poly1305 decryption errors. Handle key/nonce issues, authentication tag verification, and AAD."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ChaCha20-Poly1305 Error

ChaCha20-Poly1305 errors occur when using the `chacha20poly1305` crate for AEAD encryption — key length issues, nonce reuse, and authentication failures.

## Common Causes

```rust
use chacha20poly1305::{ChaCha20Poly1305, Key, Nonce, aead::Aead};

// Wrong key size — must be 32 bytes
let key = Key::from_slice(b"short"); // ERROR: wrong length

// Nonce reuse breaks security
let nonce = Nonce::from_slice(b"12-byte nonce!!"); // 12 bytes required
// Reusing nonce with same key is catastrophic

// Authentication failure on wrong key
let plaintext = cipher.decrypt(nonce, ciphertext.as_ref()); // Err if wrong key
```

## How to Fix

1. **Generate correct-sized keys and nonces**

```rust
use chacha20poly1305::{ChaCha20Poly1305, Key};
use chacha20poly1305::aead::OsRng;
use chacha20poly1305::aead::rand_core::RngCore;

let key = ChaCha20Poly1305::generate_key(&mut OsRng);
let cipher = ChaCha20Poly1305::new(&key);

let mut nonce_bytes = [0u8; 12];
OsRng.fill_bytes(&mut nonce_bytes);
```

2. **Use unique nonces for each encryption**

```rust
use chacha20poly1305::{ChaCha20Poly1305, Nonce, Key};
use chacha20poly1305::aead::{Aead, OsRng, rand_core::RngCore};

let key = ChaCha20Poly1305::generate_key(&mut OsRng);
let cipher = ChaCha20Poly1305::new(&key);

let mut nonce = [0u8; 12];
OsRng.fill_bytes(&mut nonce);

let ciphertext = cipher.encrypt(Nonce::from_slice(&nonce), b"secret".as_ref()).unwrap();
```

3. **Verify authentication on decryption**

```rust
use chacha20poly1305::{ChaCha20Poly1305, Nonce, Key};
use chacha20poly1305::aead::Aead;

let key = Key::<ChaCha20Poly1305>::from_slice(&[0u8; 32]);
let cipher = ChaCha20Poly1305::new(key);
let nonce = Nonce::from_slice(b"unique nonce 12");

match cipher.decrypt(nonce, ciphertext.as_ref()) {
    Ok(plaintext) => println!("Decrypted: {}", String::from_utf8_lossy(&plaintext)),
    Err(_) => eprintln!("Authentication failed"),
}
```

## Examples

```rust
use chacha20poly1305::{ChaCha20Poly1305, Key, Nonce};
use chacha20poly1305::aead::{Aead, OsRng, rand_core::RngCore};

fn main() {
    let key = ChaCha20Poly1305::generate_key(&mut OsRng);
    let cipher = ChaCha20Poly1305::new(&key);

    let mut nonce = [0u8; 12];
    OsRng.fill_bytes(&mut nonce);

    let ciphertext = cipher.encrypt(Nonce::from_slice(&nonce), b"Hello, ChaCha!".as_ref()).unwrap();
    let plaintext = cipher.decrypt(Nonce::from_slice(&nonce), ciphertext.as_ref()).unwrap();
    println!("Decrypted: {}", String::from_utf8_lossy(&plaintext));
}
```

## Related Errors

- [AES-GCM Error]({{< relref "/languages/rust/aes-gcm-error" >}}) — AES-GCM encryption
- [Ring Error]({{< relref "/languages/rust/ring-error" >}}) — crypto operations
- [HMAC Error]({{< relref "/languages/rust/hmac-error" >}}) — MAC operations
