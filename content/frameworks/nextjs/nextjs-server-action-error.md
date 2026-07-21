---
title: "[Solution] Next.js Server Action Invocation Error -- How to Fix"
description: "Fix Next.js server action errors. Resolve server action function, form action, and mutation issues in Next.js."
frameworks: ["nextjs"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

A Next.js server action invocation error occurs when server actions fail to execute, return incorrect types, or are improperly invoked from client components. Server actions allow form submissions and mutations directly from components.

## Why It Happens

Server actions are async functions that run on the server. Errors occur when the `'use server'` directive is missing, when non-serializable data is returned, when the action is called from a client component without proper import, when the action references client-only code, or when form data is not properly extracted.

## Common Error Messages

```
Error: Only async functions are allowed in Server Actions
```

```
Error: Only plain objects can be passed to Client Components from Server Components
```

```
Error: An error occurred in the Server Components render
```

```
TypeError: Cannot serialize non-plain objects
```

## How to Fix It

### 1. Define Server Actions Correctly

Use the `'use server'` directive:

```typescript
// actions.ts
'use server';

import { revalidatePath } from 'next/cache';
import { redirect } from 'next/navigation';

export async function createUser(formData: FormData) {
    const name = formData.get('name') as string;
    const email = formData.get('email') as string;

    if (!name || !email) {
        return { error: 'Name and email are required' };
    }

    try {
        await db.user.create({ data: { name, email } });
        revalidatePath('/users');
        redirect('/users');
    } catch (error) {
        return { error: 'Failed to create user' };
    }
}

export async function deleteUser(userId: string) {
    await db.user.delete({ where: { id: userId } });
    revalidatePath('/users');
}
```

### 2. Invoke Server Actions from Client Components

Import and use actions in client components:

```typescript
'use client';

import { createUser } from '@/actions';
import { useFormStatus } from 'react-dom';

export function UserForm() {
    return (
        <form action={createUser}>
            <input name="name" placeholder="Name" required />
            <input name="email" type="email" placeholder="Email" required />
            <SubmitButton />
        </form>
    );
}

function SubmitButton() {
    const { pending } = useFormStatus();
    return (
        <button type="submit" disabled={pending}>
            {pending ? 'Creating...' : 'Create User'}
        </button>
    );
}
```

### 3. Use Server Actions with onClick

Call actions from event handlers:

```typescript
'use client';

import { deleteUser } from '@/actions';
import { useTransition } from 'react';

export function DeleteButton({ userId }: { userId: string }) {
    const [isPending, startTransition] = useTransition();

    return (
        <button
            onClick={() => {
                startTransition(async () => {
                    await deleteUser(userId);
                });
            }}
            disabled={isPending}
        >
            {isPending ? 'Deleting...' : 'Delete'}
        </button>
    );
}
```

### 4. Return Serialized Data from Actions

Ensure return values are serializable:

```typescript
'use server';

// Wrong: returns non-serializable data
export async function getData() {
    return {
        date: new Date(),         // Date is not serializable
        fn: () => {},             // Functions are not serializable
    };
}

// Correct: returns plain objects
export async function getData() {
    const result = await fetchData();
    return {
        date: new Date().toISOString(),
        data: result,
        success: true,
    };
}
```

## Common Scenarios

**Scenario 1: Server action called from client but runs on client.**
Ensure the `'use server'` directive is at the top of the file containing the action.

**Scenario 2: Form submits but nothing happens.**
Check that the form has `action={serverAction}` (not `onSubmit`). Server actions work with the `action` attribute.

**Scenario 3: Action returns stale data after mutation.**
Use `revalidatePath()` or `revalidateTag()` to refresh cached data after mutations.

## Prevent It

1. **Always use `'use server'` at the top** of files containing server actions.

2. **Return only plain objects** from server actions -- no Date, Map, Set, or functions.

3. **Use `useFormStatus`** to show loading states during form submissions.
