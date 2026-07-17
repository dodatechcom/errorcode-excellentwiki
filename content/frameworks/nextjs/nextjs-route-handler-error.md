---
title: "Next.js Route Handler Error"
description: "Next.js Route Handler errors occur when the App Router API handler encounters exceptions"
frameworks: ["nextjs"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Route handler errors occur when functions in the `app/api` directory encounter exceptions during request processing. These are the App Router equivalent of Pages API routes and return JSON or other responses.

## Common Causes

- Missing HTTP method exports (`GET`, `POST`, etc.)
- Unhandled exceptions in async handlers
- Incorrect request body parsing
- Missing `NextResponse` return
- Database connection failures

## How to Fix

Create proper route handlers:

```ts
// app/api/users/route.ts
import { NextResponse } from 'next/server';
import { db } from '@/lib/db';

export async function GET() {
  try {
    const users = await db.user.findMany();
    return NextResponse.json(users);
  } catch (error) {
    return NextResponse.json(
      { error: 'Failed to fetch users' },
      { status: 500 }
    );
  }
}

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const user = await db.user.create({ data: body });
    return NextResponse.json(user, { status: 201 });
  } catch (error) {
    return NextResponse.json(
      { error: 'Failed to create user' },
      { status: 500 }
    );
  }
}
```

Handle dynamic route parameters:

```ts
// app/api/users/[id]/route.ts
import { NextResponse } from 'next/server';

export async function GET(
  request: Request,
  { params }: { params: { id: string } }
) {
  const user = await db.user.findUnique({
    where: { id: params.id },
  });

  if (!user) {
    return NextResponse.json(
      { error: 'User not found' },
      { status: 404 }
    );
  }

  return NextResponse.json(user);
}
```

Handle query parameters:

```ts
// app/api/search/route.ts
import { NextRequest, NextResponse } from 'next/server';

export async function GET(request: NextRequest) {
  const searchParams = request.nextUrl.searchParams;
  const query = searchParams.get('q');

  const results = await db.post.findMany({
    where: { title: { contains: query || '' } },
  });

  return NextResponse.json(results);
}
```

## Examples

```ts
// app/api/data/route.ts
export async function GET() {
  const data = getData();
  // Missing: return NextResponse.json(data);
}
```

```text
Error: Route Handler did not return a response.
```

## Related Errors

- [API route error]({{< relref "/frameworks/nextjs/nextjs-api-route-error" >}})
- [App Router error]({{< relref "/frameworks/nextjs/nextjs-app-router-error" >}})
