---
title: "[Solution] Rust Std IO Error — How to Fix"
description: "Fix standard library I/O errors. Resolve file, network, and stream read/write failures."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Std IO Error

Std IO errors occur when using `std::io` functions — broken pipes, interrupted operations, unexpected EOF, and platform-specific I/O issues.

## Common Causes

```rust
use std::io::{self, Read, Write, BufRead};

// Broken pipe — writing to a closed pipe
let mut stdout = io::stdout();
write!(stdout, "data").unwrap(); // May fail if pipe is broken

// Unexpected EOF
let mut buf = [0u8; 1024];
let mut file = std::fs::File::open("small.txt").unwrap();
let n = file.read(&mut buf).unwrap(); // May return less than 1024

// Interrupted operation
io::stdin().read_line(&mut String::new()).unwrap(); // May be interrupted
```

## How to Fix

1. **Handle I/O errors with retry logic**

```rust
use std::io;

fn read_with_retry(path: &str) -> io::Result<String> {
    let mut attempts = 0;
    loop {
        match std::fs::read_to_string(path) {
            Ok(content) => return Ok(content),
            Err(e) if e.kind() == io::ErrorKind::Interrupted && attempts < 3 => {
                attempts += 1;
                std::thread::sleep(std::time::Duration::from_millis(100));
            }
            Err(e) => return Err(e),
        }
    }
}
```

2. **Use buffered I/O for better performance**

```rust
use std::io::{BufReader, BufWriter, Read, Write};
use std::fs::File;

fn process_file(path: &str) -> std::io::Result<()> {
    let file = File::open(path)?;
    let mut reader = BufReader::new(file);

    let mut content = String::new();
    reader.read_to_string(&mut content)?;

    let output = File::create("output.txt")?;
    let mut writer = BufWriter::new(output);
    writer.write_all(content.as_bytes())?;

    Ok(())
}
```

3. **Handle broken pipe gracefully**

```rust
use std::io::{self, Write};

fn main() {
    let stdout = io::stdout();
    let mut handle = stdout.lock();

    for i in 0..1000 {
        if writeln!(handle, "Line {}", i).is_err() {
            break; // Pipe broken, stop writing
        }
    }
}
```

## Examples

```rust
use std::io::{self, BufRead, BufReader, Write};

fn main() -> io::Result<()> {
    // Read lines from stdin
    let stdin = io::stdin();
    for line in stdin.lock().lines() {
        let line = line?;
        println!("You said: {}", line);
        if line == "quit" { break; }
    }

    // Write with explicit flushing
    let mut stdout = io::stdout();
    write!(stdout, "Processing...")?;
    stdout.flush()?;

    // Simulate work
    std::thread::sleep(std::time::Duration::from_secs(1));
    writeln!(stdout, " done!")?;

    Ok(())
}
```

## Related Errors

- [Std FS Error]({{< relref "/languages/rust/rust-std-fs-error" >}}) — filesystem operations
- [IO Error]({{< relref "/languages/rust/io-error" >}}) — general I/O errors
- [Connection Refused]({{< relref "/languages/rust/connection-refused" >}}) — network I/O
