---
title: "[Solution] Rust Use of Moved Value — Value Moved Error"
description: "Fix Rust use of moved value error. Learn why Rust moves ownership and how to use Clone, Copy, or references to fix move errors."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Use of Moved Value — Value Moved Error

A compiler error with the message "use of moved value" occurs when you try to use a variable after its value has been moved to another owner.

## Description

In Rust, assigning a value to a new variable or passing it to a function by value _moves_ ownership. The original variable becomes invalid. This prevents double-free bugs without a garbage collector. Types implementing `Copy` (integers, bools) are copied instead of moved.

Common scenarios:

- **Passing a String to a function** — String is moved, original is invalid.
- **Assigning to another variable** — `let b = a;` moves a into b.
- **Using after `for` loop** — `for x in vec` moves the vec.
- **Returning from match** — value moved in one arm, used in another.

## Common Causes

```rust
// Cause 1: Passing to function
fn print(s: String) { println!("{}", s); }
let name = String::from("Alice");
print(name);
println!("{}", name); // Error: used after move

// Cause 2: Assigning
let s1 = String::from("hello");
let s2 = s1;
println!("{}", s1); // Error: used after move

// Cause 3: Consuming in loop
let items = vec![1, 2, 3];
for item in items { println!("{}", item); }
println!("{:?}", items); // Error: items was moved

// Cause 4: Double use in match
let opt = Some(String::from("data"));
match opt {
    Some(s) => println!("Got: {}", s),
    None => {}
}
match opt { // Error: used after move
    Some(s) => println!("Got: {}", s),
    None => {}
}
```

## Solutions

### Fix 1: Clone the value

```rust
let s1 = String::from("hello");
let s2 = s1.clone();
println!("{} {}", s1, s2); // Both valid
```

### Fix 2: Borrow with & instead of moving

```rust
fn print(s: &str) { println!("{}", s); }
let name = String::from("Alice");
print(&name);
println!("{}", name); // Still valid
```

### Fix 3: Use Copy types when appropriate

```rust
let n1 = 42;
let n2 = n1; // Copied, not moved
println!("{} {}", n1, n2); // Both valid
```

### Fix 4: Iterate by reference

```rust
let items = vec![1, 2, 3];
for item in &items {
    println!("{}", item);
}
println!("Length: {}", items.len()); // Still valid
```

## Examples

```rust
fn main() {
    let greeting = String::from("Hello, world!");
    let moved = greeting;

    println!("{}", greeting);
}
```

Output:
```
error[E0382]: borrow of moved value: `greeting`
```

## Related Errors

- [Borrow Checker]({{< relref "/languages/rust/borrow-checker-2" >}}) — mutable/immutable borrow conflict.
- [Clone]({{< relref "/languages/rust/clone-2" >}}) — value doesn't live long enough.
- [Lifetime]({{< relref "/languages/rust/lifetime-2" >}}) — references don't live long enough.
