---
title: "[Solution] InfluxDB TLS Certificate Error — How to Fix"
description: "Fix InfluxDB TLS certificate errors including expired certificates, CN mismatches, and trust chain issues"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB TLS Certificate Error

TLS certificate errors occur when InfluxDB or its clients encounter invalid, expired, or misconfigured SSL/TLS certificates during secure connections.

## Why It Happens

- Server certificate has expired
- Certificate Common Name (CN) does not match the hostname
- Certificate is signed by an unknown Certificate Authority
- Client cannot verify the server trust chain
- Private key does not match the certificate
- TLS protocol version mismatch between client and server

## Common Error Messages

```
x509: certificate has expired or is not yet valid
```

```
x509: cannot validate certificate for IP because it does not contain any IP SANs
```

```
tls: failed to verify certificate: x509: certificate signed by unknown authority
```

## How to Fix It

### 1. Regenerate Expired Certificate

```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout /etc/influxdb/influxdb.key \
  -out /etc/influxdb/influxdb.crt \
  -subj "/CN=influxdb.example.com"
```

### 2. Fix Hostname Mismatch with SAN

```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout server.key -out server.crt \
  -subj "/CN=influxdb.example.com" \
  -addext "subjectAltName=DNS:influxdb.example.com,DNS:localhost,IP:10.0.0.1"
```

### 3. Configure InfluxDB TLS

```bash
[http]
  tls-cert = "/etc/influxdb/influxdb.crt"
  tls-key = "/etc/influxdb/influxdb.key"
  tls-min-version = "1.2"
```

### 4. Add Custom CA to Client

```bash
sudo cp my-ca.crt /usr/local/share/ca-certificates/
sudo update-ca-certificates
```

## Examples

```
$ curl https://influxdb.example.com:8086/ping
curl: (60) SSL certificate problem: certificate has expired
```

## Prevent It

- Set certificate expiration reminders at 30 days before expiry
- Automate certificate renewal with Let's Encrypt or cert-manager
- Monitor certificate expiration in monitoring dashboards

## Related Pages

- [InfluxDB Connection Error](/tools/influxdb/influxdb-connection-error)
- [InfluxDB HTTP Error](/tools/influxdb/influxdb-http-error)
- [InfluxDB Secret Error](/tools/influxdb/influxdb-secret-error)
