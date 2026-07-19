---
title: "Next.js environment variables errors"
description: "Next.js errors related to environment variables. Common issues include exposing server-side env vars to the client, incorrect variable naming, or missing env validation."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "nextjs"
tags: ["error", "env", "environment", "security"]
severity: "error"
solution: "Use NEXT_PUBLIC_ prefix for client-side variables. Never expose sensitive keys to the client. Validate environment variables at build time. Use .env files properly with .gitignore."
---

Next.js errors related to environment variables. Common issues include exposing server-side env vars to the client, incorrect variable naming, or missing env validation.

## Solution

Use NEXT_PUBLIC_ prefix for client-side variables. Never expose sensitive keys to the client. Validate environment variables at build time. Use .env files properly with .gitignore.

## Code Example

```javascript
  // BAD: Exposing secret key to client
  // This will be exposed in browser!
  NEXT_PUBLIC_SECRET_KEY=abc123
  
  // GOOD: Server-only variables
  // .env.local
  DATABASE_URL=postgresql://...
  API_SECRET_KEY=abc123
  
  // Client-accessible variables
  NEXT_PUBLIC_API_URL=https://api.example.com
  
  // GOOD: Validate environment variables
  // lib/env.ts
  function getEnvVariable(key: string, required = true): string {
    const value = process.env[key];
    
    if (required && !value) {
      throw new Error(`Missing environment variable: ${key}`);
    }
    
    return value || '';
  }
  
  export const env = {
    DATABASE_URL: getEnvVariable('DATABASE_URL'),
    API_SECRET_KEY: getEnvVariable('API_SECRET_KEY'),
    API_URL: getEnvVariable('NEXT_PUBLIC_API_URL'),
  };
  
  // GOOD: Using env validation at build time
  // next.config.js
  const { z } = require('zod');
  
  const envSchema = z.object({
    DATABASE_URL: z.string().url(),
    API_SECRET_KEY: z.string().min(1),
  });
  
  try {
    envSchema.parse(process.env);
  } catch (error) {
    console.error('Invalid environment variables:', error.format());
    process.exit(1);
  }
  
  // GOOD: Access env in different contexts
  // Server Component or API Route
  import { env } from '@/lib/env';
  
  export default async function Page() {
    const data = await fetch(env.API_SECRET_KEY);
    // ...
  }
  
  // Client Component
  'use client';
  
  // Can only access NEXT_PUBLIC_ variables
  const apiUrl = process.env.NEXT_PUBLIC_API_URL;
```
