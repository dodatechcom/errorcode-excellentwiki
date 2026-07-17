---
title: "[Solution] Rust Broken Pipe — Pipe Closed Error"
description: "Fix Rust broken pipe error. Learn why writing to a closed pipe fails and how to handle SIGPIPE and broken pipe conditions gracefully."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Broken Pipe — Pipe Closed Error

An IO error with the message "Broken pipe (os error 32)" occurs when you write to a pipe or socket whose reading end has been closed.

## Description

In Unix, pipes connect processes — stdout of one to stdin of another. When the reader exits, the writer gets a `SIGPIPE` signal. Rust ignores `SIGPIPE` by default and returns an IO error instead (error code 32, `EPIPE`).

Common scenarios:

- **Piping to `head`** — `cargo run | head -5` closes after 5 lines.
- **Piping to `grep`** — grep exits after finding matches.
- **Client disconnects** — HTTP client closes before response is sent.
- **Log consumer crashes** — log producer writes to dead pipe.

## Common Causes

```rust
// Cause 1: Piping to head
// cargo run | head -1
fn main() {
    for i in 0..1000 {
        println!("line {}", i); // broken pipe after line 1
    }
}

// Cause 2: Writing after client disconnect
use std::io::Write;
fn main() {
    let mut stdout = std::io::stdout().lock();
    for i in 0..1000 {
        writeln!(stdout, "data {}", i).unwrap(); // broken pipe
    }
}

// Cause 3: Writing to closed socket
use std::net::TcpStream;
use std::io::Write;
let mut stream = TcpStream::connect("server:8080")?;
// Client disconnects
stream.write_all(b"data")?; // broken pipe
```

## Solutions

### Fix 1: Handle BrokenPipe gracefully

```rust
use std::io::{self, Write};

fn write_line(data: &str) -> io::Result<()> {
    let mut stdout = io::stdout().lock();
    match writeln!(stdout, "{}", data) {
        Ok(()) => Ok(()),
        Err(e) if e.kind() == io::ErrorKind::BrokenPipe => {
            std::process::exit(0); // exit cleanly
        }
        Err(e) => Err(e),
    }
}

fn main() {
    for i in 0..1000 {
        if write_line(&format!("line {}", i)).is_err() {
            break;
        }
    }
}
```

### Fix 2: Restore default SIGPIPE handler

```rust
use std::os::unix::signal;

fn main() {
    unsafe {
        signal::signal(signal::Signal::SIGPIPE, signal::SigHandler::SigDfl)
            .expect("failed to set handler");
    }
    for i in 0..1000 {
        println!("line {}", i);
    }
}
```

### Fix 3: Check before writing

```rust
use std::io::{self, Write, BufWriter};

fn main() {
    let mut writer = BufWriter::new(io::stdout().lock());
    for i in 0..1000 {
        let line = format!("line {}\n", i);
        match writer.write_all(line.as_bytes()) {
            Ok(()) => {}
            Err(e) if e.kind() == io::ErrorKind::BrokenPipe => break,
            Err(e) => { eprintln!("Error: {}", e); break; }
        }
    }
    let _ = writer.flush();
}
```

### Fix 4: Use the nix crate for SIGPIPE control

```rust
// Cargo.toml: nix = { version = "0.29", features = ["signal"] }
use nix::sys::signal::{signal, SigHandler, Signal};

fn main() {
    unsafe { signal(Signal::SIGPIPE, SigHandler::SigDfl).ok(); }
    for i in 0..1000 {
        println!("line {}", i);
    }
}
```

## Examples

```rust
fn main() {
    for i in 0..100 {
        println!("line {}", i);
    }
}
```

Running `cargo run | head -5` produces:
```
line 0
line 1
line 2
line 3
line 4
```
Program exits with code 141 (128 + 13 for SIGPIPE).

## Related Errors

- [Connection Reset]({{< relref "/languages/rust/connection-reset-2" >}}) — connection forcibly closed by peer.
- [IO Error]({{< relref "/languages/rust/io-error-2" >}}) — general I/O error handling.
- [Address in Use]({{< relref "/languages/rust/address-in-use-2" >}}) — port binding conflict.
