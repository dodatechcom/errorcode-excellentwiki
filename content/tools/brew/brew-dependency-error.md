---
title: "[Solution] Brew Dependency Error — Fix Unsatisfied Dependencies in Homebrew"
description: "Fix Homebrew dependency errors when required formulas are missing or cannot be installed. Update Homebrew and resolve formula conflicts between packages."
tools: ["brew"]
error-types: ["dependency-error"]
severities: ["error"]
weight: 5
---

This error means a formula you are trying to install depends on other formulas that are not installed, not available, or cannot be resolved. Homebrew refuses to install the formula until all dependencies are satisfied.

## What This Error Means

Homebrew formulas declare dependencies in their Ruby formula files. When a dependency is missing, Homebrew tries to install it automatically. If that fails too, you get:

```
Error: Unsatisfied dependency: <dependency-name>
```

Or:

```
Error: Cannot install <formula> because conflicting formulae are installed:
  <other-formula>
```

## Why It Happens

- A required dependency formula is not available for your macOS or architecture
- Two formulas conflict because they install the same binary (e.g., two versions of `gcc`)
- The dependency was recently renamed or deprecated
- Homebrew's formula repository is out of date
- A keg-only formula is not linked and another formula cannot find it

## How to Fix It

### Update Homebrew

```bash
brew update
```

This refreshes the formula list and may resolve missing dependency issues.

### Install the Missing Dependency Manually

```bash
brew install <dependency-name>
brew install <formula>
```

### Check for Conflicts

```bash
brew list | grep <conflicting-formula>
```

If a conflicting formula is installed, remove it first:

```bash
brew uninstall <conflicting-formula>
brew install <formula>
```

### Use `--force` to Override Conflicts

```bash
brew install --force <formula>
```

This skips conflict checking. Use only when you know what you are doing.

### Find Keg-Only Formulas

```bash
brew info <formula>
```

If the formula is keg-only, link it or add its path to `PATH`:

```bash
export PATH="/opt/homebrew/opt/<formula>/bin:$PATH"
```

### Install Bottles Instead of Building from Source

```bash
brew install --force-bottle <formula>
```

Bottles pre-built binaries may have fewer dependency issues than source builds.

## Common Mistakes

- Running `brew install` without `brew update` first
- Not reading the conflict message and trying `--force` repeatedly
- Installing keg-only formulas and expecting them to be in PATH automatically
- Not checking if a formula is deprecated or renamed (use `brew search` to verify)

## Related Pages

- [Brew Install Error]({{< relref "/tools/brew/brew-install-error" >}}) -- formula installation failures
- [Brew Tap Error]({{< relref "/tools/brew/brew-tap-error" >}}) -- tap repository errors
- [Brew Xcode Error]({{< relref "/tools/brew/brew-xcode-error" >}}) -- Xcode tools required
