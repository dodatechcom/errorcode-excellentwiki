---
title: "[Solution] indicatif Progress Bar Error Fix"
description: "Fix indicatif progress bar errors. Handle terminal rendering, multi-progress, and draw errors."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Indicatif Error

Indicatif errors occur when using the `indicatif` crate for progress bars — display conflicts and tick rate issues.

## Common Causes

```rust
// Progress bar in non-terminal context
let pb = ProgressBar::new(100);
pb.inc(1); // May not display properly

// Wrong tick rate
pb.set_tick_rate(0); // Too fast — CPU spin
```

## How to Fix

1. **Use MultiProgress for multiple bars**

```rust
use indicatif::{MultiProgress, ProgressBar};

let mp = MultiProgress::new();
let pb1 = mp.add(ProgressBar::new(100));
let pb2 = mp.add(ProgressBar::new(100));
```

2. **Set appropriate tick rate**

```rust
use indicatif::ProgressBar;

let pb = ProgressBar::new(100);
pb.set_tick_rate(std::time::Duration::from_millis(100));
```

3. **Use styled progress bars**

```rust
use indicatif::{ProgressBar, ProgressStyle};

let pb = ProgressBar::new(100);
pb.set_style(ProgressStyle::default_bar()
    .template("[{elapsed_precise}] [{bar:40.cyan/blue}] {pos}/{len} ({eta})")
    .unwrap()
    .progress_chars("#>-"));
```

## Examples

```rust
use indicatif::{ProgressBar, ProgressStyle};

fn main() {
    let pb = ProgressBar::new(100);
    pb.set_style(ProgressStyle::default_bar()
        .template("[{elapsed_precise}] [{bar:40.cyan/blue}] {pos}/{len} ({eta})")
        .unwrap()
        .progress_chars("#>-"));

    for _ in 0..100 {
        pb.inc(1);
        std::thread::sleep(std::time::Duration::from_millis(20));
    }
    pb.finish_with_message("done");
}
```

## Related Errors

- [Crossterm Error]({{< relref "/languages/rust/crossterm-error" >}}) — terminal handling
- [Colored Error]({{< relref "/languages/rust/colored-error" >}}) — colors
- [Dialoguer Error]({{< relref "/languages/rust/dialoguer-error" >}}) — prompts
