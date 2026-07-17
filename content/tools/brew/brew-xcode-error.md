---
title: "[Solution] Brew Xcode Error — Fix Xcode Command Line Tools Required"
description: "Fix Homebrew errors when Xcode Command Line Tools are missing or outdated on macOS. Install, reinstall, and configure the developer directory after upgrades."
tools: ["brew"]
error-types: ["xcode-error"]
severities: ["error"]
weight: 5
---

This error means Homebrew requires Xcode Command Line Tools but they are not installed, not configured, or an outdated version is present. Many formulas fail to compile without the compiler and headers these tools provide.

## What This Error Means

Homebrew uses `clang` from Xcode Command Line Tools to compile formulas from source. When the tools are missing or broken:

```
Error: No Xcode or CLT version detected!
```

Or:

```
Error: An exception occurred within a child process:
  Errno::ENOENT: No such file or directory - xcrun
```

Or:

```
Xcode alone is not enough on Catalina.
You must also have the command line tools installed.
```

## Why It Happens

- Xcode Command Line Tools were never installed
- macOS was upgraded and the tools need to be reinstalled
- The tools are installed to a non-standard location (e.g., external drive)
- `xcode-select --print-path` points to a path that does not exist
- The Xcode.app installation is corrupted or incomplete
- SIP restrictions changed between macOS versions

## How to Fix It

### Install or Reinstall Command Line Tools

```bash
xcode-select --install
```

This opens a dialog to download and install the tools.

### Reset the Developer Directory

```bash
sudo xcode-select --reset
```

### Point to the Correct Xcode Installation

If you have full Xcode installed:

```bash
sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
```

For Command Line Tools only:

```bash
sudo xcode-select --switch /Library/Developer/CommandLineTools
```

### Verify the Installation

```bash
xcode-select --print-path
xcrun --show-sdk-path
clang --version
```

All three commands should return valid paths and versions.

### Reinstall After macOS Upgrade

After every major macOS upgrade, reinstall the tools:

```bash
sudo rm -rf /Library/Developer/CommandLineTools
xcode-select --install
```

### Fix `xcrun` Errors

```bash
sudo xcrun --kill-cache
```

This clears a stale SDK cache that may point to a removed path.

### Accept the License

```bash
sudo xcodebuild -license accept
```

Some formulas check if the license has been accepted.

## Common Mistakes

- Installing full Xcode from the App Store without running `xcode-select --switch`
- Not reinstalling Command Line Tools after a macOS upgrade
- Assuming `gcc` or `make` are available without the tools
- Having both Xcode and Command Line Tools installed to different paths

## Related Pages

- [Brew Install Error]({{< relref "/tools/brew/brew-install-error" >}}) -- formula installation failures
- [Brew Permission Error]({{< relref "/tools/brew/brew-permission-error" >}}) -- permission issues
- [Brew Update Error]({{< relref "/tools/brew/brew-update-error" >}}) -- brew update failures
