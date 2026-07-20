---
title: "[Solution] notify File Watcher Error Fix"
description: "Fix notify file watcher errors. Handle platform-specific issues, recursive watching, and debounce."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Notify Error

Notify errors occur when using the `notify` crate for filesystem watching — permission errors and platform limitations.

## Common Causes

```rust
// Permission denied on watched directory
watcher.watch(Path::new("/root"), RecursiveMode::Recursive)?;

// File system events not supported
// Some network filesystems don't support inotify
```

## How to Fix

1. **Handle watcher errors**

```rust
use notify::{Watcher, RecursiveMode, watcher};
use std::sync::mpsc::channel;

let (tx, rx) = channel();
let mut watcher = watcher(tx, Duration::from_secs(1))?;
watcher.watch(Path::new("."), RecursiveMode::Recursive)?;
```

2. **Filter events**

```rust
use notify::{Event, EventKind};

match rx.recv() {
    Ok(Ok(event)) => match event.kind {
        EventKind::Create(_) => println!("File created"),
        EventKind::Modify(_) => println!("File modified"),
        EventKind::Remove(_) => println!("File removed"),
        _ => {}
    },
    Err(e) => eprintln!("Watch error: {}", e),
    _ => {}
}
```

3. **Use debounce**

```rust
let mut watcher = watcher(tx, Duration::from_millis(500))?;
```

## Examples

```rust
use notify::{Watcher, RecursiveMode, watcher};
use std::sync::mpsc::channel;
use std::time::Duration;
use std::path::Path;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let (tx, rx) = channel();
    let mut watcher = watcher(tx, Duration::from_secs(1))?;
    watcher.watch(Path::new("."), RecursiveMode::Recursive)?;

    println!("Watching for changes...");
    for res in rx {
        match res {
            Ok(event) => println!("Event: {:?}", event),
            Err(e) => eprintln!("Error: {}", e),
        }
    }
    Ok(())
}
```

## Related Errors

- [FS Extra Error]({{< relref "/languages/rust/fs-extra-error" >}}) — filesystem
- [Glob Error]({{< relref "/languages/rust/glob-error" >}}) — glob patterns
- [WalkDir Error]({{< relref "/languages/rust/walkdir-error" >}}) — directory walking
