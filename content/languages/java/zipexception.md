---
title: "[Solution] Java ZipException — Corrupt ZIP Archive Fix"
description: "Fix Java ZipException by verifying archive integrity, re-downloading corrupted files, checking for truncation, and using ZipFile for recovery."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 77
---

# ZipException — Corrupt ZIP Archive Fix

A `ZipException` is thrown when the JVM encounters a ZIP format error while reading or writing a ZIP/JAR file. This can indicate corruption, truncation, or an invalid ZIP structure in the archive.

## Description

`java.util.zip.ZipException` extends `IOException`. Common variants include:

- `java.util.zip.ZipException: invalid entry CRC`
- `java.util.zip.ZipException: invalid entry size`
- `java.util.zip.ZipException: duplicate entry: ...`
- `java.util.zip.ZipException: archive is not a ZIP archive`
- `java.util.zip.ZipException: unexpected end of ZIP file`

This exception is thrown by `ZipFile`, `ZipInputStream`, `ZipOutputStream`, `JarFile`, and `JarOutputStream` when the archive structure does not conform to the ZIP specification.

## Common Causes

```java
// Cause 1: Reading a corrupted ZIP/JAR file
ZipFile zip = new ZipFile("corrupted.jar");  // ZipException: invalid entry CRC

// Cause 2: Writing duplicate entries
ZipOutputStream zos = new ZipOutputStream(new FileOutputStream("out.zip"));
zos.putNextEntry(new ZipEntry("file.txt"));  // first entry
zos.putNextEntry(new ZipEntry("file.txt"));  // ZipException: duplicate entry

// Cause 3: Truncated download
// Network interrupted download of a JAR file
JarFile jar = new JarFile("incomplete.jar");  // ZipException: unexpected end of ZIP file

// Cause 4: Wrong file extension or format
ZipFile zip = new ZipFile("not-a-zip.txt");  // ZipException: not a ZIP archive

// Cause 5: Concurrent access to ZIP file
ZipFile zip = new ZipFile("shared.zip");
// Another process modifying the file while reading
InputStream is = zip.getInputStream(entry);  // ZipException: invalid entry
```

## Solutions

### Fix 1: Verify archive integrity before reading

```java
public static boolean isZipValid(Path path) {
    try (ZipFile zip = new ZipFile(path.toFile())) {
        // Attempt to read all entries
        zip.stream().forEach(e -> {
            try (InputStream is = zip.getInputStream(e)) {
                is.readAllBytes();
            } catch (IOException ex) {
                throw new UncheckedIOException(ex);
            }
        });
        return true;
    } catch (IOException e) {
        return false;
    }
}
```

### Fix 2: Handle duplicate entries in ZipOutputStream

```java
public static void createZipWithoutDuplicates(Path outputPath, Map<String, byte[]> entries)
        throws IOException {
    Set<String> seen = new HashSet<>();
    try (ZipOutputStream zos = new ZipOutputStream(Files.newOutputStream(outputPath))) {
        for (Map.Entry<String, byte[]> entry : entries.entrySet()) {
            if (seen.add(entry.getKey())) {
                zos.putNextEntry(new ZipEntry(entry.getKey()));
                zos.write(entry.getValue());
                zos.closeEntry();
            } else {
                System.err.println("Skipping duplicate entry: " + entry.getKey());
            }
        }
    }
}
```

### Fix 3: Re-download or verify the archive with checksums

```java
public static void verifyJar(Path jarPath, String expectedSha256) throws Exception {
    MessageDigest digest = MessageDigest.getInstance("SHA-256");
    byte[] hash = digest.digest(Files.readAllBytes(jarPath));
    String actual = HexFormat.of().formatHex(hash);

    if (!actual.equals(expectedSha256)) {
        throw new ZipException("Checksum mismatch for " + jarPath);
    }
}
```

### Fix 4: Use try-with-resources to ensure proper cleanup

```java
try (ZipFile zip = new ZipFile("archive.zip")) {
    Enumeration<? extends ZipEntry> entries = zip.entries();
    while (entries.hasMoreElements()) {
        ZipEntry entry = entries.nextElement();
        try (InputStream is = zip.getInputStream(entry)) {
            processEntry(entry.getName(), is);
        }
    }
} catch (ZipException e) {
    System.err.println("ZIP format error: " + e.getMessage());
}
```

## Prevention Checklist

- Always verify JAR/ZIP integrity after download (checksums)
- Use `try-with-resources` when reading ZIP files
- Avoid concurrent access to ZIP files
- Check for truncated files before attempting to read
- Validate ZIP structure using `ZipFile` before passing to other libraries

## Related Errors

- [IOException](/languages/java/ioerror/) — Parent class of ZipException
- [DataFormatException](/languages/java/dataformatexception/) — Related decompression errors
- [FileNotFoundException](/languages/java/ioerror/) — ZIP file not found
