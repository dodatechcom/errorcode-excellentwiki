---
title: "[Solution] Java StackOverflowError — two methods call each other without termination"
description: "Fix Java StackOverflowError when two methods call each other without termination with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# StackOverflowError — two methods call each other without termination

A `StackOverflowError` occurs when Expr parseExpression() {
    Term t = parseTerm();
    if (match('+')) { Expr r = parseExpression(); ... }
    return t;
}
Term parseTerm() {
    if (match('(')) { Expr e = parseExpression(); ... }
    return parseNumber();
}.

## Common Causes

```java
Expr parseExpression() {
    Term t = parseTerm();
    if (match('+')) { Expr r = parseExpression(); ... }
    return t;
}
Term parseTerm() {
    if (match('(')) { Expr e = parseExpression(); ... }
    return parseNumber();
}
```

## Solutions

```java
// Fix: iterative with explicit stack
void processTree(TreeNode root) {
    Deque<TreeNode> stack = new ArrayDeque<>();
    stack.push(root);
    while (!stack.isEmpty()) {
        TreeNode n = stack.pop();
        process(n);
        if (n.right!=null) stack.push(n.right);
        if (n.left!=null) stack.push(n.left);
    }
}

// Fix: depth limit
void process(TreeNode n, int depth) {
    if (depth > MAX_DEPTH) throw new RuntimeException("max depth");
    if (n.left!=null) process(n.left, depth+1);
    if (n.right!=null) process(n.right, depth+1);
}
```

## Prevention Checklist

- Convert recursion to iterative with explicit stack.
- Add depth counters.
- Use BFS for deep trees.

## Related Errors

OutOfMemoryError, StackOverflowError
