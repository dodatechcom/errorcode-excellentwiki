---
title: "[Solution] Cargo Owner Failed -- Fix Crate Owner Management"
description: "Fix cargo owner failed errors when adding or removing crate owners on crates.io. Verify permissions and token scope."
tools: ["cargo"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `cargo owner --add` or `cargo owner --remove` failed on crates.io.

## Common Causes

- You are not the owner of the crate
- The user does not exist on crates.io
- Your token lacks owner management scope
- The crate name is misspelled

## How to Fix

### 1. Verify Ownership

Visit the crate page on crates.io to check owners.

### 2. Check Token Scope

Generate a new token with full permissions:

```bash
cargo login <new-token>
```

### 3. Verify Username

```bash
# Check the exact username on crates.io
cargo owner --add <exact-username> <crate>
```

### 4. List Current Owners

```bash
cargo owner --list <crate>
```

## Examples

```bash
$ cargo owner --add teammate mycrate
error: you are not an owner of `mycrate`

$ cargo owner --list mycrate
username1 (owner)
```
