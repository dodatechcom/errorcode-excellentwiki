---
title: "Next.js Server Actions errors"
description: "Next.js errors related to Server Actions. Common issues include incorrect function placement, missing 'use server' directive, or not handling form submissions correctly."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "nextjs"
tags: ["error", "server-actions", "forms", "mutation"]
severity: "error"
solution: "Place 'use server' at the top of files containing Server Actions. Use proper form handling with FormData. Handle errors in Server Actions. Use useTransition for pending states. Revalidate data after mutations."
---

Next.js errors related to Server Actions. Common issues include incorrect function placement, missing 'use server' directive, or not handling form submissions correctly.

## Solution

Place 'use server' at the top of files containing Server Actions. Use proper form handling with FormData. Handle errors in Server Actions. Use useTransition for pending states. Revalidate data after mutations.

## Code Example

```javascript
  // BAD: Missing 'use server' directive
  export async function createPost(formData) {
    // Missing: 'use server';
    await db.posts.create({ data: { title: formData.get('title') } });
  }
  
  // GOOD: Proper Server Action
  // actions.ts
  'use server';
  import { revalidatePath } from 'next/cache';
  
  export async function createPost(formData: FormData) {
    const title = formData.get('title') as string;
    
    if (!title) {
      return { error: 'Title is required' };
    }
    
    await db.posts.create({ data: { title } });
    revalidatePath('/posts');
    return { success: true };
  }
  
  // GOOD: Using Server Action in form
  // app/posts/new/page.tsx
  import { createPost } from './actions';
  
  export default function NewPost() {
    return (
      <form action={createPost}>
        <input name="title" required />
        <button type="submit">Create Post</button>
      </form>
    );
  }
  
  // GOOD: With useTransition for pending state
  'use client';
  import { useTransition } from 'react';
  import { createPost } from './actions';
  
  export function NewPostForm() {
    const [isPending, startTransition] = useTransition();
    const [error, setError] = useState(null);
    
    const handleSubmit = async (formData: FormData) => {
      startTransition(async () => {
        const result = await createPost(formData);
        if (result.error) {
          setError(result.error);
        }
      });
    };
    
    return (
      <form action={handleSubmit}>
        <input name="title" required />
        <button type="submit" disabled={isPending}>
          {isPending ? 'Creating...' : 'Create Post'}
        </button>
        {error && <p className="error">{error}</p>}
      </form>
    );
  }
```
