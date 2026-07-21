---
title: "[Solution] Vercel Postgres Error"
description: "Fix Vercel Postgres database connection and query errors."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vercel Postgres Error

Vercel Postgres fails to connect or execute queries.

```
Error: Connection refused to Vercel Postgres
```

## Common Causes

- Postgres database not provisioned
- Connection string misconfigured
- Database sleeping due to inactivity
- Query timeout exceeded
- SSL required but not configured

## How to Fix

### Connect to Vercel Postgres

```typescript
import { sql } from '@vercel/postgres';

export default async function handler(req, res) {
  try {
    const result = await sql`SELECT NOW()`;
    res.status(200).json({ time: result.rows[0] });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}
```

### Check Connection String

```bash
# Verify env vars
echo $POSTGRES_URL
echo $POSTGRES_PRISMA_URL
echo $POSTGRES_URL_NON_POOLING
```

### Use Connection Pooling

```typescript
// Use pooled connection for most queries
import { Pool } from '@vercel/postgres';

const pool = new Pool({
  connectionString: process.env.POSTGRES_URL
});

export default async function handler(req, res) {
  const client = await pool.connect();
  try {
    const result = await client.query('SELECT NOW()');
    res.status(200).json(result.rows);
  } finally {
    client.release();
  }
}
```

### Handle Sleeping Database

```typescript
// First request may be slow (database waking up)
export const runtime = 'edge';

export async function GET() {
  const result = await sql`SELECT 1 as alive`;
  return Response.json({ status: 'ok' });
}
```

### Use Drizzle ORM

```typescript
import { drizzle } from 'drizzle-orm/vercel-postgres';
import { sql } from '@vercel/postgres';

const db = drizzle(sql);

const result = await db.select().from(users);
```

## Examples

```typescript
// Complete Postgres example
import { sql } from '@vercel/postgres';

export default async function handler(req, res) {
  try {
    // Create table if not exists
    await sql`
      CREATE TABLE IF NOT EXISTS todos (
        id SERIAL PRIMARY KEY,
        title TEXT NOT NULL,
        completed BOOLEAN DEFAULT false
      )
    `;

    // Insert
    await sql`INSERT INTO todos (title) VALUES ('Learn Vercel Postgres')`;

    // Query
    const todos = await sql`SELECT * FROM todos`;
    res.status(200).json(todos.rows);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}
```
