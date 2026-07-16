---
title: "[Solution] macOS OSStatus -41 (errNoSuchName) — No Such Name"
description: "Fix macOS OSStatus -41 (errNoSuchName). Resolve no such name errors in Core Services, Carbon, and legacy Mac framework applications."
platforms: ["macos"]
severities: ["error"]
error_types: ["os-error"]
tags: ["errnosuchname", "osstatus-41", "no-such-name", "core-services", "carbon", "not-found"]
weight: 5
---

# macOS OSStatus -41 (errNoSuchName) — No Such Name

OSStatus -41 (errNoSuchName) indicates that the specified name, resource identifier, or label could not be found in the system or within the expected context. This error is returned by Core Services, Carbon, and older macOS APIs when a named resource, service, or configuration entry does not exist at the specified location.

## Common Causes

- The specified resource name does not exist in the resource file or database
- A keychain item, preference, or configuration entry with the given name was not found
- The resource fork of the application or file does not contain the requested named resource
- A service or protocol name was referenced but is not registered with the system
- The name was misspelled or refers to a resource that was removed in an update

## How to Fix errNoSuchName

### 1. Verify the Resource Name

Check that the name exists and is spelled correctly:

```bash
# List resources in a bundle
ls /path/to/App.app/Contents/Resources/

# Search for a specific resource
find /path/to/App.app -name "ResourceName*"

# Check for named resources in a plist
plutil -p /path/to/file.plist | grep "ResourceName"
```

### 2. Check Keychain for Named Items

If the error relates to a keychain item, verify it exists:

```bash
# Search keychain for a named item
security find-generic-password -s "ServiceName" -a "AccountName"

# List all keychain items
security dump-keychain
```

### 3. Verify Configuration Entries

Check that the named configuration or preference entry exists:

```bash
# Read a preference domain
defaults read com.example.app "PreferenceKey"

# List all preferences for an app
defaults read com.example.app
```

### 4. Check Resource Fork Contents

Verify the resource fork contains the expected named resources:

```bash
# List resource fork entries
/Developer/Tools/DeRez /path/to/file

# Or use Rez and DeRez from Xcode tools
xcrun derez /path/to/file
```

### 5. Register Missing Services

If a service name is not registered, ensure the service is properly configured:

```swift
// Check if a Bonjour service is available
NetServiceBrowser().searchForServices(ofType: "_myservice._tcp.", inDomain: "")
```

## Examples

This error commonly occurs when:

- An application tries to load a named resource that was removed from the bundle
- A keychain lookup uses a service name that does not exist
- A Carbon application requests a named resource from a corrupted resource fork
- A preference key is accessed that has never been set for the application
- A DNS or Bonjour name lookup fails because the service is not registered

## Related Error Codes

- paramErr (OSStatus -50) — [Parameter Error](/os/macos/osstatus-9/)
- osLogicError (OSStatus -66) — [Logic Error](/os/macos/osstatus-8/)
- errNotImplemented (OSStatus -4) — [Not Implemented](/os/macos/osstatus-10/)
- dsBadRoute (OSStatus -3) — [Bad Route](/os/macos/osstatus-6/)
