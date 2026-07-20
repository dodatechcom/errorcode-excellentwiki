---
title: "[Solution] Java EmptyStackException — Empty Stack Fix"
description: "Fix Java EmptyStackException by checking isEmpty() before pop/peek, using ArrayDeque instead of Stack, and using Optional."
languages: ["java"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# EmptyStackException — Empty Stack Fix

An `EmptyStackException` is thrown when an operation such as `pop()` or `peek()` is performed on an empty stack. This is a subclass of `java.util.EmptyStackException` extending `RuntimeException`.

## Description

The exception occurs when trying to access the top element of a stack that contains no elements. It is part of Java's legacy `Stack` class and is also thrown by other stack-like data structures when they are empty.

## Common Causes

```java
// Cause 1: Popping from an empty Stack
Stack<Integer> stack = new Stack<>();
stack.pop(); // EmptyStackException — stack is empty

// Cause 2: Peeking at an empty Stack
Stack<String> stack = new Stack<>();
stack.peek(); // EmptyStackException — no elements

// Cause 3: Popping from an empty ArrayDeque used as stack
Deque<String> stack = new ArrayDeque<>();
stack.pop(); // EmptyStackException

// Cause 4: Calling lastElement() on empty Vector
Vector<String> vector = new Vector<>();
vector.lastElement(); // EmptyStackException

// Cause 5: Multiple pops exhausting the stack
Stack<Integer> stack = new Stack<>();
stack.push(1);
stack.pop(); // removes 1
stack.pop(); // EmptyStackException — now empty
```

## Solutions

### Fix 1: Check isEmpty() Before pop/peek

```java
Stack<Integer> stack = new Stack<>();
// ... push elements ...

if (!stack.isEmpty()) {
    Integer value = stack.pop();
    // process value
} else {
    // handle empty stack
}
```

### Fix 2: Use ArrayDeque Instead of Stack

```java
Deque<Integer> stack = new ArrayDeque<>();
stack.push(1);
stack.push(2);

Optional<Integer> top = Optional.ofNullable(stack.peek());
top.ifPresent(System.out::println);

if (!stack.isEmpty()) {
    Integer value = stack.pop();
}
```

### Fix 3: Use Optional for Safe Access

```java
public class SafeStack<T> {
    private final Deque<T> deque = new ArrayDeque<>();

    public Optional<T> safePop() {
        return Optional.ofNullable(deque.poll());
    }

    public Optional<T> safePeek() {
        return Optional.ofNullable(deque.peek());
    }
}
```

### Fix 4: Use poll() Instead of pop()

```java
Deque<Integer> stack = new ArrayDeque<>();
stack.push(1);
stack.push(2);

Integer value = stack.poll(); // returns 2, or null if empty
if (value != null) {
    // process value
}
```

### Fix 5: Check Size Before Access

```java
Stack<String> stack = new Stack<>();
// ... push elements ...

if (stack.size() > 0) {
    String top = stack.lastElement();
}
```

## Prevention Checklist

- Always check `isEmpty()` before calling `pop()`, `peek()`, or `lastElement()`
- Prefer `ArrayDeque` over legacy `Stack` class — it is faster and thread-safe for single-threaded use
- Use `poll()` instead of `pop()` when absence of elements is expected
- Use `Optional` return types for methods that may not have a value
- Track stack size to avoid underflow

## Related Errors

- [NoSuchElementException]({{< relref "/languages/java/nosuchelementexception" >}}) — no element in iterator or collection
- [UnsupportedOperationException]({{< relref "/languages/java/unsupportedoperationexception" >}}) — operation not supported
- [IllegalStateException]({{< relref "/languages/java/illegalstateexception" >}}) — object in invalid state
