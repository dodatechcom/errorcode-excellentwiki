---
title: "[Solution] termion Terminal Error Fix"
description: "Fix termion terminal errors. Handle cursor, color, and terminal size operations."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# termion Terminal Error

The `termion` crate provides Unix terminal manipulation including cursor control, colors, and raw mode. Errors occur when stdout is not a terminal (e.g., piped output), when the terminal doesn't support requested features (like truecolor), or when raw mode cannot be enabled. termion is Unix-only and does not compile on Windows.

## Common Causes

```rust
use termion::raw::IntoRawMode;
use termion::input::TermRead;
use std::io::{self, Write};

// 1. Not a terminal — raw mode fails when piped
let mut stdout = io::stdout().into_raw_mode().unwrap();
// panics if stdout is piped (not a TTY)

// 2. Reading stdin in raw mode without a terminal
let stdin = io::stdin();
for key in stdin.keys() {
    // Fails if stdin is not a terminal
}

// 3. Terminal doesn't support requested color mode
use termion::color;
print!("{}", color::Fg(color::Rgb(255, 128, 0)));
// Garbage output on terminals without truecolor support

// 4. termion is Unix-only — won't compile on Windows
// error[E0433]: failed to resolve: use of undeclared crate or module `termion`
```

## How to Fix

1. **Guard raw mode behind a TTY check**

```rust
use termion::raw::IntoRawMode;
use std::io::{self, Write};

fn run_terminal_ui() -> io::Result<()> {
    if !termion::is_tty(&io::stdin()) {
        eprintln!("Interactive mode requires a terminal");
        return Ok(());
    }

    let mut stdout = io::stdout().into_raw_mode()?;
    write!(stdout, "{}", termion::cursor::Goto(1, 1))?;
    write!(stdout, "Hello, terminal!")?;
    stdout.flush()?;
    Ok(())
}
```

2. **Use RawTerminal with DropGuard for cleanup**

```rust
use termion::raw::IntoRawMode;
use std::io::{self, Write};

fn main() -> io::Result<()> {
    let mut stdout = io::stdout().into_raw_mode()?;

    // Write directly — raw mode auto-restores on drop
    write!(stdout, "{}{}",
        termion::clear::All,
        termion::cursor::Goto(1, 1),
    )?;
    write!(stdout, "Press 'q' to quit")?;
    stdout.flush()?;

    let stdin = io::stdin();
    for key in stdin.keys() {
        if let Ok(key) = key {
            match key {
                termion::event::Key::Char('q') => break,
                _ => {}
            }
        }
    }
    // Raw mode automatically disabled when stdout drops
    Ok(())
}
```

3. **Handle alternate screen for full-screen apps**

```rust
use termion::screen::IntoAlternateScreen;
use termion::raw::IntoRawMode;
use std::io::{self, Write};

fn main() -> io::Result<()> {
    let mut screen = io::stdout().into_alternate_screen()?;
    write!(screen, "In alternate screen (restored on exit)")?;
    screen.flush()?;

    // When screen drops, returns to main screen
    Ok(())
}
```

4. **Use termion with colors safely**

```rust
use termion::color;
use std::io::{self, Write};

fn main() -> io::Result<()> {
    let mut stdout = io::stdout();

    writeln!(stdout, "{}Red text{}",
        color::Fg(color::Red),
        color::Fg(color::Reset),
    )?;
    writeln!(stdout, "{}Blue on yellow{}",
        color::Fg(color::Blue),
        color::Fg(color::Reset),
    )?;
    writeln!(stdout, "{}Bold and underline{}",
        termion::style::Bold,
        termion::style::Reset,
    )?;
    Ok(())
}
```

## Examples

```rust
use termion::raw::IntoRawMode;
use termion::input::TermRead;
use termion::{cursor, color, style};
use std::io::{self, Write};

fn main() -> io::Result<()> {
    if !termion::is_tty(&io::stdin()) {
        println!("Not a terminal");
        return Ok(());
    }

    let mut stdout = io::stdout().into_raw_mode()?;
    write!(stdout, "{}{}", termion::clear::All, cursor::Goto(1, 1))?;
    write!(stdout, "{}╔══════════════════╗{}", style::Bold, style::Reset)?;
    write!(stdout, "{}║  Terminal Demo   ║{}", cursor::Goto(1, 2), style::Reset)?;
    write!(stdout, "{}╚══════════════════╝{}", cursor::Goto(1, 3), style::Reset)?;
    write!(stdout, "{}", cursor::Goto(1, 5))?;
    write!(stdout, "{}Press q to exit{}", color::Fg(color::Green), color::Fg(color::Reset))?;
    stdout.flush()?;

    let stdin = io::stdin();
    for key in stdin.keys() {
        if let Ok(termion::event::Key::Char('q')) = key {
            break;
        }
    }
    Ok(())
}
```

## Related Errors

- [Crossterm Error]({{< relref "/languages/rust/crossterm-error" >}}) — cross-platform terminal
- [Colored Error]({{< relref "/languages/rust/colored-error" >}}) — ANSI colors
- [Dialoguer Error]({{< relref "/languages/rust/dialoguer-error" >}}) — interactive prompts
