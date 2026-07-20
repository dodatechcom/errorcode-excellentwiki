---
title: "[Solution] PHP OpenSSL Certificate Error — Certificate Validation Failed"
description: "Fix PHP OpenSSL certificate error by verifying certificate chain, checking expiration, installing certificates, and validating CA. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 18
---

# PHP OpenSSL Certificate Error — Certificate Validation Failed

A certificate validation error occurred during an OpenSSL operation. This affects SSL/TLS connections, certificate verification, and PKI operations. Common issues include expired certificates, untrusted CAs, and chain validation failures.

## Common Causes

```php
// Cause 1: Expired certificate
$cert = openssl_x509_read(file_get_contents('expired.pem'));
// Certificate past validity period

// Cause 2: Untrusted CA certificate
$ca = file_get_contents('untrusted-ca.pem');
$valid = openssl_x509_verify($cert, $ca); // Returns 0

// Cause 3: Certificate chain incomplete
$context = stream_context_create([
    'ssl' => [
        'verify_peer' => true,
        'cafile' => '/wrong/path/cacert.pem',
    ],
]);
$fp = fopen('https://example.com', 'r', false, $context); // CA not found

// Cause 4: Hostname mismatch
// Certificate issued for different hostname
$context = stream_context_create([
    'ssl' => [
        'verify_peer' => true,
        'verify_peer_name' => true,
    ],
]);
$fp = fopen('https://different.host.com', 'r', false, $context);

// Cause 5: Self-signed certificate
$cert = openssl_x509_read(file_get_contents('self-signed.pem'));
$ca = openssl_x509_read(file_get_contents('self-signed.pem'));
$valid = openssl_x509_verify($cert, $ca); // Self-signed, may not be trusted
```

## How to Fix

### Fix 1: Set Up Proper CA Bundle

```php
// Find the CA bundle path
$caPath = ini_get('openssl.cafile');
if (empty($caPath)) {
    $caPath = '/etc/ssl/certs/ca-certificates.crt';
}

$context = stream_context_create([
    'ssl' => [
        'verify_peer' => true,
        'verify_peer_name' => true,
        'cafile' => $caPath,
    ],
]);
```

```bash
# Download or locate CA certificates
# Ubuntu/Debian: /etc/ssl/certs/ca-certificates.crt
# CentOS/RHEL: /etc/pki/tls/certs/ca-bundle.crt

# Or download Mozilla's CA bundle
curl -o /etc/ssl/certs/ca-certificates.crt https://curl.se/ca/cacert.pem
```

### Fix 2: Verify Certificate Chain

```php
function verifyCertificate(string $certPath, string $caPath): array {
    $cert = openssl_x509_read(file_get_contents($certPath));
    if ($cert === false) {
        return ['valid' => false, 'error' => 'Failed to read certificate'];
    }

    $ca = openssl_x509_read(file_get_contents($caPath));
    if ($ca === false) {
        return ['valid' => false, 'error' => 'Failed to read CA certificate'];
    }

    $result = openssl_x509_verify($cert, $ca);

    $info = openssl_x509_parse($cert);

    return [
        'valid' => $result === 1,
        'subject' => $info['subject']['CN'] ?? 'unknown',
        'issuer' => $info['issuer']['CN'] ?? 'unknown',
        'valid_from' => date('Y-m-d', $info['validFrom_time_t']),
        'valid_to' => date('Y-m-d', $info['validTo_time_t']),
        'error' => $result === 0 ? 'Verification failed' : null,
    ];
}
```

### Fix 3: Handle Certificate Expiration

```php
function checkCertificateExpiration(string $certPath, int $warningDays = 30): array {
    $cert = openssl_x509_read(file_get_contents($certPath));
    if ($cert === false) {
        return ['status' => 'error', 'message' => 'Cannot read certificate'];
    }

    $info = openssl_x509_parse($cert);
    $validTo = $info['validTo_time_t'];
    $now = time();
    $daysUntilExpiry = (int)(($validTo - $now) / 86400);

    if ($now > $validTo) {
        return ['status' => 'expired', 'message' => 'Certificate has expired'];
    }

    if ($daysUntilExpiry < $warningDays) {
        return [
            'status' => 'expiring',
            'message' => "Certificate expires in {$daysUntilExpiry} days",
            'expires' => date('Y-m-d', $validTo),
        ];
    }

    return [
        'status' => 'valid',
        'message' => 'Certificate is valid',
        'expires' => date('Y-m-d', $validTo),
    ];
}
```

### Fix 4: Allow Self-Signed Certificates (Development Only)

```php
// WARNING: Only use in development environments
$context = stream_context_create([
    'ssl' => [
        'verify_peer' => false,
        'verify_peer_name' => false,
        'allow_self_signed' => true,
    ],
]);
```

## Examples

```php
// Example: Secure HTTPS client with certificate validation
function secureHttpRequest(string $url, array $options = []): ?string {
    $defaults = [
        'timeout' => 30,
        'verify_peer' => true,
        'verify_peer_name' => true,
    ];
    $options = array_merge($defaults, $options);

    $context = stream_context_create([
        'ssl' => [
            'verify_peer' => $options['verify_peer'],
            'verify_peer_name' => $options['verify_peer_name'],
            'cafile' => ini_get('openssl.cafile') ?: '/etc/ssl/certs/ca-certificates.crt',
            'crypto_method' => STREAM_CRYPTO_METHOD_TLSv1_2_CLIENT | STREAM_CRYPTO_METHOD_TLSv1_3_CLIENT,
        ],
        'http' => [
            'timeout' => $options['timeout'],
            'follow_location' => true,
        ],
    ]);

    $response = @file_get_contents($url, false, $context);
    if ($response === false) {
        $errors = error_get_last();
        error_log('HTTPS request failed: ' . ($errors['message'] ?? 'unknown'));
        return null;
    }

    return $response;
}
```

## Related Errors

- [OpenSSL error](/languages/php/openssl-error/)
- [OpenSSL SSL error](/languages/php/openssl-ssl-error/)
