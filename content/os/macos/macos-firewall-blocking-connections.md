---
title: "[Solution] macOS Firewall Blocking Connections -- Mac Firewall Preventing App Access"
description: "Fix macOS firewall blocking connections when the built-in firewall prevents apps from accessing the network. Resolve firewall blocks on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Firewall Blocking Connections -- Mac Firewall Preventing App Access

The macOS application firewall can block incoming and sometimes outgoing connections for specific applications. When misconfigured, it may block legitimate apps from accessing the network.

## Common Causes
- Firewall is set to block all incoming connections
- Application was set to 'Block' in firewall settings
- Third-party firewall is more restrictive than the built-in one
- Firewall rules were corrupted by a system update
- Stealth mode is preventing response to network probes

## How to Fix
1. Open System Preferences > Security & Privacy > Firewall
2. Check the firewall list and ensure your app is set to 'Allow'
3. Remove overly restrictive third-party firewall software
4. Reset firewall rules to default
5. Temporarily disable the firewall to test if it is the cause

```bash
# Check firewall status
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate

# Check firewall logging
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --getloggingmode

# Add an app to the firewall allow list
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --add /Applications/AppName.app
```

## Examples

```bash
# List all apps in the firewall rules
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --listapps
```

This error is common after installing a new app that needs network access, when firewall rules are corrupted after a macOS update, or when a third-party firewall conflicts with the built-in one.
