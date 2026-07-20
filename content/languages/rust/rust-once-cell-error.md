---
title: "[Solution] Rust OnceCell Error — How to Fix"
description: "Fix OnceCell and OnceLock initialization errors. Resolve double initialization, thread safety, and lazy static issues."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# OnceCell Error

OnceCell errors occur when using `OnceCell` or `OnceLock` — calling `get_or_init` or `get_or_try_init` in a way that causes deadlock, or using `set` after initialization.

## Common Causes

```rust
use std::sync::OnceLock;

static CELL: OnceLock<String> = OnceLock::new();

// Trying to set twice — returns Err
CELL.set("first".into()).unwrap();
CELL.set("second".into()).unwrap(); // ERROR: AlreadyInitialized

// Calling get() before init
let val = CELL.get(); // Returns None

// Deadlock in multi-threaded init
static A: OnceLock<String> = OnceLock::new();
static B: OnceLock<String> = OnceLock::new();

// Thread 1: A.get_or_init(|| B.get().unwrap().clone()) — waits for B
// Thread 2: B.get_or_init(|| A.get().unwrap().clone()) — waits for A
// DEADLOCK
```

## How to Fix

1. **Use `get_or_init` for lazy initialization**

```rust
use std::sync::OnceLock;

static CONFIG: OnceLock<String> = OnceLock::new();

fn get_config() -> &'static String {
    CONFIG.get_or_init(|| {
        std::env::var("APP_CONFIG").unwrap_or_else(|_| "default".into())
    })
}

fn main() {
    println!("Config: {}", get_config());
    println!("Config: {}", get_config()); // Same value, no re-init
}
```

2. **Use `get_or_try_init` for fallible initialization**

```rust
use std::sync::OnceLock;

static DB_URL: OnceLock<String> = OnceLock::new();

fn get_db_url() -> Result<&'static String, String> {
    DB_URL.get_or_try_init(|| -> Result<String, String> {
        std::env::var("DATABASE_URL").map_err(|_| "DATABASE_URL not set".into())
    })
}

fn main() {
    match get_db_url() {
        Ok(url) => println!("Connected to: {}", url),
        Err(e) => eprintln!("Error: {}", e),
    }
}
```

3. **Use `const` initialization where possible**

```rust
use std::sync::OnceLock;

static APP_NAME: OnceLock<String> = OnceLock::new();

// Initialize at compile time if possible
const fn init_name() -> String {
    String::new() // Cannot use dynamic values in const fn (yet)
}

// Or use lazy_static for complex initialization
```

## Examples

```rust
use std::sync::OnceLock;
use std::collections::HashMap;

static CACHE: OnceLock<HashMap<String, String>> = OnceLock::new();

fn get_cache() -> &'static HashMap<String, String> {
    CACHE.get_or_init(|| {
        let mut map = HashMap::new();
        map.insert("api_key".into(), "secret123".into());
        map.insert("timeout".into(), "30".into());
        map
    })
}

fn main() {
    let cache = get_cache();
    println!("API Key: {}", cache.get("api_key").unwrap());
    println!("Timeout: {}", cache.get("timeout").unwrap());
}
```

## Related Errors

- [Mutex Error]({{< relref "/languages/rust/rust-mutex-error" >}}) — thread-safe initialization
- [RwLock Error]({{< relref "/languages/rust/rust-rwlock-error" >}}) — concurrent access
- [Arc Error]({{< relref "/languages/rust/rust-arc-error" >}}) — shared ownership
