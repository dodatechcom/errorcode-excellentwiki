---
title: "[Solution] Rust Broken Pipe — Broken Pipe Error"
description: "Fix Rust broken pipe error. Learn why writing to a closed pipe fails and how to handle SIGPIPE and broken pipe conditions."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Broken Pipe — Broken Pipe Error

An IO error with the message "Broken pipe (os error 32)" occurs when you try to write to a pipe or socket whose reading end has been closed. This commonly happens when piping Rust program output to another program that exits early.

## Description

In Unix-like systems, pipes connect the stdout of one process to the stdin of another. When the reading process exits, the writing process receives a `SIGPIPE` signal. If not handled, this signal terminates the process. In Rust, the default behavior is to ignore `SIGPIPE` and return an `IO` error instead.

Error code 32 (`EPIPE`) occurs when:

- Piping to a program that exits early (e.g., `head`).
- Writing to a closed socket.
- Writing to a file descriptor that was closed.
- Client disconnects before server finishes writing.

Common scenarios:

- **Piping to `head`** — `cargo run | head -5` kills the pipe.
- **Piping to `grep`** — grep exits after finding enough matches.
- **Client disconnects** — HTTP client closes connection early.
- **Log piping** — log consumer crashes while producer writes.

## Common Causes

```rust
// Cause 1: Piping output to a program that exits early
// cargo run | head -1
fn main() {
    for i in 0..1000 {
        println!("line {}", i); // broken pipe after 1 line
    }
}

// Cause 2: Writing to stdout after client disconnects
use std::io::Write;
fn main() {
    let stdout = std::io::stdout();
    let mut handle = stdout.lock();
    for i in 0..1000 {
        writeln!(handle, "data {}", i).unwrap(); // broken pipe
    }
}

// Cause 3: Writing to a closed socket
use std::net::TcpStream;
use std::io::Write;
let mut stream = TcpStream::connect("client:8080")?;
// Client disconnects
stream.write_all(b"data")?; // broken pipe
```

## Solutions

### Fix 1: Handle broken pipe errors gracefully

```rust
use std::io::{self, Write};

fn write_to_stdout(data: &str) -> io::Result<()> {
    let stdout = io::stdout();
    let mut handle = stdout.lock();

    match writeln!(handle, "{}", data) {
        Ok(()) => Ok(()),
        Err(e) if e.kind() == io::ErrorKind::BrokenPipe => {
            // Reader closed the pipe, exit gracefully
            std::process::exit(0);
        }
        Err(e) => Err(e),
    }
}

fn main() {
    for i in 0..1000 {
        if write_to_stdout(&format!("line {}", i)).is_err() {
            break;
        }
    }
}
```

### Fix 2: Restore default SIGPIPE handler

```rust
use std::os::unix::signal;

fn main() {
    // Restore default SIGPIPE handling (terminate on broken pipe)
    unsafe {
        signal::signal(signal::Signal::SIGPIPE, signal::SigHandler::SigDfl)
            .expect("failed to set SIGPIPE handler");
    }

    for i in 0..1000 {
        println!("line {}", i);
    }
}
```

### Fix 3: Check for broken pipe before writing

```rust
use std::io::{self, Write, BufWriter};

fn main() {
    let stdout = io::stdout();
    let mut writer = BufWriter::new(stdout.lock());

    for i in 0..1000 {
        let line = format!("line {}\n", i);
        match writer.write_all(line.as_bytes()) {
            Ok(()) => {}
            Err(e) if e.kind() == io::ErrorKind::BrokenPipe => {
                break;
            }
            Err(e) => {
                eprintln!("Write error: {}", e);
                break;
            }
        }
    }

    // Flush to catch any remaining errors
    let _ = writer.flush();
}
```

### Fix 4: Use the nix crate for explicit SIGPIPE handling

```toml
# Cargo.toml
[dependencies]
nix = { version = "0.29", features = ["signal"] }
```

```rust
use nix::sys::signal::{signal, SigHandler, Signal};

fn main() {
    unsafe {
        signal(Signal::SIGPIPE, SigHandler::SigDfl).ok();
    }

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

Running `cargo run | head -5` will produce:
```
line 0
line 1
line 2
line 3
line 4
```
And the program exits with code 141 (128 + 13 for SIGPIPE).

## Related Errors

- [Connection Reset]({{< relref "/languages/rust/connection-reset" >}}) — connection forcibly closed by peer.
- [IO Error]({{< relref "/languages/rust/io-error" >}}) — general IO error handling.
- [Address in Use]({{< relref "/languages/rust/address-in-use" >}}) — port binding conflict.
