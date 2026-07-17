---
title: "Invalid key error in COBOL"
description: "Invalid key errors in COBOL occur when referencing a record key that doesn't match the file's key structure."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Invalid key errors occur when the key value used in READ, WRITE, REWRITE, or DELETE doesn't match the indexed file's key structure, or the key is not in ascending order for sequential access.

## Common Causes

- Key value not in the file's key definition
- START statement with invalid key condition
- Sequential access with non-sequential keys
- Missing or incorrect KEY IS clause

## How to Fix

```cobol
       * WRONG: Key doesn't match file definition
       READ CUSTOMER-FILE
           KEY IS WRONG-KEY-FIELD
           INVALID KEY DISPLAY 'Invalid key'.
```

```cobol
       * CORRECT: Use the defined key field
       READ CUSTOMER-FILE
           KEY IS CUSTOMER-ID
           INVALID KEY DISPLAY 'Key not found'
       END-READ.
```

```cobol
       * CORRECT: Use START for dynamic access
       START CUSTOMER-FILE
           KEY IS GREATER THAN WS-SEARCH-KEY
           INVALID KEY DISPLAY 'No matching key'
       END-START.
```

## Examples

```cobol
       * Invalid START condition
       START CUSTOMER-FILE
           KEY IS LESS THAN CUSTOMER-ID
           INVALID KEY DISPLAY 'No records match'
       END-START.
```

## Related Errors

- [Duplicate Key](/languages/cobol/duplicate-key) - duplicate key errors
- [Subscript Error](/languages/cobol/subscript-error) - index errors
