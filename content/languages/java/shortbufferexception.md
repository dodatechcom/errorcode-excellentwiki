---
title: "[Solution] Java ShortBufferException — Output Buffer Too Small"
description: "Fix Java ShortBufferException by calculating required size, using correct buffer size, and checking cipher output size. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 12
---

# ShortBufferException — Output Buffer Too Small

`javax.crypto.ShortBufferException` is thrown when the output buffer provided to a cipher operation is too small to hold the result.

## Description

This exception occurs when you use the `cipher.update()` or `cipher.doFinal()` methods with a pre-allocated buffer that is too small. Message variants include:

- `ShortBufferException: Output buffer too small`
- `ShortBufferException: Required buffer size exceeded`
- `ShortBufferException: Not enough space in output buffer`

## Common Causes

**1. Buffer too small for encrypted data:**
```java
Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
cipher.init(Cipher.ENCRYPT_MODE, key, ivSpec);
byte[] output = new byte[10]; // AES adds padding — needs at least 16 bytes
cipher.doFinal(data, 0, data.length, output, 0); // ShortBufferException
```

**2. Wrong buffer size calculation:**
```java
byte[] output = new byte[data.length]; // too small — padding adds bytes
cipher.doFinal(data, 0, data.length, output, 0); // ShortBufferException
```

**3. Decryption buffer too small:**
```java
// Encrypted data is 32 bytes, but buffer is only 16
byte[] output = new byte[16];
cipher.doFinal(encryptedData, 0, encryptedData.length, output, 0);
// ShortBufferException
```

**4. Using offset incorrectly:**
```java
byte[] output = new byte[64];
// Starting at offset 50 leaves only 14 bytes of space
cipher.doFinal(data, 0, data.length, output, 50); // ShortBufferException
```

## Solutions

### Fix 1: Use the Output Buffer Size Method

```java
Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
cipher.init(Cipher.ENCRYPT_MODE, key, ivSpec);

// Get the exact required output size
int outputSize = cipher.getOutputSize(data.length);
byte[] output = new byte[outputSize];
cipher.doFinal(data, 0, data.length, output, 0);
```

### Fix 2: Use the Return-Value Version

```java
Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
cipher.init(Cipher.ENCRYPT_MODE, key, ivSpec);

// doFinal returns a new byte array of the correct size
byte[] encrypted = cipher.doFinal(data); // no buffer needed
```

### Fix 3: Pre-Calculate for Streaming Operations

```java
Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
cipher.init(Cipher.ENCRYPT_MODE, key, gcmSpec);

// For streaming, allocate extra space
int maxOutput = cipher.getOutputSize(chunkSize) + 256;
byte[] buffer = new byte[maxOutput];

int bytesRead;
while ((bytesRead = input.read(data)) != -1) {
    int outputLen = cipher.update(data, 0, bytesRead, buffer, 0);
    output.write(buffer, 0, outputLen);
}
int finalLen = cipher.doFinal(buffer, 0);
output.write(buffer, 0, finalLen);
```

### Fix 4: Handle Buffer for Both Encrypt and Decrypt

```java
public static byte[] safeCipher(Cipher cipher, byte[] input)
        throws Exception {
    int outputSize = cipher.getOutputSize(input.length);
    byte[] output = new byte[outputSize];
    int len = cipher.doFinal(input, 0, input.length, output, 0);
    return Arrays.copyOf(output, len);
}
```

## Prevention Checklist

- Always call `cipher.getOutputSize(data.length)` before allocating buffers
- Use the version of `doFinal()` that returns a `byte[]` when possible
- Account for IV, authentication tag, and padding when pre-calculating buffer sizes
- For GCM mode, add 16 bytes to account for the authentication tag
- Test with worst-case data sizes, not just typical inputs

## Related Errors

- [IllegalBlockSizeException](/languages/java/illegalblocksizeexception)
- [BadPaddingException](/languages/java/badpaddingexception)
- [BufferOverflowException](/languages/java/bufferoverflowexception)
