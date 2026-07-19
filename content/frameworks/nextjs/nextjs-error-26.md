---
title: "Next.js dynamic metadata generation errors"
description: "Next.js errors when generating metadata dynamically. Common issues include missing generateMetadata function, incorrect async handling, or metadata not updating when params change."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "nextjs"
tags: ["error", "metadata", "dynamic", "seo"]
severity: "error"
solution: "Export generateMetadata as an async function. Use params and searchParams to generate dynamic metadata. Return proper Metadata type. Handle errors in metadata generation gracefully."
---

Next.js errors when generating metadata dynamically. Common issues include missing generateMetadata function, incorrect async handling, or metadata not updating when params change.

## Solution

Export generateMetadata as an async function. Use params and searchParams to generate dynamic metadata. Return proper Metadata type. Handle errors in metadata generation gracefully.

## Code Example

```javascript
  // BAD: Static metadata for dynamic route
  // app/posts/[id]/page.tsx
  export const metadata = {
    title: 'Post', // Same for all posts!
  };
  
  // GOOD: Dynamic metadata generation
  // app/posts/[id]/page.tsx
  import type { Metadata } from 'next';
  
  export async function generateMetadata({ 
    params 
  }: { 
    params: { id: string } 
  }): Promise<Metadata> {
    try {
      const post = await getPost(params.id);
      
      if (!post) {
        return { title: 'Post Not Found' };
      }
      
      return {
        title: post.title,
        description: post.excerpt,
        openGraph: {
          title: post.title,
          description: post.excerpt,
          images: [post.coverImage],
          type: 'article',
        },
        twitter: {
          card: 'summary_large_image',
          title: post.title,
          description: post.excerpt,
        },
      };
    } catch (error) {
      return { title: 'Error Loading Post' };
    }
  }
  
  export default async function PostPage({ params }) {
    const post = await getPost(params.id);
    
    if (!post) {
      notFound();
    }
    
    return <article>{post.content}</article>;
  }
  
  // GOOD: Metadata with searchParams
  export async function generateMetadata({ 
    searchParams 
  }: { 
    searchParams: { [key: string]: string | undefined } 
  }): Promise<Metadata> {
    const category = searchParams.category || 'All';
    
    return {
      title: `Products - ${category}`,
      description: `Browse ${category} products`,
    };
  }
```
