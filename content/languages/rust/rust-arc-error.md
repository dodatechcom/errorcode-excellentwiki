---
title: "[Solution] Rust Arc Error — How to Fix"
description: "Fix Arc atomic reference counting errors. Resolve shared ownership, thread safety, and reference cycle issues."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# Arc Error

Arc errors occur when using `std::sync::Arc` incorrectly, leading to reference cycles, attempts to mutate shared data through immutable references, or lifetime issues across threads.

## Common Causes

```rust
use std::sync::{Arc, Mutex};

// Attempting to mutate through a shared Arc without interior mutability
let data = Arc::new(vec![1, 2, 3]);
data.push(4); // ERROR: cannot borrow data in Arc via immutable reference

// Creating reference cycles with Arc
struct Node { next: Option<Arc<Mutex<Node>>> }
let a = Arc::new(Mutex::new(Node { next: None }));
let b = Arc::new(Mutex::new(Node { next: Some(Arc::clone(&a)) }));
a.lock().unwrap().next = Some(Arc::clone(&b)); // Cycle: a -> b -> a — memory leak
```

## How to Fix

1. **Use `Arc<Mutex<T>>` for mutable shared data**

```rust
use std::sync::{Arc, Mutex};
use std::thread;

let shared = Arc::new(Mutex::new(vec![1, 2, 3]));
let shared_clone = Arc::clone(&shared);
thread::spawn(move || {
    let mut data = shared_clone.lock().unwrap();
    data.push(4);
}).join().unwrap();

let data = shared.lock().unwrap();
println!("{:?}", *data);
```

2. **Use `Weak<T>` to break reference cycles**

```rust
use std::sync::{Arc, Mutex, Weak};

struct Node { value: i32, parent: Weak<Mutex<Node>>, children: Vec<Arc<Mutex<Node>>> }

let parent = Arc::new(Mutex::new(Node { value: 1, parent: Weak::new(), children: vec![] }));
let child = Arc::new(Mutex::new(Node {
    value: 2,
    parent: Arc::downgrade(&parent), // Weak — no cycle
    children: vec![],
}));
parent.lock().unwrap().children.push(Arc::clone(&child));
```

3. **Clone the Arc explicitly, not by dereferencing**

```rust
use std::sync::Arc;

let original = Arc::new(String::from("hello"));
let cloned = Arc::clone(&original); // Correct: increments ref count
assert_eq!(*original, *cloned);
assert!(Arc::strong_count(&original) == 2);
```

## Examples

```rust
use std::sync::{Arc, RwLock};
use std::thread;

fn main() {
    let config = Arc::new(RwLock::new(std::collections::HashMap::new()));
    let mut handles = vec![];
    for i in 0..5 {
        let config = Arc::clone(&config);
        handles.push(thread::spawn(move || {
            let mut map = config.write().unwrap();
            map.insert(format!("key_{}", i), i * 100);
        }));
    }
    for h in handles { h.join().unwrap(); }
    let map = config.read().unwrap();
    for (k, v) in map.iter() { println!("{}: {}", k, v); }
}
```

## Related Errors

- [Mutex Error]({{< relref "/languages/rust/rust-mutex-error" >}}) — mutex poisoning
- [RwLock Error]({{< relref "/languages/rust/rust-rwlock-error" >}}) — read-write lock issues
- [RC Error]({{< relref "/languages/rust/rust-rc-error" >}}) — reference counted pointers
