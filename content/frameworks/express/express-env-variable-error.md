---
title: "[Solution] Express Environment Variable Error"
description: "Fix Express environment variable errors when config values are undefined or missing at runtime."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when Express tries to access environment variables that are not defined, causing `undefined` values to be used in configuration, database connections, or API calls. This is common when `.env` files are not loaded or variable names are misspelled.

## Common Causes

- `.env` file not loaded by `dotenv` before app initialization
- Variable name typo (e.g., `process.env.DB_HOST` vs `process.env.db_host`)
- Environment variables not set in production deployment
- `dotenv.config()` called after the variables are already accessed
- Process manager or Docker container missing environment configuration

## How to Fix

1. Load environment variables at the top of your entry file:

```javascript
require('dotenv').config(); // Must be first

const express = require('express');
const app = express();

const dbHost = process.env.DB_HOST || 'localhost';
const dbPort = parseInt(process.env.DB_PORT, 10) || 5432;
```

2. Validate required environment variables on startup:

```javascript
const required = ['DB_HOST', 'DB_PASSWORD', 'JWT_SECRET'];
const missing = required.filter((key) => !process.env[key]);

if (missing.length > 0) {
  console.error(`Missing required env vars: ${missing.join(', ')}`);
  process.exit(1);
}
```

3. Use a typed config module to avoid typos:

```javascript
// config.js
const config = {
  port: parseInt(process.env.PORT, 10) || 3000,
  db: {
    host: process.env.DB_HOST,
    port: parseInt(process.env.DB_PORT, 10) || 5432,
    name: process.env.DB_NAME
  },
  jwt: {
    secret: process.env.JWT_SECRET,
    expiresIn: process.env.JWT_EXPIRES_IN || '24h'
  }
};

module.exports = config;
```

## Examples

```javascript
// Bug: dotenv loaded too late
const app = express();
const pool = require('pg').Pool({
  host: process.env.DB_HOST // undefined -- dotenv not loaded yet
});

require('dotenv').config(); // Too late, connection already failed
```

```text
TypeError: Cannot destructure property 'host' of undefined
```

```bash
# Load .env before starting
node -r dotenv/config server.js
```
