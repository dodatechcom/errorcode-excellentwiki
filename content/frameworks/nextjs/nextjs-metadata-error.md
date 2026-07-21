---
title: "[Solution] Next.js Metadata or SEO Error -- How to Fix"
description: "Fix Next.js metadata and SEO errors. Resolve meta tags, Open Graph, and structured data issues in Next.js."
frameworks: ["nextjs"]
error-types: ["configuration-error"]
severities: ["warning"]
weight: 5
comments: true
---

A Next.js metadata or SEO error occurs when meta tags are missing, duplicated, or incorrectly generated. The Metadata API in Next.js App Router provides a structured way to manage SEO and social sharing metadata.

## Why It Happens

Metadata errors occur when the `metadata` export is incorrectly structured, when dynamic metadata uses `generateMetadata` incorrectly, when parent layout metadata conflicts with child metadata, when Open Graph images are not properly configured, or when metadata is generated at the wrong rendering level.

## Common Error Messages

```
Error: Metadata must be an object, but got: [object Promise]
```

```
Error: "metadata.title" must be a string or object, got: undefined
```

```
Warning: Duplicate Open Graph metadata found
```

```
Error: generateMetadata must return an object
```

## How to Fix It

### 1. Define Static Metadata

Export metadata from page or layout files:

```typescript
// app/layout.tsx
import type { Metadata } from 'next';

export const metadata: Metadata = {
    title: {
        default: 'My App',
        template: '%s | My App',
    },
    description: 'The best application ever',
    openGraph: {
        title: 'My App',
        description: 'The best application ever',
        url: 'https://myapp.com',
        siteName: 'My App',
        locale: 'en_US',
        type: 'website',
    },
    twitter: {
        card: 'summary_large_image',
        title: 'My App',
        description: 'The best application ever',
    },
    robots: {
        index: true,
        follow: true,
    },
};

export default function RootLayout({ children }) {
    return (
        <html lang="en">
            <body>{children}</body>
        </html>
    );
}
```

```typescript
// app/page.tsx
import type { Metadata } from 'next';

export const metadata: Metadata = {
    title: 'Home',
    description: 'Welcome to My App',
};

export default function HomePage() {
    return <main>Welcome!</main>;
}
```

### 2. Generate Dynamic Metadata

Use `generateMetadata` for dynamic pages:

```typescript
// app/blog/[slug]/page.tsx
import type { Metadata } from 'next';

type Props = {
    params: { slug: string };
};

export async function generateMetadata({ params }: Props): Promise<Metadata> {
    const post = await getPost(params.slug);

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
            publishedTime: post.publishedAt,
            authors: [post.author],
        },
    };
}

export default async function BlogPost({ params }: Props) {
    const post = await getPost(params.slug);
    return <article>{post.content}</article>;
}
```

### 3. Override Parent Metadata

Control metadata inheritance in nested layouts:

```typescript
// app/dashboard/layout.tsx
import type { Metadata } from 'next';

export const metadata: Metadata = {
    title: 'Dashboard',
    robots: { index: false },  // Don't index dashboard pages
};

// app/dashboard/page.tsx
import type { Metadata } from 'next';

// Override parent title
export const metadata: Metadata = {
    title: 'My Dashboard',  // Will be "My Dashboard | My App" using template
};

export default function Dashboard() {
    return <div>Dashboard content</div>;
}
```

### 4. Add Structured Data (JSON-LD)

Include structured data for rich snippets:

```typescript
// app/blog/[slug]/page.tsx
export default async function BlogPost({ params }) {
    const post = await getPost(params.slug);

    const jsonLd = {
        '@context': 'https://schema.org',
        '@type': 'BlogPosting',
        headline: post.title,
        description: post.excerpt,
        image: post.coverImage,
        datePublished: post.publishedAt,
        author: {
            '@type': 'Person',
            name: post.author.name,
        },
    };

    return (
        <>
            <script
                type="application/ld+json"
                dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
            />
            <article>
                <h1>{post.title}</h1>
                <p>{post.content}</p>
            </article>
        </>
    );
}
```

## Common Scenarios

**Scenario 1: Title shows twice on child pages.**
Use the `title.template` in the parent layout and `title.absolute` in child pages when needed.

**Scenario 2: Open Graph image not showing on social media.**
Ensure the image URL is absolute (not relative) and the image dimensions are at least 1200x630.

**Scenario 3: Metadata not updating between pages.**
Check that `generateMetadata` is properly awaited and returns the correct data for each page.

## Prevent It

1. **Use the Metadata API** instead of manual `<head>` tags for consistent metadata management.

2. **Test with social media debuggers** (Facebook, Twitter) to verify Open Graph metadata.

3. **Use `title.template`** to maintain consistent title formatting across pages.
