---
title: "[Solution] macOS Focus Mode Error — Do Not Disturb Blocks All Notifications"
description: "Fix macOS Focus mode not working: Do Not Disturb blocks all notifications, Focus filters not applying, Focus modes not syncing."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 127
---

# Focus Mode Error — Do Not Disturb Blocks All Notifications

Fix macOS Focus mode not working: Do Not Disturb blocks all notifications, Focus filters not applying, Focus modes not syncing.

## Common Causes

- Focus mode configured to block all notifications universally
- Focus filter rules misconfigured or overly restrictive
- Focus mode not syncing between Mac and iPhone via iCloud
- Third-party app notification not in allowed exceptions list

## How to Fix

### 1. Review Focus Mode Settings

```bash
# System Settings → Focus → Select active Focus mode
defaults read com.apple.dnd
```

### 2. Fix Focus Sync Between Devices

```bash
#
 
S
y
s
t
e
m
 
S
e
t
t
i
n
g
s
 
→
 
F
o
c
u
s
 
→
 
E
n
a
b
l
e
 
S
h
a
r
e
 
A
c
r
o
s
s
 
D
e
v
i
c
e
s
```

### 3. Adjust Focus Filters for Apps

```bash
#
 
S
y
s
t
e
m
 
S
e
t
t
i
n
g
s
 
→
 
F
o
c
u
s
 
→
 
F
i
l
t
e
r
s
 
→
 
A
d
d
 
o
r
 
r
e
m
o
v
e
 
a
p
p
 
f
i
l
t
e
r
s
```

### 4. Reset Focus Mode Configuration

```bash
defaults delete com.apple.dnd
# System Settings → Focus → Delete Focus → Create new Focus
```

## Common Scenarios

This error commonly occurs when:

- Focus mode silences all notifications including those marked as allowed
- Focus mode activated on Mac does not activate on iPhone
- Focus filters block specific email accounts when only app filtering needed
- Focus mode turns on automatically at wrong time due to schedule

## Prevent It

- Review Focus mode settings after each macOS update for changes
- Test Focus configuration by sending test notifications periodically
- Keep Share Across Devices enabled for consistent Focus behavior
- Create specific allowed people and apps lists rather than blocking all
