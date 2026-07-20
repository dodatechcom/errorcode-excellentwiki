---
title: "[Solution] Java NotLinkException — File Is Not a Symbolic Link Fix"
description: "Fix Java NotLinkException by checking isSymbolicLink(), using Files.readSymbolicLink properly, and verifying file type before symlink operations."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# NotLinkException — File Is Not a Symbolic Link Fix

A `NotLinkException` is thrown when an operation that requires a symbolic link is attempted on a file that is not a symlink. This occurs when `Files.readSymbolicLink()` is called on a regular file, directory, or hard link.

## Description

`java.nio.file.NotLinkException` extends `FileSystemException` and is thrown when the target of a symlink-related operation is not a symbolic link. Common message variants:

- `java.nio.file.NotLinkException: /path/to/file`
- `Not a symbolic link`

## Common Causes

```java
// Cause 1: Reading symlink target on a regular file
Path regularFile = Path.of("/etc/hosts");
Path target = Files.readSymbolicLink(regularFile);  // NotLinkException

// Cause 2: Confusing hard links with symbolic links
Path hardLink = Path.of("/app/data/backup.dat");  // Hard link, not symlink
Path target = Files.readSymbolicLink(hardLink);  // NotLinkException

// Cause 3: Assuming path is a symlink without checking
Path path = Path.of("/app/current");
// Developer assumes /app/current is always a symlink
Path target = Files.readSymbolicLink(path);  // NotLinkException if it's a regular directory

// Cause 4: Configuration file specifies a path assumed to be symlink
String configPath = System.getProperty("deploy.link", "/opt/app/current");
Path linkPath = Path.of(configPath);
Path deployTarget = Files.readSymbolicLink(linkPath);  // NotLinkException

// Cause 5: File was symlink but got replaced with regular file
// During deployment, symlink was replaced with actual directory
Path path = Path.of("/app/active");
// Was symlink yesterday, now it's a real directory
Files.readSymbolicLink(path);  // NotLinkException
```

## Solutions

### Fix 1: Check isSymbolicLink() before reading symlink target

```java
Path path = Path.of("/app/current");

if (Files.isSymbolicLink(path)) {
    Path target = Files.readSymbolicLink(path);
    System.out.println("Symlink points to: " + target);
} else if (Files.isDirectory(path)) {
    System.out.println("Path is a regular directory");
} else if (Files.isRegularFile(path)) {
    System.out.println("Path is a regular file");
}
```

### Fix 2: Safely resolve symlink with fallback

```java
public static Path resolvePath(Path path) throws IOException {
    if (Files.isSymbolicLink(path)) {
        return Files.readSymbolicLink(path).toRealPath();
    }
    return path.toRealPath();
}

// Usage
Path resolved = resolvePath(Path.of("/app/current"));
```

### Fix 3: Verify file type before symlink operations

```java
public static void processPath(Path path) throws IOException {
    if (!Files.exists(path)) {
        throw new NoSuchFileException(path.toString());
    }

    if (Files.isSymbolicLink(path)) {
        handleSymlink(path);
    } else if (Files.isDirectory(path)) {
        handleDirectory(path);
    } else if (Files.isRegularFile(path)) {
        handleFile(path);
    }
}

private static void handleSymlink(Path linkPath) throws IOException {
    Path target = Files.readSymbolicLink(linkPath);
    System.out.println(linkPath + " -> " + target);

    // Verify target exists
    Path resolvedTarget = linkPath.resolveSibling(target);
    if (!Files.exists(resolvedTarget)) {
        System.err.println("Broken symlink: " + linkPath);
    }
}
```

### Fix 4: Handle both symlinks and regular paths transparently

```java
public static Stream<Path> walkWithSymlinkResolution(Path start, int maxDepth)
        throws IOException {
    return Files.walk(start, maxDepth, FileVisitOption.FOLLOW_LINKS)
        .filter(path -> {
            try {
                if (Files.isSymbolicLink(path)) {
                    Path target = Files.readSymbolicLink(path);
                    return Files.exists(path.resolveSibling(target));
                }
                return true;
            } catch (IOException e) {
                return false;
            }
        });
}

// Usage
walkWithSymlinkResolution(Path.of("/app"), 5)
    .forEach(System.out::println);
```

### Fix 5: Check and handle all link types

```java
public static void describeFileType(Path path) throws IOException {
    if (Files.isSymbolicLink(path)) {
        Path target = Files.readSymbolicLink(path);
        System.out.println("Symbolic link: " + path + " -> " + target);
    } else if (Files.exists(path)) {
        // Check for hard links by link count
        try {
            BasicFileAttributes attrs = Files.readAttributes(path,
                BasicFileAttributes.class, LinkOption.NOFOLLOW_LINKS);
            // On POSIX systems, link count > 1 means hard links
            System.out.println("Regular file: " + path);
        } catch (IOException e) {
            System.out.println("Path: " + path);
        }
    } else {
        System.out.println("Non-existent path: " + path);
    }
}
```

### Fix 6: Use try-catch for graceful symlink handling

```java
Path linkPath = Path.of("/app/current");

try {
    Path target = Files.readSymbolicLink(linkPath);
    System.out.println("Resolved: " + target.toRealPath());
} catch (NotLinkException e) {
    // Path is not a symlink — use it directly
    if (Files.isDirectory(linkPath)) {
        System.out.println("Using directory directly: " + linkPath);
    } else {
        System.err.println("Path is neither a symlink nor a directory: " + linkPath);
    }
}
```

## Prevention Checklist

- Always check `Files.isSymbolicLink()` before calling `Files.readSymbolicLink()`.
- Handle `NotLinkException` gracefully when path type may vary between environments.
- Use `FileVisitOption.FOLLOW_LINKS` with `Files.walk()` to transparently resolve symlinks.
- Verify symlink targets exist after resolution to detect broken links.
- Test symlink handling across all target operating systems.

## Related Errors

- [NoSuchFileException](../nosuchfileexception) — symlink target does not exist.
- [FileSystemLoopException](../filesystemloopexception) — symlink cycle detected.
- [NotDirectoryException](../notdirectoryexception) — file is not a directory.
- [IOException](../ioexception) — parent class for all I/O failures.
