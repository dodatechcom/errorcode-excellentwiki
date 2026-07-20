---
title: "[Solution] Rust Embedded Error — How to Fix"
description: "Fix embedded Rust errors. Resolve HAL, PAC, and bare-metal programming issues."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# Embedded Error

Embedded errors occur when developing for microcontroller targets using Rust — issues with no_std environments, linker scripts, memory layout, and hardware peripheral access.

## Common Causes

```rust
// Using std in no_std environment
#![no_std]
use std::collections::HashMap; // ERROR: std not available in no_std

// Missing allocator for heap-dependent crates
// #[global_allocator] not defined

// Linker script issues — missing entry point
// .cargo/config.toml not configured for target

// GPIO peripheral access conflicts
// Taking exclusive ownership of a peripheral twice
```

## How to Fix

1. **Use `#![no_std]` with `extern crate alloc` for heap types**

```rust
#![no_std]
#![no_main]

use cortex_m_rt::entry;
use panic_halt as _; // Panic handler

#[entry]
fn main() -> ! {
    // Access hardware peripherals
    let peripherals = stm32f1xx_hal::pac::Peripherals::take().unwrap();
    let gpioa = peripherals.GPIOA;

    loop {
        // Main loop
        cortex_m::asm::wfi(); // Wait for interrupt
    }
}
```

2. **Configure target and linker in `.cargo/config.toml`**

```toml
# .cargo/config.toml
[build]
target = "thumbv7em-none-eabihf"

[target.thumbv7em-none-eabihf]
linker = "arm-none-eabi-gcc"
runner = "probe-rs run"
rustflags = ["-C", "link-arg=-Tlink.x"]

[aliases]
objcopy = "objcopy --binary"
```

3. **Use HAL crates for safe peripheral access**

```rust
#![no_std]
#![no_main]

use defmt_rtt as _;
use panic_probe as _;
use stm32f4xx_hal::{pac, prelude::*};

#[entry]
fn main() -> ! {
    let dp = pac::Peripherals::take().unwrap();
    let gpioa = dp.GPIOA.split();
    let mut led = gpioa.pa5.into_push_pull_output();

    loop {
        led.set_high();
        cortex_m::asm::delay(8_000_000);
        led.set_low();
        cortex_m::asm::delay(8_000_000);
    }
}
```

## Examples

```rust
#![no_std]
#![no_main]

use cortex_m_rt::entry;
use panic_halt as _;

#[entry]
fn main() -> ! {
    let peripherals = cortex_m::Peripherals::take().unwrap();
    let mut syst = peripherals.SYST;

    // Configure SysTick for 1ms ticks
    syst.set_clock_source(cortex_m::peripheral::syst::SystClkSource::Core);
    syst.set_reload(8_000_000); // 8MHz / 1000 = 8000 cycles per ms
    syst.clear_current();
    syst.enable_counter();

    let mut count: u32 = 0;
    loop {
        while !syst.has_wrapped() {}
        count += 1;
    }
}
```

## Related Errors

- [ESP-IDF Error]({{< relref "/languages/rust/rust-esp-idf-error" >}}) — ESP-IDF targets
- [RISC-V Error]({{< relref "/languages/rust/rust-riscv-error" >}}) — RISC-V targets
- [STM32 Error]({{< relref "/languages/rust/rust-stm32-error" >}}) — STM32 targets
- [No Std Error]({{< relref "/languages/rust/rust-no-std-error-rs" >}}) — no_std issues
