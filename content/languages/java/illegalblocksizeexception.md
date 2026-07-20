---
title: "[Solution] Java IllegalBlockSizeException — Incorrect Block Size for Cipher"
description: "Fix Java IllegalBlockSizeException by checking data length, verifying cipher mode, and handling padding properly. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 10
---

# IllegalBlockSizeException — Incorrect Block Size for Cipher

`javax.crypto.IllegalBlockSizeException` is thrown when the data length is not a multiple of the cipher's block size, or when the data length exceeds the maximum for the cipher mode.

## Description

This exception occurs during encryption or decryption when the input data does not match the block size requirements. Message variants include:

- `IllegalBlockSizeException: Input length must be multiple of 16`
- `IllegalBlockSizeException: Data must not be longer than 117 bytes`
- `IllegalBlockSizeException: last block incomplete in encryption`

## Common Causes

**1. Data length not multiple of block size (without padding):**
```java
Cipher cipher = Cipher.getInstance("AES/CBC/NoPadding");
byte[] data = new byte[15]; // not a multiple of 16
cipher.init(Cipher.ENCRYPT_MODE, key, ivSpec);
cipher.doFinal(data); // IllegalBlockSizeException
```

**2. RSA encryption with data too large:**
```java
Cipher cipher = Cipher.getInstance("RSA/ECB/PKCS1Padding");
byte[] largeData = new byte[256]; // exceeds RSA key size
cipher.init(Cipher.ENCRYPT_MODE, rsaKey);
cipher.doFinal(largeData); // IllegalBlockSizeException
```

**3. Decryption with wrong data format:**
```java
byte[] wrongData = "not encrypted data".getBytes();
cipher.init(Cipher.DECRYPT_MODE, key);
cipher.doFinal(wrongData); // IllegalBlockSizeException or BadPaddingException
```

**4. Using doFinal multiple times incorrectly:**
```java
cipher.init(Cipher.ENCRYPT_MODE, key);
cipher.doFinal(data1);
cipher.doFinal(data2); // may throw if state is wrong
```

## Solutions

### Fix 1: Use Padding When Needed

```java
// Add PKCS5Padding to handle non-block-aligned data
Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
cipher.init(Cipher.ENCRYPT_MODE, key, ivSpec);
byte[] encrypted = cipher.doFinal(data); // works with any data length
```

### Fix 2: Chunk RSA Encrypted Data

```java
public static byte[] rsaEncrypt(Cipher cipher, byte[] data)
        throws Exception {
    int keySize = cipher.getOutputSize(0);
    int maxBlockSize = keySize - 11; // PKCS1Padding overhead
    // For OAEP: keySize - 2 * 20 - 2

    ByteArrayOutputStream out = new ByteArrayOutputStream();
    int offset = 0;
    while (offset < data.length) {
        int len = Math.min(maxBlockSize, data.length - offset);
        byte[] chunk = Arrays.copyOfRange(data, offset, offset + len);
        out.write(cipher.doFinal(chunk));
        offset += len;
    }
    return out.toByteArray();
}
```

### Fix 3: Verify Data Is Properly Formatted Before Decryption

```java
public static byte[] safeDecrypt(Cipher cipher, byte[] encryptedData)
        throws Exception {
    cipher.init(Cipher.DECRYPT_MODE, key, ivSpec);

    // Verify data length is reasonable for this cipher
    int expectedBlockSize = cipher.getBlockSize();
    if (expectedBlockSize > 0 && encryptedData.length % expectedBlockSize != 0) {
        throw new IllegalBlockSizeException(
            "Data length " + encryptedData.length +
            " is not a multiple of block size " + expectedBlockSize);
    }
    return cipher.doFinal(encryptedData);
}
```

### Fix 4: Use Cipher.update() for Large Data

```java
cipher.init(Cipher.ENCRYPT_MODE, key, ivSpec);
cipher.update(chunk1); // buffered
cipher.update(chunk2); // buffered
byte[] finalBlock = cipher.doFinal(lastChunk); // processes all buffered data
```

## Prevention Checklist

- Use a padding scheme (`PKCS5Padding`) unless you have a specific reason not to
- Limit RSA-encrypted data to key size minus padding overhead
- Verify data is in the correct format before calling `doFinal()` for decryption
- Use `Cipher.update()` to stream large data through the cipher
- Always handle `IllegalBlockSizeException` alongside `BadPaddingException`

## Related Errors

- [BadPaddingException](/languages/java/badpaddingexception)
- [ShortBufferException](/languages/java/shortbufferexception)
- [InvalidKeyException](/languages/java/invalidkeyexception)
