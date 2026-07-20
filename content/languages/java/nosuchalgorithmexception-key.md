---
title: "[Solution] Java NoSuchAlgorithmException — Key Generation Algorithm Not Found"
description: "Fix Java NoSuchAlgorithmException for key generation by checking algorithm name, verifying provider, and using standard algorithm names. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 17
---

# NoSuchAlgorithmException — Key Generation Algorithm Not Found

`java.security.NoSuchAlgorithmException` is thrown when the requested key generation algorithm is not available in the registered security providers.

## Description

This specific variant of `NoSuchAlgorithmException` occurs when calling `KeyPairGenerator.getInstance()` or `KeyGenerator.getInstance()` with an algorithm name that no provider supports. Message variants include:

- `NoSuchAlgorithmException: RSA KeyPairGenerator not available`
- `NoSuchAlgorithmException: EC KeyGenerator not available`
- `NoSuchAlgorithmException: sun.security.ec.ECKeyPairGenerator not found`
- `NoSuchAlgorithmException: KeyGenerator not available for AES`

## Common Causes

**1. Algorithm name not recognized:**
```java
// Wrong — "RSA" is correct, "Rsa" or "rsa" may not work
KeyPairGenerator kpg = KeyPairGenerator.getInstance("Rsa");
```

**2. KeyPairGenerator vs KeyGenerator confusion:**
```java
// Wrong — use KeyGenerator for symmetric keys
KeyPairGenerator kpg = KeyPairGenerator.getInstance("AES");
// Use: KeyGenerator.getInstance("AES")
```

**3. Algorithm removed or restricted in newer JDK:**
```java
// DSA key generation may not be available in all distributions
KeyPairGenerator kpg = KeyPairGenerator.getInstance("DSA");
```

**4. FIPS mode restricts available algorithms:**
```java
// Non-FIPS algorithms unavailable in FIPS-compliant JVMs
KeyGenerator kg = KeyGenerator.getInstance("Blowfish");
```

**5. Custom provider not registered:**
```java
// Ed25519 may require a specific provider
KeyPairGenerator kpg = KeyPairGenerator.getInstance("Ed25519");
```

## Solutions

### Fix 1: Use Correct Algorithm Names

```java
// Symmetric key generation
KeyGenerator aesKg = KeyGenerator.getInstance("AES");
aesKg.init(256);
SecretKey aesKey = aesKg.generateKey();

// Asymmetric key pair generation
KeyPairGenerator rsaKpg = KeyPairGenerator.getInstance("RSA");
rsaKpg.initialize(2048);
KeyPair rsaKeyPair = rsaKpg.generateKeyPair();
```

### Fix 2: Use the Right Generator Class

```java
// For symmetric keys (AES, ChaCha20, HmacSHA256)
KeyGenerator keyGen = KeyGenerator.getInstance("ChaCha20");
keyGen.init(256);
SecretKey key = keyGen.generateKey();

// For asymmetric key pairs (RSA, EC, Ed25519)
KeyPairGenerator keyPairGen = KeyPairGenerator.getInstance("EC");
keyPairGen.initialize(new ECGenParameterSpec("secp256r1"));
KeyPair keyPair = keyPairGen.generateKeyPair();
```

### Fix 3: Add BouncyCastle for Extended Algorithm Support

```java
import org.bouncycastle.jce.provider.BouncyCastleProvider;
import java.security.Security;

Security.addProvider(new BouncyCastleProvider());

// Now use BouncyCastle-supported algorithms
KeyPairGenerator edKpg = KeyPairGenerator.getInstance("Ed25519", "BC");
KeyPair edKeyPair = edKpg.generateKeyPair();
```

### Fix 4: List Available Key Generation Algorithms

```java
import java.security.Provider;
import java.security.Security;

public class AvailableKeyAlgorithms {
    public static void main(String[] args) {
        for (Provider provider : Security.getProviders()) {
            for (Provider.Service service : provider.getServices()) {
                if ("KeyPairGenerator".equals(service.getType()) ||
                    "KeyGenerator".equals(service.getType())) {
                    System.out.printf("%s: %s%n",
                        service.getType(), service.getAlgorithm());
                }
            }
        }
    }
}
```

## Prevention Checklist

- Use standard algorithm names: `AES`, `RSA`, `EC`, `Ed25519`, `Ed448`
- Use `KeyGenerator` for symmetric keys and `KeyPairGenerator` for asymmetric keys
- Add BouncyCastle dependency for algorithms not in the default JCA provider
- Verify algorithm availability in your target JVM at startup
- Prefer well-supported algorithms (`AES`, `RSA`, `EC`) over exotic ones

## Related Errors

- [NoSuchAlgorithmException](/languages/java/nosuchalgorithmexception)
- [NoSuchProviderException](/languages/java/nosuchproviderexception)
- [InvalidAlgorithmParameterException](/languages/java/invalidalgorithmparameterexception)
- [InvalidKeyException](/languages/java/invalidkeyexception)
