---
title: "[Solution] Rust Std Time Error — How to Fix"
description: "Fix standard library time errors. Resolve SystemTime, Instant, and duration arithmetic issues."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Std Time Error

Std time errors occur when using `std::time` — overflow in duration arithmetic, system clock issues, and monotonic clock violations.

## Common Causes

```rust
use std::time::{Duration, SystemTime, Instant};

// Duration arithmetic overflow
let d1 = Duration::from_secs(u64::MAX);
let d2 = Duration::from_secs(1);
let d3 = d1 + d2; // PANIC: overflow

// SystemTime going backwards
let now = SystemTime::now();
let past = now - Duration::from_secs(3600);
// If NTP adjusts clock backward, past > now

// Instant not monotonic on some platforms
let start = Instant::now();
// Very long operation
let elapsed = start.elapsed();
// elapsed may be less than expected on some platforms
```

## How to Fix

1. **Use `checked_add` and `checked_sub` for duration math**

```rust
use std::time::Duration;

let d1 = Duration::from_secs(u64::MAX - 10);
let d2 = Duration::from_secs(5);

if let Some(d3) = d1.checked_add(d2) {
    println!("Sum: {:?}", d3);
} else {
    eprintln!("Duration overflow");
}

if let Some(d4) = d1.checked_sub(d2) {
    println!("Diff: {:?}", d4);
}
```

2. **Handle SystemTime errors gracefully**

```rust
use std::time::{Duration, SystemTime};

fn get_file_age(path: &str) -> Result<Duration, String> {
    let metadata = std::fs::metadata(path)
        .map_err(|e| format!("Metadata error: {}", e))?;
    let modified = metadata.modified()
        .map_err(|e| format!("Modified time not supported: {}", e))?;

    modified.elapsed().map_err(|e| format!("Time error: {}", e))
}
```

3. **Use `Instant` for measuring elapsed time**

```rust
use std::time::Instant;

let start = Instant::now();
// Perform computation
let mut sum: u64 = 0;
for i in 0..1_000_000 {
    sum += i;
}
let elapsed = start.elapsed();
println!("Sum: {} (took {:?})", sum, elapsed);
```

## Examples

```rust
use std::time::{Duration, Instant, SystemTime, UNIX_EPOCH};

fn main() {
    // Measure execution time
    let start = Instant::now();
    let result: u64 = (1..=1000).sum();
    println!("Sum: {} in {:?}", result, start.elapsed());

    // System time
    match SystemTime::now().duration_since(UNIX_EPOCH) {
        Ok(d) => println!("Seconds since epoch: {}", d.as_secs()),
        Err(e) => eprintln!("Time error: {}", e),
    }

    // Duration formatting
    let d = Duration::from_millis(3661000);
    let hours = d.as_secs() / 3600;
    let minutes = (d.as_secs() % 3600) / 60;
    let seconds = d.as_secs() % 60;
    println!("{:02}:{:02}:{:02}", hours, minutes, seconds);
}
```

## Related Errors

- [Time Error]({{< relref "/languages/rust/time-error-rs" >}}) — time crate issues
- [Chrono Error]({{< relref "/languages/rust/chrono-error" >}}) — chrono crate
- [Std Thread Error]({{< relref "/languages/rust/rust-std-thread-error" >}}) — thread timing
