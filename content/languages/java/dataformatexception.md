---
title: "[Solution] Java DataFormatException — Decompression Data Error Fix"
description: "Fix Java DataFormatException by verifying compressed data integrity, checking GZIP stream format, and handling corrupted input gracefully."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 78
---

# DataFormatException — Decompression Data Error Fix

A `DataFormatException` is thrown when compressed data cannot be decompressed because it is corrupt, truncated, or not in the expected format. This exception is thrown by `java.util.zip.Inflater` when it encounters invalid compressed data.

## Description

`java.util.zip.DataFormatException` extends `Exception` (checked exception). Common variants include:

- `java.util.zip.DataFormatException: invalid stored block lengths`
- `java.util.zip.DataFormatException: incorrect header check`
- `java.util.zip.DataFormatException: invalid distance too far back`
- `java.util.zip.DataFormatException: oversubscribed dynamic bit lengths tree`

The exception indicates the compressed data stream is malformed or the data has been corrupted since compression.

## Common Causes

```java
// Cause 1: Corrupt compressed data
byte[] compressed = loadCompressedData();
Inflater inflater = new Inflater();
inflater.setInput(compressed);
byte[] buffer = new byte[1024];
int result = inflater.inflate(buffer);  // DataFormatException: corrupt data

// Cause 2: Wrong decompression algorithm
// Data compressed with GZIP, decompressed with raw Deflater
Inflater inflater = new Inflater(true);  // nowrap mode for raw deflate
inflater.setInput(gzipCompressedData);   // DataFormatException: wrong header

// Cause 3: Truncated compressed stream
byte[] truncated = Arrays.copyOfRange(compressed, 0, compressed.length / 2);
Inflater inflater = new Inflater();
inflater.setInput(truncated);
inflater.inflate(output);  // DataFormatException: unexpected end of data

// Cause 4: Mixing compression libraries
// Apache Commons Compress output fed to java.util.zip.Inflater
// Different formats/headers

// Cause 5: Data corrupted in transit
// Network transmission without error checking
// Disk corruption affecting the compressed file
```

## Solutions

### Fix 1: Use GZIPInputStream for GZIP-formatted data

```java
import java.util.zip.GZIPInputStream;

public static byte[] decompressGzip(byte[] compressed) throws IOException {
    ByteArrayInputStream bais = new ByteArrayInputStream(compressed);
    try (GZIPInputStream gzis = new GZIPInputStream(bais);
         ByteArrayOutputStream baos = new ByteArrayOutputStream()) {
        byte[] buffer = new byte[1024];
        int len;
        while ((len = gzis.read(buffer)) != -1) {
            baos.write(buffer, 0, len);
        }
        return baos.toByteArray();
    }
}
```

### Fix 2: Verify data integrity before decompression

```java
public static byte[] safeDecompress(byte[] compressed) throws DataFormatException {
    Inflater inflater = new Inflater();
    try {
        inflater.setInput(compressed);
        ByteArrayOutputStream baos = new ByteArrayOutputStream(compressed.length * 2);
        byte[] buffer = new byte[1024];
        while (!inflater.finished()) {
            int count = inflater.inflate(buffer);
            if (count == 0) {
                throw new DataFormatException("Inflate returned 0 — possible corruption");
            }
            baos.write(buffer, 0, count);
        }
        return baos.toByteArray();
    } catch (DataFormatException e) {
        System.err.println("Decompression failed: " + e.getMessage());
        throw e;
    } finally {
        inflater.end();
    }
}
```

### Fix 3: Use try-with-resources for proper cleanup

```java
public static byte[] decompressFile(Path compressedPath) throws IOException {
    try (InflaterInputStream iis = newInflaterInputStream(compressedPath);
         ByteArrayOutputStream baos = new ByteArrayOutputStream()) {
        byte[] buffer = new byte[4096];
        int len;
        while ((len = iis.read(buffer)) != -1) {
            baos.write(buffer, 0, len);
        }
        return baos.toByteArray();
    }
}

private static InflaterInputStream newInflaterInputStream(Path path) throws IOException {
    return new InflaterInputStream(Files.newInputStream(path));
}
```

### Fix 4: Handle decompression errors with fallback

```java
public static byte[] decompressWithFallback(byte[] data) {
    try {
        return safeDecompress(data);
    } catch (DataFormatException e) {
        System.err.println("Decompression failed, returning original data");
        return data;  // or throw, or return null, depending on requirements
    }
}
```

## Prevention Checklist

- Always verify compressed data integrity before decompression
- Use checksums (CRC32, Adler32) to validate compressed streams
- Ensure compression and decompression use the same algorithm and settings
- Use `try-with-resources` for `Inflater` and `InflaterInputStream`
- Store compressed data with length headers or checksums for validation

## Related Errors

- [ZipException](/languages/java/zipexception/) — ZIP format structure errors
- [IOException](/languages/java/ioerror/) — Parent class for I/O decompression failures
- [EOFException](/languages/java/ioerror/) — Unexpected end of compressed stream
