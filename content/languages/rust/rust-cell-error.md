---
title: "[Solution] Rust Cell Error — How to Fix"
description: "Fix Cell and RefCell interior mutability errors. Resolve borrow rule violations and runtime borrow checking."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# Cell Error

Cell errors occur when using `std::cell::Cell` or `std::cell::RefCell` incorrectly, such as creating overlapping borrows, using `Cell` with non-Copy types, or borrowing violations at runtime.

## Common Causes

```rust
use std::cell::{Cell, RefCell};

// Cell does not work with non-Copy types
let c = Cell::new(String::from("hello"));
let val = c.get(); // ERROR: String does not implement Copy

// RefCell runtime borrow violations
let r = RefCell::new(vec![1, 2, 3]);
let mut borrow1 = r.borrow_mut();
let borrow2 = r.borrow(); // PANIC: already mutably borrowed

// Using Cell in multi-threaded context (Cell is !Sync)
let c = Cell::new(42);
std::thread::spawn(move || { c.set(100); }); // ERROR: Cell !Send + !Sync
```

## How to Fix

1. **Use `Cell::new` and `Cell::set` only with `Copy` types**

```rust
use std::cell::Cell;

let count = Cell::new(0u32);
count.set(count.get() + 1);
println!("Count: {}", count.get());
```

2. **Check borrow status before borrowing RefCell**

```rust
use std::cell::RefCell;

let r = RefCell::new(vec![1, 2, 3]);

// Check before borrowing
if r.try_borrow().is_ok() {
    let borrow = r.borrow();
    println!("{:?}", *borrow);
}

// Or handle the error
match r.try_borrow_mut() {
    Ok(mut data) => data.push(4),
    Err(e) => eprintln!("Borrow failed: {}", e),
}
```

3. **Use `Cell` or `RefCell` within a `Sync` wrapper for threads**

```rust
use std::cell::RefCell;
use std::sync::Mutex;

// Thread-safe interior mutability
let data = Mutex::new(RefCell::new(vec![1, 2, 3]));
{
    let guard = data.lock().unwrap();
    guard.borrow_mut().push(4);
}
```

## Examples

```rust
use std::cell::{Cell, RefCell};

#[derive(Debug)]
struct Counter {
    count: Cell<u32>,
    log: RefCell<Vec<String>>,
}

impl Counter {
    fn new() -> Self {
        Counter { count: Cell::new(0), log: RefCell::new(vec![]) }
    }
    fn increment(&self) {
        self.count.set(self.count.get() + 1);
        self.log.borrow_mut().push(format!("Incremented to {}", self.count.get()));
    }
}

fn main() {
    let c = Counter::new();
    c.increment();
    c.increment();
    println!("Count: {}", c.count.get());
    println!("Log: {:?}", *c.log.borrow());
}
```

## Related Errors

- [Mutex Error]({{< relref "/languages/rust/rust-mutex-error" >}}) — thread-safe mutability
- [RwLock Error]({{< relref "/languages/rust/rust-rwlock-error" >}}) — read-write locks
- [Arc Error]({{< relref "/languages/rust/rust-arc-error" >}}) — shared ownership
