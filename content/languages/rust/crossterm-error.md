---
title: "[Solution] crossterm Terminal Error Fix"
description: "Fix crossterm terminal errors. Handle cursor control, event polling, and terminal mode changes."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Crossterm Error

Crossterm errors occur when using the `crossterm` crate for terminal manipulation — raw mode issues, event handling failures, and unsupported features.

## Common Causes

```rust
use crossterm::event::{self, Event, KeyCode};
use crossterm::terminal;

// Not entering raw mode
terminal::enable_raw_mode().unwrap();
// Events not working without raw mode

// Blocking event read in async context
let event = event::read().unwrap(); // Blocks — problematic in async

// Terminal not restored after panic
// Need to call disable_raw_mode in Drop or cleanup
```

## How to Fix

1. **Use `crossterm::event::poll` for non-blocking reads**

```rust
use crossterm::event::{self, Event, KeyCode};
use std::time::Duration;

fn handle_events() -> std::io::Result<bool> {
    if event::poll(Duration::from_millis(100))? {
        if let Event::Key(key) = event::read()? {
            match key.code {
                KeyCode::Char('q') => return Ok(true),
                KeyCode::Char(c) => println!("Key: {}", c),
                _ => {}
            }
        }
    }
    Ok(false)
}
```

2. **Use `scopeguard` or `Drop` to restore terminal**

```rust
use crossterm::terminal;

struct RawModeGuard;

impl Drop for RawModeGuard {
    fn drop(&mut self) { let _ = terminal::disable_raw_mode(); }
}

fn main() -> std::io::Result<()> {
    terminal::enable_raw_mode()?;
    let _guard = RawModeGuard; // Restored on drop
    // Terminal operations here
    Ok(())
}
```

3. **Use `crossterm::execute!` macro for commands**

```rust
use crossterm::{execute, cursor, terminal};
use std::io::{self, Write};

fn main() -> io::Result<()> {
    let mut stdout = io::stdout();
    execute!(stdout, cursor::MoveTo(0, 0))?;
    execute!(stdout, terminal::Clear(terminal::ClearType::All))?;
    execute!(stdout, cursor::Hide)?;
    // ... work ...
    execute!(stdout, cursor::Show)?;
    Ok(())
}
```

## Examples

```rust
use crossterm::{event::{self, Event, KeyCode, KeyModifiers}, terminal, cursor, execute};
use std::io::{self, Write};

fn main() -> io::Result<()> {
    terminal::enable_raw_mode()?;
    let mut stdout = io::stdout();

    loop {
        if event::poll(std::time::Duration::from_millis(100))? {
            if let Event::Key(key) = event::read()? {
                match key.code {
                    KeyCode::Char('c') if key.modifiers.contains(KeyModifiers::CONTROL) => break,
                    KeyCode::Char(c) => write!(stdout, "{}", c)?,
                    KeyCode::Enter => writeln!(stdout)?,
                    _ => {}
                }
                stdout.flush()?;
            }
        }
    }

    terminal::disable_raw_mode()?;
    Ok(())
}
```

## Related Errors

- [Termion Error]({{< relref "/languages/rust/termion-error" >}}) — terminal I/O
- [Indicatif Error]({{< relref "/languages/rust/indicatif-error" >}}) — progress bars
- [Dialoguer Error]({{< relref "/languages/rust/dialoguer-error" >}}) — interactive prompts
