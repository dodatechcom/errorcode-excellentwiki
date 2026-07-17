---
title: "[Solution] C Is a directory: EISDIR"
description: "Fix C is a directory (EISDIR). Don't use directory paths for file operations."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Is a directory: EISDIR

EISDIR occurs when you try to open, read, or write a path that is actually a directory. Directories are not regular files and cannot be read with standard file I/O.

## Common Causes

```c
// Cause 1: Reading a directory as file
int fd = open("/home/user", O_RDONLY); // EISDIR

// Cause 2: Writing to directory path
write(fd, "data", 4); // if fd points to directory

// Cause 3: Using fopen on directory
FILE *f = fopen("/tmp", "r"); // EISDIR
```

## How to Fix

### Fix 1: Check if path is directory

```c
struct stat st;
if (stat(path, &st) == 0 && S_ISDIR(st.st_mode)) {
    fprintf(stderr, "%s is a directory\n", path);
}
```

### Fix 2: Use directory functions

```c
DIR *dir = opendir("/home/user");
if (dir) {
    struct dirent *entry;
    while ((entry = readdir(dir)) != NULL) {
        printf("%s\n", entry->d_name);
    }
    closedir(dir);
}
```

### Fix 3: Add filename to path

```c
char path[256];
snprintf(path, sizeof(path), "%s/%s", dir_path, filename);
```

## Related Errors

- [Not a directory]({{< relref "/languages/c/not-a-directory" >}}) — ENOTDIR.
- [No such file]({{< relref "/languages/c/no-such-file" >}}) — ENOENT.
- [Bad file descriptor]({{< relref "/languages/c/bad-file-descriptor" >}}) — EBADF.
