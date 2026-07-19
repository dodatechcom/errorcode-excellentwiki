---
title: "Next.js Metadata API errors"
description: "Next.js errors related to the Metadata API. Common issues include incorrect metadata format, duplicate metadata, or conflicting metadata between layout and page files."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "nextjs"
tags: ["error", "metadata", "seo", "head"]
severity: "error"
solution: "Use the Metadata type for TypeScript support. Export metadata or generateMetadata function from pages. Don't mix static and dynamic metadata. Use generateMetadata for dynamic metadata based on params."
---

Next.js errors related to the Metadata API. Common issues include incorrect metadata format, duplicate metadata, or conflicting metadata between layout and page files.

## Solution

Use the Metadata type for TypeScript support. Export metadata or generateMetadata function from pages. Don't mix static and dynamic metadata. Use generateMetadata for dynamic metadata based on params.

## Code Example

```javascript
  // BAD: Incorrect metadata format
  // app/page.tsx
  export default function Page() {
    return <div>Page</div>;
  }
  
  export const metadata = {
    title: 'Page',
    // Missing other required fields for complex metadata
  };
  
  // GOOD: Static metadata
  // app/page.tsx
  import type { Metadata } from 'next';
  
  export const metadata: Metadata = {
    title: 'My Page',
    description: 'Page description',
    openGraph: {
      title: 'My Page',
      description: 'Page description',
      url: 'https://example.com',
      siteName: 'My Site',
      images: [
        {
          url: 'https://example.com/og.png',
          width: 800,
          height: 600,
        },
      ],
    },
  };
  
  export default function Page() {
    return <div>Page</div>;
  }
  
  // GOOD: Dynamic metadata
  // app/posts/[id]/page.tsx
  import type { Metadata } from 'next';
  
  export async function generateMetadata({ params }): Promise<Metadata> {
    const post = await getPost(params.id);
    
    return {
      title: post.title,
      description: post.excerpt,
      openGraph: {
        title: post.title,
        description: post.excerpt,
        images: [post.image],
      },
    };
  }
  
  export default async function PostPage({ params }) {
    const post = await getPost(params.id);
    return <article>{post.content}</article>;
  }
  
  // GOOD: Layout metadata inheritance
  // app/layout.tsx
  export const metadata: Metadata = {
    title: {
      default: 'My Site',
      template: '%s | My Site',
    },
    description: 'Site description',
  };
  
  // app/about/page.tsx
  export const metadata: Metadata = {
    title: 'About', // Renders as "About | My Site"
  };
```
