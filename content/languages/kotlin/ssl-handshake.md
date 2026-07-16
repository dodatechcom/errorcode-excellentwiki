---
title: "[Solution] Kotlin SSLHandshakeException — SSL/TLS Handshake Fix"
description: "Fix Kotlin SSLHandshakeException when SSL/TLS handshake fails. Check certificates, trust stores, and TLS versions."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["sslhandshakeexception", "ssl", "tls", "certificate", "security"]
weight: 5
---

# SSLHandshakeException — SSL/TLS Handshake Fix

An `SSLHandshakeException` is thrown when the SSL/TLS handshake fails. This indicates a problem with the secure connection negotiation between client and server.

## Description

The SSL/TLS handshake involves certificate verification, key exchange, and protocol negotiation. Failure at any step throws this exception. It's a subclass of `IOException`.

Common scenarios:

- **Expired certificate** — server's certificate has expired.
- **Self-signed certificate** — certificate not signed by trusted CA.
- **Hostname mismatch** — certificate doesn't match the hostname.
- **Protocol version mismatch** — client and server support different TLS versions.
- **Missing intermediate certificates** — certificate chain incomplete.

## Common Causes

```kotlin
// Cause 1: Self-signed certificate
val url = URL("https://self-signed.example.com")
url.openConnection()  // SSLHandshakeException

// Cause 2: Expired certificate
val url = URL("https://expired-cert.example.com")
url.openConnection()  // SSLHandshakeException

// Cause 3: Hostname mismatch
// Certificate for *.example.com, connecting to different.example.com
val url = URL("https://different.example.com")
url.openConnection()  // SSLHandshakeException

// Cause 4: Weak protocol
// Server only supports TLS 1.0, client requires TLS 1.2+
val url = URL("https://weak-server.example.com")
url.openConnection()  // SSLHandshakeException
```

## Solutions

### Fix 1: Update trust store (development only)

```kotlin
// WRONG — only for development/testing, never in production!
val trustAllCerts = arrayOf<TrustManager>(object : X509TrustManager {
    override fun checkClientTrusted(chain: Array<X509Certificate>, authType: String) {}
    override fun checkServerTrusted(chain: Array<X509Certificate>, authType: String) {}
    override fun getAcceptedIssuers(): Array<X509Certificate> = arrayOf()
})

val sslContext = SSLContext.getInstance("TLS")
sslContext.init(null, trustAllCerts, java.security.SecureRandom())

val url = URL("https://self-signed.example.com")
val conn = url.openConnection() as HttpsURLConnection
conn.sslSocketFactory = sslContext.socketFactory
```

### Fix 2: Add certificate to trust store (production)

```kotlin
// Correct — add the certificate to the trust store
// keytool -importcert -alias mycert -file cert.pem -keystore truststore.jks

val trustStore = KeyStore.getInstance("JKS")
FileInputStream("truststore.jks").use { fis ->
    trustStore.load(fis, "password".toCharArray())
}

val tmf = TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm())
tmf.init(trustStore)

val sslContext = SSLContext.getInstance("TLS")
sslContext.init(null, tmf.trustManagers, null)
```

### Fix 3: Use OkHttp with certificate pinning

```kotlin
// Using OkHttp with proper certificate handling
val client = OkHttpClient.Builder()
    .certificatePinner(
        CertificatePinner.Builder()
            .add("example.com", "sha256/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=")
            .build()
    )
    .build()
```

### Fix 4: Configure TLS version

```kotlin
// Force specific TLS version
val sslContext = SSLContext.getInstance("TLSv1.2")
sslContext.init(null, null, null)

val factory = sslContext.socketFactory
val socket = factory.createSocket("server", 443)
```

## Examples

```kotlin
import javax.net.ssl.*

fun main() {
    try {
        val url = java.net.URL("https://example.com")
        val connection = url.openConnection() as HttpsURLConnection
        connection.connectTimeout = 5000
        connection.readTimeout = 10_000

        val data = connection.inputStream.bufferedReader().readText()
        println("Connected successfully")
    } catch (e: javax.net.ssl.SSLHandshakeException) {
        println("SSL Handshake failed: ${e.message}")
        println("Check if the server certificate is valid and trusted")
    }
}
```

## Related Errors

- [SocketTimeoutException]({{< relref "/languages/kotlin/socket-timeout" >}}) — connection timed out.
- [ConnectException]({{< relref "/languages/kotlin/connection-refused" >}}) — connection refused.
- [IOException]({{< relref "/languages/kotlin/io-exception" >}}) — general I/O error.
