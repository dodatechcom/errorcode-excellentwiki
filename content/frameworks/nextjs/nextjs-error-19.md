---
title: "Next.js pages router to app router migration errors"
description: "Common errors when migrating from Next.js Pages Router to App Router. Issues include incorrect data fetching patterns, improper component structure, or mixing old and new patterns incorrectly."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "nextjs"
tags: ["error", "migration", "pages-router", "app-router"]
severity: "error"
solution: "Migrate incrementally. Convert pages to app directory structure. Replace getStaticProps/getServerSideProps with async Server Components. Update API routes to Route Handlers. Test thoroughly after each migration step."
---

Common errors when migrating from Next.js Pages Router to App Router. Issues include incorrect data fetching patterns, improper component structure, or mixing old and new patterns incorrectly.

## Solution

Migrate incrementally. Convert pages to app directory structure. Replace getStaticProps/getServerSideProps with async Server Components. Update API routes to Route Handlers. Test thoroughly after each migration step.

## Code Example

```javascript
  // OLD: Pages Router
  // pages/about.js
  export async function getStaticProps() {
    return { props: { title: 'About' } };
  }
  
  export default function About({ title }) {
    return <h1>{title}</h1>;
  }
  
  // NEW: App Router
  // app/about/page.tsx
  export default async function AboutPage() {
    return <h1>About</h1>;
  }
  
  // OLD: API Route
  // pages/api/posts.js
  export default async function handler(req, res) {
    const posts = await getPosts();
    res.status(200).json(posts);
  }
  
  // NEW: Route Handler
  // app/api/posts/route.ts
  import { NextResponse } from 'next/server';
  
  export async function GET() {
    const posts = await getPosts();
    return NextResponse.json(posts);
  }
  
  // OLD: Layout in _app.js
  // pages/_app.js
  export default function App({ Component, pageProps }) {
    return (
      <Layout>
        <Component {...pageProps} />
      </Layout>
    );
  }
  
  // NEW: Layout in layout.tsx
  // app/layout.tsx
  export default function RootLayout({ children }) {
    return (
      <html>
        <body>
          <Layout>{children}</Layout>
        </body>
      </html>
    );
  }
  
  // OLD: Dynamic routes
  // pages/posts/[id].js
  export async function getServerSideProps({ params }) {
    const post = await getPost(params.id);
    return { props: { post } };
  }
  
  // NEW: Dynamic routes
  // app/posts/[id]/page.tsx
  export default async function PostPage({ params }) {
    const post = await getPost(params.id);
    return <article>{post.content}</article>;
  }
```
