---
title: "React 19 Form Actions errors"
description: "React 19 error related to form actions not working correctly. Form actions must be functions that accept FormData, and cannot be async functions directly on the form element without proper handling."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "react"
tags: ["error", "react-19", "forms", "actions"]
severity: "error"
solution: "Use Server Actions or client-side actions with the form action prop. Handle form data using FormData API. Use useActionState for form state management. Ensure actions are properly typed and handle all form fields."
---

React 19 error related to form actions not working correctly. Form actions must be functions that accept FormData, and cannot be async functions directly on the form element without proper handling.

## Solution

Use Server Actions or client-side actions with the form action prop. Handle form data using FormData API. Use useActionState for form state management. Ensure actions are properly typed and handle all form fields.

## Code Example

```javascript
  import { useActionState } from 'react';
  
  // BAD: Async function on form action (causes issues)
  function BadForm() {
    return (
      <form action={async (formData) => { // Not recommended
        await submitForm(formData);
      }}>
        <input name="email" type="email" />
        <button type="submit">Submit</button>
      </form>
    );
  }
  
  // GOOD: Using Server Action
  // actions.ts
  'use server';
  export async function submitEmail(prevState, formData) {
    const email = formData.get('email');
    
    try {
      await sendEmail(email);
      return { success: true, message: 'Email sent!' };
    } catch (error) {
      return { success: false, message: 'Failed to send email' };
    }
  }
  
  // GOOD: Using useActionState
  'use client';
  import { useActionState } from 'react';
  import { submitEmail } from './actions';
  
  export function EmailForm() {
    const [state, formAction, isPending] = useActionState(submitEmail, null);
    
    return (
      <form action={formAction}>
        <input name="email" type="email" required />
        <button type="submit" disabled={isPending}>
          {isPending ? 'Sending...' : 'Send Email'}
        </button>
        {state && (
          <p className={state.success ? 'success' : 'error'}>
            {state.message}
          </p>
        )}
      </form>
    );
  }
```
