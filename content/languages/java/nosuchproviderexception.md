---
title: "[Solution] Java NoSuchProviderException — Security Provider Not Found"
description: "Fix Java NoSuchProviderException by installing provider, checking provider name, or using default provider. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 3
---

# NoSuchProviderException — Security Provider Not Found

`java.security.NoSuchProviderException` is thrown when a requested security provider is not installed in the JVM.

## Description

When you specify a provider name in a `getInstance()` call, Java looks for that provider among the registered security providers. If the provider is not found, this exception is thrown. Message variants include:

- `NoSuchProviderException: BouncyCastle`
- `NoSuchProviderException: provider "BC" not found`
- `NoSuchProviderException: SunJCE`

## Common Causes

**1. Provider not added to the JVM:**
```java
// BouncyCastle not installed
Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding", "BC");
```

**2. Typo in provider name (case-sensitive):**
```java
// Wrong — "bc" is not "BC"
Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding", "bc");
```

**3. Provider JAR not on classpath:**
```java
// BouncyCastle JAR missing from classpath
Security.addProvider(new BouncyCastleProvider()); // ClassNotFoundException first
```

**4. Using a provider from a different Java version:**
```java
// "SunRsaSign" may not exist in all JDK distributions
Signature sig = Signature.getInstance("SHA256withRSA", "SunRsaSign");
```

## Solutions

### Fix 1: Add the Provider Before Use

```java
import org.bouncycastle.jce.provider.BouncyCastleProvider;
import java.security.Security;

// Register BouncyCastle if not already present
if (Security.getProvider("BC") == null) {
    Security.addProvider(new BouncyCastleProvider());
}

// Now use the provider
Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding", "BC");
```

### Fix 2: Use the Provider Name Case-Sensitively

```java
// Provider names are case-sensitive — use the exact registered name
String providerName = "BC";  // correct
// String providerName = "bc";  // wrong

KeyPairGenerator kpg = KeyPairGenerator.getInstance("RSA", providerName);
```

### Fix 3: Use the Default Provider (Omit Provider Name)

```java
// Use the first available provider that supports the algorithm
Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
// instead of: Cipher.getInstance("AES/CBC/PKCS5Padding", "BC")
```

### Fix 4: Verify Available Providers at Startup

```java
import java.security.Security;

public class SecurityCheck {
    public static void main(String[] args) {
        System.out.println("Available providers:");
        for (Security.Provider provider : Security.getProviders()) {
            System.out.printf("  %s v%s%n", provider.getName(), provider.getVersion());
        }
    }
}
```

## Prevention Checklist

- Add required provider JARs to your build dependencies
- Register providers early in application startup
- Avoid hardcoding provider names — prefer algorithm-only lookups when possible
- Verify provider availability in your target deployment environment
- Use `Security.getProviders()` to audit available providers

## Related Errors

- [NoSuchAlgorithmException](/languages/java/nosuchalgorithmexception)
- [GeneralSecurityException](/languages/java/generalsecurityexception)
- [NoSuchPaddingException](/languages/java/nosuchpaddingexception)
