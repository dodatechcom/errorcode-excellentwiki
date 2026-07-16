---
title: "[Solution] Rust Borrow Checker — Mutable and Immutable Borrow Conflict"
description: "Fix Rust borrow checker error: cannot borrow as mutable because it is also borrowed as immutable. Learn ownership rules and solutions."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
tags: ["borrow", "mutable", "immutable", "ownership", "reference", "borrow-checker"]
weight: 5
---

# Borrow Checker — Mutable and Immutable Borrow Conflict

A compiler error with the message "cannot borrow as mutable because it is also borrowed as immutable" occurs when you attempt a mutable borrow while an immutable borrow is still active.

## Description

Rust enforces three borrowing rules at compile time:
1. Any number of immutable borrows (`&T`) can coexist.
2. Exactly one mutable borrow (`&mut T`) is allowed at a time.
3. Mutable and immutable borrows cannot overlap.

These rules prevent data races at compile time. The error fires when an `&mut` borrow is created while an `&` borrow is still in scope.

Common scenarios:

- **Modifying while iterating** — pushing to a Vec while iterating over it.
- **Returning a reference then mutating** — holding a reference while changing the data.
- **Two mutable borrows** — creating two `&mut` to the same data.
- **Partial borrows** — borrowing one field while another is mutably borrowed.

## Common Causes

```rust
// Cause 1: Modifying during iteration
let mut v = vec![1, 2, 3];
for item in &v {
    v.push(*item + 10); // Error: immutable borrow during iteration
}

// Cause 2: Reference outlives mutation
let mut data = vec![1, 2, 3];
let first = &data[0]; // immutable borrow
data.push(4);          // mutable borrow conflicts
println!("{}", first);

// Cause 3: Two mutable borrows
let mut x = 5;
let r1 = &mut x;
let r2 = &mut x; // Error: second mutable borrow
println!("{} {}", r1, r2);

// Cause 4: Borrow in closure
let mut data = vec![1, 2, 3];
let len = data.len();
data.iter().for_each(|x| {
    println!("{} (len={})", x, len);
});
data.push(4); // OK here — closure already consumed
```

## Solutions

### Fix 1: Collect first, then mutate

```rust
let mut v = vec![1, 2, 3];
let extras: Vec<i32> = v.iter().map(|x| x * 10).collect();
v.extend(extras);
println!("{:?}", v); // [1, 2, 3, 10, 20, 30]
```

### Fix 2: Copy values before borrowing

```rust
let mut data = vec![1, 2, 3];
let first_val = data[0]; // Copy the value, no borrow
data.push(4);
println!("First was: {}", first_val);
```

### Fix 3: Use split_at_mut for independent borrows

```rust
let mut data = vec![1, 2, 3, 4, 5];
let (left, right) = data.split_at_mut(2);
left[0] = 100;
right[0] = 200;
println!("{:?}", data); // [100, 2, 3, 200, 5]
```

### Fix 4: Use indices instead of references

```rust
let mut v = vec![1, 2, 3];
let len = v.len();
for i in 0..len {
    if v[i] == 2 {
        v.push(42);
    }
}
```

## Examples

```rust
fn main() {
    let mut names = vec!["Alice", "Bob", "Charlie"];

    for name in &names {
        if name.len() > 3 {
            names.push("David");
        }
    }
}
```

Output:
```
error[E0502]: cannot borrow `names` as mutable because it is also borrowed as immutable
```

## Related Errors

- [Move]({{< relref "/languages/rust/move-2" >}}) — using a value after it was moved.
- [Lifetime]({{< relref "/languages/rust/lifetime-2" >}}) — references don't live long enough.
- [Clone]({{< relref "/languages/rust/clone-2" >}}) — value doesn't live long enough.
