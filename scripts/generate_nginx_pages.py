#!/usr/bin/env python3
"""Generate Nginx error pages"""
import os

BASE = '/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools/nginx'
EXISTING = {f.replace('.md', '') for f in os.listdir(BASE) if f.endswith('.md')}

def make_page(title, desc, body):
    lines = [
        '---',
        f'title: "[Solution] {title}"',
        f'description: "{desc}"',
        'tools: ["nginx"]',
        'error-types: ["tool-error"]',
        'severities: ["error"]',
        '---',
        '',
        body,
    ]
    return '\n'.join(lines)

PAGES = []

def add(slug, title, desc, body):
    PAGES.append((slug, title, desc, body))

def B(slug, title, desc, causes, fixes, examples):
    """Shorthand builder for page body"""
    body = f"""## Description

{desc}

## Common Causes

{causes}

## How to Fix

{fixes}

## Examples

{examples}"""
    PAGES.append((slug, title, desc, body))


add("nginx-unknown-directive-error", "Nginx Unknown Directive Error", "Nginx fails to start because of an unknown directive in the configuration file.", """## Description

Nginx fails to start because of an unknown directive in the configuration file.

## Common Causes

- **Typo in directive name** (e.g., `direcitve` instead of `directive`)
- **Module not loaded** - the directive requires a module not compiled in
- **Deprecated syntax** no longer supported in your version
- **Wrong context** - using a directive where it is not allowed

## How to Fix

1. Check for typos: `grep -n 'unknown directive' /var/log/nginx/error.log`
2. Verify module: `nginx -V 2>&1 | grep -o 'with-[a-z_-]*' | sort`
3. Check the line number from the error and correct it
4. Validate: `sudo nginx -t`

## Examples

**Incorrect (typo):**
```nginx
server { lisetn 80; }  # typo
```
**Correct:**
```nginx
server { listen 80; server_name example.com; }
```
**Testing:**
```bash
sudo nginx -t
# syntax is ok
# test is successful
```""")
add("nginx-invalid-port-error", "Nginx Invalid Port Error", "Nginx rejects a port number in a listen directive that is out of range or invalid.", """## Description

Nginx rejects a port number in a listen directive that is out of range or invalid.

## Common Causes

- Port number **exceeds 65535**
- Port number is **zero or negative**
- **Duplicate listen ports** across server blocks
- Using **privileged ports** (< 1024) without proper permissions

## How to Fix

1. Use valid port range (1-65535)
2. For privileged ports: `sudo setcap cap_net_bind_service=+ep /usr/sbin/nginx`
3. Check duplicates: `grep -rn 'listen ' /etc/nginx/`
4. Validate: `sudo nginx -t`

## Examples

**Invalid:**
```nginx
server { listen 70000; }  # error: port > 65535
```
**Valid:**
```nginx
server { listen 80; listen 443 ssl; server_name example.com; }
server { listen 192.168.1.10:8080; server_name internal.example.com; }
```""")
add("nginx-duplicate-server-name-error", "Nginx Duplicate Server Name Error", "Two server blocks share the same server_name on the same port, causing a conflict.", """## Description

Two server blocks share the same server_name on the same port, causing a conflict.

## Common Causes

- **Multiple config files** defining the same server_name
- **Copy-paste errors** duplicating server blocks
- **Include glob** pulling in files with overlapping names
- **Default server** conflicts

## How to Fix

1. Find duplicates: `grep -rn 'server_name' /etc/nginx/conf.d/ | sort`
2. Remove duplicates or make names unique
3. Use `default_server` for catch-all: `listen 80 default_server; server_name _;`
4. Validate: `sudo nginx -t && sudo nginx -s reload`

## Examples

**Broken:**
```nginx
# a.conf: server { listen 80; server_name example.com; }
# b.conf: server { listen 80; server_name example.com; }  # conflict
```
**Fixed:**
```nginx
server { listen 80; server_name example.com; }
server { listen 80; server_name www.example.com; }
```""")
add("nginx-invalid-worker-connections-error", "Nginx Invalid Worker Connections Error", "The worker_connections value in nginx.conf is invalid or too low for expected load.", """## Description

The worker_connections value in nginx.conf is invalid or too low for expected load.

## Common Causes

- **Value set to 0 or negative**
- **Value exceeds system file descriptor limits**
- **Too low for production traffic**

## How to Fix

1. Set reasonable value (1024-65535)
2. Increase file descriptors: edit `/etc/security/limits.conf` -> `* soft nofile 65535`
3. Set `worker_rlimit_nofile` higher than `worker_connections`
4. Verify: `sudo nginx -t`

## Examples

**Invalid:**
```nginx
events { worker_connections 0; }  # error: must be > 0
```
**Production:**
```nginx
worker_processes auto;
worker_rlimit_nofile 65535;
events { worker_connections 16384; use epoll; multi_accept on; }
```""")
add("nginx-invalid-listen-directive-error", "Nginx Invalid Listen Directive Error", "The listen directive contains invalid syntax or unsupported parameters.", """## Description

The listen directive contains invalid syntax or unsupported parameters.

## Common Causes

- Using **protocol names** instead of port numbers
- **Invalid IP:port format**
- Misspelled **parameters** (e.g., `defualt_server`)
- **Deprecated parameters** in newer versions

## How to Fix

1. Use correct syntax: `listen [IP]:PORT [parameters];`
2. Valid params: `default_server`, `ssl`, `http2`, `reuseport`, `backlog=N`
3. Check for typos
4. Validate: `sudo nginx -t`

## Examples

**Invalid:**
```nginx
listen http;           # error: not a port
listen 80 default;     # error: should be default_server
```
**Valid:**
```nginx
listen 80;
listen 443 ssl;
listen [::]:80 default_server;
listen 8080 reuseport backlog=1024;
```""")
add("nginx-missing-server-block-error", "Nginx Missing Server Block Error", "Nginx cannot start because no server block is defined to handle incoming requests.", """## Description

Nginx cannot start because no server block is defined to handle incoming requests.

## Common Causes

- **All server blocks removed** during cleanup
- **Commented out** server blocks
- **Empty conf.d directory**
- **Wrong include path**

## How to Fix

1. Add at minimum one server block
2. Check include paths: `grep -n include /etc/nginx/nginx.conf`
3. Restore default server block if deleted
4. Validate: `sudo nginx -t`

## Examples

**Broken:**
```nginx
http { # no server blocks defined }
```
**Fixed:**
```nginx
http {
    include /etc/nginx/conf.d/*.conf;
    server { listen 80 default_server; server_name _; return 404; }
}
```""")
add("nginx-conflicting-server-name-error", "Nginx Conflicting Server Name Error", "Multiple server blocks have conflicting server_name entries on the same listen address.", """## Description

Multiple server blocks have conflicting server_name entries on the same listen address.

## Common Causes

- **Wildcard conflicts** (`*.example.com` and `example.com`)
- **Same domain** in multiple config files
- **Symlinked configs** loaded twice

## How to Fix

1. List declarations: `grep -rn 'server_name' /etc/nginx/ --include='*.conf'`
2. Remove duplicates
3. Use `default_server` for catch-all
4. Validate: `sudo nginx -t && sudo nginx -s reload`

## Examples

**Fixed:**
```nginx
server { listen 443 ssl; server_name app.example.com; }
server { listen 443 ssl; server_name admin.example.com; }
```""")
add("nginx-invalid-location-pattern-error", "Nginx Invalid Location Pattern Error", "A location block contains an invalid regex pattern or malformed URI prefix.", """## Description

A location block contains an invalid regex pattern or malformed URI prefix.

## Common Causes

- **Malformed regex** - unescaped special characters
- **Missing URI prefix**
- **Conflicting location modifiers**
- **Unclosed brackets** in regex

## How to Fix

1. Test regex: `echo test-string | pcregrep '/pattern/'`
2. Escape special characters properly
3. Use `location ^~` for prefix matches
4. Validate: `sudo nginx -t`

## Examples

**Invalid:**
```nginx
location ~ /path/(.+)+/file { }  # error: nothing to repeat
```
**Valid:**
```nginx
location ~ /path/([^/]+)/file$ { }
location ^~ /static/ { alias /var/www/static/; }
```""")
add("nginx-invalid-upstream-name-error", "Nginx Invalid Upstream Name Error", "The upstream block name contains invalid characters or conflicts with a reserved name.", """## Description

The upstream block name contains invalid characters or conflicts with a reserved name.

## Common Causes

- **Special characters** in name (`@`, `#`, spaces)
- **Name starts with digit or hyphen**
- **Duplicate upstream names** in different files

## How to Fix

1. Use only alphanumeric, hyphens, underscores, dots
2. Check duplicates: `grep -rn 'upstream ' /etc/nginx/conf.d/`
3. Validate: `sudo nginx -t`

## Examples

**Invalid:**
```nginx
upstream backend@pool { }   # @ not allowed
upstream 1backend { }       # starts with digit
```
**Valid:**
```nginx
upstream backend_pool { }
upstream api-v2 { }
```""")
add("nginx-missing-closing-bracket-error", "Nginx Missing Closing Bracket Error", "A block in the Nginx configuration is missing a closing curly bracket.", """## Description

A block in the Nginx configuration is missing a closing curly bracket.

## Common Causes

- **Accidentally deleted** closing bracket
- **Nested blocks** where one bracket was forgotten
- **Include files** breaking bracket nesting
- **Copy-paste errors**

## How to Fix

1. Count brackets: `grep -c '{' /etc/nginx/nginx.conf` vs `grep -c '}'`
2. Use bracket-matching editor
3. Check include files too
4. Validate: `sudo nginx -t`

## Examples

**Missing:**
```nginx
server {
    listen 80;
    location / {
        proxy_pass http://backend;
    # missing }
}
```
**Fixed:**
```nginx
server {
    listen 80;
    location / { proxy_pass http://backend; }
}
```""")
add("nginx-unexpected-eof-error", "Nginx Unexpected End of File Error", "Nginx reached the end of a configuration file before all blocks or directives are properly closed.", """## Description

Nginx reached the end of a configuration file before all blocks or directives are properly closed.

## Common Causes

- **Truncated config file**
- **Missing semicolons** at end of directives
- **Unclosed blocks**
- **Empty config files**

## How to Fix

1. Check the line number from the error
2. Ensure file is not truncated: `wc -l file.conf; tail -5 file.conf`
3. Add missing semicolons or brackets
4. Validate: `sudo nginx -t`

## Examples

**Truncated:**
```nginx
server {
    listen 80;
    server_name example.com  # missing semicolon, file ends
```
**Fixed:**
```nginx
server { listen 80; server_name example.com; location / { root /var/www; } }
```""")
add("nginx-invalid-map-directive-error", "Nginx Invalid Map Directive Error", "The map directive has invalid syntax or conflicting source/target definitions.", """## Description

The map directive has invalid syntax or conflicting source/target definitions.

## Common Causes

- **Duplicate source values** in same map block
- **Missing `default`** when no source matches
- **Invalid regex patterns**
- **Wrong number of parameters**

## How to Fix

1. Check for duplicates: `grep -A20 'map ' file.conf | sort | uniq -d`
2. Use `default` for unmatched values
3. Ensure only one `default` per map block
4. Validate: `sudo nginx -t`

## Examples

**Invalid - duplicate:**
```nginx
map $uri $handler {
    default file_a; /api handler_api; /api handler_api2;
}
```
**Fixed:**
```nginx
map $uri $handler { default file_a; /api handler_api; /dashboard handler_dash; }
```""")
add("nginx-invalid-if-condition-error", "Nginx Invalid If Condition Error", "An if directive contains an invalid condition or uses unsupported operators.", """## Description

An if directive contains an invalid condition or uses unsupported operators.

## Common Causes

- **Wrong operator** (Nginx if only supports =, !=, ~, ~*, ^~, -f, -d, -e, -x)
- **Missing quotes** around regex
- **Using if with proxy_pass** ("if is evil")
- **Complex boolean logic**

## How to Fix

1. Use only supported operators
2. Prefer separate location blocks over if
3. Use map for complex conditions
4. Validate: `sudo nginx -t`

## Examples

**Invalid:**
```nginx
if ($host ~= "example.com") { }  # ~= not valid
```
**Valid:**
```nginx
if ($host = "example.com") { return 301 https://www.example.com$request_uri; }
```""")
add("nginx-geo-directive-error", "Nginx Geo Directive Error", "The geo block contains invalid IP ranges, overlapping CIDR blocks, or incorrect syntax.", """## Description

The geo block contains invalid IP ranges, overlapping CIDR blocks, or incorrect syntax.

## Common Causes

- **Incomplete CIDR notation**
- **Overlapping IP ranges**
- **Invalid variable name** or missing default
- **Mixing IPv4 and IPv6** incorrectly

## How to Fix

1. Use proper CIDR: `192.168.1.0/24`
2. Check overlapping: `grep -A30 'geo ' /etc/nginx/nginx.conf`
3. Use geo only at http level
4. Validate: `sudo nginx -t`

## Examples

**Invalid:**
```nginx
geo $region { default 0; 192.168.1 1; }  # missing /24
```
**Fixed:**
```nginx
geo $trusted { default 0; 192.168.0.0/16 1; 10.0.0.0/8 1; }
```""")
add("nginx-split-clients-error", "Nginx Split Clients Error", "The split_clients block has an invalid hash source or percentage range.", """## Description

The split_clients block has an invalid hash source or percentage range.

## Common Causes

- **Percentages exceeding 100%** total
- **Missing hash source**
- **Invalid variable** name
- **Ranges that do not add up**

## How to Fix

1. Ensure percentages do not exceed 100%
2. Use `*` catch-all for remainder
3. Provide valid hash source ($request_id, $remote_addr)
4. Validate: `sudo nginx -t`

## Examples

**Invalid:**
```nginx
split_clients $remote_addr $v { 60% a; 60% b; }  # total > 100%
```
**Fixed:**
```nginx
split_clients $remote_addr $v { 50% a; 50% b; }
```""")
add("nginx-no-ssl-configured-error", "Nginx No SSL Configured Error", "SSL parameters are referenced but no SSL certificate or key is configured.", """## Description

SSL parameters are referenced but no SSL certificate or key is configured.

## Common Causes

- **ssl on** without certificate directives
- **listen 443 ssl** without ssl_certificate
- **Missing include** for SSL fragment
- **Certificate directives commented out**

## How to Fix

1. Always provide both certificate and key
2. Create reusable SSL snippet
3. Validate: `sudo nginx -t`

## Examples

**Broken:**
```nginx
server { listen 443 ssl; server_name example.com; }
```
**Fixed:**
```nginx
server {
    listen 443 ssl http2; server_name example.com;
    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
}
```""")
add("nginx-cert-not-found-error", "Nginx Certificate Not Found Error", "Nginx cannot locate the SSL certificate file specified in the configuration.", """## Description

Nginx cannot locate the SSL certificate file specified in the configuration.

## Common Causes

- **File path typo** in ssl_certificate
- **Certificate not generated** or expired
- **Permissions issue**
- **Certificate deleted or moved** by renewal

## How to Fix

1. Verify: `ls -la /etc/ssl/certs/example.com.pem`
2. Check permissions: `sudo -u nginx cat /path/to/cert.pem`
3. Renew if needed: `sudo certbot renew`
4. Fix the path in config

## Examples

**Broken (typo):**
```nginx
ssl_certificate /etc/ssl/certs/exmaple.com.pem;
```
**Fixed:**
```nginx
ssl_certificate /etc/ssl/certs/example.com.pem;
ssl_certificate_key /etc/ssl/private/example.com.key;
```
**Verify:**
```bash
openssl x509 -in /etc/ssl/certs/example.com.pem -noout -text | head -5
```""")
add("nginx-cert-expired-error", "Nginx Certificate Expired Error", "The SSL certificate has passed its validity period and can no longer be used.", """## Description

The SSL certificate has passed its validity period and can no longer be used.

## Common Causes

- **Auto-renewal failed** (certbot timer not running)
- **Manual certificate** not renewed
- **Clock skew** on server
- **Wrong certificate file** linked

## How to Fix

1. Check: `openssl x509 -in cert.pem -noout -dates`
2. Renew: `sudo certbot renew --force-renewal && sudo nginx -s reload`
3. Enable auto-renewal: `sudo systemctl enable --now certbot.timer`
4. Check clock: `timedatectl`

## Examples

**Check expiry:**
```bash
openssl x509 -in /etc/ssl/certs/example.com.pem -noout -enddate
```
**Renew:**
```bash
sudo certbot renew
sudo nginx -t && sudo nginx -s reload
```""")
add("nginx-key-file-mismatch-error", "Nginx Key File Mismatch Error", "The SSL certificate and private key do not match each other.", """## Description

The SSL certificate and private key do not match each other.

## Common Causes

- **Mixed up certificate files** from different domains
- **Certificate regenerated** without updating key
- **Copied wrong key** during migration
- **Overwritten key** during renewal

## How to Fix

1. Verify match:
```bash
openssl x509 -noout -modulus -in cert.pem | md5sum
openssl rsa -noout -modulus -in key.pem | md5sum
# Both must be identical
```
2. Regenerate key pair if needed
3. Obtain new certificate
4. Validate: `sudo nginx -t && sudo nginx -s reload`

## Examples

**Verify match:**
```bash
openssl x509 -noout -modulus -in cert.pem | openssl md5
openssl rsa -noout -modulus -in key.pem | openssl md5
# If different -> files don't match
```""")
add("nginx-ssl-handshake-failed-error", "Nginx SSL Handshake Failed Error", "The SSL/TLS handshake between client and server failed during connection.", """## Description

The SSL/TLS handshake between client and server failed during connection.

## Common Causes

- **Protocol version mismatch**
- **Cipher suite mismatch**
- **Invalid or expired certificate**
- **SNI mismatch**
- **Client certificate required** but not provided

## How to Fix

1. Enable multiple protocols: `ssl_protocols TLSv1.2 TLSv1.3;`
2. Use broad cipher suite: `ssl_ciphers HIGH:!aNULL:!MD5:!RC4;`
3. Debug: `openssl s_client -connect example.com:443`
4. Check error logs: `tail -50 /var/log/nginx/error.log | grep SSL`

## Examples

**Debug:**
```bash
openssl s_client -connect example.com:443 2>&1 | grep -E 'Protocol|Cipher|Verify'
openssl s_client -connect example.com:443 -tls1_2
```""")
add("nginx-protocol-mismatch-error", "Nginx Protocol Mismatch Error", "The client and server could not agree on a TLS protocol version during handshake.", """## Description

The client and server could not agree on a TLS protocol version during handshake.

## Common Causes

- **Server only allows TLS 1.3** but client needs 1.2
- **Server disabled TLS 1.2** but old clients require it
- **Client too old** (only TLS 1.0/1.1)

## How to Fix

1. Enable both: `ssl_protocols TLSv1.2 TLSv1.3;`
2. Test: `openssl s_client -connect example.com:443 -tls1_2`
3. Never enable TLS 1.0/1.1 in production

## Examples

**Too restrictive:**
```nginx
ssl_protocols TLSv1.3;
```
**Balanced:**
```nginx
ssl_protocols TLSv1.2 TLSv1.3;
ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256;
```""")
add("nginx-ciphers-error", "Nginx Ciphers Error", "The configured SSL cipher suites are invalid or no common cipher exists with the client.", """## Description

The configured SSL cipher suites are invalid or no common cipher exists with the client.

## Common Causes

- **Invalid cipher string** format
- **Using deprecated ciphers** (RC4, DES, MD5)
- **Strict cipher list** that few clients support
- **Cipher order** causing failures

## How to Fix

1. Use tested config: `ssl_ciphers HIGH:!aNULL:!MD5:!RC4:!3DES;`
2. List ciphers: `openssl ciphers -v 'HIGH:!aNULL' | head -20`
3. Test: `openssl s_client -connect example.com:443 -cipher ECDHE-RSA-AES128-GCM-SHA256`

## Examples

**Invalid:**
```nginx
ssl_ciphers BROKEN_CIPHER;
```
**Secure:**
```nginx
ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256;
ssl_prefer_server_ciphers on;
ssl_ecdh_curve X25519:secp384r1;
```""")
add("nginx-session-cache-error", "Nginx Session Cache Error", "The SSL session cache configuration is invalid or the shared memory zone cannot be created.", """## Description

The SSL session cache configuration is invalid or the shared memory zone cannot be created.

## Common Causes

- **Invalid size format**
- **Zone name missing** for shared type
- **Zero or negative cache size**
- **Multiple caches with conflicting zones**

## How to Fix

1. Use proper syntax: `ssl_session_cache shared:SSL:10m;`
2. Size appropriately (10MB = ~40k sessions)
3. Disable only for testing: `ssl_session_cache off;`

## Examples

**Invalid:**
```nginx
ssl_session_cache shared:;           # missing size
ssl_session_cache shared:SSL 10m;    # missing colon
```
**Valid:**
```nginx
ssl_session_cache shared:SSL:10m;
ssl_session_timeout 1d;
ssl_session_tickets on;
```""")
add("nginx-ocsp-stapling-error", "Nginx OCSP Stapling Error", "OCSP stapling failed because the responder URL is missing or unreachable.", """## Description

OCSP stapling failed because the responder URL is missing or unreachable.

## Common Causes

- **Responder URL unreachable**
- **Firewall blocking** outbound port 80
- **Intermediate CA missing**
- **Nginx cannot resolve** responder hostname

## How to Fix

1. Provide intermediate chain: `ssl_trusted_certificate /path/to/fullchain.pem;`
2. Configure stapling with resolver
3. Test: `openssl s_client -connect example.com:443 -status`
4. Allow outbound port 80

## Examples

**Config:**
```nginx
server {
    listen 443 ssl;
    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
    ssl_trusted_certificate /etc/letsencrypt/live/example.com/chain.pem;
    ssl_stapling on;
    ssl_stapling_verify on;
    resolver 1.1.1.1 8.8.8.8 valid=300s;
}
```""")
add("nginx-dh-key-too-small-error", "Nginx DH Key Too Small Error", "The Diffie-Hellman key size is below the minimum acceptable threshold (typically < 2048 bits).", """## Description

The Diffie-Hellman key size is below the minimum acceptable threshold (typically < 2048 bits).

## Common Causes

- **Default DH params** from old OpenSSL (1024-bit)
- **Self-generated DH file** with insufficient length
- **Missing DH parameters file**

## How to Fix

1. Generate strong DH params: `openssl dhparam -out /etc/ssl/dhparam.pem 4096`
2. Reference in Nginx: `ssl_dhparam /etc/ssl/dhparam.pem;`
3. Prefer ECDHE: `ssl_ecdh_curve X25519:secp384r1;`
4. Verify: `openssl dhparam -in /etc/ssl/dhparam.pem -text -noout | head -2`

## Examples

**Generate:**
```bash
openssl dhparam -out /etc/ssl/dhparam.pem 4096
```
**Config:**
```nginx
ssl_dhparam /etc/ssl/dhparam.pem;
ssl_ecdh_curve X25519:secp384r1;
```""")
add("nginx-verify-client-error", "Nginx Verify Client Error", "Client certificate verification failed during mutual TLS handshake.", """## Description

Client certificate verification failed during mutual TLS handshake.

## Common Causes

- **Client did not send certificate**
- **Self-signed cert** not in trusted CA file
- **Certificate expired**
- **Intermediate CA missing**
- **ssl_verify_depth too shallow**

## How to Fix

1. Provide CA chain: `ssl_client_certificate /path/to/ca-bundle.pem;`
2. Use `optional` for optional access: `ssl_verify_client optional;`
3. Check client cert: `openssl s_client -connect example.com:443 -cert client.pem -key client-key.pem`
4. Ensure CA bundle includes all intermediates

## Examples

**Mutual TLS:**
```nginx
server {
    listen 443 ssl; server_name internal.example.com;
    ssl_certificate /etc/ssl/certs/server.pem;
    ssl_certificate_key /etc/ssl/private/server.key;
    ssl_client_certificate /etc/ssl/certs/ca.pem;
    ssl_verify_client on;
    ssl_verify_depth 3;
}
```""")
add("nginx-ssl-password-required-error", "Nginx SSL Password Required Error", "The SSL private key file is encrypted and Nginx cannot read it without the passphrase.", """## Description

The SSL private key file is encrypted and Nginx cannot read it without the passphrase.

## Common Causes

- **Key generated with passphrase** (e.g., `openssl genrsa -aes256`)
- **Key not decrypted** before placing in Nginx path
- **Wrong key file** that is still encrypted

## How to Fix

1. Remove passphrase: `openssl rsa -in encrypted.key -out decrypted.key`
2. Place decrypted key: `sudo mv decrypted.key /etc/ssl/private/server.key`
3. Restrict permissions: `sudo chmod 600 /etc/ssl/private/server.key`

## Examples

**Decrypt:**
```bash
cp server.key server.key.bak
openssl rsa -in server.key.bak -out server.key
chmod 600 server.key
```
**Verify not encrypted:**
```bash
head -1 server.key
# Should be: -----BEGIN PRIVATE KEY-----
```""")
add("nginx-tls-version-too-old-error", "Nginx TLS Version Too Old Error", "The server is configured to use deprecated TLS versions (1.0 or 1.1) that are no longer accepted.", """## Description

The server is configured to use deprecated TLS versions (1.0 or 1.1) that are no longer accepted.

## Common Causes

- **Only TLS 1.0/1.1** in ssl_protocols
- **Client refusing** old TLS
- **PCI compliance** rejecting old protocols

## How to Fix

1. Use only modern: `ssl_protocols TLSv1.2 TLSv1.3;`
2. Remove TLS 1.0/1.1
3. Verify: `nginx -t` and `openssl s_client -connect example.com:443 -tls1_2`

## Examples

**Insecure:**
```nginx
ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
```
**Secure:**
```nginx
ssl_protocols TLSv1.2 TLSv1.3;
ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256;
```""")
add("nginx-cert-chain-incomplete-error", "Nginx Certificate Chain Incomplete Error", "The server does not send the full certificate chain, causing client verification failures.", """## Description

The server does not send the full certificate chain, causing client verification failures.

## Common Causes

- **Only leaf certificate** in ssl_certificate file
- **Missing intermediate certificates**
- **Wrong file** used for ssl_certificate
- **Certbot cert.pem** not fullchain.pem

## How to Fix

1. Use fullchain: `ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;`
2. Concatenate: `cat server.crt intermediate.crt root.crt > fullchain.crt`
3. Verify: `openssl verify -CAfile ca-certificates.crt fullchain.pem`
4. Test: `openssl s_client -connect example.com:443 2>&1 | grep Verify`

## Examples

**Check chain:**
```bash
openssl s_client -connect example.com:443 2>&1 | grep -E 'depth=|Verify'
```
**Build chain:**
```bash
cat your-domain.crt intermediate.crt > fullchain.pem
```""")
add("nginx-stapling-error", "Nginx OCSP Stapling Retrieval Error", "The OCSP stapling mechanism fails to retrieve or cache a valid OCSP response.", """## Description

The OCSP stapling mechanism fails to retrieve or cache a valid OCSP response.

## Common Causes

- **OCSP response expired** in Nginx cache
- **Responder returning malformed data**
- **Clock skew** causing rejection
- **ssl_trusted_certificate not configured**

## How to Fix

1. Set trusted cert: `ssl_trusted_certificate /path/to/ca-chain.pem;`
2. Set resolver: `resolver 1.1.1.1 8.8.8.8 valid=300s;`
3. Check clock: `date && ntpdate -q pool.ntp.org`
4. Test: `openssl s_client -connect example.com:443 -status`

## Examples

**Complete config:**
```nginx
server {
    listen 443 ssl;
    ssl_certificate /etc/ssl/certs/fullchain.pem;
    ssl_certificate_key /etc/ssl/private/server.key;
    ssl_trusted_certificate /etc/ssl/certs/ca-chain.pem;
    ssl_stapling on;
    ssl_stapling_verify on;
    resolver 1.1.1.1 8.8.8.8 valid=300s;
}
```""")
add("nginx-upstream-timed-out-error", "Nginx Upstream Timed Out Error", "The upstream server did not respond within the configured timeout values.", """## Description

The upstream server did not respond within the configured timeout values.

## Common Causes

- **Backend processing too slow**
- **Timeout values too low**
- **Backend overloaded**
- **Network latency** between Nginx and upstream

## How to Fix

1. Increase timeouts: `proxy_read_timeout 300s;`
2. Check backend: `curl -w '@curl-format.txt' http://backend:8080/api`
3. Use keepalive connections
4. Optimize backend queries

## Examples

**Extended:**
```nginx
proxy_connect_timeout 30s;
proxy_send_timeout 60s;
proxy_read_timeout 300s;
```
**With keepalive:**
```nginx
upstream backend { server 127.0.0.1:8080; keepalive 32; }
proxy_http_version 1.1;
proxy_set_header Connection "";
```""")
add("nginx-upstream-prematurely-closed-error", "Nginx Upstream Prematurely Closed Connection Error", "The upstream server closed the connection before sending a complete response.", """## Description

The upstream server closed the connection before sending a complete response.

## Common Causes

- **Backend worker crash** or OOM kill
- **FastCGI/php-fpm worker timeout**
- **Backend not handling keepalive**
- **Buffer too small** for response

## How to Fix

1. Increase buffers: `proxy_buffer_size 16k; proxy_buffers 4 32k;`
2. Add retry: `proxy_next_upstream error timeout http_502 http_503;`
3. Check backend logs: `journalctl -u app-backend --since '10 min ago'`
4. Match keepalive settings

## Examples

**Robust:**
```nginx
proxy_buffer_size 16k;
proxy_buffers 4 32k;
proxy_busy_buffers_size 64k;
proxy_connect_timeout 30s;
proxy_read_timeout 300s;
proxy_next_upstream error timeout http_502 http_503;
```""")
add("nginx-no-live-upstreams-error", "Nginx No Live Upstreams Error", "All servers in the upstream pool are marked as down or have failed health checks.", """## Description

All servers in the upstream pool are marked as down or have failed health checks.

## Common Causes

- **All backends down** or unreachable
- **Health checks failing** on all servers
- **max_fails threshold reached**
- **Network partition**

## How to Fix

1. Check backends: `curl -I http://backend1:8080/health`
2. Add backup server: `server 10.0.0.3:8080 backup;`
3. Adjust max_fails: `server 10.0.0.1:8080 max_fails=5 fail_timeout=60s;`
4. Review upstream config

## Examples

**With backup:**
```nginx
upstream app {
    server 10.0.0.1:8080 max_fails=5 fail_timeout=60s;
    server 10.0.0.2:8080 max_fails=5 fail_timeout=60s;
    server 10.0.0.3:8080 backup;
}
```""")
add("nginx-upstream-invalid-header-error", "Nginx Upstream Sent Invalid Header Error", "The upstream server returned a malformed or invalid HTTP header in its response.", """## Description

The upstream server returned a malformed or invalid HTTP header in its response.

## Common Causes

- **Backend generating malformed headers**
- **Duplicate headers** not allowed
- **Encoding issues** in header values
- **Backend proxy forwarding bad headers**

## How to Fix

1. Inspect: `curl -v http://backend:8080/api 2>&1 | head -30`
2. Use proxy manipulation: `proxy_hide_header X-Powered-By;`
3. Fix the backend
4. Enable debug: `error_log /var/log/nginx/error.log debug;`

## Examples

**Filter:**
```nginx
location /api/ {
    proxy_pass http://backend;
    proxy_hide_header X-Invalid-Header;
    proxy_set_header Accept-Encoding "";
}
```""")
add("nginx-upstream-big-header-error", "Nginx Upstream Sent Too Big Header Error", "The upstream response headers exceed the configured proxy_buffer_size limit.", """## Description

The upstream response headers exceed the configured proxy_buffer_size limit.

## Common Causes

- **Large cookies** or session data
- **Many Set-Cookie headers**
- **Large Authorization headers**
- **Default buffer too small** (4k/8k)

## How to Fix

1. Increase buffer: `proxy_buffer_size 16k; proxy_buffers 4 16k;`
2. Reduce header size in backend
3. Strip headers: `proxy_hide_header Set-Cookie;`

## Examples

**Large buffer:**
```nginx
location /api/ {
    proxy_buffer_size 32k;
    proxy_buffers 8 32k;
    proxy_busy_buffers_size 64k;
    proxy_pass http://backend;
}
```""")
add("nginx-upstream-connection-refused-error", "Nginx Upstream Connection Refused Error", "Nginx cannot establish a TCP connection to the upstream server because it refused the connection.", """## Description

Nginx cannot establish a TCP connection to the upstream server because it refused the connection.

## Common Causes

- **Backend service not running**
- **Backend listening on wrong port/IP**
- **Firewall blocking**
- **Backend backlog full**

## How to Fix

1. Check backend: `systemctl status app-backend; ss -tlnp | grep 8080`
2. Verify upstream address matches
3. Check firewall: `sudo iptables -L -n | grep 8080`
4. Increase backlog: `listen 8080 backlog=65535;`

## Examples

**Verify:**
```bash
ss -tlnp | grep 8080
# LISTEN 0 128 0.0.0.0:8080 users:("node",pid=1234)
```
**Check process:**
```bash
ps aux | grep 'node|gunicorn|java' | grep -v grep
```""")
add("nginx-upstream-resolver-error", "Nginx Upstream Resolver Error", "Nginx cannot resolve the upstream hostname due to DNS resolution failure.", """## Description

Nginx cannot resolve the upstream hostname due to DNS resolution failure.

## Common Causes

- **DNS server unreachable**
- **Invalid resolver address**
- **DNS timeout**
- **Missing resolver directive**

## How to Fix

1. Configure resolver: `resolver 8.8.8.8 8.8.4.4 valid=300s;`
2. Use dynamic with resolver: `set $upstream http://backend.example.com:8080;`
3. Test DNS: `dig backend.example.com +short`
4. Check /etc/resolv.conf

## Examples

**Complete:**
```nginx
resolver 8.8.8.8 1.1.1.1 valid=300s ipv6=off;
resolver_timeout 5s;
server {
    listen 80; server_name app.example.com;
    location / { set $upstream http://backend.internal:8080; proxy_pass $upstream; }
}
```""")
add("nginx-upstream-name-not-resolved-error", "Nginx Upstream Name Not Resolved Error", "The hostname in the upstream block could not be resolved to an IP address.", """## Description

The hostname in the upstream block could not be resolved to an IP address.

## Common Causes

- **Domain does not exist** or misspelled
- **DNS not available** during startup
- **Temporary DNS outage**

## How to Fix

1. Verify: `dig backend.example.com +short`
2. Use IPs for static upstreams
3. Use resolver with variable for dynamic
4. Add to /etc/hosts as temporary fix

## Examples

**Static (IP-based):**
```nginx
upstream backend { server 10.0.0.1:8080; server 10.0.0.2:8080; }
```
**Dynamic with resolver:**
```nginx
resolver 8.8.8.8 valid=300s;
location / { proxy_pass http://backend.example.com:8080; }
```""")
add("nginx-upstream-no-suitable-server-error", "Nginx Upstream Has No Suitable Server Error", "All servers in the upstream were skipped due to constraints like down, backup, or max_fails.", """## Description

All servers in the upstream were skipped due to constraints like down, backup, or max_fails.

## Common Causes

- **All primary servers down** and no backup
- **Backup servers** cannot serve regular traffic
- **max_fails exceeded** on all servers
- **slow_start** preventing immediate use

## How to Fix

1. Remove `down` markers
2. Add non-backup servers
3. Reduce max_fails sensitivity
4. Validate: `sudo nginx -t`

## Examples

**Balanced:**
```nginx
upstream backend {
    server 10.0.0.1:8080 max_fails=3 fail_timeout=60s;
    server 10.0.0.2:8080 max_fails=3 fail_timeout=60s;
    server 10.0.0.3:8080 backup;
}
```""")
add("nginx-upstream-ssl-verify-error", "Nginx Upstream SSL Verify Failed Error", "Nginx cannot verify the SSL certificate presented by the upstream server.", """## Description

Nginx cannot verify the SSL certificate presented by the upstream server.

## Common Causes

- **Self-signed certificate** on backend
- **Expired certificate**
- **Missing CA certificate**
- **Hostname mismatch**

## How to Fix

1. Provide CA: `proxy_ssl_trusted_certificate /path/to/ca.pem; proxy_ssl_verify on;`
2. Dev only: `proxy_ssl_verify off;`
3. Set SNI: `proxy_ssl_name backend.example.com; proxy_ssl_server_name on;`
4. Test: `openssl s_client -connect backend:8443 -CAfile ca.pem`

## Examples

**Full verification:**
```nginx
location / {
    proxy_pass https://backend:8443;
    proxy_ssl_trusted_certificate /etc/ssl/certs/ca.pem;
    proxy_ssl_verify on;
    proxy_ssl_verify_depth 3;
    proxy_ssl_name backend.example.com;
    proxy_ssl_server_name on;
}
```""")
add("nginx-proxy-redirect-error", "Nginx Proxy Redirect Error", "The proxy_redirect directive is misconfigured or cannot rewrite the Location header.", """## Description

The proxy_redirect directive is misconfigured or cannot rewrite the Location header.

## Common Causes

- **Invalid proxy_redirect syntax**
- **Redirect URL does not match** upstream response
- **Missing proxy_redirect default**
- **Multiple conflicting redirects**

## How to Fix

1. Use default: `proxy_redirect default;`
2. Override specific: `proxy_redirect http://backend:8080/ https://example.com/;`
3. Disable: `proxy_redirect off;`

## Examples

**Rewrite:**
```nginx
location /api/ {
    proxy_pass http://backend:8080/api/;
    proxy_redirect http://backend:8080/ https://example.com/;
}
```
**Default:**
```nginx
location / { proxy_pass http://backend:8080/; proxy_redirect default; }
```""")
add("nginx-proxy-buffer-size-error", "Nginx Proxy Buffer Size Error", "The proxy buffer is too small to hold the upstream response headers or body.", """## Description

The proxy buffer is too small to hold the upstream response headers or body.

## Common Causes

- **Default buffer too small** (4k)
- **Large cookies/auth tokens**
- **Multiple Set-Cookie headers**
- **Response larger than buffers**

## How to Fix

1. Increase: `proxy_buffer_size 16k; proxy_buffers 4 32k;`
2. Temp files: `proxy_max_temp_file_size 1024m;`
3. Disable for streaming: `proxy_buffering off;`

## Examples

**Upload (no buffering):**
```nginx
location /upload/ {
    proxy_buffering off;
    proxy_request_buffering off;
    client_max_body_size 100M;
    proxy_pass http://backend:8080;
}
```
**API:**
```nginx
proxy_buffer_size 16k; proxy_buffers 8 16k; proxy_busy_buffers_size 32k;
```""")
add("nginx-upstream-keepalive-error", "Nginx Upstream Keepalive Error", "The keepalive connections to the upstream are misconfigured or exhausted.", """## Description

The keepalive connections to the upstream are misconfigured or exhausted.

## Common Causes

- **Missing keepalive directive**
- **keepalive value too low**
- **Missing Connection header**
- **Backend not supporting keepalive**

## How to Fix

1. Add keepalive: `upstream backend { server 10.0.0.1:8080; keepalive 32; }`
2. Set headers: `proxy_http_version 1.1; proxy_set_header Connection "";`
3. Set timeout: `keepalive_timeout 60s;`

## Examples

**Complete:**
```nginx
upstream backend {
    server 10.0.0.1:8080; server 10.0.0.2:8080;
    keepalive 64; keepalive_requests 1000; keepalive_timeout 60s;
}
server {
    location / {
        proxy_pass http://backend;
        proxy_http_version 1.1;
        proxy_set_header Connection "";
    }
}
```""")
add("nginx-upstream-hash-key-error", "Nginx Upstream Hash Key Error", "The hash directive in the upstream block has an invalid key or configuration.", """## Description

The hash directive in the upstream block has an invalid key or configuration.

## Common Causes

- **Missing hash key**
- **Undefined variable** as key
- **Hash with consistent placed incorrectly**

## How to Fix

1. Provide valid key: `hash $request_uri consistent;`
2. Use well-known vars ($request_uri, $remote_addr, $host)
3. Validate: `sudo nginx -t`

## Examples

**Invalid:**
```nginx
upstream backend { hash; server 10.0.0.1:8080; }  # missing key
```
**Valid:**
```nginx
upstream backend { hash $request_uri consistent; server 10.0.0.1:8080; server 10.0.0.2:8080; }
```""")
add("nginx-least-conn-error", "Nginx Least Connections Error", "The least_conn load balancing algorithm is not available or misconfigured.", """## Description

The least_conn load balancing algorithm is not available or misconfigured.

## Common Causes

- **Module not compiled in**
- **Used inside server block** instead of upstream
- **Combined with incompatible directives**

## How to Fix

1. Check module: `nginx -V 2>&1 | grep http_upstream_least_conn`
2. Use inside upstream: `upstream backend { least_conn; ... }`
3. Recompile if missing

## Examples

**Valid:**
```nginx
upstream app {
    least_conn;
    server 10.0.0.1:8080 weight=3;
    server 10.0.0.2:8080 weight=2;
    server 10.0.0.3:8080 weight=1;
}
```""")
add("nginx-ip-hash-unbalanced-error", "Nginx IP Hash Unbalanced Error", "The ip_hash algorithm distributes traffic unevenly due to NAT gateways or proxy IPs.", """## Description

The ip_hash algorithm distributes traffic unevenly due to NAT gateways or proxy IPs.

## Common Causes

- **Large NAT gateways** funneling many users
- **CDN or proxy IPs** aggregating traffic
- **Few public IPs** in pool

## How to Fix

1. Use hash with $request_id
2. Consider least_conn instead
3. Use weighted servers
4. Monitor: `awk '{print $1}' access.log | sort | uniq -c | sort -rn | head`

## Examples

**Alternative:**
```nginx
upstream backend {
    hash $remote_addr consistent;
    server 10.0.0.1:8080; server 10.0.0.2:8080;
}
```""")
add("nginx-sticky-cookie-error", "Nginx Sticky Cookie Error", "The sticky cookie directive (commercial or third-party module) is misconfigured.", """## Description

The sticky cookie directive (commercial or third-party module) is misconfigured.

## Common Causes

- **Module not loaded** (Nginx Plus required)
- **Invalid cookie parameters**
- **Duplicate sticky directives**

## How to Fix

1. Check module: `nginx -V 2>&1 | grep sticky`
2. Use correct syntax
3. Use open-source alternative with map/cookies

## Examples

**Nginx Plus:**
```nginx
upstream backend {
    sticky cookie srv_id expires=1h domain=.example.com path=/;
    server 10.0.0.1:8080; server 10.0.0.2:8080;
}
```""")
add("nginx-slow-start-error", "Nginx Slow Start Error", "The slow_start parameter is used with incompatible load balancing methods.", """## Description

The slow_start parameter is used with incompatible load balancing methods.

## Common Causes

- **slow_start with ip_hash** (incompatible)
- **slow_start with hash** (incompatible)
- **Module not compiled in**

## How to Fix

1. Remove ip_hash or use without slow_start
2. slow_start only works with least_conn or round-robin
3. Validate: `sudo nginx -t`

## Examples

**Compatible:**
```nginx
upstream backend {
    server 10.0.0.1:8080 slow_start=60s;
    server 10.0.0.2:8080 slow_start=60s;
    server 10.0.0.3:8080 backup;
}
```""")
add("nginx-backup-server-failed-error", "Nginx Backup Server Failed Error", "A backup server in the upstream block is unreachable or misconfigured.", """## Description

A backup server in the upstream block is unreachable or misconfigured.

## Common Causes

- **Backup server also down**
- **Port mismatch**
- **Not listening** on expected address
- **Firewall blocking**

## How to Fix

1. Verify: `curl -I http://backup:8080/health`
2. Ensure same config as primaries
3. Add multiple backups for redundancy

## Examples

**Test:**
```bash
for s in 10.0.0.1 10.0.0.2 10.0.0.3; do
    echo -n "$s:8080 -> "
    curl -s -o /dev/null -w "%{http_code}" http://$s:8080/health
done
```""")
add("nginx-fail-timeout-error", "Nginx Fail Timeout Expired Error", "A server was marked as failed and will not be retried until fail_timeout expires.", """## Description

A server was marked as failed and will not be retried until fail_timeout expires.

## Common Causes

- **Server repeatedly failing** health checks
- **max_fails threshold** reached
- **Short fail_timeout** causing frequent ejections
- **Backend not recovering**

## How to Fix

1. Adjust: `server 10.0.0.1:8080 max_fails=3 fail_timeout=30s;`
2. Fix the failing backend
3. Set reasonable fail_timeout (30s-120s)
4. Monitor: `tail -f /var/log/nginx/error.log | grep upstream`

## Examples

**Balanced:**
```nginx
upstream backend {
    server 10.0.0.1:8080 max_fails=5 fail_timeout=60s;
    server 10.0.0.2:8080 max_fails=5 fail_timeout=60s;
}
```""")
add("nginx-max-fails-exceeded-error", "Nginx Max Fails Exceeded Error", "A server in the upstream pool exceeded max_fails and is temporarily disabled.", """## Description

A server in the upstream pool exceeded max_fails and is temporarily disabled.

## Common Causes

- **Backend crashing** or returning 5xx
- **Network issues**
- **Timeout errors**
- **Health checks failing consistently**

## How to Fix

1. Increase tolerance: `server 10.0.0.1:8080 max_fails=10 fail_timeout=120s;`
2. Investigate: `grep upstream /var/log/nginx/error.log | tail -20`
3. Add retry: `proxy_next_upstream error timeout http_502 http_503;`
4. Fix the backend

## Examples

**Monitor:**
```bash
grep -c 'connect() failed' /var/log/nginx/error.log
grep -c 'upstream timed out' /var/log/nginx/error.log
```""")
add("nginx-upstream-zone-not-found-error", "Nginx Upstream Zone Not Found Error", "The shared memory zone referenced by the upstream block does not exist or is misconfigured.", """## Description

The shared memory zone referenced by the upstream block does not exist or is misconfigured.

## Common Causes

- **Zone name mismatch**
- **Zone deleted** during reload
- **Multiple configs** defining same upstream

## How to Fix

1. Check: `grep -rn 'upstream' /etc/nginx/conf.d/ | grep -v '#'`
2. Ensure each upstream defined once
3. Validate: `sudo nginx -t`

## Examples

**Properly defined:**
```nginx
upstream backend {
    zone backend_zone 64k;
    server 10.0.0.1:8080; server 10.0.0.2:8080;
}
```""")
add("nginx-health-check-failed-error", "Nginx Health Check Failed Error", "Nginx or a third-party module detected that a backend server is unhealthy.", """## Description

Nginx or a third-party module detected that a backend server is unhealthy.

## Common Causes

- **Backend returning non-200**
- **Health endpoint errors**
- **Timeout on health checks**
- **Backend not deployed**

## How to Fix

1. Verify: `curl -I http://backend:8080/health`
2. Use proxy_next_upstream to failover
3. Fix the backend health endpoint

## Examples

**Config:**
```nginx
upstream backend {
    server 10.0.0.1:8080 max_fails=3 fail_timeout=30s;
    server 10.0.0.2:8080 max_fails=3 fail_timeout=30s;
}
location / {
    proxy_pass http://backend;
    proxy_next_upstream error timeout http_502 http_503;
}
```""")
add("nginx-malformed-headers-error", "Nginx Client Sent Malformed Headers Error", "The client sent HTTP headers that are syntactically invalid or malformed.", """## Description

The client sent HTTP headers that are syntactically invalid or malformed.

## Common Causes

- **Invalid characters** (control chars, null bytes)
- **Missing colon separator**
- **Extremely long header lines**
- **Binary data** in text headers

## How to Fix

1. Check client application
2. Increase buffers: `large_client_header_buffers 4 16k;`
3. Enable logging: `error_log /var/log/nginx/error.log warn;`
4. Use proxy_set_header to fix upstream headers

## Examples

**Increase:**
```nginx
server { listen 80; large_client_header_buffers 4 32k; }
```
**Inspect:**
```bash
tail -f /var/log/nginx/error.log | grep invalid
```""")
add("nginx-client-closed-connection-error", "Nginx Client Closed Connection Error", "The client terminated the connection before the server finished processing.", """## Description

The client terminated the connection before the server finished processing.

## Common Causes

- **Browser timeout**
- **User navigated away**
- **Load balancer health check timeout**
- **Client too short timeout**

## How to Fix

1. Tune timeouts: `client_body_timeout 60s; client_header_timeout 60s;`
2. Investigate backend latency
3. Set proxy_read_timeout
4. Monitor 499: `awk '$9 == 499' access.log | wc -l`

## Examples

**Adjust:**
```nginx
client_body_timeout 120s;
client_header_timeout 60s;
send_timeout 30s;
```
**Monitor:**
```bash
grep ' 499 ' /var/log/nginx/access.log | tail -10
```""")
add("nginx-request-line-too-long-error", "Nginx Request Line Too Long Error", "The HTTP request line exceeds the configured buffer size.", """## Description

The HTTP request line exceeds the configured buffer size.

## Common Causes

- **Very long URL** with many params
- **Session tokens** in URL
- **Malicious oversized URIs**
- **Default buffer too small** (8k)

## How to Fix

1. Increase: `large_client_header_buffers 4 16k;`
2. Limit URI length at app level
3. Use POST for large data
4. Set client_header_buffer_size

## Examples

**Default (may be too small):**
```nginx
# large_client_header_buffers 4 8k
```
**Increased:**
```nginx
large_client_header_buffers 4 32k;
```
**Check:**
```bash
awk '{print length($6), $7}' /var/log/nginx/access.log | sort -rn | head
```""")
add("nginx-uri-too-long-error", "Nginx URI Too Long Error", "The requested URI is longer than the maximum allowed length (HTTP 414).", """## Description

The requested URI is longer than the maximum allowed length (HTTP 414).

## Common Causes

- **Excessive query parameters**
- **Session data in URL**
- **Malformed client** generating long URLs
- **API clients** constructing URLs wrong

## How to Fix

1. Increase buffer: `large_client_header_buffers 4 32k;`
2. Set header buffer: `client_header_buffer_size 4k;`
3. Return 414 for long URIs
4. Fix client app

## Examples

**Check lengths:**
```bash
awk '{print length($7), $7}' /var/log/nginx/access.log | sort -rn | head
```
**Buffer:**
```nginx
client_header_buffer_size 4k;
large_client_header_buffers 4 32k;
```""")
add("nginx-headers-too-large-error", "Nginx Headers Too Large Error", "The total size of all request headers exceeds the configured buffer limit.", """## Description

The total size of all request headers exceeds the configured buffer limit.

## Common Causes

- **Too many cookies**
- **Large Authorization headers** (JWT)
- **Custom headers with large values**
- **Browser accumulating cookies**

## How to Fix

1. Increase: `large_client_header_buffers 4 32k;`
2. Reduce cookie size
3. Move large data to body
4. Strip cookies: `proxy_set_header Cookie $cookie_small;`

## Examples

**Increase:**
```nginx
large_client_header_buffers 8 16k;
```
**Strip cookies:**
```nginx
location /api/ { proxy_set_header Cookie ""; proxy_pass http://backend; }
```""")
add("nginx-body-too-large-error", "Nginx Request Body Too Large Error", "The client request body exceeds the client_max_body_size limit (HTTP 413).", """## Description

The client request body exceeds the client_max_body_size limit (HTTP 413).

## Common Causes

- **File upload exceeds limit**
- **Large JSON payloads**
- **Default limit too small** (1MB)
- **Uncompressed uploads**

## How to Fix

1. Increase: `client_max_body_size 100M;`
2. Set per-location limits
3. Disable (caution): `client_max_body_size 0;`
4. Enable buffering: `client_body_buffer_size 128k;`

## Examples

**Default (1MB):**
```nginx
client_max_body_size 1M;
```
**Per-location:**
```nginx
location /upload/ { client_max_body_size 1G; client_body_buffer_size 128k; }
```""")
add("nginx-content-length-mismatch-error", "Nginx Content Length Mismatch Error", "The actual request body size does not match the Content-Length header value.", """## Description

The actual request body size does not match the Content-Length header value.

## Common Causes

- **Client miscalculating** Content-Length
- **Chunked encoding** mixed with Content-Length
- **Compression** changing body size
- **Client sending after declaring close**

## How to Fix

1. Verify client sends correct Content-Length
2. Enable strict parsing: `client_body_in_single_buffer on;`
3. Check client HTTP library

## Examples

**Test:**
```bash
curl -X POST -d '{"key":"value"}' -H 'Content-Type: application/json' http://localhost:8080/api
```
**Buffer:**
```nginx
client_body_buffer_size 128k; client_max_body_size 100M;
```""")
add("nginx-method-not-allowed-error", "Nginx Method Not Allowed Error", "The client sent an HTTP method not permitted for the requested resource (HTTP 405).", """## Description

The client sent an HTTP method not permitted for the requested resource (HTTP 405).

## Common Causes

- **Wrong method** (POST to GET-only)
- **CORS preflight** (OPTIONS) not handled
- **Restrictive Nginx config**

## How to Fix

1. Allow methods: `if ($request_method !~ ^(GET|POST|PUT|DELETE|PATCH)$) { return 405; }`
2. Use limit_except
3. Handle OPTIONS for CORS

## Examples

**Restrict:**
```nginx
location /upload/ {
    limit_except POST { deny all; }
    client_max_body_size 100M;
    proxy_pass http://backend;
}
```""")
add("nginx-unsupported-media-type-error", "Nginx Unsupported Media Type Error", "The client sent a Content-Type that the server or backend does not accept (HTTP 415).", """## Description

The client sent a Content-Type that the server or backend does not accept (HTTP 415).

## Common Causes

- **Wrong Content-Type** (text/plain instead of application/json)
- **Backend rejecting** types
- **Missing Content-Type header**
- **Multipart boundary issues**

## How to Fix

1. Check client: `curl -X POST -H 'Content-Type: application/json' ...`
2. Validate at Nginx level
3. Ensure backend accepts the type

## Examples

**Validate:**
```nginx
location /api/ {
    set $valid 0;
    if ($content_type ~* '^(application/json|application/x-www-form-urlencoded)$') { set $valid 1; }
    if ($valid = 0) { return 415; }
    proxy_pass http://backend;
}
```""")
add("nginx-range-not-satisfiable-error", "Nginx Range Not Satisfiable Error", "The client requested a byte range outside the bounds of the available resource (HTTP 416).", """## Description

The client requested a byte range outside the bounds of the available resource (HTTP 416).

## Common Causes

- **Range start exceeds** file size
- **Range end exceeds** file size
- **Malformed Range header**
- **File size changed** since calculation

## How to Fix

1. Ensure backend handles Range correctly
2. Validate Range format
3. Disable if not needed: `proxy_set_header Range "";`

## Examples

**Test:**
```bash
curl -r 0-1023 http://example.com/file.zip -o /dev/null -w '%{http_code}'
# Valid: 206 Partial Content
# Invalid: 416 Range Not Satisfiable
```""")
add("nginx-rewrite-cycle-error", "Nginx Rewrite or Internal Redirect Cycle Error", "Nginx detected an infinite loop of rewrites or internal redirects.", """## Description

Nginx detected an infinite loop of rewrites or internal redirects.

## Common Causes

- **Rewrite rules redirecting to themselves**
- **try_files pointing to looping location**
- **Recursive rewrites** without terminal condition
- **Broken alias/root**

## How to Fix

1. Trace: `curl -vL http://example.com/page 2>&1 | grep -i location`
2. Check self-referencing rules
3. Add break or condition
4. Use return instead of rewrite

## Examples

**Broken:**
```nginx
location / { try_files $uri $uri/ @fallback; }
location @fallback { rewrite ^ /index.php last; }  # loops
```
**Fixed:**
```nginx
location / { try_files $uri $uri/ /index.php?$args; }
```""")
add("nginx-rewrite-not-allowed-error", "Nginx Rewrite Directive Not Allowed Error", "The rewrite directive is used in a context where it is not permitted.", """## Description

The rewrite directive is used in a context where it is not permitted.

## Common Causes

- **rewrite inside if** in location block
- **rewrite inside limit_except**
- **Wrong nesting level**

## How to Fix

1. Move rewrite to correct context
2. Use return inside if blocks
3. Use named locations for complex rewrites

## Examples

**Invalid:**
```nginx
location / {
    if ($request_uri ~ '^/old') { rewrite ^ /new permanent; }  # not allowed
}
```
**Fixed:**
```nginx
location ~ ^/old/(.*) { return 301 /new/$1; }
```""")
add("nginx-return-directive-error", "Nginx Return Directive Error", "The return directive has an invalid status code or malformed redirect URL.", """## Description

The return directive has an invalid status code or malformed redirect URL.

## Common Causes

- **Non-numeric status code**
- **Status code outside valid range**
- **Missing URL for redirect codes** (301, 302)

## How to Fix

1. Use valid codes: 200, 204, 301, 302, 303, 304, 307, 308, 400-599
2. Ensure redirects have URL
3. Use body for non-redirect codes

## Examples

**Valid:**
```nginx
return 200 'Welcome!';
return 301 https://www.example.com$request_uri;
return 403;
return 503 'Service Unavailable';
```
**Invalid:**
```nginx
return 999;    # invalid code
return 301;    # missing URL
```""")
add("nginx-if-is-evil-error", "Nginx If Is Evil Error", "Using the if directive inside a location block causes unexpected behavior with other directives.", """## Description

Using the if directive inside a location block causes unexpected behavior with other directives.

## Common Causes

- **if with proxy_pass** applies both location and if directives
- **if with add_header** causes duplicate headers
- **if with try_files** causes unexpected routing
- **if does NOT create a separate scope**

## How to Fix

1. Use separate location blocks instead of if
2. Only use if safely with: return, rewrite...last, set
3. Use map for complex conditions

## Examples

**Safe:**
```nginx
location / {
    set $backend default;
    if ($host = admin.example.com) { set $backend admin; }
    proxy_pass http://$backend;
}
```
**Unsafe:**
```nginx
location / {
    if ($request_uri ~ '^/api') {
        add_header X-API true;  # duplicated!
        proxy_pass http://api;
    }
    proxy_pass http://default;
}
```""")
add("nginx-break-error", "Nginx Break Directive Error", "The break directive is used in the wrong context or causes unintended behavior.", """## Description

The break directive is used in the wrong context or causes unintended behavior.

## Common Causes

- **break inside if** not stopping rewrites as expected
- **break in wrong nesting level**
- **Mixing break with rewrite** causing confusion

## How to Fix

1. Use break only in server/location context
2. break stops rewrite processing but does not change URI
3. Use last to restart location matching

## Examples

**break vs last:**
```nginx
rewrite ^/test$ /test.html break;    # stops rewrites, processes location
rewrite ^/old$ /new last;            # restarts location matching
```
**Valid:**
```nginx
location / {
    rewrite ^/(.*)$ /index.php?path=$1 break;
    fastcgi_pass unix:/run/php-fpm.sock;
}
```""")
add("nginx-rewrite-duplicate-error", "Nginx Rewrite Duplicate Error", "Multiple rewrite rules with identical patterns cause conflicts.", """## Description

Multiple rewrite rules with identical patterns cause conflicts.

## Common Causes

- **Copy-paste errors**
- **Include files** with same rewrites
- **Multiple rewrites** with identical regex

## How to Fix

1. Find: `grep -rn 'rewrite' /etc/nginx/conf.d/ | sort`
2. Remove or merge duplicates
3. Use break/last appropriately

## Examples

**Duplicate:**
```nginx
rewrite ^/old/(.*)$ /new/$1 permanent;
rewrite ^/old/(.*)$ /new/$1 permanent;
```
**Fixed:**
```nginx
rewrite ^/old/(.*)$ /new/$1 permanent;
```""")
add("nginx-named-location-recursion-error", "Nginx Named Location Recursion Error", "A named location references itself or creates an infinite recursion chain.", """## Description

A named location references itself or creates an infinite recursion chain.

## Common Causes

- **error_page** pointing to location triggering same error
- **try_files** referencing looping location
- **Recursive @location chains**

## How to Fix

1. Check error_page directives
2. Ensure named locations have terminal actions
3. Trace: `grep -rn '@' /etc/nginx/conf.d/ | grep -E 'error_page|try_files'`

## Examples

**Loop:**
```nginx
error_page 404 @fallback;
location @fallback { try_files /index.html @fallback; }  # loops
```
**Fixed:**
```nginx
error_page 404 @fallback;
location @fallback { root /var/www; try_files /index.html =404; }
```""")
add("nginx-redirect-loop-error", "Nginx Redirect Loop Error", "The server creates an infinite redirect loop between HTTP and HTTPS or between URLs.", """## Description

The server creates an infinite redirect loop between HTTP and HTTPS or between URLs.

## Common Causes

- **HTTP-to-HTTPS redirect** not accounting for LB
- **Missing X-Forwarded-Proto** from LB
- **Both HTTP and HTTPS** redirecting to each other
- **Proxy passing** to self-redirecting server

## How to Fix

1. Use X-Forwarded-Proto for LBs
2. Handle forwarded headers
3. Trace: `curl -vL http://example.com 2>&1 | grep -i location`

## Examples

**Broken:**
```nginx
server { listen 80; return 301 https://example.com; }
server { listen 443 ssl; return 301 http://example.com; }  # loop
```
**Fixed:**
```nginx
server { listen 80; return 301 https://example.com$request_uri; }
server { listen 443 ssl; server_name example.com; root /var/www/html; }
```""")
add("nginx-limit-req-zone-missing-error", "Nginx Limit Req Zone Missing Error", "The limit_req directive references a zone not defined with limit_req_zone.", """## Description

The limit_req directive references a zone not defined with limit_req_zone.

## Common Causes

- **limit_req used without** limit_req_zone
- **Zone name mismatch**
- **limit_req_zone in wrong context** (must be http level)

## How to Fix

1. Define zone first: `limit_req_zone $binary_remote_addr zone=api_limit:10m rate=10r/s;`
2. Check name matches exactly
3. Ensure at http level

## Examples

**Complete:**
```nginx
http {
    limit_req_zone $binary_remote_addr zone=login:10m rate=1r/s;
    limit_req_zone $binary_remote_addr zone=api:10m rate=100r/s;
    server {
        location /login { limit_req zone=login burst=3 nodelay; proxy_pass http://backend; }
        location /api/ { limit_req zone=api burst=50 nodelay; proxy_pass http://backend; }
    }
}
```""")
add("nginx-limit-conn-zone-missing-error", "Nginx Limit Conn Zone Missing Error", "The limit_conn directive references a zone not defined with limit_conn_zone.", """## Description

The limit_conn directive references a zone not defined with limit_conn_zone.

## Common Causes

- **limit_conn without limit_conn_zone**
- **Zone name typo**
- **Wrong context**

## How to Fix

1. Define: `limit_conn_zone $binary_remote_addr zone=conn_limit:10m;`
2. Verify name matches

## Examples

**Config:**
```nginx
http {
    limit_conn_zone $binary_remote_addr zone=per_ip:10m;
    limit_conn_zone $server_name zone=per_host:10m;
    server {
        location /large-files/ {
            limit_conn per_ip 5;
            limit_conn per_host 100;
            proxy_pass http://backend;
        }
    }
}
```""")
add("nginx-auth-basic-user-file-error", "Nginx Auth Basic User File Error", "The htpasswd file referenced by auth_basic_user_file cannot be read or is malformed.", """## Description

The htpasswd file referenced by auth_basic_user_file cannot be read or is malformed.

## Common Causes

- **File does not exist**
- **Incorrect permissions**
- **Malformed htpasswd entries**
- **Wrong path**

## How to Fix

1. Create: `htpasswd -c /etc/nginx/.htpasswd admin`
2. Permissions: `chown root:www-data /etc/nginx/.htpasswd; chmod 640 /etc/nginx/.htpasswd`
3. Verify: `sudo -u www-data cat /etc/nginx/.htpasswd`
4. Validate: `sudo nginx -t`

## Examples

**Config:**
```nginx
location /admin/ {
    auth_basic "Restricted Area";
    auth_basic_user_file /etc/nginx/.htpasswd;
    proxy_pass http://backend;
}
```
**Create:**
```bash
sudo apt install apache2-utils
sudo htpasswd -c /etc/nginx/.htpasswd admin
```""")
add("nginx-auth-request-error", "Nginx Auth Request Error", "The auth_request subrequest to the authentication service failed or returned an error.", """## Description

The auth_request subrequest to the authentication service failed or returned an error.

## Common Causes

- **Auth service down**
- **Auth returning 500**
- **Timeout connecting**
- **Wrong URI**

## How to Fix

1. Verify: `curl -I http://auth-service:8080/verify`
2. Set timeout: `proxy_connect_timeout 5s; proxy_read_timeout 5s;`
3. Handle failures gracefully

## Examples

**Setup:**
```nginx
location /api/ { auth_request /auth; proxy_pass http://backend; }
location = /auth {
    internal;
    proxy_pass http://auth:8080/validate;
    proxy_pass_request_body off;
    proxy_set_header Content-Length "";
    proxy_set_header X-Original-URI $request_uri;
}
```""")
add("nginx-stub-status-error", "Nginx Stub Status Error", "The stub_status module is not enabled or the status endpoint is misconfigured.", """## Description

The stub_status module is not enabled or the status endpoint is misconfigured.

## Common Causes

- **Module not compiled in**
- **stub_status outside location block**
- **Wrong context**

## How to Fix

1. Check: `nginx -V 2>&1 | grep http_stub_status`
2. Configure: `location /nginx_status { stub_status; allow 127.0.0.1; deny all; }`
3. Recompile if missing

## Examples

**Config:**
```nginx
server {
    listen 8080; server_name localhost;
    location /nginx_status {
        stub_status; access_log off; allow 127.0.0.1; deny all;
    }
}
```
**Check:**
```bash
curl http://localhost:8080/nginx_status
```""")
add("nginx-sub-filter-types-error", "Nginx Sub Filter Types Mismatch Error", "The sub_filter_types directive does not include the MIME type of the response being filtered.", """## Description

The sub_filter_types directive does not include the MIME type of the response being filtered.

## Common Causes

- **Default sub_filter_types** only includes text/html
- **API responses** with application/json not included
- **Custom MIME types** missing

## How to Fix

1. Add types: `sub_filter_types text/html text/plain application/json application/javascript;`
2. Use * for all (careful with binary)
3. Set sub_filter_once: `sub_filter_once off;`

## Examples

**Filter HTML and JSON:**
```nginx
sub_filter_types text/html application/json text/plain;
sub_filter 'example.com' 'newdomain.com';
sub_filter_once off;
```
**With proxy:**
```nginx
location / {
    sub_filter 'http://' 'https://';
    sub_filter_types text/html text/css application/javascript;
    proxy_pass http://backend;
}
```""")
add("nginx-addition-types-error", "Nginx Addition Types Error", "The addition_types directive does not match the MIME type of the response being modified.", """## Description

The addition_types directive does not match the MIME type of the response being modified.

## Common Causes

- **Default addition_types** only includes text/html
- **Response type not matching**
- **Module not compiled in**

## How to Fix

1. Add types: `addition_types text/html text/plain application/json;`
2. Add content before/after response

## Examples

**Config:**
```nginx
location / {
    addition_types text/html text/plain;
    add_before_body /includes/header.html;
    add_after_body /includes/footer.html;
    proxy_pass http://backend;
}
```""")
add("nginx-perl-module-error", "Nginx Perl Module Error", "The embedded Perl module encountered a compilation or runtime error.", """## Description

The embedded Perl module encountered a compilation or runtime error.

## Common Causes

- **Perl syntax error**
- **Missing Perl module**
- **Module not compiled in**
- **File permission issues**

## How to Fix

1. Test: `perl -c /etc/nginx/perl/handler.pl`
2. Check: `nginx -V 2>&1 | grep http_perl_module`
3. Install missing: `sudo cpan install JSON`
4. Check handler syntax

## Examples

**Handler:**
```nginx
location /hello {
    perl 'sub {
        my $r = shift;
        $r->headers_out->set("Content-Type", "text/plain");
        $r->send_http_header("200 OK");
        $r->print("Hello from Perl!\n");
        return OK;
    }';
}
```""")
add("nginx-split-clients-range-error", "Nginx Split Clients Range Overflow Error", "The split_clients percentage values exceed 100% or have overlapping ranges.", """## Description

The split_clients percentage values exceed 100% or have overlapping ranges.

## Common Causes

- **Percentages summing > 100%**
- **Overlapping ranges**
- **Missing catch-all ***

## How to Fix

1. Ensure total <= 100%
2. Use * for remainder: `50% a; * b;`
3. Validate: `sudo nginx -t`

## Examples

**Invalid:**
```nginx
split_clients $request_id $v { 60% a; 50% b; }  # > 100%
```
**Valid:**
```nginx
split_clients $request_id $v { 25% v1; 25% v2; 25% v3; 25% v4; }
```""")
add("nginx-geo-block-invalid-error", "Nginx Geo Block Invalid Error", "The geo block contains invalid IP addresses, overlapping CIDR ranges, or malformed syntax.", """## Description

The geo block contains invalid IP addresses, overlapping CIDR ranges, or malformed syntax.

## Common Causes

- **Prefix length > 32** (IPv4) or > 128 (IPv6)
- **Invalid IP format**
- **Overlapping CIDR ranges**
- **Missing default**

## How to Fix

1. Use valid CIDR: `192.168.0.0/16`
2. Validate: `python3 -c "import ipaddress; print(ipaddress.ip_network('192.168.0.0/16'))"`
3. Ensure default set
4. Validate: `sudo nginx -t`

## Examples

**Invalid:**
```nginx
geo $region { default 0; 192.168.1.1/33 1; }  # prefix > 32
```
**Valid:**
```nginx
geo $region { default 0; 192.168.0.0/16 1; 10.0.0.0/8 1; 172.16.0.0/12 1; }
```""")
add("nginx-failed-accept-connection-error", "Nginx Failed to Accept New Connection Error", "Nginx cannot accept new TCP connections because the accept mutex or socket is in a bad state.", """## Description

Nginx cannot accept new TCP connections because the accept mutex or socket is in a bad state.

## Common Causes

- **File descriptor limit reached**
- **Socket backlog full**
- **Network interface saturated**
- **Port already in use**

## How to Fix

1. Increase FDs: `ulimit -n 65535`
2. Increase backlog: `listen 80 backlog=65535;`
3. Check ports: `ss -tlnp | grep :80`
4. Use reuseport: `listen 80 reuseport;`

## Examples

**Optimized:**
```nginx
listen 80 reuseport backlog=65535;
listen 443 ssl reuseport backlog=65535;
```
**Check:**
```bash
ls /proc/$(cat /run/nginx.pid)/fd | wc -l
cat /proc/$(cat /run/nginx.pid)/limits | grep 'Max open files'
```""")
add("nginx-out-of-memory-error", "Nginx Out of Memory Error", "Nginx worker process was killed by the OOM killer due to excessive memory usage.", """## Description

Nginx worker process was killed by the OOM killer due to excessive memory usage.

## Common Causes

- **Large client body buffering**
- **Too many workers**
- **Memory leak** in module
- **Large proxy buffers/cache**
- **High concurrency**

## How to Fix

1. Reduce buffers: `client_body_buffer_size 8k; proxy_buffer_size 4k;`
2. Limit workers: `worker_processes 4;`
3. Monitor: `ps aux | grep nginx | awk '{sum+=$6} END {print sum/1024 " MB"}'`
4. Check: `free -h`

## Examples

**Memory-conscious:**
```nginx
worker_processes 4;
worker_rlimit_nofile 16384;
events { worker_connections 4096; }
http {
    client_body_buffer_size 8k;
    proxy_buffer_size 4k;
    proxy_buffers 4 4k;
}
```""")
add("nginx-worker-process-exited-error", "Nginx Worker Process Exited Abnormally Error", "An Nginx worker process terminated unexpectedly with a non-zero exit code.", """## Description

An Nginx worker process terminated unexpectedly with a non-zero exit code.

## Common Causes

- **Segmentation fault** in module
- **Invalid memory access**
- **Third-party module crash**
- **Corrupted shared memory**
- **Insufficient shared memory**

## How to Fix

1. Check logs: `grep 'worker process' /var/log/nginx/error.log | tail -10`
2. Update Nginx and modules
3. Increase shared memory: `echo 268435456 | sudo tee /proc/sys/kernel/shmmax`
4. Disable problematic modules

## Examples

**Check signal:**
```bash
grep 'worker process' /var/log/nginx/error.log | tail -5
# Look for signal: 11 (SIGSEGV), 7 (SIGBUS), etc.
```""")
add("nginx-could-not-build-server-names-error", "Nginx Could Not Build Server Names Error", "Nginx failed to build the server names hash table, typically due to too many unique server names.", """## Description

Nginx failed to build the server names hash table, typically due to too many unique server names.

## Common Causes

- **Too many unique server names**
- **Server name hash bucket too small**
- **Wildcard conflicts**

## How to Fix

1. Increase hash: `server_names_hash_bucket_size 128;`
2. Or disable: `server_names_hash_max_size 4096; server_names_hash_bucket_size 128;`
3. Remove unused server names

## Examples

**Config:**
```nginx
http {
    server_names_hash_bucket_size 128;
    server_names_hash_max_size 4096;
    # ...
}
```""")
add("nginx-api-not-enabled-error", "Nginx API Not Enabled Error", "The Nginx API or status module is not enabled in the compiled binary.", """## Description

The Nginx API or status module is not enabled in the compiled binary.

## Common Causes

- **Module not compiled in**
- **Trying to use stub_status or api without module**
- **Wrong Nginx build**

## How to Fix

1. Check: `nginx -V 2>&1 | grep -E 'stub_status|api'`
2. Use official Nginx package with modules
3. Recompile with --with-http_stub_status_module

## Examples

**Check modules:**
```bash
nginx -V 2>&1 | tr ' ' '\n' | grep 'with-'
```""")
add("nginx-process-id-out-of-range-error", "Nginx Process ID Out of Range Error", "The Nginx master process PID file contains an invalid or out-of-range process ID.", """## Description

The Nginx master process PID file contains an invalid or out-of-range process ID.

## Common Causes

- **Corrupted PID file**
- **Stale PID file** from old process
- **PID file from wrong Nginx instance**

## How to Fix

1. Check PID file: `cat /run/nginx.pid`
2. Verify process: `ps -p $(cat /run/nginx.pid)`
3. Remove stale: `rm /run/nginx.pid && sudo nginx`
4. Check for multiple instances

## Examples

**Check:**
```bash
cat /run/nginx.pid
ps -p $(cat /run/nginx.pid)
# If no process, PID file is stale
```
**Fix:**
```bash
sudo rm /run/nginx.pid
sudo nginx
```""")
add("nginx-socket-file-not-found-error", "Nginx Socket File Not Found Error", "The Unix socket file referenced in the configuration does not exist.", """## Description

The Unix socket file referenced in the configuration does not exist.

## Common Causes

- **Socket file deleted**
- **Backend not creating socket**
- **Wrong path** in config
- **Permission issues**

## How to Fix

1. Check: `ls -la /run/nginx.sock`
2. Verify backend creates socket
3. Fix path in config
4. Check permissions

## Examples

**Check:**
```bash
ls -la /run/nginx.sock
# If missing, backend may need restart
```
**Fix:**
```bash
sudo systemctl restart app-backend
ls -la /run/nginx.sock
```""")
add("nginx-open-file-limit-error", "Nginx Open File Limit Reached Error", "Nginx has reached the system limit for open file descriptors.", """## Description

Nginx has reached the system limit for open file descriptors.

## Common Causes

- **Too many open connections**
- **Cache files** consuming FDs
- **Keepalive connections** not releasing
- **FD limit too low**

## How to Fix

1. Check: `cat /proc/$(cat /run/nginx.pid)/limits | grep 'Max open files'`
2. Increase: `worker_rlimit_nofile 65535;` in nginx.conf
3. System limits: `ulimit -n 65535`
4. Monitor: `ls /proc/$(cat /run/nginx.pid)/fd | wc -l`

## Examples

**Config:**
```nginx
worker_rlimit_nofile 65535;
events { worker_connections 16384; }
```
**System:**
```bash
# /etc/security/limits.conf
* soft nofile 65535
* hard nofile 65535
```""")
add("nginx-worker-connections-overflow-error", "Nginx Worker Connections Overflow Error", "The worker_connections limit is being exceeded by active connections.", """## Description

The worker_connections limit is being exceeded by active connections.

## Common Causes

- **Traffic spike** exceeding capacity
- **worker_connections too low**
- **Keep-alive connections** accumulating
- **Slow backend** causing connections to pile up

## How to Fix

1. Increase: `worker_connections 16384;`
2. Increase FDs: `worker_rlimit_nofile 65535;`
3. Use multi_accept: `multi_accept on;`
4. Monitor: `curl http://localhost/nginx_status`

## Examples

**Production:**
```nginx
worker_processes auto;
worker_rlimit_nofile 65535;
events {
    worker_connections 16384;
    use epoll;
    multi_accept on;
}
```""")
add("nginx-connect-unix-socket-error", "Nginx Connect to Unix Socket Failed Error", "Nginx cannot connect to the upstream Unix socket.", """## Description

Nginx cannot connect to the upstream Unix socket.

## Common Causes

- **Socket file does not exist**
- **Backend not running**
- **Permission denied**
- **Socket path wrong**

## How to Fix

1. Check socket: `ls -la /run/php-fpm.sock`
2. Verify backend running: `systemctl status php-fpm`
3. Check permissions: `ls -la /run/php-fpm.sock`
4. Fix path in config

## Examples

**Check:**
```bash
ls -la /run/php-fpm.sock
# If missing, restart backend
sudo systemctl restart php-fpm
```
**Config:**
```nginx
location ~ \.php$ {
    fastcgi_pass unix:/run/php-fpm.sock;
    fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
}
```""")
add("nginx-access-log-open-error", "Nginx Access Log File Open Error", "Nginx cannot open the access log file for writing.", """## Description

Nginx cannot open the access log file for writing.

## Common Causes

- **Directory does not exist**
- **Permission denied**
- **Disk full**
- **Invalid path** in config

## How to Fix

1. Check directory: `ls -la /var/log/nginx/`
2. Permissions: `chown nginx:nginx /var/log/nginx/`
3. Disk space: `df -h /var/log/`
4. Fix path in config

## Examples

**Check:**
```bash
ls -la /var/log/nginx/
df -h /var/log/
```
**Fix:**
```bash
sudo mkdir -p /var/log/nginx
sudo chown nginx:nginx /var/log/nginx/
```""")
add("nginx-error-log-open-error", "Nginx Error Log File Open Error", "Nginx cannot open the error log file for writing.", """## Description

Nginx cannot open the error log file for writing.

## Common Causes

- **Directory does not exist**
- **Permission denied**
- **Disk full**
- **Invalid path**

## How to Fix

1. Check: `ls -la /var/log/nginx/`
2. Permissions: `sudo chown nginx:nginx /var/log/nginx/`
3. Disk: `df -h`
4. Validate: `sudo nginx -t`

## Examples

**Fix:**
```bash
sudo mkdir -p /var/log/nginx
sudo chown nginx:nginx /var/log/nginx/
sudo nginx -t
```""")
add("nginx-log-format-undefined-error", "Nginx Log Format Undefined Error", "The access_log directive references a log format that was not defined with log_format.", """## Description

The access_log directive references a log format that was not defined with log_format.

## Common Causes

- **access_log referencing undefined format**
- **log_format in wrong context**
- **Typo in format name**

## How to Fix

1. Define format before use
2. Check name matches exactly
3. Ensure at http level

## Examples

**Config:**
```nginx
http {
    log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                    '$status $body_bytes_sent "$http_referer" "$http_user_agent"';
    access_log /var/log/nginx/access.log main;
}
```""")
add("nginx-syslog-connection-error", "Nginx Syslog Connection Error", "Nginx cannot establish a connection to the syslog server for log forwarding.", """## Description

Nginx cannot establish a connection to the syslog server for log forwarding.

## Common Causes

- **Syslog server unreachable**
- **Firewall blocking**
- **Invalid syslog address**
- **DNS resolution failure**

## How to Fix

1. Check: `nc -zv syslog-server 514`
2. Verify address in config
3. Check firewall
4. Test DNS: `dig syslog-server.example.com +short`

## Examples

**Config:**
```nginx
access_log syslog:server=192.168.1.100:514,facility=local7,tag=nginx main;
```
**Test:**
```bash
nc -zv 192.168.1.100 514
```""")
add("nginx-log-rotation-failed-error", "Nginx Log Rotation Failed Error", "The log rotation process failed to properly rotate Nginx log files.", """## Description

The log rotation process failed to properly rotate Nginx log files.

## Common Causes

- **Logrotate script error**
- **Nginx not receiving USR1 signal**
- **Permission issues** on log directory
- **Disk space** during rotation

## How to Fix

1. Check logrotate: `cat /etc/logrotate.d/nginx`
2. Send USR1: `sudo kill -USR1 $(cat /run/nginx.pid)`
3. Check permissions
4. Verify: `ls -la /var/log/nginx/`

## Examples

**Manual rotation:**
```bash
mv /var/log/nginx/access.log /var/log/nginx/access.log.1
sudo kill -USR1 $(cat /run/nginx.pid)
```
**Logrotate config:**
```
/var/log/nginx/*.log {
    daily
    missingok
    rotate 52
    compress
    delaycompress
    notifempty
    create 0640 nginx adm
    sharedscripts
    postrotate
        [ -f /run/nginx.pid ] && kill -USR1 $(cat /run/nginx.pid)
    endscript
}
```""")
add("nginx-invalid-log-level-error", "Nginx Invalid Log Level Error", "The error_log directive specifies an invalid or unrecognized log level.", """## Description

The error_log directive specifies an invalid or unrecognized log level.

## Common Causes

- **Misspelled level** (e.g., "debg" instead of "debug")
- **Unsupported level** for your Nginx version
- **Level without debug module**

## How to Fix

1. Valid levels: debug, info, notice, warn, error, crit, alert, emerg
2. Debug requires --with-debug compilation
3. Check syntax

## Examples

**Valid levels:**
```nginx
error_log /var/log/nginx/error.log warn;
error_log /var/log/nginx/error.log error;
error_log /var/log/nginx/error.log crit;
error_log /var/log/nginx/error.log emerg;
```
**Debug (requires module):**
```nginx
error_log /var/log/nginx/error.log debug;
```""")
add("nginx-cache-log-error", "Nginx Cache Log Error", "Nginx encountered an error writing to the cache-related log or the cache log path is invalid.", """## Description

Nginx encountered an error writing to the cache-related log or the cache log path is invalid.

## Common Causes

- **Cache directory does not exist**
- **Permission denied** on cache path
- **Disk full**
- **Invalid cache_path directive**

## How to Fix

1. Check: `ls -la /var/cache/nginx/`
2. Permissions: `sudo chown nginx:nginx /var/cache/nginx/`
3. Disk: `df -h /var/cache/`
4. Validate: `sudo nginx -t`

## Examples

**Fix:**
```bash
sudo mkdir -p /var/cache/nginx
sudo chown nginx:nginx /var/cache/nginx/
sudo nginx -t
```
**Config:**
```nginx
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:10m;
```""")
add("nginx-open-log-handler-failed-error", "Nginx Open Log Handler Failed Error", "Nginx failed to open a log handler, often a custom log processing script or pipe.", """## Description

Nginx failed to open a log handler, often a custom log processing script or pipe.

## Common Causes

- **Log pipe/handler not available**
- **Script does not exist**
- **Permission denied**
- **Handler crashed**

## How to Fix

1. Check handler exists and is executable
2. Permissions: `chmod +x /path/to/handler`
3. Test handler independently
4. Check error log for details

## Examples

**Check:**
```bash
ls -la /path/to/handler
# Ensure executable
chmod +x /path/to/handler
```
**Debug:**
```bash
tail -f /var/log/nginx/error.log | grep handler
```""")
add("nginx-cache-file-not-found-error", "Nginx Cache File Not Found Error", "A cached response file is missing or was deleted from the cache directory.", """## Description

A cached response file is missing or was deleted from the cache directory.

## Common Causes

- **Cache purged externally**
- **Disk error** corrupted cache
- **Cache cleared** by admin
- **Temporary files** not committed

## How to Fix

1. Rebuild cache by clearing and re-fetching
2. Check disk: `df -h /var/cache/nginx/`
3. Verify cache_path exists
4. Re-enable caching

## Examples

**Clear and rebuild:**
```bash
rm -rf /var/cache/nginx/my_cache/*
sudo nginx -s reload
```
**Verify:**
```bash
ls -la /var/cache/nginx/my_cache/
```""")
add("nginx-cache-key-too-long-error", "Nginx Cache Key Too Long Error", "The computed cache key exceeds the maximum allowed length.", """## Description

The computed cache key exceeds the maximum allowed length.

## Common Causes

- **Very long URL** with many parameters
- **Complex cache_key** configuration
- **Default key too long** for your hash table

## How to Fix

1. Simplify cache_key
2. Use hash of long keys: `set $cache_key $host$uri;`
3. Use a shorter key template

## Examples

**Simple key:**
```nginx
proxy_cache_key "$scheme$request_method$host$uri";
```
**Complex key:**
```nginx
set $cache_key "$scheme$request_method$host$uri$is_args$args";
proxy_cache_key $cache_key;
```""")
add("nginx-cache-lock-timeout-error", "Nginx Cache Lock Timeout Error", "The cache lock timeout was reached while waiting to populate the cache.", """## Description

The cache lock timeout was reached while waiting to populate the cache.

## Common Causes

- **Backend very slow** to respond
- **cache_lock_timeout too short**
- **Multiple requests** hitting same uncached URI
- **Backend returning errors**

## How to Fix

1. Increase timeout: `proxy_cache_lock_timeout 60s;`
2. Use lock_age: `proxy_cache_lock_age 5s;`
3. Disable lock: `proxy_cache_lock off;`
4. Fix slow backend

## Examples

**Config:**
```nginx
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:10m;

location / {
    proxy_cache my_cache;
    proxy_cache_lock on;
    proxy_cache_lock_timeout 60s;
    proxy_cache_lock_age 5s;
    proxy_pass http://backend;
}
```""")
add("nginx-cache-loader-error", "Nginx Cache Loader Error", "The Nginx cache loader process failed to load cached files into memory.", """## Description

The Nginx cache loader process failed to load cached files into memory.

## Common Causes

- **Cache directory permissions** wrong
- **Corrupted cache files**
- **Cache zone too small**
- **Loader process crashed**

## How to Fix

1. Check permissions: `ls -la /var/cache/nginx/`
2. Clear corrupted files
3. Increase zone: `keys_zone=my_cache:100m;`
4. Restart Nginx

## Examples

**Fix:**
```bash
sudo rm -rf /var/cache/nginx/my_cache/*
sudo nginx -s reload
```
**Increase zone:**
```nginx
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:100m max_size=10g;
```""")
add("nginx-cache-purger-error", "Nginx Cache Purger Error", "The cache purger failed to remove cached files, possibly due to permission or path issues.", """## Description

The cache purger failed to remove cached files, possibly due to permission or path issues.

## Common Causes

- **purger module not compiled in**
- **Wrong purge method** (proxy_cache_purge)
- **Cache path wrong**
- **Permission denied**

## How to Fix

1. Check module: `nginx -V 2>&1 | grep purge`
2. Verify cache_path
3. Use correct purge method

## Examples

**Purge config:**
```nginx
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:10m purge=on;

location ~ /purge(/.*) {
    allow 127.0.0.1;
    deny all;
    proxy_cache_purge my_cache $host$1$is_args$args;
}
```
**Manual purge:**
```bash
rm -rf /var/cache/nginx/my_cache/*
sudo nginx -s reload
```""")
add("nginx-cache-zone-not-defined-error", "Nginx Cache Zone Not Defined Error", "The proxy_cache directive references a zone not defined with proxy_cache_path.", """## Description

The proxy_cache directive references a zone not defined with proxy_cache_path.

## Common Causes

- **proxy_cache without proxy_cache_path**
- **Zone name mismatch**
- **proxy_cache_path in wrong context**

## How to Fix

1. Define zone: `proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:10m;`
2. Check name matches
3. Ensure at http level

## Examples

**Config:**
```nginx
http {
    proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:10m;
    server {
        location / {
            proxy_cache my_cache;
            proxy_cache_valid 200 10m;
            proxy_pass http://backend;
        }
    }
}
```""")
add("nginx-stale-cache-error", "Nginx Stale Cache Error", "The cached response is stale and Nginx is configured to not serve stale content.", """## Description

The cached response is stale and Nginx is configured to not serve stale content.

## Common Causes

- **Cache expired**
- **proxy_cache_use_stale not configured**
- **Backend unreachable** while cache expired
- **No fallback for stale**

## How to Fix

1. Enable stale: `proxy_cache_use_stale error timeout updating http_500 http_502 http_503;`
2. Use updating: `proxy_cache_background_update on;`
3. Set graceful period

## Examples

**Stale config:**
```nginx
location / {
    proxy_cache my_cache;
    proxy_cache_valid 200 5m;
    proxy_cache_use_stale error timeout updating http_500 http_502 http_503;
    proxy_cache_background_update on;
    proxy_cache_lock on;
    proxy_pass http://backend;
}
```""")
add("nginx-bypass-cache-rule-invalid-error", "Nginx Bypass Cache Rule Invalid Error", "The proxy_cache_bypass or proxy_no_cache directive has invalid syntax or logic.", """## Description

The proxy_cache_bypass or proxy_no_cache directive has invalid syntax or logic.

## Common Causes

- **Invalid variable** in bypass rule
- **Missing semicolon**
- **Conflicting bypass and no_cache**
- **Logic error** (always bypassing)

## How to Fix

1. Check syntax: `proxy_cache_bypass $http_pragma;`
2. Test: `curl -H 'Pragma: no-cache' http://example.com/`
3. Verify variables are set
4. Validate: `sudo nginx -t`

## Examples

**Bypass config:**
```nginx
location / {
    proxy_cache my_cache;
    proxy_cache_bypass $http_x_no_cache;
    proxy_no_cache $http_x_no_cache;
    proxy_pass http://backend;
}
```
**Test:**
```bash
# Bypass cache
curl -H 'X-No-Cache: 1' http://example.com/
# Normal cached response
curl http://example.com/
```""")
add("nginx-no-cache-key-error", "Nginx No Cache Key Error", "No cache key was configured or the computed key is empty, preventing cache storage.", """## Description

No cache key was configured or the computed key is empty, preventing cache storage.

## Common Causes

- **proxy_cache_key not set**
- **Key evaluates to empty string**
- **Variables in key are empty**
- **Default key not suitable**

## How to Fix

1. Set explicit key: `proxy_cache_key "$scheme$request_method$host$uri";`
2. Ensure variables have values
3. Debug: add key to header
4. Validate: `sudo nginx -t`

## Examples

**Config:**
```nginx
location / {
    proxy_cache my_cache;
    proxy_cache_key "$scheme$request_method$host$uri$is_args$args";
    proxy_pass http://backend;
}
```
**Debug key:**
```nginx
add_header X-Cache-Key $scheme$request_method$host$uri;
```
**Verify:**
```bash
curl -I http://example.com/
# Look for X-Cache-Key header
```""")

count = 0
for slug, title, desc, body in PAGES:
    if slug in EXISTING:
        print(f"SKIP (exists): {slug}")
        continue
    content = make_page(title, desc, body)
    path = os.path.join(BASE, f"{slug}.md")
    with open(path, 'w') as f:
        f.write(content)
    count += 1
    print(f"CREATED: {slug}")

print(f"\nTotal pages in PAGES: {len(PAGES)}")
print(f"Already existing: {len(EXISTING)}")
print(f"New pages created: {count}")
print(f"Total .md files now: {len([f for f in os.listdir(BASE) if f.endswith('.md')])}")
