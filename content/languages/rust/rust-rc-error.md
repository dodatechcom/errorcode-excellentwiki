---
title: "[Solution] Rust Rc Error — How to Fix"
description: "Fix Rc reference counting errors. Resolve non-thread-safe shared ownership and reference cycle issues."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# RC Error

RC errors occur when using `Rc` or `Arc` for reference counting — circular references causing memory leaks, use-after-free, or thread-safety violations with `Rc`.

## Common Causes

```rust
use std::rc::Rc;
use std::cell::RefCell;

// Circular reference — memory leak
struct Node {
    value: i32,
    next: Option<Rc<RefCell<Node>>>,
}

let a = Rc::new(RefCell::new(Node { value: 1, next: None }));
let b = Rc::new(RefCell::new(Node { value: 2, next: Some(Rc::clone(&a)) }));
a.borrow_mut().next = Some(Rc::clone(&b)); // Cycle: a -> b -> a

// Using Rc across threads — Rc is !Send + !Sync
use std::thread;
let data = Rc::new(42);
thread::spawn(move || println!("{}", data)); // ERROR: Rc cannot be sent between threads

// Use-after-free: holding reference after last Rc is dropped
```

## How to Fix

1. **Use `Weak<T>` to break reference cycles**

```rust
use std::rc::{Rc, Weak};
use std::cell::RefCell;

struct Node {
    value: i32,
    parent: Weak<RefCell<Node>>,
    children: Vec<Rc<RefCell<Node>>>,
}

let parent = Rc::new(RefCell::new(Node {
    value: 1,
    parent: Weak::new(),
    children: vec![],
}));

let child = Rc::new(RefCell::new(Node {
    value: 2,
    parent: Rc::downgrade(&parent), // Weak reference — no cycle
    children: vec![],
}));

parent.borrow_mut().children.push(Rc::clone(&child));
```

2. **Use `Arc` instead of `Rc` for multi-threaded scenarios**

```rust
use std::sync::{Arc, Mutex};
use std::thread;

let shared = Arc::new(Mutex::new(vec![1, 2, 3]));
let mut handles = vec![];

for i in 0..5 {
    let shared = Arc::clone(&shared);
    handles.push(thread::spawn(move || {
        shared.lock().unwrap().push(i);
    }));
}
for h in handles { h.join().unwrap(); }
println!("{:?}", *shared.lock().unwrap());
```

3. **Use `Rc::strong_count` to debug reference cycles**

```rust
use std::rc::Rc;

let a = Rc::new(String::from("hello"));
println!("Count after creation: {}", Rc::strong_count(&a)); // 1

let b = Rc::clone(&a);
println!("Count after clone: {}", Rc::strong_count(&a)); // 2

drop(b);
println!("Count after drop: {}", Rc::strong_count(&a)); // 1
```

## Examples

```rust
use std::rc::{Rc, Weak};
use std::cell::RefCell;

#[derive(Debug)]
struct Tree {
    value: String,
    parent: Weak<RefCell<Tree>>,
    children: Vec<Rc<RefCell<Tree>>>,
}

fn new_tree(value: &str) -> Rc<RefCell<Tree>> {
    Rc::new(RefCell::new(Tree {
        value: value.to_string(),
        parent: Weak::new(),
        children: vec![],
    }))
}

fn add_child(parent: &Rc<RefCell<Tree>>, child: &Rc<RefCell<Tree>>) {
    child.borrow_mut().parent = Rc::downgrade(parent);
    parent.borrow_mut().children.push(Rc::clone(child));
}

fn main() {
    let root = new_tree("root");
    let child1 = new_tree("child1");
    let child2 = new_tree("child2");

    add_child(&root, &child1);
    add_child(&root, &child2);

    println!("Root: {:?}", root.borrow());
    println!("Root strong count: {}", Rc::strong_count(&root)); // 1 — no cycle
}
```

## Related Errors

- [Arc Error]({{< relref "/languages/rust/rust-arc-error" >}}) — atomic reference counting
- [Mutex Error]({{< relref "/languages/rust/rust-mutex-error" >}}) — thread-safe mutability
- [Cell Error]({{< relref "/languages/rust/rust-cell-error" >}}) — interior mutability
