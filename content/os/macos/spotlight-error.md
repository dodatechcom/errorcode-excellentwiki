---
title: "[Solution] macOS Spotlight Error — Search Not Working"
description: "Fix macOS Spotlight not working: search returns no results, indexing stuck or paused, Spotlight uses excessive CPU."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 111
---

# Spotlight Error — Search Not Working

Fix macOS Spotlight not working: search returns no results, indexing stuck or paused, Spotlight uses excessive CPU.

## Common Causes

- Spotlight index database corrupted or incomplete
- mds_stores process crashed preventing indexing
- Privacy settings excluding folders from search index
- Low disk space preventing index from being built

## How to Fix

### 1. Check Spotlight Indexing Status

```bash
mdutil -s /
log show --predicate 'subsystem == "com.apple.Spotlight"' --last 5m | head -20
```

### 2. Rebuild Spotlight Index

```bash
sudo mdutil -i off /
sudo mdutil -E /
sudo mdutil -i on /
mdutil -s /
```

### 3. Fix Privacy Exclusions

```bash
d
e
f
a
u
l
t
s
 
d
e
l
e
t
e
 
c
o
m
.
a
p
p
l
e
.
S
p
o
t
l
i
g
h
t
 
o
r
d
e
r
e
d
I
t
e
m
s
```

### 4. Restart Spotlight and mds Processes

```bash
sudo killall mds
sudo killall mds_stores
# They will restart automatically and begin reindexing
```

## Common Scenarios

This error commonly occurs when:

- Spotlight search returns no results for files that definitely exist
- mds_stores uses 100% CPU for extended periods after macOS update
- Spotlight indexing appears stuck at the same percentage
- Spotlight finds apps but not documents or emails

## Prevent It

- Keep sufficient free disk space for Spotlight index (10%+ of disk)
- Avoid excluding critical folders from Spotlight search index
- Restart Mac if Spotlight indexing seems stuck for more than an hour
- Run 'mdutil -s /' periodically to verify index health
