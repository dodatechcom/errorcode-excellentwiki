---
title: "Prisma Error in Next.js"
description: "Prisma raises errors in Next.js when database queries fail, schema migrations have issues, or connections are lost"
frameworks: ["nextjs"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Prisma errors in Next.js occur when the Prisma Client encounters issues with database connections, query execution, schema mismatches, or data validation. These errors typically manifest during server-side rendering, API routes, or server actions.

## Common Causes

- Database connection string misconfigured
- Prisma schema not migrated to database
- Query references non-existent model or field
- Connection pool exhausted
- Missing Prisma Client generation

## How to Fix

Configure Prisma client properly:

```ts
// lib/prisma.ts
import { PrismaClient } from '@prisma/client';

const globalForPrisma = globalThis as unknown as {
  prisma: PrismaClient | undefined;
};

export const prisma = globalForPrisma.prisma ?? new PrismaClient();

if (process.env.NODE_ENV !== 'production') globalForPrisma.prisma = prisma;
```

Use Prisma in server components:

```tsx
// app/users/page.tsx
import { prisma } from '@/lib/prisma';

export default async function UsersPage() {
  const users = await prisma.user.findMany({
    include: { posts: true },
  });

  return (
    <ul>
      {users.map((user) => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}
```

Handle Prisma errors in API routes:

```ts
// app/api/users/route.ts
import { NextResponse } from 'next/server';
import { prisma } from '@/lib/prisma';
import { Prisma } from '@prisma/client';

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const user = await prisma.user.create({ data: body });
    return NextResponse.json(user, { status: 201 });
  } catch (error) {
    if (error instanceof Prisma.PrismaClientKnownRequestError) {
      if (error.code === 'P2002') {
        return NextResponse.json(
          { error: 'Unique constraint violation' },
          { status: 409 }
        );
      }
    }
    return NextResponse.json(
      { error: 'Failed to create user' },
      { status: 500 }
    );
  }
}
```

Run migrations before deployment:

```bash
npx prisma generate
npx prisma db push
```

## Examples

```ts
const user = await prisma.user.findUnique({
  where: { email: 'test@example.com' },
});
// Error if User model doesn't exist in schema
```

```text
PrismaClientUnknownRequestError:
Invalid `prisma.user.findUnique()` invocation
The table `User` does not exist in the current database.
```

## Related Errors

- [Build error]({{< relref "/frameworks/nextjs/build-error" >}})
- [API route error]({{< relref "/frameworks/nextjs/nextjs-api-route-error" >}})
