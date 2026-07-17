---
title: "[Solution] Cargo Feature Error — Fix Required Feature Not Enabled"
description: "Fix cargo feature errors when a required feature flag is missing from a dependency. Enable features in Cargo.toml and inspect the feature dependency tree."
tools: ["cargo"]
error-types: ["feature-error"]
severities: ["error"]
weight: 5
---

This error means a crate requires a feature flag that was not enabled on one of its dependencies. The compiler or cargo rejects the build because optional functionality is not compiled in.

## What This Error Means

Rust crates use Cargo features to conditionally compile code. When you (or a transitive dependency) call code that requires a feature that was not enabled, you get:

```
error[E0432]: unresolved import `serde_json::from_str`
  --> src/main.rs:3:20
```

Or a more explicit message:

```
error: crate `tokio` does not have the feature `full` enabled
```

## Why It Happens

- You forgot to enable a feature in your `Cargo.toml` dependency declaration
- A crate updated and moved functionality behind a new feature flag
- A transitive dependency requires a feature that you need to explicitly enable
- You are using `default-features = false` without re-enabling the features you need
- The feature name was renamed or removed in a newer version

## How to Fix It

### Enable the Feature in Cargo.toml

```toml
[dependencies]
tokio = { version = "1", features = ["full"] }
```

### Re-enable Defaults After Disabling Them

```toml
[dependencies]
serde = { version = "1", default-features = false, features = ["derive", "std"] }
```

If you disable defaults, you must explicitly list the features you need.

### List All Available Features

```bash
cargo metadata --format-version 1 | jq '.packages[] | select(.name == "tokio") | .features'
```

Or check the crate's documentation on docs.rs.

### Use `cargo tree` to Find Feature Dependencies

```bash
cargo tree -e features
```

This shows which features are enabled on every crate in the dependency tree.

### Enable Features on Transitive Dependencies

If a dependency of a dependency needs a feature:

```toml
[dependencies.my-crate]
version = "1.0"
features = ["nested-dep/feature-name"]
```

## Common Mistakes

- Using `default-features = false` and forgetting to add back the features you actually need
- Not reading the crate's documentation for which features exist
- Assuming `features = ["full"]` always exists (it is a convention, not a requirement)
- Upgrading a crate and not checking if the feature flags changed

## Related Pages

- [Cargo Dependency Error]({{< relref "/tools/cargo/cargo-dependency-error" >}}) -- version selection failures
- [Cargo Compilation Error]({{< relref "/tools/cargo/cargo-compilation-error" >}}) -- build failures
- [Cargo Lock Error]({{< relref "/tools/cargo/cargo-lock-error" >}}) -- lock file issues
