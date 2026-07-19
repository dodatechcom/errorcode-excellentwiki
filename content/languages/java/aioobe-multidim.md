---
title: "[Solution] Java ArrayIndexOutOfBoundsException — wrong row or column index in 2D/N-D arrays"
description: "Fix Java ArrayIndexOutOfBoundsException when wrong row or column index in 2d/n-d arrays with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ArrayIndexOutOfBoundsException — wrong row or column index in 2D/N-D arrays

A `ArrayIndexOutOfBoundsException` occurs when int[][] m = {{1,2},{3,4}};
int v = m[5][0];  // AIOOBE — only 2 rows.

## Common Causes

```java
int[][] m = {{1,2},{3,4}};
int v = m[5][0];  // AIOOBE — only 2 rows
```

## Solutions

```java
// Fix: validate both dims
if (row >= 0 && row < m.length && col >= 0 && col < m[row].length) {
    int v = m[row][col];
}

// Fix: safe get
public static int safeGet(int[][] m, int r, int c) {
    if (r<0||r>=m.length) throw new AIOOBE(r);
    if (c<0||c>=m[r].length) throw new AIOOBE(c);
    return m[r][c];
}
```

## Prevention Checklist

- Validate both row and column indices.
- Use matrix.length for rows, matrix[row].length for cols.
- Use Arrays.deepToString() for debugging.

## Related Errors

ArrayIndexOutOfBoundsException, NullPointerException
