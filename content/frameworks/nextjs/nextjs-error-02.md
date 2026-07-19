---
title: "Image optimization errors with next/image"
description: "Next.js error related to image optimization. Common issues include incorrect image configuration, missing width/height props, unsupported image formats, or improper use of the priority prop."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "nextjs"
tags: ["error", "image", "optimization", "next/image"]
severity: "error"
solution: "Always provide width and height props for static images. Use the fill prop for responsive images. Configure allowed image domains in next.config.js. Use priority for above-the-fold images. Handle loading states properly."
---

Next.js error related to image optimization. Common issues include incorrect image configuration, missing width/height props, unsupported image formats, or improper use of the priority prop.

## Solution

Always provide width and height props for static images. Use the fill prop for responsive images. Configure allowed image domains in next.config.js. Use priority for above-the-fold images. Handle loading states properly.

## Code Example

```javascript
  // BAD: Missing dimensions
  import Image from 'next/image';
  
  function BadImage() {
    return <Image src="/photo.jpg" alt="Photo" />; // Error!
  }
  
  // GOOD: With explicit dimensions
  function GoodImage() {
    return (
      <Image
        src="/photo.jpg"
        alt="Photo"
        width={500}
        height={300}
      />
    );
  }
  
  // GOOD: Responsive with fill
  function ResponsiveImage() {
    return (
      <div style={{ position: 'relative', width: '100%', height: '400px' }}>
        <Image
          src="/photo.jpg"
          alt="Photo"
          fill
          style={{ objectFit: 'cover' }}
        />
      </div>
    );
  }
  
  // GOOD: External images configuration
  // next.config.js
  module.exports = {
    images: {
      remotePatterns: [
        {
          protocol: 'https',
          hostname: 'example.com',
          pathname: '/images/**',
        },
      ],
    },
  };
  
  // GOOD: Priority for above-the-fold
  function HeroImage() {
    return (
      <Image
        src="/hero.jpg"
        alt="Hero"
        width={1200}
        height={600}
        priority
      />
    );
  }
  
  // GOOD: Placeholder with blur
  function BlurredImage() {
    return (
      <Image
        src="/photo.jpg"
        alt="Photo"
        width={500}
        height={300}
        placeholder="blur"
        blurDataURL="data:image/jpeg;base64,/9j/4AAQ..."
      />
    );
  }
```
