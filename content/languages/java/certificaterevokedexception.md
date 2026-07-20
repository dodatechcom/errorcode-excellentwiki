---
title: "[Solution] Java CertificateRevokedException — Certificate Has Been Revoked"
description: "Fix Java CertificateRevokedException by checking CRL, using OCSP, verifying revocation status, and handling revoked certificates. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 8
---

# CertificateRevokedException — Certificate Has Been Revoked

`java.security.cert.CertificateRevokedException` is thrown when a certificate has been revoked by its issuing Certificate Authority (CA) before its expiration date.

## Description

This exception occurs when certificate revocation checking detects a revoked certificate. Message variants include:

- `CertificateRevokedException: certificate has been revoked`
- `CertificateRevokedException: revocation time: <timestamp>`
- `CertificateRevokedException: reason: keyCompromise`

## Common Causes

**1. Certificate revoked due to key compromise:**
```java
// Server certificate was revoked after private key leak
SSLContext sslContext = SSLContext.getInstance("TLS");
// Handshake fails because server cert is revoked
```

**2. CRL checking finds the certificate:**
```java
CertPathValidator validator = CertPathValidator.getInstance("PKIX");
PKIXParameters params = new PKIXParameters(trustStore);
params.setRevocationEnabled(true); // CRL check enabled
validator.validate(certPath, params); // CertificateRevokedException
```

**3. OCSP responder reports revocation:**
```java
// Online Certificate Status Protocol reports "revoked"
CertificateRevocationChecker checker = new CertificateRevocationChecker();
```

**4. Certificate expired after revocation:**
```java
// Both conditions: revoked and expired
X509Certificate cert = loadCertificate();
cert.checkValidity(); // May show expired, but revocation is separate issue
```

## Solutions

### Fix 1: Check Revocation Status with CRL

```java
public static boolean isRevoked(X509Certificate cert, URL crlUrl)
        throws Exception {
    CertificateFactory cf = CertificateFactory.getInstance("X.509");
    CRL crl = cf.generateCRL(crlUrl.openStream());

    if (crl instanceof X509CRL) {
        X509CRL x509Crl = (X509CRL) crl;
        return x509Crl.isRevoked(cert);
    }
    return false;
}
```

### Fix 2: Use OCSP for Online Revocation Checking

```java
import java.security.cert.CertificateRevocationChecker;
import java.security.cert.PKIXRevocationChecker;
import java.security.cert.PKIXParameters;

TrustManagerFactory tmf = TrustManagerFactory.getInstance("SunX509");
tmf.init(trustStore);

PKIXRevocationChecker rc = new PKIXRevocationChecker();
rc.setOptions(EnumSet.of(PKIXRevocationChecker.Option.NO_FALLBACK));

PKIXParameters params = new PKIXParameters(trustStore);
params.setRevocationEnabled(true);
params.addCertPathChecker(rc);

CertPathValidator validator = CertPathValidator.getInstance("PKIX");
validator.validate(certPath, params);
```

### Fix 3: Handle Revoked Certificates Gracefully

```java
public static SSLContext createSSLContext(KeyManager[] km, TrustManager[] tm)
        throws Exception {
    SSLContext sslContext = SSLContext.getInstance("TLS");
    sslContext.init(km, tm, new SecureRandom());
    return sslContext;
}

// Custom TrustManager that handles revocation
TrustManager[] trustManagers = new TrustManager[]{
    new X509TrustManager() {
        public void checkClientTrusted(X509Certificate[] chain, String authType)
                throws CertificateException {
            try {
                validateCertificate(chain);
            } catch (CertificateRevokedException e) {
                System.err.println("Certificate revoked: " + e.getMessage());
                // Log and handle gracefully — reject connection
                throw new CertificateException("Revoked certificate", e);
            }
        }
        // ... other methods
    }
};
```

### Fix 4: Disable Revocation Checking for Development

```java
// Only for development — NOT for production
System.setProperty("com.sun.security.enableCRLChecks", "false");

// Or set PKIXParameters
PKIXParameters params = new PKIXParameters(trustStore);
params.setRevocationEnabled(false); // disable revocation checking
```

## Prevention Checklist

- Enable revocation checking in production TLS configurations
- Maintain up-to-date CRL distributions or OCSP responder URLs
- Handle `CertificateRevokedException` explicitly in TLS code paths
- Monitor certificate expiration and revocation status proactively
- Do NOT disable revocation checking in production environments

## Related Errors

- [CertificateException](/languages/java/certificateexception)
- [SSLHandshakeException](/languages/java/sslhandshakeexception)
- [GeneralSecurityException](/languages/java/generalsecurityexception)
