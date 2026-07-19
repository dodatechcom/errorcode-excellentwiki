---
title: "[Solution] Segmentation Fault (SIGSEGV) in Node.js — Core Dump Fix"
description: "Fix segmentation fault / core dumped errors in Node.js. Diagnose native module crashes and V8 engine issues."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Segmentation Fault in Node.js

A segfault usually means a native addon or V8 bug.

## Diagnosis

```bash
# Get core dump
ulimit -c unlimited
node script.js

# Analyze
gdb node core
(gdb) bt
```

## Common Causes

1. Native addon compiled for wrong Node version
2. Memory corruption in N-API module
3. V8 bug (upgrade Node.js)

```bash
# Rebuild native modules
npm rebuild
```
