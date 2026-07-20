---
title: "[Solution] PHP OpenSSL SSL Error — SSL/TLS Handshake Failed"
description: "Fix PHP OpenSSL SSL error by checking SSL configuration, verifying certificates, enabling ciphers, and handling protocol version. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 19
---

# PHP OpenSSL SSL Error — SSL/TLS Handshake Failed

An SSL/TLS handshake error occurred during a secure connection. This prevents establishing an encrypted connection to a remote server and is commonly caused by protocol version mismatches, cipher suite incompatibilities, or certificate issues.

## Common Causes

```php
// Cause 1: Protocol version mismatch (server requires TLS 1.2+)
$context = stream_context_create([
    'ssl' => [
        'crypto_method' => STREAM_CRYPTO_METHOD_TLSv1_CLIENT,
    ],
]);
$fp = fopen('https://modern-server.com', 'r', false, $context); // Fails

// Cause 2: Weak cipher rejected
$context = stream_context_create([
    'ssl' => [
        'ciphers' => 'RC4-SHA', // Deprecated cipher
    ],
]);
$fp = fopen('https://server.com', 'r', false, $context);

// Cause 3: SNI mismatch
$context = stream_context_create([
    'ssl' => [
        'peer_name' => 'wrong-hostname.com',
    ],
]);
$fp = fopen('https://server.com', 'r', false, $context);

// Cause 4: Certificate verification failure
$context = stream_context_create([
    'ssl' => [
        'verify_peer' => true,
        'cafile' => '/nonexistent/cacert.pem',
    ],
]);

// Cause 5: Server requires specific client certificate
$context = stream_context_create([
    'ssl' => [
        'local_cert' => 'client.pem',
        'local_pk' => 'client-key.pem',
    ],
]);
```

## How to Fix

### Fix 1: Configure Protocol Versions

```php
// Allow TLS 1.2 and 1.3 only (modern configuration)
$context = stream_context_create([
    'ssl' => [
        'crypto_method' => STREAM_CRYPTO_METHOD_TLSv1_2_CLIENT | STREAM_CRYPTO_METHOD_TLSv1_3_CLIENT,
        'verify_peer' => true,
        'verify_peer_name' => true,
    ],
]);

$fp = @stream_socket_client('ssl://server.com:443', $errno, $errstr, 30, STREAM_CLIENT_CONNECT, $context);
if ($fp === false) {
    error_log("SSL handshake failed: {$errstr} ({$errno})");
}
```

### Fix 2: Set Strong Ciphers

```php
// Use only strong ciphers
$context = stream_context_create([
    'ssl' => [
        'ciphers' => 'HIGH:!aNULL:!MD5:!RC4:!3DES',
        'verify_peer' => true,
        'verify_peer_name' => true,
        'disable_compression' => true,
    ],
]);
```

### Fix 3: Enable SNI Properly

```php
function connectWithSni(string $host, int $port = 443, array $options = []): ?resource {
    $context = stream_context_create([
        'ssl' => array_merge([
            'verify_peer' => true,
            'verify_peer_name' => true,
            'peer_name' => $host,
            'crypto_method' => STREAM_CRYPTO_METHOD_TLSv1_2_CLIENT | STREAM_CRYPTO_METHOD_TLSv1_3_CLIENT,
            'ciphers' => 'HIGH:!aNULL:!MD5:!RC4',
        ], $options),
    ]);

    $fp = @stream_socket_client(
        "ssl://{$host}:{$port}",
        $errno,
        $errstr,
        $options['timeout'] ?? 30,
        STREAM_CLIENT_CONNECT,
        $context
    );

    if ($fp === false) {
        error_log("SSL connect to {$host}:{$port} failed: {$errstr}");
        return null;
    }

    return $fp;
}
```

### Fix 4: Debug SSL Handshake Issues

```php
function debugSslConnection(string $host, int $port = 443): void {
    $context = stream_context_create([
        'ssl' => [
            'verify_peer' => false,
            'verify_peer_name' => false,
        ],
    ]);

    $fp = @stream_socket_client("ssl://{$host}:{$port}", $errno, $errstr, 10, STREAM_CLIENT_CONNECT, $context);

    if ($fp === false) {
        echo "Connection failed: {$errstr} ({$errno})\n";
        return;
    }

    $params = stream_context_get_params($fp);
    $sslOptions = $params['options']['ssl'] ?? [];

    echo "Connection established to {$host}:{$port}\n";
    echo "Peer certificate:\n";

    $cert = stream_context_get_params($fp);
    $peer = stream_get_meta_data($fp);

    print_r($peer);

    fclose($fp);
}
```

## Examples

```php
// Example: Robust HTTPS client with SSL error handling
class SecureHttpClient {
    private array $defaults = [
        'timeout' => 30,
        'verify_peer' => true,
        'verify_peer_name' => true,
    ];

    public function __construct(array $options = []) {
        $this->defaults = array_merge($this->defaults, $options);
    }

    public function get(string $url): array {
        $context = stream_context_create([
            'ssl' => [
                'verify_peer' => $this->defaults['verify_peer'],
                'verify_peer_name' => $this->defaults['verify_peer_name'],
                'crypto_method' => STREAM_CRYPTO_METHOD_TLSv1_2_CLIENT | STREAM_CRYPTO_METHOD_TLSv1_3_CLIENT,
                'ciphers' => 'HIGH:!aNULL:!MD5:!RC4',
                'disable_compression' => true,
                'SNI_enabled' => true,
            ],
            'http' => [
                'method' => 'GET',
                'timeout' => $this->defaults['timeout'],
                'follow_location' => true,
                'ignore_errors' => true,
                'header' => "User-Agent: PHP-SSL-Client/1.0\r\n",
            ],
        ]);

        $response = @file_get_contents($url, false, $context);

        if ($response === false) {
            $error = error_get_last();
            return [
                'success' => false,
                'error' => $error['message'] ?? 'Unknown SSL error',
                'context' => $context,
            ];
        }

        $headers = $this->extractHeaders($http_response_header ?? []);

        return [
            'success' => true,
            'body' => $response,
            'headers' => $headers,
        ];
    }

    private function extractHeaders(array $rawHeaders): array {
        $headers = [];
        foreach ($rawHeaders as $header) {
            if (strpos($header, ':') !== false) {
                [$key, $value] = explode(':', $header, 2);
                $headers[trim($key)] = trim($value);
            }
        }
        return $headers;
    }
}

// Usage
$client = new SecureHttpClient(['timeout' => 10]);
$result = $client->get('https://api.example.com/data');
if ($result['success']) {
    echo $result['body'];
} else {
    error_log('SSL Error: ' . $result['error']);
}
```

## Related Errors

- [OpenSSL error](/languages/php/openssl-error/)
- [OpenSSL certificate error](/languages/php/openssl-certificate-error/)
