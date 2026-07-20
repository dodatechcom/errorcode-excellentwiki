---
title: "[Solution] chrono-tz Timezone Error Fix"
description: "Fix chrono-tz timezone errors. Handle timezone lookup, conversion, and DST transitions."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Chrono-TZ Error

Chrono-TZ errors occur when using the `chrono-tz` crate for timezone handling — invalid timezone names and conversion failures.

## Common Causes

```rust
use chrono_tz::Tz;

// Invalid timezone name
let tz: Tz = "Invalid/Timezone".parse().unwrap(); // ERROR: unknown timezone

// Off-by-one in DST transitions
```

## How to Fix

1. **Use valid IANA timezone names**

```rust
use chrono_tz::Tz;

let tz: Tz = "America/New_York".parse().unwrap();
let now = chrono::Utc::now().with_timezone(&tz);
println!("NYC time: {}", now);
```

2. **Handle DST transitions**

```rust
use chrono_tz::Tz;

let tz: Tz = "US/Eastern".parse().unwrap();
let dt = chrono::Utc.with_ymd_and_hms(2023, 3, 12, 7, 0, 0).unwrap();
let local = dt.with_timezone(&tz);
println!("During DST: {}", local);
```

3. **Use timezone list for validation**

```rust
use chrono_tz::{Tz, TZ_VARIANTS};

fn is_valid_tz(name: &str) -> bool {
    name.parse::<Tz>().is_ok()
}

fn main() {
    println!("America/New_York valid: {}", is_valid_tz("America/New_York"));
    println!("Invalid valid: {}", is_valid_tz("Invalid/Zone"));
}
```

## Examples

```rust
use chrono_tz::Tz;
use chrono::{TimeZone, Utc};

fn main() {
    let timezones = vec!["UTC", "US/Eastern", "Europe/London", "Asia/Tokyo"];
    let now = Utc::now();

    for tz_str in timezones {
        let tz: Tz = tz_str.parse().unwrap();
        let local = now.with_timezone(&tz);
        println!("{}: {}", tz_str, local.format("%Y-%m-%d %H:%M:%S %Z"));
    }
}
```

## Related Errors

- [Chrono Error]({{< relref "/languages/rust/chrono-error" >}}) — chrono core
- [Time Error]({{< relref "/languages/rust/time-error-rs" >}}) — time crate
- [Std Env Error]({{< relref "/languages/rust/rust-std-env-error" >}}) — TZ env var
