---
title: "Next.js response caching errors"
description: "Next.js errors related to response caching. Common issues include incorrect cache configuration, stale responses, or cache not being invalidated properly after mutations."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "nextjs"
tags: ["error", "caching", "cache", "performance"]
severity: "error"
solution: "Understand Next.js caching layers. Use cache tags for fine-grained control. Implement proper cache invalidation. Use unstable_cache for data caching. Monitor cache hit rates in production."
---

Next.js errors related to response caching. Common issues include incorrect cache configuration, stale responses, or cache not being invalidated properly after mutations.

## Solution

Understand Next.js caching layers. Use cache tags for fine-grained control. Implement proper cache invalidation. Use unstable_cache for data caching. Monitor cache hit rates in production.

## Code Example

```javascript
  // BAD: No cache control
  export async function getStaticProps() {
    const data = await fetchData();
    return { props: { data } };
  }
  
  // GOOD: Time-based caching
  export async function getStaticProps() {
    const data = await fetchData();
    
    return {
      props: { data },
      revalidate: 60, // Cache for 60 seconds
    };
  }
  
  // GOOD: Tag-based caching
  // lib/data.ts
  import { unstable_cache } from 'next/cache';
  
  export const getCachedPosts = unstable_cache(
    async () => {
      const posts = await db.posts.findMany();
      return posts;
    },
    ['posts'],
    { revalidate: 3600, tags: ['posts'] }
  );
  
  // GOOD: Cache invalidation
  'use server';
  import { revalidateTag } from 'next/cache';
  
  export async function updatePost(id: string, data: PostData) {
    await db.posts.update({ where: { id }, data });
    revalidateTag('posts');
  }
  
  // GOOD: Route segment cache config
  // app/api/data/route.ts
  export const dynamic = 'force-static';
  export const revalidate = 3600;
  
  export async function GET() {
    const data = await fetchData();
    return Response.json(data);
  }
  
  // GOOD: Fetch cache options
  async function getData() {
    const res = await fetch('https://api.example.com/data', {
      next: {
        revalidate: 3600,
        tags: ['data'],
      },
    });
    
    return res.json();
  }
```
