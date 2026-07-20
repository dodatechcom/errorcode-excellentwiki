---
title: "[Solution] yubico HSM Error Fix"
description: "Fix yubico HSM errors. Handle device communication, PIV operations, and key management."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# yubico HSM Error

The `yubico` crate provides an interface to YubiKey hardware security modules (HSMs) for PIV (Personal Identity Verification) operations. Errors occur when the YubiKey is not detected, when PIV slot operations fail, when PIN verification fails, or when the device is locked after too many incorrect PIN attempts.

## Common Causes

```rust
// 1. YubiKey not detected — USB device not connected or not recognised
// let device = yubico::get_yubikey()?;
// Fails with "No YubiKey found" if not plugged in

// 2. Wrong PIN — PIV has a 3-attempt lockout
// After 3 wrong PINs, the PIV applet is locked
// Requires PUK to reset

// 3. Wrong slot — PIV has specific slot usage
// Slot 9a: PIV Authentication (cert-based auth)
// Slot 9c: Digital Signature
// Using wrong slot for the operation

// 4. Device permissions — USB device requires root or udev rules
// On Linux: /dev/hidraw* must be accessible
```

## How to Fix

1. **Set up udev rules for YubiKey access on Linux**

```bash
# /etc/udev/rules.d/70-yubikey.rules
# Allow user access to YubiKey HID devices
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="1050", ATTRS{idProduct}=="0407", MODE="0666"
SUBSYSTEM=="usb", ATTRS{idVendor}=="1050", ATTRS{idProduct}=="0407", MODE="0666"

# Reload rules
sudo udevadm control --reload-rules
sudo udevadm trigger
```

2. **Handle PIN verification with retry logic**

```rust
use yubico::yubikey::YubiKey;

fn authenticate_with_pin(yk: &mut YubiKey, pin: &str) -> Result<(), Box<dyn std::error::Error>> {
    match yk.verify_pin(pin.as_bytes()) {
        Ok(()) => {
            println!("PIN verified");
            Ok(())
        }
        Err(e) => {
            eprintln!("PIN verification failed: {}", e);
            eprintln!("WARNING: 3 failed attempts locks the PIV applet!");
            Err(e.into())
        }
    }
}
```

3. **Select the correct PIV slot for your operation**

```rust
use yubico::yubikey::{YubiKey, Slot};

fn sign_data(yk: &mut YubiKey, data: &[u8]) -> Result<Vec<u8>, Box<dyn std::error::Error>> {
    // Slot 9c is for digital signatures
    let signature = yk.sign_data(data, Slot::Signature)?;
    Ok(signature)
}
```

4. **Reset a locked YubiKey with PUK**

```rust
// If PIN is locked (3 failed attempts), use PUK to reset
// WARNING: This requires knowing the PUK (default: 12345678)
use yubico::yubikey::YubiKey;

// Reset requires physical touch on the YubiKey
// yk.verify_puk(puk.as_bytes())?;
// yk.set_pin(new_pin.as_bytes())?;
```

## Examples

```rust
use yubico::yubikey::YubiKey;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut yk = YubiKey::open()?;
    println!("YubiKey detected: serial {}", yk.serial());

    // Verify PIN
    yk.verify_pin(b"123456")?;

    // Read certificate from slot 9a
    let cert = yk.read_certificate(Slot::Authentication)?;
    println!("Certificate: {} bytes", cert.len());

    // Sign data
    let data = b"message to sign";
    let signature = yk.sign_data(data, Slot::Signature)?;
    println!("Signature: {} bytes", signature.len());

    Ok(())
}
```

## Related Errors

- [Keyring Error]({{< relref "/languages/rust/keyring-error" >}}) — credential storage
- [Ring Error]({{< relref "/languages/rust/ring-error" >}}) — crypto operations
- [WebAuthn RS Error]({{< relref "/languages/rust/webauthn-rs-error" >}}) — WebAuthn
