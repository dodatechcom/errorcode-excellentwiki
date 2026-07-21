---
title: "[Solution] R write.table Error"
description: "write.table fails to export data."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R write.table Error

write.table fails to export data.

### Common Causes
Object not data frame; file not writable

### How to Fix
```r
df <- as.data.frame(my_data)
write.table(df, "output.txt", row.names = FALSE)
```

### Examples
```r
write.table(as.data.frame(my_list), "out.txt", row.names = FALSE, sep = "\t")
```
