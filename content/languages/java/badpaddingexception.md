---
title: "[Solution] Java BadPaddingException — Padding Error During Decryption"
description: "Fix Java BadPaddingException by verifying correct key, checking padding scheme, and ensuring data integrity. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 11
---

# BadPaddingException — Padding Error During Decryption

`javax.crypto.BadPaddingException` is thrown when the padding scheme is incorrect during decryption, typically indicating a wrong key or corrupted ciphertext.

## Description

This exception occurs during `doFinal()` decryption when the decrypted data does not have valid padding. Message variants include:

- `BadPaddingException: Given final block not properly padded`
- `BadPaddingException: Error finalizing padding`
- `BadPaddingException: padding check failed`

## Common Causes

**1. Wrong decryption key:**
```java
// Encrypt with key1, decrypt with key2
cipher.init(Cipher.ENCRYPT_MODE, key1);
byte[] encrypted = cipher.doFinal(data);

cipher.init(Cipher.DECRYPT_MODE, key2); // different key
cipher.doFinal(encrypted); // BadPaddingException
```

**2. Wrong algorithm or mode for decryption:**
```java
// Encrypt with AES/CBC/PKCS5Padding, decrypt with AES/ECB/PKCS5Padding
Cipher encCipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
encCipher.init(Cipher.ENCRYPT_MODE, key, ivSpec);
byte[] encrypted = encCipher.doFinal(data);

Cipher decCipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
decCipher.init(Cipher.DECRYPT_MODE, key);
decCipher.doFinal(encrypted); // BadPaddingException
```

**3. Corrupted ciphertext:**
```java
byte[] encrypted = getEncryptedData();
encrypted[0] ^= 0xFF; // corrupt one byte
cipher.init(Cipher.DECRYPT_MODE, key, ivSpec);
cipher.doFinal(encrypted); // BadPaddingException
```

**4. IV mismatch between encryption and decryption:**
```java
// Encrypt with IV1
cipher.init(Cipher.ENCRYPT_MODE, key, ivSpec1);
byte[] encrypted = cipher.doFinal(data);

// Decrypt with IV2
cipher.init(Cipher.DECRYPT_MODE, key, ivSpec2);
cipher.doFinal(encrypted); // may produce BadPaddingException
```

**5. Truncated ciphertext:**
```java
byte[] fullEncrypted = getEncryptedData();
byte[] truncated = Arrays.copyOf(fullEncrypted, fullEncrypted.length - 1);
cipher.init(Cipher.DECRYPT_MODE, key, ivSpec);
cipher.doFinal(truncated); // BadPaddingException
```

## Solutions

### Fix 1: Verify the Correct Key Is Used

```java
// Store the key securely and retrieve it for decryption
SecretKey key = retrieveKeyFromKeyStore("alias", password);
Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
cipher.init(Cipher.DECRYPT_MODE, key, ivSpec);
byte[] decrypted = cipher.doFinal(encrypted);
```

### Fix 2: Use Matching Algorithm, Mode, and IV

```java
public static byte[] decrypt(byte[] encrypted, SecretKey key, byte[] iv)
        throws Exception {
    // Use exactly the same transformation as encryption
    Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
    IvParameterSpec ivSpec = new IvParameterSpec(iv);
    cipher.init(Cipher.DECRYPT_MODE, key, ivSpec);
    return cipher.doFinal(encrypted);
}
```

### Fix 3: Detect Corruption Before Decryption

```java
// Verify HMAC before decryption
Mac mac = Mac.getInstance("HmacSHA256");
mac.init(hmacKey);
byte[] expectedMac = mac.doFinal(encrypted);

if (!MessageDigest.isEqual(expectedMac, storedMac)) {
    throw new SecurityException("Data integrity check failed — data may be corrupted");
}

// Safe to decrypt
cipher.init(Cipher.DECRYPT_MODE, key, ivSpec);
byte[] decrypted = cipher.doFinal(encrypted);
```

### Fix 4: Handle BadPaddingException Gracefully

```java
try {
    cipher.init(Cipher.DECRYPT_MODE, key, ivSpec);
    byte[] decrypted = cipher.doFinal(encrypted);
} catch (BadPaddingException e) {
    // Key mismatch or corruption — do not reveal which
    throw new SecurityException("Decryption failed", e);
}
```

## Prevention Checklist

- Always use the same algorithm, mode, padding, and IV for encryption and decryption
- Protect the decryption key with a proper key management system
- Implement HMAC verification before decryption to detect tampering
- Never reveal padding error details to end users (security risk)
- Store the IV alongside ciphertext (the IV is not secret)

## Related Errors

- [IllegalBlockSizeException](/languages/java/illegalblocksizeexception)
- [InvalidKeyException](/languages/java/invalidkeyexception)
- [NoSuchPaddingException](/languages/java/nosuchpaddingexception)
