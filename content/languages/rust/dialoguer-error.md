---
title: "[Solution] dialoguer Prompt Error Fix"
description: "Fix dialoguer prompt errors. Handle terminal input, validation, and user interaction."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Dialoguer Error

Dialoguer errors occur when using the `dialoguer` crate for interactive CLI prompts — terminal I/O issues and input validation failures.

## Common Causes

```rust
use dialoguer::{Input, Select};

// Not in raw mode for password input
let password = Input::<String>::new()
    .with_prompt("Password")
    .interact_text()?; // Plain text, not masked

// Empty selection list
let selection = Select::new()
    .items(&[]) // ERROR: no items
    .interact()?;
```

## How to Fix

1. **Use `Password` for sensitive input**

```rust
use dialoguer::Password;

let password = Password::new()
    .with_prompt("Password")
    .with_confirmation("Confirm password", "Passwords don't match")
    .interact()?;

println!("Password length: {}", password.len());
```

2. **Validate selection lists**

```rust
use dialoguer::Select;

let options = vec!["Option 1", "Option 2", "Option 3"];
if options.is_empty() {
    eprintln!("No options available");
    return Ok(());
}

let selection = Select::new()
    .with_prompt("Choose")
    .items(&options)
    .default(0)
    .interact()?;

println!("Selected: {}", options[selection]);
```

3. **Use `Confirm` for yes/no prompts**

```rust
use dialoguer::Confirm;

let confirmed = Confirm::new()
    .with_prompt("Do you want to continue?")
    .default(true)
    .interact()?;

if confirmed {
    println!("Continuing...");
} else {
    println!("Cancelled");
}
```

## Examples

```rust
use dialoguer::{Input, Select, Password, Confirm};

fn main() -> std::io::Result<()> {
    let name: String = Input::new()
        .with_prompt("Your name")
        .default("World".into())
        .interact_text()?;

    let language = Select::new()
        .with_prompt("Language")
        .items(&["Rust", "Python", "Go"])
        .default(0)
        .interact()?;

    let password = Password::new()
        .with_prompt("Password")
        .interact()?;

    let proceed = Confirm::new()
        .with_prompt(format!("Hello {}, continue?", name))
        .interact()?;

    if proceed {
        println!("Selected: {}, Password len: {}", language, password.len());
    }
    Ok(())
}
```

## Related Errors

- [Crossterm Error]({{< relref "/languages/rust/crossterm-error" >}}) — terminal handling
- [Termion Error]({{< relref "/languages/rust/termion-error" >}}) — terminal I/O
- [Indicatif Error]({{< relref "/languages/rust/indicatif-error" >}}) — progress bars
