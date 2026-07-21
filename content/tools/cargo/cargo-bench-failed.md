---
title: "[Solution] Cargo Bench Failed -- Fix Benchmark Execution Error"
description: "Fix cargo bench failed errors when benchmarks fail to compile or run. Check benchmark code and dependencies."
tools: ["cargo"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `cargo bench` failed to compile or execute benchmarks in your project.

## Common Causes

- Benchmark code has compilation errors
- Missing dev-dependencies for benchmarks
- Benchmark harness is misconfigured
- The benchmark panics at runtime

## How to Fix

### 1. Run Benchmarks with Verbose Output

```bash
cargo bench -- --nocapture
```

### 2. Check Benchmark Compilation

```bash
cargo bench --no-run
```

### 3. Add Missing Dev Dependencies

```toml
[dev-dependencies]
criterion = "0.5"
```

### 4. Fix Benchmark Code

```rust
// benches/my_bench.rs
use criterion::{black_box, criterion_group, criterion_main, Criterion};

fn criterion_benchmark(c: &mut Criterion) {
    c.bench_function("my_bench", |b| b.iter(|| black_box(1 + 1)));
}

criterion_group!(benches, criterion_benchmark);
criterion_main!(benches);
```

## Examples

```bash
$ cargo bench
error[E0433]: failed to resolve: use of undeclared crate `criterion`

$ cargo add --dev criterion
$ cargo bench
benchmy_bench      time: [1.2 ns 1.3 ns 1.4 ns]
```
