---
title: "[Solution] Java NoSuchAlgorithmException — Cryptographic Algorithm Not Available"
description: "Fix Java NoSuchAlgorithmException by checking provider, verifying algorithm name, adding security provider, or using alternative algorithm. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 2
---

# NoSuchAlgorithmException — Cryptographic Algorithm Not Available

`java.security.NoSuchAlgorithmException` is thrown when a requested cryptographic algorithm is not available in the current environment.

## Description

This exception occurs when you request an algorithm (e.g., `"RSA"`, `"AES"`, `"SHA-256"`) that the JVM cannot find in any registered security provider. Common message variants include:

- `NoSuchAlgorithmException: RSA KeyPairGenerator not available`
- `NoSuchAlgorithmException: SHA-256 MessageDigest not available`
- `NoSuchAlgorithmException: AES Cipher not available`
- `NoSuchAlgorithmException: sun.security.rsa.RSASignature$SHA256withRSA not found`

## Common Causes

**1. Typo in algorithm name:**
```java
// Wrong — "SHA256withRSA" is valid but "SHA256_WITH_RSA" is not
Signature sig = Signature.getInstance("SHA256_WITH_RSA");
```

**2. Provider does not support the algorithm:**
```java
// BouncyCastle not added — some algorithms may be missing
Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
```

**3. Restricted security environment (e.g., FIPS mode):**
```java
// FIPS-compliant JVMs may not support certain algorithms
KeyPairGenerator kpg = KeyPairGenerator.getInstance("RSA");
```

**4. Algorithm removed in newer Java versions:**
```java
// MD5-based RSA signatures deprecated in newer JDKs
Signature sig = Signature.getInstance("MD5withRSA");
```

**5. Incorrect transformation string:**
```java
// Wrong — missing padding scheme
Cipher cipher = Cipher.getInstance("AES");
```

## Solutions

### Fix 1: Check and Correct the Algorithm Name

```java
// Correct standard algorithm names
MessageDigest md = MessageDigest.getInstance("SHA-256");     // not "SHA256"
Signature sig = Signature.getInstance("SHA256withRSA");     // correct
Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding"); // include mode and padding
```

### Fix 2: Add BouncyCastle Provider

```java
import org.bouncycastle.jce.provider.BouncyCastleProvider;
import java.security.Security;

// Add BouncyCastle before calling getInstance
if (Security.getProvider("BC") == null) {
    Security.addProvider(new BouncyCastleProvider());
}

Signature sig = Signature.getInstance("SHA256withRSA", "BC");
```

**Maven dependency:**
```xml
<dependency>
    <groupId>org.bouncycastle</groupId>
    <artifactId>bcprov-jdk18on</artifactId>
    <version>1.77</version>
</dependency>
```

### Fix 3: Use a Fallback Algorithm

```java
public static MessageDigest getDigest() {
    String[] algorithms = {"SHA-256", "SHA-384", "SHA-512"};
    for (String alg : algorithms) {
        try {
            return MessageDigest.getInstance(alg);
        } catch (NoSuchAlgorithmException e) {
            // Continue to next algorithm
        }
    }
    throw new RuntimeException("No secure hash algorithm available");
}
```

### Fix 4: Specify the Provider Explicitly

```java
// Use a specific provider that supports the algorithm
KeyPairGenerator kpg = KeyPairGenerator.getInstance("RSA", "SunRsaSign");
```

## Prevention Checklist

- Verify algorithm names against the Java Cryptography Architecture documentation
- Always include BouncyCastle as a dependency for production applications
- Test crypto operations in the target deployment environment
- List available providers with `Security.getProviders()` during startup
- Use algorithm names from the JCA standard, not informal abbreviations

## Related Errors

- [NoSuchProviderException](/languages/java/nosuchproviderexception)
- [NoSuchPaddingException](/languages/java/nosuchpaddingexception)
- [NoSuchAlgorithmException (Key Generation)](/languages/java/nosuchalgorithmexception-key)
- [GeneralSecurityException](/languages/java/generalsecurityexception)
