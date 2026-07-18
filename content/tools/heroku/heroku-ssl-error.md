---
title: "[Solution] Heroku SSL Endpoint Configuration Error — How to Fix"
description: "Fix Heroku SSL endpoint errors by configuring certificates correctly, enabling ACM, verifying DNS targets, using proper SSL/TLS addon, and resolving certificate chain issues."
tools: ["heroku"]
error-types: ["ssl-error"]
severities: ["error"]
weight: 5
comments: true
---

A Heroku SSL error occurs when SSL/TLS certificates are not configured correctly for custom domains. This can prevent HTTPS access to your application or cause certificate warnings in browsers.

## What This Error Means

Heroku supports SSL/TLS through several mechanisms: Automated Certificate Management (ACM), SSL Endpoint addon, and the newer Heroku SSL addon. SSL errors can occur at certificate provisioning, renewal, or request time. The error may be in the Heroku configuration or in the certificate itself (expired, wrong domain, incomplete chain).

Unlike router errors (H12) that happen at request time, SSL errors typically occur during certificate setup or when the certificate does not match the requested domain.

## Why It Happens

- The SSL certificate has expired and ACM renewal failed
- The certificate's Common Name (CN) or Subject Alternative Names (SANs) do not match the custom domain
- The certificate chain is incomplete (missing intermediate certificates)
- ACM is not enabled or is disabled for the application
- DNS is not pointed to Heroku's SSL endpoint
- The Heroku SSL addon is not provisioned
- A self-signed certificate is used instead of a trusted CA
- The private key does not match the certificate

## Common Error Messages

```
 ▸    ACM: certificate issuance failed — domain not verified
# or
 ▸    SSL: certificate is not valid for any names
# or
 ▸    SSL: certificate expired
# or
 ▸    SSL: certificate chain is incomplete
```

## How to Fix It

### 1. Enable Automated Certificate Management

```bash
# Enable ACM for automatic Let's Encrypt certificates
heroku certs:auto:enable -a my-app

# Check ACM status
heroku certs:auto -a my-app

# Refresh ACM if certificates are stuck
heroku certs:auto:refresh -a my-app
```

ACM automatically provisions and renews Let's Encrypt certificates for your custom domains. This is the recommended approach for most applications.

### 2. Verify DNS Configuration

```bash
# Check which domains are configured
heroku domains -a my-app

# Verify DNS target
heroku domains -a my-app | grep "DNS Target"

# Test DNS resolution
dig www.example.com CNAME +short
# Should return: my-app.herokuapp.com
```

DNS must point to Heroku's DNS target for certificate validation to work.

### 3. Upload a Custom Certificate

```bash
# Upload a certificate from a CA
heroku certs:add server.crt server.key -a my-app

# Upload a certificate with intermediate chain
heroku certs:add fullchain.pem server.key -a my-app

# Upload a wildcard certificate
heroku certs:add wildcard.crt server.key -a my-app
```

### 4. Check Certificate Details

```bash
# List installed certificates
heroku certs -a my-app

# Get certificate details
heroku certs:info -a my-app

# Check certificate expiration
echo | openssl s_client -connect my-app.herokuapp.com:443 2>/dev/null | \
    openssl x509 -noout -dates

# Verify certificate matches domain
echo | openssl s_client -connect my-app.herokuapp.com:443 2>/dev/null | \
    openssl x509 -noout -subject -ext subjectAltName
```

### 5. Fix Incomplete Certificate Chain

```bash
# The certificate file must include intermediate certificates
# Concatenate your certificate and intermediates:
cat your_domain.crt intermediate.crt root.crt > fullchain.pem

# Upload the combined chain
heroku certs:add fullchain.pem your_private.key -a my-app

# Verify the chain:
openssl s_client -connect my-app.herokuapp.com:443 -showcerts
```

### 6. Use Heroku SSL Addon

```bash
# Provision the Heroku SSL addon
heroku addons:create heroku-ssl -a my-app

# This is the newer SSL solution with better performance
# It works with ACM and custom certificates

# For the older SSL Endpoint addon:
heroku addons:create ssl:endpoint -a my-app
```

### 7. Configure Strict-Transport-Security

```bash
# Enable HSTS to force HTTPS
heroku headers:add Strict-Transport-Security "max-age=31536000; includeSubDomains" -a my-app

# Or set it in your application code:
```

```python
# Flask example
@app.after_request
def add_hsts(response):
    if request.is_secure:
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response
```

### 8. Force HTTPS Redirect

```bash
# In your application code, redirect HTTP to HTTPS:

# Node.js Express
app.use((req, res, next) => {
  if (req.headers['x-forwarded-proto'] !== 'https') {
    return res.redirect(`https://${req.headers.host}${req.url}`);
  }
  next();
});

# Python Flask
from flask import redirect, request

@app.before_request
def redirect_to_https():
    if request.headers.get('X-Forwarded-Proto', 'http') == 'http':
        return redirect(f"https://{request.host}{request.path}", 301)
```

## Common Scenarios

### ACM Fails After Domain Migration

A company changes its domain from `old-company.com` to `new-company.com`. ACM cannot issue a certificate for `new-company.com` because the DNS is still pointing to the old hosting provider. Update the CNAME records for `new-company.com` to point to Heroku's DNS target and wait for DNS propagation before ACM succeeds.

### Expired Certificate with No ACM

An application uses a manually uploaded certificate that expired six months ago. ACM was never enabled. Browsers show a security warning. The fix is to either enable ACM (automatic renewal) or upload a new certificate from a CA.

### Certificate for Wrong Domain

A developer uploads a certificate for `www.example.com` but the application domain is `app.example.com`. The certificate validation fails because the domain does not match. Regenerate the certificate with the correct domain in the SANs.

## Prevent It

- Enable ACM on all production apps for automatic certificate management
- Set up ACM renewal alerts in case automatic renewal fails
- Use wildcard certificates if you have multiple subdomains
- Monitor certificate expiration dates with external monitoring tools
- Test SSL configuration with SSL Labs or similar tools
- Keep Heroku SSL addon provisioned even if using ACM
- Use Heroku Pipelines to ensure SSL configuration is consistent across environments
- Document DNS requirements for SSL certificate validation

## Related Pages

- [Heroku Router Error](/tools/heroku/heroku-router-error)
- [Heroku Config Error](/tools/heroku/heroku-config-error)
- [Heroku App Not Found](/tools/heroku/heroku-app-not-found)
