---
title: "[Solution] Java StackOverflowError — Infinite Recursion Fix"
description: "Fix Java StackOverflowError caused by infinite recursion or deep call stacks. Debug recursive methods, add base cases, and increase -Xss stack size."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
tags: ["stackoverflowerror", "recursion", "stack", "call-stack"]
weight: 50
---

# StackOverflowError — Infinite Recursion Fix

A `StackOverflowError` is thrown when a thread's call stack exceeds its maximum depth. This is almost always caused by infinite recursion — a method that calls itself without a proper base case, or two methods that call each other in a cycle.

## Description

Each method call pushes a frame onto the JVM stack. When the stack is full and a new frame is needed, the JVM throws `StackOverflowError`. This is a subclass of `VirtualMachineError` (not an `Exception`), so catching it with `catch (Exception e)` will not work.

Common variants:

- `java.lang.StackOverflowError`
- `java.lang.StackOverflowError: null` (with no stack trace in some JVM versions)
- Infinite recursion in `toString()`, `hashCode()`, or `equals()` methods.

## Common Causes

```java
// Cause 1: Missing base case in recursion
int factorial(int n) {
    return n * factorial(n - 1);  // no base case — calls forever
}

// Cause 2: Mutual recursion without termination
void methodA() {
    methodB();
}
void methodB() {
    methodA();  // A -> B -> A -> B -> ... StackOverflowError
}

// Cause 3: Circular toString() calls
public class Node {
    Node next;
    public String toString() {
        return "Node{" + next.toString() + "}";  // circular if next == this
    }
}

// Cause 4: Circular equals() / hashCode()
public boolean equals(Object o) {
    return this.equals(o);  // infinite recursion
}

// Cause 5: Circular bean references
public class Parent {
    Child child;
}
public class Child {
    Parent parent;
    // If parent references child which references parent,
    // serialization or deep copy triggers infinite recursion
}
```

## Solutions

### Fix 1: Add a proper base case to recursive methods

```java
// Wrong — no base case
int factorial(int n) {
    return n * factorial(n - 1);
}

// Correct — base case stops the recursion
int factorial(int n) {
    if (n <= 1) return 1;  // base case
    return n * factorial(n - 1);
}

// Even better — use iteration to avoid stack overflow entirely
int factorial(int n) {
    int result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}
```

### Fix 2: Break mutual recursion with a termination flag

```java
// Wrong — unbounded mutual recursion
void methodA() {
    methodB();
}
void methodB() {
    methodA();
}

// Correct — track depth or use a termination condition
void methodA(int depth) {
    if (depth > 100) return;  // safety limit
    methodB(depth + 1);
}
void methodB(int depth) {
    if (depth > 100) return;
    methodA(depth + 1);
}
```

### Fix 3: Fix circular toString() references

```java
// Wrong — circular reference causes infinite toString()
public class Employee {
    Employee manager;
    public String toString() {
        return "Employee{manager=" + manager.toString() + "}";
    }
}

// Correct — break the cycle
public class Employee {
    Employee manager;
    public String toString() {
        if (manager == this) return "Employee{manager=self}";
        return "Employee{name=" + name + "}";
    }
}

// Or use a visited set for complex object graphs
String toString(Object obj, Set<Object> visited) {
    if (obj == null) return "null";
    if (!visited.add(obj)) return "... (circular reference)";
    return obj.toString();
}
```

### Fix 4: Use iterative algorithms instead of recursive

```java
// Wrong — recursive tree traversal may overflow on deep trees
void traverse(TreeNode node) {
    if (node == null) return;
    process(node);
    traverse(node.left);
    traverse(node.right);
}

// Correct — iterative traversal using an explicit stack
void traverse(TreeNode root) {
    Deque<TreeNode> stack = new ArrayDeque<>();
    stack.push(root);
    while (!stack.isEmpty()) {
        TreeNode node = stack.pop();
        if (node == null) continue;
        process(node);
        stack.push(node.right);
        stack.push(node.left);
    }
}
```

### Fix 5: Increase stack size as a temporary fix

```bash
# Default stack is 512 KB — increase it
java -Xss2m -jar myapp.jar

# For very deep recursion
java -Xss8m -jar myapp.jar
```

```java
// Note: Increasing -Xss is a band-aid, not a real fix.
// Deep recursion can still overflow, and it uses more memory per thread.
```

### Fix 6: Use `@tailrec` or compiler optimizations where available

```java
// Java doesn't have @tailrec like Scala, but you can simulate it:
// Convert tail-recursive calls to loops manually.

// Wrong — tail-recursive but JVM still adds stack frames
int sum(int n, int accumulator) {
    if (n == 0) return accumulator;
    return sum(n - 1, accumulator + n);  // tail position, but not optimized
}

// Correct — rewrite as a loop
int sum(int n) {
    int accumulator = 0;
    while (n > 0) {
        accumulator += n;
        n--;
    }
    return accumulator;
}
```

## Debugging Tips

```bash
# Increase stack trace depth in error output
java -XX:MaxJavaStackTraceDepth=-1 -jar myapp.jar

# Enable stack overflow logging
java -XX:+UnlockDiagnosticVMOptions -XX:+DebugNonSafepoints -jar myapp.jar

# Use jstack to dump thread stacks for analysis
jstack <PID> > thread_dump.txt
```

- Look for the repeated pattern in the stack trace — the same method appears hundreds of times.
- Check `toString()`, `hashCode()`, `equals()`, and bean property getters/setters first — they are the most common culprits.

## Related Errors

- [OutOfMemoryError](outofmemoryerror) — heap memory exhausted (different resource than stack).
- [Infinite Loop / CPU 100%](#) — while loop without exit condition (no stack overflow, but CPU spins).
- [ConcurrentModificationException](#) — modifying a collection during iteration.
