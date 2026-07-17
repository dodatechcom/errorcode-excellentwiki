---
title: "[Solution] R Error — Error in Write Fix"
description: "Fix R 'error in write' when writing data to files. Check file permissions, path, and data structure."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Error in Write — Fix

The error `Error in write(x, file) : error in writing to connection` or `invalid 'ncol' value` occurs when `write()` fails to save data due to file access issues or invalid parameters.

## Common Causes

```r
# Cause 1: File doesn't exist or no write permission
write(1:10, "readonly_file.txt")  # Error if no permission

# Cause 2: Wrong ncol parameter
write(1:10, "data.txt", ncol = 3)  # 10 not divisible by 3

# Cause 3: Non-vector data
write(list(1, 2, 3), "data.txt")  # Error: list not supported

# Cause 4: File path contains special characters
write(1:10, "my file.txt")  # May error with spaces
```

## How to Fix

### Fix 1: Check file permissions

```r
# Wrong
write(1:10, "/root/file.txt")  # Permission denied

# Correct
file_path <- "output.txt"
tryCatch(
  write(1:10, file_path),
  error = function(e) cat("Write error:", conditionMessage(e), "\n")
)
```

### Fix 2: Ensure ncol divides evenly

```r
# Wrong
write(1:10, "data.txt", ncol = 3)

# Correct
write(1:10, "data.txt", ncol = 2)  # 10 / 2 = 5 rows
```

### Fix 3: Convert data before writing

```r
# Wrong
write(list(1, 2, 3), "data.txt")

# Correct
write(unlist(list(1, 2, 3)), "data.txt")
```

### Fix 4: Quote file paths with spaces

```r
# Wrong
write(1:10, my file.txt)

# Correct
write(1:10, "my file.txt")
```

## Examples

```r
# Example 1: Permission denied
write(1:10, "/system/file.txt")
# Error in file(file, "wt") : cannot open the connection

# Example 2: Working write
write(1:10, "numbers.txt", ncol = 2)

# Example 3: Write matrix
mat <- matrix(1:12, nrow = 3, ncol = 4)
write(mat, "matrix.txt", ncol = 4)

# Example 4: Write with append
write("line1", "log.txt")
write("line2", "log.txt", append = TRUE)
```

## Related Errors

- [error-in-read.csv]({{< relref "/languages/r/error-in-read.csv" >}}) — reading data files
- [error-in-cat]({{< relref "/languages/r/error-in-cat" >}}) — cat function error
- [error-in-sink]({{< relref "/languages/r/error-in-sink" >}}) — sink function error
