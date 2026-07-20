---
title: "[Solution] aes-gcm Decrypt Error Fix"
description: "Fix AES-GCM decryption errors. Handle key size, nonce, and authentication tag issues."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# AES-GCM Error

AES-GCM errors occur when using the `aes-gcm` crate for authenticated encryption — invalid key lengths, nonce reuse, authentication failures, and tag verification errors.

## Common Causes

```rust
use aes_gcm::{Aes256Gcm, Key, Nonce};
use aes_gcm::aead::Aead;

// Invalid key length
let key = Key::<Aes256Gcm>::from_slice(b"short"); // ERROR: must be 32 bytes

// Nonce reuse — catastrophic for security
let nonce = Nonce::from_slice(b"unique nonce 12");
let cipher1 = Aes256Gcm::new(key);
let cipher2 = Aes256Gcm::new(key);
// Using same nonce with different messages breaks security

// Authentication failure — wrong key for decryption
let plaintext = cipher.decrypt(nonce, ciphertext.as_ref()); // Err if wrong key
```

## How to Fix

1. **Use correct key sizes**

```rust
use aes_gcm::{Aes256Gcm, Key};
use aes_gcm::aead::OsRng;
use aes_gcm::aead::rand_core::RngCore;

// Generate a random 256-bit key
let key = Aes256Gcm::generate_key(&mut OsRng);
let cipher = Aes256Gcm::new(&key);

// Or from bytes (must be exactly 32 bytes)
let key = Key::<Aes256Gcm>::from_slice(&[0u8; 32]);
let cipher = Aes256Gcm::new(key);
```

2. **Generate unique nonces for each encryption**

```rust
use aes_gcm::{Aes256Gcm, Nonce, Key};
use aes_gcm::aead::Aead;
use aes_gcm::aead::OsRng;
use aes_gcm::aead::rand_core::RngCore;

let key = Aes256Gcm::generate_key(&mut OsRng);
let cipher = Aes256Gcm::new(&key);

let mut nonce_bytes = [0u8; 12];
OsRng.fill_bytes(&mut nonce_bytes);
let nonce = Nonce::from_slice(&nonce_bytes);

let ciphertext = cipher.encrypt(nonce, b"secret message".as_ref()).unwrap();
```

3. **Verify authentication on decryption**

```rust
use aes_gcm::{Aes256Gcm, Key, Nonce};
use aes_gcm::aead::Aead;

let key = Key::<Aes256Gcm>::from_slice(&[0u8; 32]);
let cipher = Aes256Gcm::new(key);
let nonce = Nonce::from_slice(b"unique nonce 12");

let plaintext = cipher.decrypt(nonce, ciphertext.as_ref());
match plaintext {
    Ok(msg) => println!("Decrypted: {}", String::from_utf8_lossy(&msg)),
    Err(_) => eprintln!("Decryption failed — wrong key or tampered data"),
}
```

## Examples

```rust
use aes_gcm::{Aes256Gcm, Key, Nonce};
use aes_gcm::aead::{Aead, NewAead, OsRng, rand_core::RngCore};

fn encrypt(key: &[u8; 32], plaintext: &[u8]) -> (Vec<u8>, [u8; 12]) {
    let cipher = Aes256Gcm::new(Key::from_slice(key));
    let mut nonce_bytes = [0u8; 12];
    OsRng.fill_bytes(&mut nonce_bytes);
    let nonce = Nonce::from_slice(&nonce_bytes);
    let ciphertext = cipher.encrypt(nonce, plaintext).unwrap();
    (ciphertext, nonce_bytes)
}

fn decrypt(key: &[u8; 32], nonce: &[u8; 12], ciphertext: &[u8]) -> Option<Vec<u8>> {
    let cipher = Aes256Gcm::new(Key::from_slice(key));
    cipher.decrypt(Nonce::from_slice(nonce), ciphertext).ok()
}

fn main() {
    let key = [0u8; 32]; // In production, use a real key
    let (ciphertext, nonce) = encrypt(&key, b"Hello, AES-GCM!");
    println!("Ciphertext: {:02x?}", &ciphertext[..16]);
    let plaintext = decrypt(&key, &nonce, &ciphertext).unwrap();
    println!("Plaintext: {}", String::from_utf8_lossy(&plaintext));
}
```

## Related Errors

- [Ring Error]({{< relref "/languages/rust/ring-error" >}}) — cryptographic operations
- [Chacha20poly1305 Error]({{< relref "/languages/rust/chacha20poly1305-error" >}}) — AEAD encryption
- [HMAC Error]({{< relref "/languages/rust/hmac-error" >}}) — MAC operations
