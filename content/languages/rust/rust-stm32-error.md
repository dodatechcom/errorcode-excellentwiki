---
title: "[Solution] Rust STM32 Error — How to Fix"
description: "Fix STM32 embedded Rust errors. Resolve STM32 HAL, PAC, and peripheral configuration issues."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# STM32 Error

STM32 errors occur when developing for STM32 microcontrollers with Rust — linker script issues, peripheral initialization failures, and HAL compatibility problems.

## Common Causes

```rust
#![no_std]
#![no_main]

use stm32f1xx_hal::prelude::*;

// Missing linker script
// .cargo/config.toml not pointing to correct memory.x

// Peripheral not initialized before use
#[entry]
fn main() -> ! {
    let dp = stm32f1xx_hal::pac::Peripherals::take().unwrap();
    let gpioa = dp.GPIOA.split();
    let mut led = gpioa.pa5.into_push_pull_output();
    // Trying to use gpioa after split — already moved
    let mut other = gpioa.pa6.into_push_pull_output(); // ERROR: gpioa moved

    loop { cortex_m::asm::wfi(); }
}

// Clock configuration errors
// Using wrong HSE frequency
```

## How to Fix

1. **Configure `.cargo/config.toml` for STM32 targets**

```toml
# .cargo/config.toml
[build]
target = "thumbv7m-none-eabi"

[target.thumbv7m-none-eabi]
linker = "arm-none-eabi-gcc"
rustflags = ["-C", "link-arg=-Tlink.x"]
runner = "probe-rr run"
```

2. **Initialize peripherals correctly with HAL**

```rust
#![no_std]
#![no_main]

use cortex_m_rt::entry;
use panic_halt as _;
use stm32f1xx_hal::{pac, prelude::*};

#[entry]
fn main() -> ! {
    let dp = pac::Peripherals::take().unwrap();
    let mut flash = dp.FLASH.constrain();
    let rcc = dp.RCC.constrain();

    let clocks = rcc.cfgr.hclk(8.MHz()).freeze(&mut flash.acr);
    let mut gpioa = dp.GPIOA.split();

    let mut led = gpioa.pa5.into_push_pull_output();

    loop {
        led.set_high();
        cortex_m::asm::delay(8_000_000);
        led.set_low();
        cortex_m::asm::delay(8_000_000);
    }
}
```

3. **Use probe-rs for debugging**

```bash
# Install probe-rs
$ cargo install probe-rs

# Flash and run
$ cargo run

# Debug with GDB
$ cargo run -- -g
```

## Examples

```rust
#![no_std]
#![no_main]

use cortex_m_rt::entry;
use panic_halt as _;
use stm32f1xx_hal::{pac, prelude::*, timer::Timer};

#[entry]
fn main() -> ! {
    let dp = pac::Peripherals::take().unwrap();
    let mut flash = dp.FLASH.constrain();
    let rcc = dp.RCC.constrain();
    let clocks = rcc.cfgr.hclk(8.MHz()).freeze(&mut flash.acr);

    let mut gpioa = dp.GPIOA.split();
    let mut led = gpioa.pa5.into_push_pull_output();
    let mut timer = Timer::tim2(dp.TIM1, &clocks).start::<1000_u32>();

    loop {
        led.toggle();
        nb::block!(timer.wait()).unwrap();
    }
}
```

## Related Errors

- [Embedded Error]({{< relref "/languages/rust/rust-embedded-error" >}}) — embedded targets
- [RISC-V Error]({{< relref "/languages/rust/rust-riscv-error" >}}) — RISC-V targets
- [No Std Error]({{< relref "/languages/rust/rust-no-std-error-rs" >}}) — no_std issues
