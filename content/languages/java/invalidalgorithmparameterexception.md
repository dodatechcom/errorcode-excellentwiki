---
title: "[Solution] Java InvalidAlgorithmParameterException — Invalid Algorithm Parameters"
description: "Fix Java InvalidAlgorithmParameterException by verifying parameter values, checking algorithm requirements, and using correct parameter spec. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# InvalidAlgorithmParameterException — Invalid Algorithm Parameters

`java.security.InvalidAlgorithmParameterException` is thrown when algorithm parameters are invalid, incompatible, or do not meet the algorithm's requirements.

## Description

This exception occurs when you pass parameters that the algorithm cannot accept. Message variants include:

- `InvalidAlgorithmParameterException: parameters not valid for EC`
- `InvalidAlgorithmParameterException: IV must be 16 bytes for AES/CBC`
- `InvalidAlgorithmParameterException: Invalid parameter for RSA`
- `InvalidAlgorithmParameterException: null parameter`

## Common Causes

**1. Wrong IV (Initialization Vector) size:**
```java
byte[] wrongIV = new byte[8]; // 8 bytes — AES/CBC needs 16
IvParameterSpec ivSpec = new IvParameterSpec(wrongIV);
Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
cipher.init(Cipher.ENCRYPT_MODE, key, ivSpec); // InvalidAlgorithmParameterException
```

**2. Invalid key size for the algorithm:**
```java
AlgorithmParameterSpec paramSpec = new RSAKeyGenParameterSpec(512, RSAKeyGenParameterSpec.F4);
KeyPairGenerator kpg = KeyPairGenerator.getInstance("RSA");
kpg.initialize(paramSpec); // May throw if size too small
```

**3. Null or empty parameter spec:**
```java
Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
cipher.init(Cipher.ENCRYPT_MODE, key, null); // may fail for some modes
```

**4. Incompatible parameters for key generation:**
```java
ECGenParameterSpec ecSpec = new ECGenParameterSpec("invalid-curve-name");
KeyPairGenerator kpg = KeyPairGenerator.getInstance("EC");
kpg.initialize(ecSpec); // InvalidAlgorithmParameterException
```

**5. Salt or iteration count out of range:**
```java
PBEParameterSpec pbeSpec = new PBEParameterSpec(salt, -1); // negative iterations
```

## Solutions

### Fix 1: Use Correct IV Size

```java
// AES/CBC requires a 16-byte IV
byte[] iv = new byte[16];
SecureRandom random = new SecureRandom();
random.nextBytes(iv);
IvParameterSpec ivSpec = new IvParameterSpec(iv);

Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
cipher.init(Cipher.ENCRYPT_MODE, key, ivSpec);
```

### Fix 2: Use Valid EC Curve Names

```java
// Use standard curve names
ECGenParameterSpec ecSpec = new ECGenParameterSpec("secp256r1"); // not "invalid"
KeyPairGenerator kpg = KeyPairGenerator.getInstance("EC");
kpg.initialize(ecSpec);
```

### Fix 3: Provide GCM Parameters Correctly

```java
GCMParameterSpec gcmSpec = new GCMParameterSpec(128, iv); // 128-bit tag, 12-byte IV
Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
cipher.init(Cipher.ENCRYPT_MODE, key, gcmSpec);
```

### Fix 4: Use Valid PBE Parameters

```java
// Salt must be non-null, iterations must be positive
byte[] salt = new byte[16];
new SecureRandom().nextBytes(salt);
PBEParameterSpec pbeSpec = new PBEParameterSpec(salt, 10000); // positive iteration count
```

## Prevention Checklist

- Verify IV length matches the cipher mode requirements (16 bytes for AES/CBC, 12 bytes for AES/GCM)
- Use standard, well-known curve names for EC algorithms
- Set positive iteration counts for PBE algorithms
- Check parameter compatibility before calling `init()`
- Use JCA-standard parameter spec classes (e.g., `GCMParameterSpec`, `IvParameterSpec`)

## Related Errors

- [InvalidKeyException](/languages/java/invalidkeyexception)
- [NoSuchAlgorithmException](/languages/java/nosuchalgorithmexception)
- [NoSuchPaddingException](/languages/java/nosuchpaddingexception)
- [InvalidParameterSpecException](/languages/java/invalidalgorithmspecexception)
