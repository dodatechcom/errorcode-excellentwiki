---
title: "[Solution] MongoDB Client-Side Field Level Encryption Error"
description: "Fix MongoDB client-side field level encryption errors including key management failures and schema violations"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB Client-Side Field Level Encryption Error

Client-side field level encryption (CSFLE) fails when the KMS key cannot be accessed, the encrypted field schema is misconfigured, or the decryption key does not match.

## Common Causes

- KMS credentials are expired or invalid
- Encryption key vault collection is inaccessible
- Encrypted fields are queried without the proper autoencryption options
- Data key ID does not match any key in the key vault
- Schema validator references a non-existent encryption key

## How to Fix

### Verify KMS Connection

```javascript
const encryption = new ClientEncryption(keyVaultClient, {
  keyVaultNamespace: 'keyvault.datakeys',
  kmsProviders: {
    aws: {
      accessKeyId: process.env.AWS_ACCESS_KEY_ID,
      secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY
    }
  }
});

// Test key access
const dataKey = await encryption.createDataKey('aws', {
  masterKey: {
    region: 'us-east-1',
    key: 'arn:aws:kms:us-east-1:123456789012:key/abc-123'
  }
});
console.log('Key created:', dataKey);
```

### Use Proper AutoEncryption Options

```javascript
const client = new MongoClient(uri, {
  autoEncryption: {
    keyVaultNamespace: 'keyvault.datakeys',
    kmsProviders: {
      local: {
        key: Buffer.from('base64encodedkey==', 'base64')
      }
    },
    schemaMap: autoEncryptionSchemaMap
  }
});
```

### Handle Decryption Failures

```javascript
async function safeReadEncrypted(collection, filter) {
  try {
    return await collection.findOne(filter);
  } catch (err) {
    if (err.code === 6371401 || err.message.includes('decryption')) {
      console.error('Cannot decrypt field -- key may be rotated');
      throw err;
    }
    throw err;
  }
}
```

## Examples

```
MongoCryptError: key not found. keyvault.datakeys does not contain
  _id: Binary('...', 0)

MongoCryptError: error in KMS HTTP response: 403 Forbidden

MongoServerError: Cannot decrypt value for field 'ssn' --
  no matching key found in key vault
```

## Related Errors

- [MongoDB Authentication Failed]({{< relref "/tools/mongodb/mongodb-authentication-failed" >}}) -- auth issues
- [MongoDB Authorization Failure]({{< relref "/tools/mongodb/mongodb-authorization-failure" >}}) -- permission issues
- [MongoDB Invalid BSON]({{< relref "/tools/mongodb/mongodb-invalid-bson" >}}) -- BSON format issues
