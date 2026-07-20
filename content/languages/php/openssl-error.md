---
title: "[Solution] PHP OpenSSL Error — Cryptographic Operation Failed"
description: "Fix PHP OpenSSL error by checking installation, verifying certificates, using correct cipher, and handling errors properly. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 17
---

# PHP OpenSSL Error — Cryptographic Operation Failed

An OpenSSL error occurred during a cryptographic operation. This can affect encryption, decryption, signing, verification, SSL connections, and certificate operations. The error is typically triggered by incorrect parameters, missing libraries, or invalid data.

## Common Causes

```php
// Cause 1: Invalid cipher method
$data = 'secret';
$encrypted = openssl_encrypt($data, 'invalid-cipher', 'key'); // Returns false

// Cause 2: OpenSSL extension not loaded
$cipher = openssl_get_cipher_methods(); // Returns false

// Cause 3: Invalid key length
$key = 'short'; // Too short for AES-256
openssl_encrypt($data, 'aes-256-cbc', $key); // Key too short

// Cause 4: Invalid IV length
$iv = 'short'; // Wrong IV length for cipher
openssl_encrypt($data, 'aes-256-cbc', $key, 0, $iv); // IV error

// Cause 5: Corrupted encrypted data
$decrypted = openssl_decrypt('corrupted-data', 'aes-256-cbc', $key); // Returns false
```

## How to Fix

### Fix 1: Verify OpenSSL Installation

```php
if (extension_loaded('openssl')) {
    echo 'OpenSSL version: ' . OPENSSL_VERSION_TEXT;
    echo "\nAvailable ciphers:\n";
    print_r(openssl_get_cipher_methods());
    echo "\nAvailable digests:\n";
    print_r(openssl_get_md_methods());
} else {
    echo 'OpenSSL extension is not installed.';
}
```

```bash
# Install OpenSSL on Ubuntu/Debian
sudo apt-get install php-openssl

# Verify
php -m | grep openssl
```

### Fix 2: Use Correct Cipher Parameters

```php
function safeEncrypt(string $data, string $password): ?array {
    $cipher = 'aes-256-cbc';
    $ivLength = openssl_cipher_iv_length($cipher);
    $iv = openssl_random_pseudo_bytes($ivLength);

    $tag = '';
    $encrypted = openssl_encrypt(
        $data,
        $cipher,
        $password,
        OPENSSL_RAW_DATA,
        $iv,
        $tag,
        '',
        16
    );

    if ($encrypted === false) {
        error_log('Encryption failed: ' . openssl_error_string());
        return null;
    }

    return [
        'encrypted' => base64_encode($encrypted),
        'iv' => base64_encode($iv),
        'tag' => base64_encode($tag),
        'cipher' => $cipher,
    ];
}

function safeDecrypt(array $encryptedData, string $password): ?string {
    $cipher = $encryptedData['cipher'] ?? 'aes-256-cbc';
    $iv = base64_decode($encryptedData['iv']);
    $tag = base64_decode($encryptedData['tag'] ?? '');
    $data = base64_decode($encryptedData['encrypted']);

    $decrypted = openssl_decrypt(
        $data,
        $cipher,
        $password,
        OPENSSL_RAW_DATA,
        $iv,
        $tag
    );

    if ($decrypted === false) {
        error_log('Decryption failed: ' . openssl_error_string());
        return null;
    }

    return $decrypted;
}
```

### Fix 3: Handle OpenSSL Errors Properly

```php
function performSecureOperation(): bool {
    // Reset OpenSSL error queue
    while (openssl_error_string() !== false) {}

    // Perform operation
    $result = openssl_digest('test data', 'sha256');

    if ($result === false) {
        // Read error queue
        while (($error = openssl_error_string()) !== false) {
            error_log("OpenSSL error: {$error}");
        }
        return false;
    }

    return true;
}
```

### Fix 4: Generate Secure Keys

```php
function generateEncryptionKey(int $bits = 256): ?string {
    $key = openssl_random_pseudo_bytes($bits / 8);
    if ($key === false) {
        error_log('Failed to generate random key');
        return null;
    }
    return $key;
}
```

## Examples

```php
// Example: Complete encryption/decryption service
class EncryptionService {
    private string $cipher = 'aes-256-gcm';

    public function encrypt(string $plaintext, string $key): ?array {
        $ivLength = openssl_cipher_iv_length($this->cipher);
        $iv = openssl_random_pseudo_bytes($ivLength);

        $tag = '';
        $ciphertext = openssl_encrypt(
            $plaintext,
            $this->cipher,
            $key,
            OPENSSL_RAW_DATA,
            $iv,
            $tag,
            'additional-data',
            16
        );

        if ($ciphertext === false) {
            error_log('Encrypt failed: ' . openssl_error_string());
            return null;
        }

        return [
            'ciphertext' => base64_encode($ciphertext),
            'iv' => base64_encode($iv),
            'tag' => base64_encode($tag),
        ];
    }

    public function decrypt(array $data, string $key): ?string {
        $ciphertext = base64_decode($data['ciphertext']);
        $iv = base64_decode($data['iv']);
        $tag = base64_decode($data['tag']);

        $plaintext = openssl_decrypt(
            $ciphertext,
            $this->cipher,
            $key,
            OPENSSL_RAW_DATA,
            $iv,
            $tag,
            'additional-data'
        );

        if ($plaintext === false) {
            error_log('Decrypt failed: ' . openssl_error_string());
            return null;
        }

        return $plaintext;
    }
}

// Usage
$key = openssl_random_pseudo_bytes(32);
$service = new EncryptionService();
$encrypted = $service->encrypt('Hello, World!', $key);
$decrypted = $service->decrypt($encrypted, $key);
```

## Related Errors

- [OpenSSL certificate error](/languages/php/openssl-certificate-error/)
- [OpenSSL SSL error](/languages/php/openssl-ssl-error/)
