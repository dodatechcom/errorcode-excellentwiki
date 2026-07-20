---
title: "[Solution] uuid Parse Error Fix"
description: "Fix uuid parsing errors. Handle invalid format, version mismatch, and generation."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# uuid Parse Error

The `uuid` crate provides UUID generation and parsing (v1, v3, v4, v5). Errors occur when parsing UUID strings in invalid formats (missing hyphens, wrong length, non-hex characters), when using the wrong version variant, or when the UUID v1 timestamp is not monotonic without a `ClockSeq` configuration.

## Common Causes

```rust
use uuid::Uuid;

// 1. Invalid UUID string format
let id = Uuid::parse_str("not-a-uuid");
// Fails: doesn't match UUID format

// 2. Wrong length
let id = Uuid::parse_str("67e55044-10b1-426f-9247-bb680e5fe0c");
// Fails: 35 chars instead of 36 (missing last hex digit)

// 3. Non-hex characters
let id = Uuid::parse_str("67e55044-10b1-426f-9247-bb680e5fe0cg");
// Fails: 'g' is not a valid hex character

// 4. Using v4! macro with incorrect syntax
// uuid::uuid!("67e55044-10b1-426f-9247-bb680e5fe0c") // compile error if wrong
```

## How to Fix

1. **Parse UUIDs with proper error handling**

```rust
use uuid::Uuid;

fn parse_uuid(input: &str) -> Result<Uuid, uuid::Error> {
    Uuid::parse_str(input)
}

fn main() {
    match parse_uuid("67e55044-10b1-426f-9247-bb680e5fe0c8") {
        Ok(uuid) => println!("Valid UUID: {}", uuid),
        Err(e) => eprintln!("Invalid UUID: {}", e),
    }
}
```

2. **Generate UUIDs correctly for each version**

```rust
use uuid::{Uuid, v4::Uuid as V4Uuid};

// v4: random
let uuid = Uuid::new_v4();
println!("v4: {}", uuid);

// v5: SHA-1 hash-based (deterministic)
let uuid = Uuid::new_v5(&Uuid::NAMESPACE_DNS, "example.com");
println!("v5: {}", uuid);

// Compile-time v4
let uuid = uuid::uuid!("67e55044-10b1-426f-9247-bb680e5fe0c8");
```

3. **Convert between formats (hyphenated, simple, URN)**

```rust
use uuid::Uuid;

let uuid = Uuid::new_v4();

// Hyphenated: 67e55044-10b1-426f-9247-bb680e5fe0c8
println!("Hyphenated: {}", uuid.hyphenated());

// Simple: 67e5504410b1426f9247bb680e5fe0c8
println!("Simple: {}", uuid.simple());

// Upper case
println!("Upper: {}", uuid.hyphenated().to_string().to_uppercase());
```

4. **Handle v1 timestamp monotonicity**

```rust
use uuid::Uuid;
use std::time::{SystemTime, UNIX_EPOCH};

// v1 requires a timestamp and node ID
let ts = SystemTime::now().duration_since(UNIX_EPOCH).unwrap();
let node = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06];

let uuid = Uuid::new_v1(
    uuid::Timestamp::from_unix(
        uuid::NoContext,
        ts.as_secs(),
        ts.subsec_nanos(),
    ),
    &node,
);
println!("v1: {}", uuid);
```

## Examples

```rust
use uuid::Uuid;

fn main() -> Result<(), uuid::Error> {
    // Generate random UUID
    let random_uuid = Uuid::new_v4();
    println!("Random: {}", random_uuid);

    // Parse from string
    let parsed = Uuid::parse_str("550e8400-e29b-41d4-a716-446655440000")?;
    println!("Parsed: {}", parsed);

    // Check version and variant
    println!("Version: {:?}", parsed.get_version_num()); // 4
    println!("Variant: {:?}", parsed.get_variant()); // RFC4122

    // Convert to bytes and back
    let bytes = parsed.as_bytes();
    let from_bytes = Uuid::from_bytes(*bytes);
    assert_eq!(parsed, from_bytes);

    // Nil UUID
    let nil = Uuid::nil();
    assert_eq!(nil.to_string(), "00000000-0000-0000-0000-000000000000");

    // Max UUID
    let max = Uuid::max();
    assert_eq!(max.to_string(), "ffffffff-ffff-ffff-ffff-ffffffffffff");

    Ok(())
}
```

## Related Errors

- [Nanoid Error]({{< relref "/languages/rust/nanoid-error" >}}) — ID generation
- [Regex Error]({{< relref "/languages/rust/regex-error" >}}) — pattern matching
- [Serde Error]({{< relref "/languages/rust/serde-error" >}}) — serialization
