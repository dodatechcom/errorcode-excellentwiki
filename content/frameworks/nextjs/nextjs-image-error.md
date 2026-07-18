---
title: "[Solution] Next.js Image Optimization Error — How to Fix"
description: "Fix Next.js Image component errors. Resolve image optimization, loading, and configuration issues in Next.js."
frameworks: ["nextjs"]
error-types: ["configuration-error"]
severities: ["error"]
weight: 5
comments: true
---

A Next.js image optimization error occurs when the `next/image` component fails to optimize, load, or display images. The Image component provides built-in optimization but requires proper configuration.

## Why It Happens

Next.js Image component automatically optimizes images. Errors occur when external image domains are not allowed in `next.config.js`, when image dimensions are incorrect, when the image source is invalid, when `priority` and `loading` attributes conflict, or when the image optimization service is unavailable.

## Common Error Messages

```
Error: Invalid src prop (https://example.com/image.png) on next/image, this host is not configured in images.remotePatterns
```

```
Error: Image is missing required "width" or "height" property
```

```
Error: Failed to optimize image: undefined
```

```
Warning: Image with src "..." was detected as the Largest Contentful Paint (LCP)
```

## How to Fix It

### 1. Configure Allowed Image Domains

Add external domains to `next.config.js`:

```javascript
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
    images: {
        remotePatterns: [
            {
                protocol: 'https',
                hostname: 'example.com',
                pathname: '/images/**',
            },
            {
                protocol: 'https',
                hostname: '*.amazonaws.com',
            },
        ],
        // Or use domains (deprecated in newer versions)
        // domains: ['example.com', 'cdn.example.com'],
        formats: ['image/avif', 'image/webp'],
        minimumCacheTTL: 60 * 60 * 24, // 24 hours
    },
};

module.exports = nextConfig;
```

### 2. Use Image Component Correctly

Provide required props:

```tsx
import Image from 'next/image';

// Static image (width and height required)
<Image
    src="/images/hero.png"
    alt="Hero banner"
    width={1200}
    height={600}
    priority
/>

// Remote image with fill
<Image
    src="https://example.com/photo.jpg"
    alt="Photo"
    fill
    sizes="(max-width: 768px) 100vw, 50vw"
/>

// With placeholder
<Image
    src="/images/product.jpg"
    alt="Product"
    width={400}
    height={300}
    placeholder="blur"
    blurDataURL="data:image/jpeg;base64,..."
/>
```

### 3. Handle Dynamic Images

Use dynamic imports for images:

```tsx
import Image from 'next/image';
import { useState } from 'react';

function ProductImage({ src, alt }: { src: string; alt: string }) {
    const [error, setError] = useState(false);

    if (error) {
        return <div className="placeholder">Image not available</div>;
    }

    return (
        <Image
            src={src}
            alt={alt}
            width={400}
            height={300}
            onError={() => setError(true)}
            priority
        />
    );
}
```

### 4. Optimize for Performance

Use proper attributes for different scenarios:

```tsx
// Above the fold — use priority
<Image
    src="/hero.jpg"
    alt="Hero"
    width={1920}
    height={1080}
    priority
/>

// Below the fold — default lazy loading
<Image
    src="/content.jpg"
    alt="Content"
    width={800}
    height={600}
/>

// Use sizes for responsive images
<Image
    src="/responsive.jpg"
    alt="Responsive"
    fill
    sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 33vw"
/>
```

## Common Scenarios

**Scenario 1: Image fails to load from external domain.**
Add the domain to `images.remotePatterns` in `next.config.js`. Restart the dev server after changes.

**Scenario 2: Image blurry or low quality.**
Use the `quality` prop (default is 75) and ensure the source image is high enough resolution.

**Scenario 3: Large images slow down page.**
Use the `sizes` prop with `fill` to let the browser choose the right image size, and enable modern formats like AVIF.

## Prevent It

1. **Always specify `alt` text** for accessibility and SEO.

2. **Use `priority` only for above-the-fold images** to avoid degrading LCP.

3. **Configure `remotePatterns`** for all external image sources before deployment.
