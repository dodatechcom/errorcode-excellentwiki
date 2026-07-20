---
title: "[Solution] Apache SSLPassPhraseDialog Error"
description: "The SSLPassPhraseDialog command fails to provide the passphrase for encrypted private keys."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The SSLPassPhraseDialog command fails to provide the passphrase for encrypted private keys.

## Common Causes

- External program path is wrong or not executable
- Program does not output the passphrase correctly
- Program requires interactive input not possible in server context

## How to Fix

- Verify the external program exists and is executable
- Ensure the program outputs the passphrase to stdout
- Use builtin: for testing or unencrypted keys for production

## Examples

```
['SSLPassPhraseDialog builtin:\n# Or external:\nSSLPassPhraseDialog exec:/usr/local/bin/ssl-passphrase.sh']
```
