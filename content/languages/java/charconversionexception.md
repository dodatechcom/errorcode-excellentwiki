---
title: "[Solution] Java CharConversionException — Character Encoding Fix"
description: "Fix Java CharConversionException by using correct charset names, validating encoding, and handling unmappable characters with CodingErrorAction."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# CharConversionException — Character Encoding Fix

A `CharConversionException` is thrown when an invalid character encoding conversion is detected during I/O operations. This occurs when a byte stream is decoded using a charset that cannot represent certain byte sequences.

## Description

`java.io.CharConversionException` extends `IOException` and is thrown by character-stream classes when they encounter bytes that cannot be converted to valid characters. Common message variants:

- `java.io.CharConversionException`
- `Invalid byte sequence found`
- `Input length = 1`

This typically happens with `InputStreamReader`, `OutputStreamWriter`, and `Serializer` classes in serialization libraries.

## Common Causes

```java
// Cause 1: Decoding UTF-8 bytes with wrong charset
byte[] data = "Hello World".getBytes(StandardCharsets.UTF_8);
InputStreamReader reader = new InputStreamReader(
    new ByteArrayInputStream(data), "ISO-8859-1");  // May corrupt multi-byte chars

// Cause 2: Mixing encoding between write and read
FileWriter writer = new FileWriter("file.txt");  // Uses platform encoding
// Later read with different encoding assumption
BufferedReader reader = new BufferedReader(
    new InputStreamReader(new FileInputStream("file.txt"), "UTF-8"));  // CharConversionException

// Cause 3: Invalid byte sequence in data stream
byte[] corrupted = new byte[]{(byte) 0xC0, (byte) 0xAF};  // Invalid UTF-8
InputStreamReader reader = new InputStreamReader(
    new ByteArrayInputStream(corrupted), StandardCharsets.UTF_8);

// Cause 4: Truncated multi-byte character
byte[] partial = "Hello".getBytes(StandardCharsets.UTF_8);
byte[] truncated = Arrays.copyOf(partial, partial.length - 1);  // Cut mid-character
InputStreamReader reader = new InputStreamReader(
    new ByteArrayInputStream(truncated), StandardCharsets.UTF_8);
```

## Solutions

### Fix 1: Use StandardCharsets constants instead of string names

```java
// Wrong — string names can be misspelled or platform-dependent
InputStreamReader reader = new InputStreamReader(is, "UTF8");

// Correct — use StandardCharsets enum
InputStreamReader reader = new InputStreamReader(is, StandardCharsets.UTF_8);
OutputStreamWriter writer = new OutputStreamWriter(os, StandardCharsets.UTF_8);
```

### Fix 2: Handle unmappable characters with CodingErrorAction

```java
import java.nio.charset.CharsetDecoder;
import java.nio.charset.CodingErrorAction;

CharsetDecoder decoder = StandardCharsets.UTF_8.newDecoder()
    .onMalformedInput(CodingErrorAction.REPLACE)
    .onUnmappableCharacter(CodingErrorAction.REPLACE)
    .replaceWith("?");

String text = decoder.decode(ByteBuffer.wrap(data));
```

### Fix 3: Validate encoding before decoding

```java
public static boolean isValidUtf8(byte[] data) {
    CharsetDecoder decoder = StandardCharsets.UTF_8.newDecoder()
        .onMalformedInput(CodingErrorAction.REPORT)
        .onUnmappableCharacter(CodingErrorAction.REPORT);
    try {
        decoder.decode(ByteBuffer.wrap(data));
        return true;
    } catch (CharacterCodingException e) {
        return false;
    }
}

// Usage
if (isValidUtf8(rawBytes)) {
    String text = new String(rawBytes, StandardCharsets.UTF_8);
} else {
    String text = new String(rawBytes, StandardCharsets.ISO_8859_1);
}
```

### Fix 4: Use explicit charset for all file I/O

```java
// Wrong — platform-dependent encoding
BufferedWriter writer = new BufferedWriter(new FileWriter("data.txt"));
BufferedReader reader = new BufferedReader(new FileReader("data.txt"));

// Correct — explicit UTF-8 everywhere
BufferedWriter writer = new BufferedWriter(
    new OutputStreamWriter(new FileOutputStream("data.txt"), StandardCharsets.UTF_8));
BufferedReader reader = new BufferedReader(
    new InputStreamReader(new FileInputStream("data.txt"), StandardCharsets.UTF_8));

// Better — use Files API
Files.writeString(Path.of("data.txt"), content, StandardCharsets.UTF_8);
String content = Files.readString(Path.of("data.txt"), StandardCharsets.UTF_8);
```

### Fix 5: Use Charset.forName() with validation for dynamic charsets

```java
public static Charset resolveCharset(String name, Charset fallback) {
    try {
        Charset charset = Charset.forName(name);
        return charset != null ? charset : fallback;
    } IllegalCharsetNameException | UnsupportedCharsetException e) {
        return fallback;
    }
}

// Usage
Charset charset = resolveCharset(userConfig.getEncoding(), StandardCharsets.UTF_8);
InputStreamReader reader = new InputStreamReader(is, charset);
```

## Prevention Checklist

- Always use `StandardCharsets` constants instead of charset name strings.
- Set the same encoding on both write and read sides of any data pipeline.
- Use `CharsetDecoder` with `CodingErrorAction.REPLACE` for tolerant decoding.
- Verify data integrity before decoding if data来源 is untrusted.
- Use `Files.readString()` and `Files.writeString()` (Java 11+) with explicit charset.

## Related Errors

- [UnsupportedEncodingException](../unsupportedencodingexception) — charset name not recognized by JVM.
- [IOException](../ioexception) — parent class for I/O failures.
- [StreamCorruptedException](../streamcorruptedexception) — serialized stream data corruption.
