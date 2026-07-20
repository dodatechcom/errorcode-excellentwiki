---
title: "[Solution] Rust Std Process Error — How to Fix"
description: "Fix standard library process errors. Resolve command execution, piping, and environment issues."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Std Process Error

Std process errors occur when using `std::process::Command` — spawn failures, non-zero exit codes, and stdio pipe issues.

## Common Causes

```rust
use std::process::Command;

// Command not found
let output = Command::new("nonexistent_command")
    .output()
    .expect("Failed to execute"); // ERROR: program not found

// Non-zero exit code
let output = Command::new("ls")
    .arg("/nonexistent")
    .output()
    .expect("Failed");
// output.status.success() is false

// Pipe closed before reading
let mut child = Command::new("cat")
    .stdin(std::process::Stdio::piped())
    .stdout(std::process::Stdio::piped())
    .spawn()
    .unwrap();
// Dropping child without waiting
```

## How to Fix

1. **Check command existence before spawning**

```rust
use std::process::Command;
use std::path::Path;

fn command_exists(name: &str) -> bool {
    Command::new("which")
        .arg(name)
        .output()
        .map(|o| o.status.success())
        .unwrap_or(false)
}

fn main() {
    if command_exists("git") {
        println!("Git is available");
    } else {
        eprintln!("Git not found");
    }
}
```

2. **Handle non-zero exit codes**

```rust
use std::process::Command;

fn run_command(program: &str, args: &[&str]) -> Result<String, String> {
    let output = Command::new(program)
        .args(args)
        .output()
        .map_err(|e| format!("Failed to execute: {}", e))?;

    if !output.status.success() {
        let stderr = String::from_utf8_lossy(&output.stderr);
        return Err(format!("Command failed ({}): {}", output.status, stderr));
    }

    Ok(String::from_utf8_lossy(&output.stdout).to_string())
}

fn main() {
    match run_command("ls", &["-la"]) {
        Ok(output) => println!("{}", output),
        Err(e) => eprintln!("Error: {}", e),
    }
}
```

3. **Use proper stdio configuration**

```rust
use std::process::{Command, Stdio};
use std::io::Write;

fn main() -> std::io::Result<()> {
    let mut child = Command::new("cat")
        .stdin(Stdio::piped())
        .stdout(Stdio::piped())
        .spawn()?;

    // Write to stdin
    if let Some(mut stdin) = child.stdin.take() {
        stdin.write_all(b"Hello from Rust!")?;
    }

    // Read from stdout
    let output = child.wait_with_output()?;
    println!("Output: {}", String::from_utf8_lossy(&output.stdout));

    Ok(())
}
```

## Examples

```rust
use std::process::Command;

fn main() {
    // Run a simple command
    let output = Command::new("echo")
        .arg("Hello, World!")
        .output()
        .expect("Failed to run echo");

    println!("stdout: {}", String::from_utf8_lossy(&output.stdout));

    // Chain commands with pipes
    let output = Command::new("sh")
        .arg("-c")
        .arg("echo 'Hello' | tr '[:upper:]' '[:lower:]'")
        .output()
        .expect("Failed");

    println!("Lowercase: {}", String::from_utf8_lossy(&output.stdout).trim());
}
```

## Related Errors

- [Std Process Error]({{< relref "/languages/rust/std-thread-error" >}}) — thread operations
- [IO Error]({{< relref "/languages/rust/rust-std-io-error" >}}) — I/O operations
- [Timed Out]({{< relref "/languages/rust/timed-out" >}}) — process timeout
