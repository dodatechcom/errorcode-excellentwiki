---
title: "Next.js revalidation errors"
description: "Next.js errors related to ISR (Incremental Static Regeneration) and on-demand revalidation. Common issues include incorrect revalidation strategies, stale data, or revalidation not working as expected."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "nextjs"
tags: ["error", "isr", "revalidation", "caching"]
severity: "error"
solution: "Use revalidate option in getStaticProps for time-based ISR. Use revalidatePath or revalidateTag for on-demand revalidation. Handle stale data gracefully. Monitor revalidation in production."
---

Next.js errors related to ISR (Incremental Static Regeneration) and on-demand revalidation. Common issues include incorrect revalidation strategies, stale data, or revalidation not working as expected.

## Solution

Use revalidate option in getStaticProps for time-based ISR. Use revalidatePath or revalidateTag for on-demand revalidation. Handle stale data gracefully. Monitor revalidation in production.

## Code Example

```javascript
  // BAD: Incorrect revalidation setup
  export async function getStaticProps() {
    const data = await fetchData();
    return {
      props: { data },
      revalidate: -1, // Invalid!
    };
  }
  
  // GOOD: Time-based ISR
  export async function getStaticProps() {
    const data = await fetchData();
    
    return {
      props: { data },
      revalidate: 60, // Revalidate every 60 seconds
    };
  }
  
  // GOOD: On-demand revalidation
  // actions.ts
  'use server';
  import { revalidatePath, revalidateTag } from 'next/cache';
  
  export async function updatePost(id: string, data: PostData) {
    await db.posts.update({ where: { id }, data });
    
    // Revalidate specific path
    revalidatePath('/posts');
    
    // Or revalidate by tag
    revalidateTag('posts');
  }
  
  // GOOD: Tag-based revalidation
  // pages/posts.js or app/posts/page.tsx
  export async function getStaticProps() {
    const posts = await fetch('https://api.example.com/posts', {
      next: { tags: ['posts'] },
    });
    
    return {
      props: { posts },
      revalidate: 3600,
    };
  }
  
  // GOOD: Handle stale data
  function Posts({ posts }) {
    return (
      <div>
        <p>Last updated: {new Date().toLocaleString()}</p>
        <ul>
          {posts.map(post => (
            <li key={post.id}>{post.title}</li>
          ))}
        </ul>
      </div>
    );
  }
```
