---
title: "Solved JavaScript busboy Error — How to Fix"
date: 2026-03-20T14:40:00+00:00
description: "Learn how to resolve JavaScript busboy multipart form data parsing and file upload errors."
categories: ["javascript"]
keywords: ["busboy error", "file upload", "multipart form", "form data", "upload error"]
error_types: ["runtime"]
severities: ["error"]
languages: ["javascript"]
weight: 5
comments: true
---

## Why It Happens

busboy errors occur when the multipart form data parser encounters invalid form boundaries, missing file fields, or size limit violations. File uploads require careful handling of streams and memory limits.

Common causes include:
- File size exceeding configured limits
- Missing or malformed Content-Type header
- Invalid multipart boundary in request
- Memory exhaustion from large file uploads
- Request timeout during slow uploads

## Common Error Messages

```
Error: Multipart: Missing end boundary
```

```
Error: Request size too large
```

```
Error: Unexpected end of multipart data
```

## How to Fix It

### 1. Configure busboy Properly

Set up busboy with appropriate limits.

```javascript
import busboy from "busboy";

function parseMultipartForm(req) {
  return new Promise((resolve, reject) => {
    const bb = busboy({
      headers: req.headers,
      limits: {
        files: 10,
        fileSize: 10 * 1024 * 1024, // 10MB
        fields: 20,
        fieldSize: 1024 * 1024, // 1MB
        headerPairs: 200
      }
    });
    
    const fields = {};
    const files = [];
    
    bb.on("field", (name, value) => {
      fields[name] = value;
    });
    
    bb.on("file", (name, file, info) => {
      const chunks = [];
      
      file.on("data", (chunk) => {
        chunks.push(chunk);
      });
      
      file.on("end", () => {
        files.push({
          fieldName: name,
          filename: info.filename,
          mimeType: info.mimeType,
          data: Buffer.concat(chunks)
        });
      });
      
      file.on("error", reject);
    });
    
    bb.on("finish", () => {
      resolve({ fields, files });
    });
    
    bb.on("error", reject);
    
    req.pipe(bb);
  });
}
```

### 2. Handle File Uploads to Storage

Stream uploads directly to storage.

```javascript
import busboy from "busboy";
import { S3Client, PutObjectCommand } from "@aws-sdk/client-s3";

const s3 = new S3Client({ region: process.env.AWS_REGION });

function uploadToS3(req) {
  return new Promise((resolve, reject) => {
    const bb = busboy({
      headers: req.headers,
      limits: { fileSize: 50 * 1024 * 1024 }
    });
    
    const uploads = [];
    
    bb.on("file", (name, file, info) => {
      const chunks = [];
      
      file.on("data", (chunk) => chunks.push(chunk));
      
      file.on("end", async () => {
        const buffer = Buffer.concat(chunks);
        
        const command = new PutObjectCommand({
          Bucket: process.env.S3_BUCKET,
          Key: `uploads/${info.filename}`,
          Body: buffer,
          ContentType: info.mimeType
        });
        
        try {
          await s3.send(command);
          uploads.push({ field: name, filename: info.filename });
        } catch (error) {
          reject(error);
        }
      });
    });
    
    bb.on("finish", () => resolve(uploads));
    bb.on("error", reject);
    
    req.pipe(bb);
  });
}
```

### 3. Implement Progress Tracking

Track upload progress for large files.

```javascript
import busboy from "busboy";
import { EventEmitter } from "events";

class UploadTracker extends EventEmitter {
  constructor(req, options = {}) {
    super();
    this.totalBytes = parseInt(req.headers["content-length"]) || 0;
    this.receivedBytes = 0;
    this.bb = busboy({
      headers: req.headers,
      limits: { fileSize: options.maxSize || 100 * 1024 * 1024 }
    });
    
    this.setupEventHandlers();
  }
  
  setupEventHandlers() {
    this.bb.on("file", (name, file, info) => {
      file.on("data", (chunk) => {
        this.receivedBytes += chunk.length;
        const progress = this.totalBytes > 0 
          ? (this.receivedBytes / this.totalBytes) * 100 
          : 0;
        this.emit("progress", { bytes: this.receivedBytes, percent: progress });
      });
    });
  }
  
  parse() {
    return new Promise((resolve, reject) => {
      const fields = {};
      const files = [];
      
      this.bb.on("field", (name, value) => {
        fields[name] = value;
      });
      
      this.bb.on("file", (name, file, info) => {
        const chunks = [];
        file.on("data", (chunk) => chunks.push(chunk));
        file.on("end", () => {
          files.push({
            field: name,
            filename: info.filename,
            mimeType: info.mimeType,
            data: Buffer.concat(chunks)
          });
        });
      });
      
      this.bb.on("finish", () => resolve({ fields, files }));
      this.bb.on("error", reject);
      
      this.req.pipe(this.bb);
    });
  }
}

// Usage
app.post("/upload", async (req, res) => {
  const tracker = new UploadTracker(req);
  
  tracker.on("progress", ({ percent }) => {
    console.log(`Upload progress: ${percent.toFixed(1)}%`);
  });
  
  try {
    const { fields, files } = await tracker.parse();
    res.json({ success: true, files: files.length });
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});
```

## Common Scenarios

### Scenario 1: Image Upload with Validation

Validate and process uploaded images:

```javascript
import busboy from "busboy";
import sharp from "sharp";

function handleImageUpload(req) {
  return new Promise((resolve, reject) => {
    const bb = busboy({
      headers: req.headers,
      limits: { fileSize: 10 * 1024 * 1024, files: 1 }
    });
    
    bb.on("file", async (name, file, info) => {
      if (!info.mimeType.startsWith("image/")) {
        file.resume(); // Drain the stream
        return reject(new Error("Only images are allowed"));
      }
      
      const chunks = [];
      file.on("data", (chunk) => chunks.push(chunk));
      
      file.on("end", async () => {
        try {
          const buffer = Buffer.concat(chunks);
          
          const metadata = await sharp(buffer).metadata();
          
          if (metadata.width > 4096 || metadata.height > 4096) {
            return reject(new Error("Image too large"));
          }
          
          const optimized = await sharp(buffer)
            .resize(800, 600, { fit: "cover" })
            .jpeg({ quality: 85 })
            .toBuffer();
          
          resolve({ buffer: optimized, metadata });
        } catch (error) {
          reject(error);
        }
      });
    });
    
    bb.on("finish", () => {});
    bb.on("error", reject);
    
    req.pipe(bb);
  });
}
```

## Prevent It

- Set `fileSize` limit to prevent memory exhaustion
- Use streaming to process files instead of buffering entire content
- Validate file types before processing
- Set `files: 0` if file uploads should be rejected
- Monitor upload progress for large file uploads