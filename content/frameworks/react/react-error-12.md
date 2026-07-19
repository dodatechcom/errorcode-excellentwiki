---
title: "React 19 Server Actions errors"
description: "React 19 Server Actions error that occurs when Server Actions are misconfigured, used outside of Server Components, or have incorrect function signatures. Server Actions must be async functions marked with 'use server'."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "react"
tags: ["error", "react-19", "server-actions", "rsc"]
severity: "error"
solution: "Ensure Server Actions are async functions with 'use server' directive. Place Server Actions in separate files or at the top of Server Components. Handle form submissions properly with the action prop. Use useTransition for pending states."
---

React 19 Server Actions error that occurs when Server Actions are misconfigured, used outside of Server Components, or have incorrect function signatures. Server Actions must be async functions marked with 'use server'.

## Solution

Ensure Server Actions are async functions with 'use server' directive. Place Server Actions in separate files or at the top of Server Components. Handle form submissions properly with the action prop. Use useTransition for pending states.

## Code Example

```javascript
  // BAD: Server Action in Client Component
  'use client';
  async function handleSubmit() {
    'use server'; // Error: cannot use in client component
    await saveData();
  }
  
  // GOOD: Server Action in separate file
  // actions.ts
  'use server';
  export async function createPost(formData) {
    const title = formData.get('title');
    await db.posts.create({ data: { title } });
    revalidatePath('/posts');
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
    
    const handleSubmit = (formData) => {
      startTransition(async () => {
        await createPost(formData);
      });
    };
    
    return (
      <form action={handleSubmit}>
        <input name="title" required />
        <button type="submit" disabled={isPending}>
          {isPending ? 'Creating...' : 'Create Post'}
        </button>
      </form>
    );
  }
```
