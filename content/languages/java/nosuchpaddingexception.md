---
title: "[Solution] Java NoSuchPaddingException — Padding Scheme Not Available"
description: "Fix Java NoSuchPaddingException by verifying padding name, checking provider capabilities, and using standard padding. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 9
---

# NoSuchPaddingException — Padding Scheme Not Available

`javax.crypto.NoSuchPaddingException` is thrown when the requested padding scheme is not available in the current security configuration.

## Description

This exception occurs when you specify a padding scheme in a cipher transformation that the JVM cannot find. Message variants include:

- `NoSuchPaddingException: PKCS5Padding not available`
- `NoSuchPaddingException: No such padding: ISO10126`
- `NoSuchPaddingException: padding not supported`

## Common Causes

**1. Typo in padding name:**
```java
// Wrong — "PKCS5Padding" is correct
Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5padding"); // case matters
```

**2. Unsupported padding for the mode:**
```java
// GCM mode does not use padding
Cipher cipher = Cipher.getInstance("AES/GCM/PKCS5Padding"); // NoSuchPaddingException
```

**3. Missing provider with the padding implementation:**
```java
// Some padding schemes require BouncyCastle
Cipher cipher = Cipher.getInstance("AES/CBC/ISO10126Padding");
```

**4. Using non-standard padding name:**
```java
Cipher cipher = Cipher.getInstance("AES/CBC/PKCS7"); // wrong — use PKCS5Padding
```

## Solutions

### Fix 1: Use Correct Padding Names

```java
// Standard padding names
Cipher.getInstance("AES/CBC/PKCS5Padding");    // correct
Cipher.getInstance("AES/CBC/NoPadding");        // no padding
Cipher.getInstance("RSA/ECB/PKCS1Padding");     // RSA padding
```

### Fix 2: Do Not Specify Padding for Modes That Do Not Use It

```java
// GCM and CTR are streaming modes — no padding needed
Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
// NOT: "AES/GCM/PKCS5Padding"
```

### Fix 3: Add BouncyCastle for Extended Padding Support

```java
import org.bouncycastle.jce.provider.BouncyCastleProvider;
import java.security.Security;

Security.addProvider(new BouncyCastleProvider());

// Now use BouncyCastle-supported padding
Cipher cipher = Cipher.getInstance("AES/CBC/ISO10126Padding", "BC");
```

### Fix 4: Use NoPadding and Handle Padding Manually

```java
Cipher cipher = Cipher.getInstance("AES/CBC/NoPadding");

// Manual PKCS7 padding
int blockSize = cipher.getBlockSize();
int paddingLength = blockSize - (data.length % blockSize);
byte[] padded = new byte[data.length + paddingLength];
System.arraycopy(data, 0, padded, 0, data.length);
Arrays.fill(padded, data.length, padded.length, (byte) paddingLength);
```

## Prevention Checklist

- Use standard padding names: `PKCS5Padding`, `NoPadding`, `PKCS1Padding`
- Do not specify padding for GCM, CTR, or CFB modes
- Include BouncyCastle dependency for ISO10126Padding or other non-standard padding
- Use `NoPadding` and implement padding manually for full control
- Verify the full transformation string before calling `Cipher.getInstance()`

## Related Errors

- [NoSuchAlgorithmException](/languages/java/nosuchalgorithmexception)
- [NoSuchProviderException](/languages/java/nosuchproviderexception)
- [InvalidKeyException](/languages/java/invalidkeyexception)
- [BadPaddingException](/languages/java/badpaddingexception)
