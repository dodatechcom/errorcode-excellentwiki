---
title: "[Solution] Java UTFDataFormatException — Malformed UTF-8 Fix"
description: "Fix Java UTFDataFormatException by validating UTF-8 data, checking string length limits, and handling encoding errors properly."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# UTFDataFormatException — Malformed UTF-8 Fix

A `UTFDataFormatException` is thrown when malformed modified UTF-8 string data is encountered while reading from a `DataInputStream`. This exception indicates the byte sequence does not conform to Java's modified UTF-8 encoding format.

## Description

`java.io.UTFDataFormatException` extends `IOException` and is thrown by `DataInputStream.readUTF()`. Java uses a modified UTF-8 encoding (not standard UTF-8) for serialization strings, and this exception occurs when the byte stream contains invalid sequences.

Common message variants:

- `java.io.UTFDataFormatException`
- `invalid modified UTF-8 byte sequence`
- `Input length = X`
- `malformed input around byte X`

## Common Causes

```java
// Cause 1: Reading non-UTF-8 data with readUTF()
byte[] notUtf8 = new byte[]{0x00, 0x05, (byte) 0xFF, (byte) 0xFE};
DataInputStream dis = new DataInputStream(new ByteArrayInputStream(notUtf8));
dis.readUTF();  // UTFDataFormatException

// Cause 2: Data written with writeUTF but corrupted in transit
// Writer uses modified UTF-8; reader expects modified UTF-8
// If bytes are modified during network transfer, readUTF() fails

// Cause 3: String exceeds 65535 bytes length limit
// writeUTF() encodes string length as 2-byte unsigned short (max 65535)
// Strings longer than this cannot be written with writeUTF()

// Cause 4: Reading from wrong offset in stream
DataInputStream dis = new DataInputStream(inputStream);
String s1 = dis.readUTF();
String s2 = dis.readUTF();  // UTFDataFormatException if s1 was corrupted

// Cause 5: Mixing DataInputStream.readUTF() with standard UTF-8
// DataOutputStream.writeUTF() uses modified UTF-8, not standard UTF-8
byte[] data = "Hello".getBytes(StandardCharsets.UTF_8);  // Standard UTF-8
DataInputStream dis = new DataInputStream(new ByteArrayInputStream(data));
dis.readUTF();  // UTFDataFormatException — expects modified UTF-8 length prefix
```

## Solutions

### Fix 1: Use DataInputStream/DataOutputStream pair for readUTF/writeUTF

```java
// Correct — use matching writeUTF/readUTF pair
ByteArrayOutputStream baos = new ByteArrayOutputStream();
DataOutputStream dos = new DataOutputStream(baos);
dos.writeUTF("Hello World");
dos.flush();

byte[] data = baos.toByteArray();
DataInputStream dis = new DataInputStream(new ByteArrayInputStream(data));
String result = dis.readUTF();  // Works correctly
```

### Fix 2: Validate string length before writing with writeUTF

```java
public static void safeWriteUTF(DataOutputStream dos, String str) throws IOException {
    if (str == null) {
        dos.writeUTF("");
        return;
    }
    // Modified UTF-8 encoding: max 65535 bytes
    // ASCII chars = 1 byte each, so max 65535 chars for ASCII
    if (str.length() > 65535) {
        throw new IllegalArgumentException(
            "String too long for writeUTF: " + str.length() + " chars");
    }
    dos.writeUTF(str);
}
```

### Fix 3: Validate UTF-8 byte sequences before decoding

```java
public static boolean isValidModifiedUtf8(byte[] data, int offset, int length) {
    int end = offset + length;
    int i = offset;
    while (i < end) {
        int b = data[i] & 0xFF;
        int skip;
        if (b <= 0x7F) {        // 0xxxxxxx
            skip = 0;
        } else if ((b & 0xE0) == 0xC0) {  // 110xxxxx
            skip = 1;
        } else if ((b & 0xF0) == 0xE0) {  // 1110xxxx
            skip = 2;
        } else {
            return false;  // Invalid leading byte
        }
        i += skip + 1;
        if (i > end) return false;  // Truncated sequence
    }
    return true;
}

// Usage
byte[] rawData = readFromNetwork();
if (isValidModifiedUtf8(rawData, 2, rawData.length - 2)) {
    DataInputStream dis = new DataInputStream(new ByteArrayInputStream(rawData));
    String value = dis.readUTF();
} else {
    // Handle corrupt data
}
```

### Fix 4: Use standard UTF-8 instead of readUTF() for interoperability

```java
// Instead of DataInputStream.readUTF(), use standard decoding
byte[] data = readFromNetwork();
String result = new String(data, StandardCharsets.UTF_8);

// For writing
byte[] bytes = str.getBytes(StandardCharsets.UTF_8);
```

### Fix 5: Handle truncation by wrapping readUTF in try-catch

```java
public static String readUTFSafely(DataInputStream dis) {
    try {
        return dis.readUTF();
    } catch (UTFDataFormatException e) {
        throw new SerializationException("Corrupt UTF-8 data in stream", e);
    } catch (IOException e) {
        throw new SerializationException("I/O error reading UTF string", e);
    }
}
```

## Prevention Checklist

- Always use `DataOutputStream.writeUTF()` and `DataInputStream.readUTF()` as a matching pair.
- Validate string length is within the 65535-byte modified UTF-8 limit before writing.
- Never mix `readUTF()` with data encoded using standard `String.getBytes()`.
- Validate byte sequences before decoding if data来源 is untrusted.
- Use standard UTF-8 encoding (`new String(bytes, StandardCharsets.UTF_8)`) for cross-platform interop.

## Related Errors

- [EOFException](../eofexception) — stream ended prematurely during read.
- [StreamCorruptedException](../streamcorruptedexception) — serialized stream corruption.
- [IOException](../ioexception) — parent class for all I/O failures.
