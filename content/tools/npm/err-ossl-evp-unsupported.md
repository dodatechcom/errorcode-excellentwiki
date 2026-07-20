---
title: "[Solution] npm install ERR_OSSL_EVP_UNSUPPORTED OpenSSL Error"
description: "Handle ERR_OSSL_EVP_UNSUPPORTED OpenSSL errors in npm install by setting legacy provider flag, updating packages, or using compatible Node version."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install ERR_OSSL_EVP_UNSUPPORTED OpenSSL Error

This guide helps you diagnose and resolve npm install ERR_OSSL_EVP_UNSUPPORTED OpenSSL Error errors encountered when running npm commands.

## Common Causes

- Package uses deprecated OpenSSL hash functions unsupported in Node 17+
- MD4 or MD5 hashing algorithm required by webpack or other build tools
- Node.js version upgraded OpenSSL without package compatibility update

## How to Fix

### Set Legacy OpenSSL Provider

```bash
NODE_OPTIONS=--openssl-legacy-provider npm install
```

### Update Affected Packages

```bash
npm update webpack <affected-package>
```

### Use Node.js 16 LTS

```bash
nvm install 16 && nvm use 16
```

## Examples

```bash
# Webpack 4 with Node 17+
npm install
# Fix: Use legacy provider
NODE_OPTIONS=--openssl-legacy-provider npm install

# Old package using MD4 hash
npm run build
# Fix: Set environment variable
export NODE_OPTIONS=--openssl-legacy-provider
npm run build

```

## Related Errors

- [Engine Mismatch]({{< relref "/tools/npm/ebadengine-engine-mismatch" >}}) -- version incompatibility
- [Build Failed]({{< relref "/tools/npm/build-failed" >}}) -- compilation error
