---
title: "[Solution] Rust Inline Assembly Error — How to Fix"
description: "Fix inline assembly errors. Resolve asm! macro usage, register allocation, and constraint issues."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# ASM (Inline Assembly) Error

Inline assembly errors in Rust occur when using `asm!` with invalid constraints, incorrect register usage, or platform-specific instructions that violate safety rules.

## Common Causes

```rust
// Using inline asm without unsafe block
let result: u64;
std::arch::asm!("mov {}, 42", out(reg) result); // Must be inside unsafe

// Platform-specific instruction on wrong architecture
#[cfg(not(target_arch = "x86_64"))]
std::arch::asm!("rdtsc", out("eax") _); // rdtsc only on x86

// Invalid operand constraint
std::arch::asm!("add {0}, 1", inlateout(reg) 0 => _, );
```

## How to Fix

1. **Always wrap `asm!` in `unsafe` and verify operand types**

```rust
let input: u64 = 42;
let output: u64;
unsafe {
    std::arch::asm!("mov {out}, {inp}", inp = in(reg) input, out = out(reg) output);
}
assert_eq!(output, 42);
```

2. **Use `cfg` for platform-specific assembly**

```rust
fn read_cycle_counter() -> u64 {
    #[cfg(target_arch = "x86_64")]
    unsafe {
        let low: u32; let high: u32;
        std::arch::asm!("rdtsc", out("eax") low, out("edx") high);
        return ((high as u64) << 32) | (low as u64);
    }
    #[cfg(not(target_arch = "x86_64"))]
    { std::time::SystemTime::now().duration_since(std::time::UNIX_EPOCH).unwrap().as_nanos() as u64 }
}
```

3. **Specify exact clobber lists for modified registers**

```rust
unsafe {
    let eax_out: u32;
    std::arch::asm!("cpuid", inout("eax") 0 => eax_out, out("ebx") _, out("ecx") _, out("edx") _);
}
```

## Examples

```rust
fn fast_add(a: u64, b: u64) -> u64 {
    let result: u64;
    unsafe {
        std::arch::asm!("add {a}, {b}", a = inout(reg) a => result, b = in(reg) b);
    }
    result
}

fn main() {
    let x = fast_add(10, 20);
    assert_eq!(x, 30);
    println!("10 + 20 = {}", x);
}
```

## Related Errors

- [Embedded Error]({{< relref "/languages/rust/rust-embedded-error" >}}) — embedded target issues
- [RISC-V Error]({{< relref "/languages/rust/rust-riscv-error" >}}) — RISC-V target issues
- [ASM Error]({{< relref "/languages/rust/rust-asm-error" >}}) — inline assembly issues
