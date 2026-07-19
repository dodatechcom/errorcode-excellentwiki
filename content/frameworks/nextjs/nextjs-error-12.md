---
title: "Next.js 16 CVE-2026-44574 security vulnerability"
description: "Critical security vulnerability in Next.js 16 related to improper input validation in middleware. This CVE allows potential path traversal attacks when middleware incorrectly handles URL paths and redirects."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "nextjs"
tags: ["security", "cve", "nextjs-16", "middleware"]
severity: "critical"
solution: "Update to the latest Next.js 16 patch version immediately. Sanitize all URL inputs in middleware. Use proper path normalization. Validate redirects against an allowlist. Run npm audit to check for vulnerabilities."
---

Critical security vulnerability in Next.js 16 related to improper input validation in middleware. This CVE allows potential path traversal attacks when middleware incorrectly handles URL paths and redirects.

## Solution

Update to the latest Next.js 16 patch version immediately. Sanitize all URL inputs in middleware. Use proper path normalization. Validate redirects against an allowlist. Run npm audit to check for vulnerabilities.

## Code Example

```javascript
  // BAD: Vulnerable middleware
  // middleware.ts
  import { NextResponse } from 'next/server';
  
  export function middleware(request) {
    const path = request.nextUrl.pathname;
    
    // Vulnerable to path traversal
    if (path.includes('..')) {
      return NextResponse.redirect(new URL(path, request.url));
    }
    
    return NextResponse.next();
  }
  
  // GOOD: Secure middleware with proper validation
  import { NextResponse } from 'next/server';
  import type { NextRequest } from 'next/server';
  
  const ALLOWED_PATHS = ['/dashboard', '/profile', '/settings'];
  
  export function middleware(request: NextRequest) {
    const path = request.nextUrl.pathname;
    
    // Normalize path
    const normalizedPath = path.replace(/\.\.+/g, '').replace(/\/+/g, '/');
    
    // Validate against allowlist
    if (!ALLOWED_PATHS.some(allowed => normalizedPath.startsWith(allowed))) {
      return NextResponse.redirect(new URL('/404', request.url));
    }
    
    // Sanitize query parameters
    const searchParams = request.nextUrl.searchParams;
    for (const [key, value] of searchParams) {
      if (value.includes('..') || value.includes('<') || value.includes('>')) {
        searchParams.delete(key);
      }
    }
    
    return NextResponse.next();
  }
  
  // GOOD: Input sanitization utility
  function sanitizePath(path: string): string {
    return path
      .replace(/\.\.+/g, '')
      .replace(/\/+/g, '/')
      .replace(/[^a-zA-Z0-9/\-_]/g, '')
      .toLowerCase();
  }
  
  // GOOD: Check for updates
  // package.json
  {
    "dependencies": {
      "next": "16.0.2" // Or latest patch version
    }
  }
  
  // Run audit
  // npm audit
  // npm audit fix
```
