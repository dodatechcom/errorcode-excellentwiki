---
title: "[Solution] Apache Proxy SSL Handshake Failed"
description: "The SSL/TLS handshake between Apache and the backend proxy target failed."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The SSL/TLS handshake between Apache and the backend proxy target failed.

## Common Causes

- Backend SSL certificate not trusted by Apache
- SSL protocol mismatch between Apache and backend
- SSLProxyCACertificateFile not configured
- Backend uses self-signed certificate

## How to Fix

- Configure SSLProxyCACertificateFile to trust the backend certificate
- Set SSLProxyVerify and SSLProxyCheckPeerCN
- Use SSLProxyNone if testing with self-signed certs

## Examples

```
['SSLProxyEngine On\nSSLProxyVerify none\nSSLProxyCheckPeerCN off\nSSLProxyCheckPeerName off']
```
