---
title: "Next.js API route errors"
description: "Next.js API route errors in both Pages Router and App Router. Common issues include incorrect request handling, missing error responses, or improper HTTP method handling."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "nextjs"
tags: ["error", "api-routes", "route-handlers", "backend"]
severity: "error"
solution: "Handle all HTTP methods properly. Return appropriate status codes. Use proper error handling. Validate request bodies. Implement authentication and authorization. Use NextResponse for App Router routes."
---

Next.js API route errors in both Pages Router and App Router. Common issues include incorrect request handling, missing error responses, or improper HTTP method handling.

## Solution

Handle all HTTP methods properly. Return appropriate status codes. Use proper error handling. Validate request bodies. Implement authentication and authorization. Use NextResponse for App Router routes.

## Code Example

```javascript
  // OLD: Pages Router API route
  // pages/api/users.js
  export default async function handler(req, res) {
    if (req.method !== 'GET') {
      return res.status(405).json({ error: 'Method not allowed' });
    }
    
    try {
      const users = await getUsers();
      res.status(200).json(users);
    } catch (error) {
      res.status(500).json({ error: 'Failed to fetch users' });
    }
  }
  
  // NEW: App Router Route Handler
  // app/api/users/route.ts
  import { NextResponse } from 'next/server';
  
  export async function GET() {
    try {
      const users = await getUsers();
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
      
      // Validate body
      if (!body.name || !body.email) {
        return NextResponse.json(
          { error: 'Name and email required' },
          { status: 400 }
        );
      }
      
      const user = await createUser(body);
      return NextResponse.json(user, { status: 201 });
    } catch (error) {
      return NextResponse.json(
        { error: 'Failed to create user' },
        { status: 500 }
      );
    }
  }
  
  // GOOD: With authentication
  // app/api/protected/route.ts
  import { auth } from '@/lib/auth';
  
  export async function GET() {
    const session = await auth();
    
    if (!session) {
      return NextResponse.json(
        { error: 'Unauthorized' },
        { status: 401 }
      );
    }
    
    const data = await getProtectedData(session.user.id);
    return NextResponse.json(data);
  }
  
  // GOOD: Dynamic Route Handler
  // app/api/posts/[id]/route.ts
  export async function GET(
    request: Request,
    { params }: { params: { id: string } }
  ) {
    const post = await getPost(params.id);
    
    if (!post) {
      return NextResponse.json(
        { error: 'Post not found' },
        { status: 404 }
      );
    }
    
    return NextResponse.json(post);
  }
```
