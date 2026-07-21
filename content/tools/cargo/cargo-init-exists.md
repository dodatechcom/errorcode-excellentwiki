---
title: "[Solution] Cargo Init Exists -- Fix Directory Already Initialized"
description: "Fix cargo init exists error when trying to initialize a project in a directory that already has a Cargo.toml. Use a different directory."
tools: ["cargo"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `cargo init` was run in a directory that already contains a `Cargo.toml` file.

## Common Causes

- You already initialized this project
- Running cargo init in the wrong directory
- Previous attempt left partial files

## How to Fix

### 1. Use a Different Directory

```bash
cargo init ../new-project
```

### 2. Remove Existing Cargo.toml

```bash
rm Cargo.toml
cargo init
```

### 3. Add to Existing Project

```bash
cargo init --lib my-new-crate
```

### 4. Check Current Directory

```bash
pwd
ls Cargo.toml
```

## Examples

```bash
$ cargo init
error: `Cargo.toml` already exists in `/home/user/project`

$ cargo init ../new-project
     Created binary (application) `new-project` package
```
