---
title: "[Solution] ERR_IMPORT_ASSERTION_TYPE_FAILED — JSON Import Assertion Fix"
description: "Fix ERR_IMPORT_ASSERTION_TYPE_FAILED when importing JSON files without proper import attributes."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ERR_IMPORT_ASSERTION_TYPE Failed

```javascript
// Correct syntax for JSON imports
import config from './config.json' with { type: 'json' };

// Fallback approach
import { readFileSync } from 'fs';
const config = JSON.parse(readFileSync('./config.json', 'utf8'));
```
