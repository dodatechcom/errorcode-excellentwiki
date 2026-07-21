---
title: "[Solution] Cargo Doc Failed -- Fix Documentation Build Error"
description: "Fix cargo doc failed errors when generating documentation for your project. Fix rustdoc warnings and errors."
tools: ["cargo"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `cargo doc` failed to generate documentation. The doc comments may contain invalid Rust code.

## Common Causes

- Doc comments contain invalid code examples
- Links in doc comments are broken
- Missing dependencies for doc generation
- Doc tests fail to compile

## How to Fix

### 1. Build Docs with Warnings

```bash
cargo doc 2>&1 | grep "warning\|error"
```

### 2. Fix Doc Test Failures

```bash
cargo test --doc
```

### 3. Open Docs Locally

```bash
cargo doc --open
```

### 4. Skip Doc Tests

```bash
cargo doc --no-deps
```

## Examples

```bash
$ cargo doc
error[E0433]: failed to resolve: use of undeclared type `Foo`

# Fix the doc comment:
/// ```
/// # use my_crate::Foo;
/// let f = Foo::new();
/// ```
```
