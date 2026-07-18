---
title: "Solved JavaScript jsonwebtoken Verify Error — How to Fix"
date: 2026-03-20T15:45:45+00:00
description: "Learn how to resolve JavaScript jsonwebtoken JWT verify and sign errors with proper error handling."
categories: ["javascript"]
keywords: ["jsonwebtoken error", "jwt verify error", "jwt sign error", "jwt token", "json web token"]
error_types: ["runtime"]
severities: ["error"]
languages: ["javascript"]
weight: 5
comments: true
---

## Why It Happens

jsonwebtoken errors occur when JWT tokens are malformed, expired, or signed with incorrect secrets. The library requires exact secret matching between sign and verify operations.

Common causes include:
- Token signed with different secret than verification
- Token has expired (`exp` claim exceeded)
- Invalid token format (not three Base64 segments)
- Algorithm mismatch between sign and verify
- Malformed payload or header

## Common Error Messages

```
JsonWebTokenError: invalid signature
```

```
TokenExpiredError: jwt expired
```

```
JsonWebTokenError: jwt malformed
```

## How to Fix It

### 1. Sign JWT Tokens

Create tokens with proper configuration.

```javascript
import jwt from "jsonwebtoken";

const SECRET = process.env.JWT_SECRET;
const REFRESH_SECRET = process.env.JWT_REFRESH_SECRET;

// Sign access token
function generateAccessToken(user) {
  return jwt.sign(
    {
      id: user.id,
      email: user.email,
      role: user.role
    },
    SECRET,
    {
      expiresIn: "15m",
      algorithm: "HS256"
    }
  );
}

// Sign refresh token
function generateRefreshToken(user) {
  return jwt.sign(
    { id: user.id },
    REFRESH_SECRET,
    {
      expiresIn: "7d",
      algorithm: "HS256"
    }
  );
}

// Sign with options
function generateTokenWithClaims(user, claims) {
  return jwt.sign(
    { ...claims, sub: user.id },
    SECRET,
    {
      expiresIn: "1h",
      issuer: "myapp",
      audience: "myapp-api"
    }
  );
}
```

### 2. Verify JWT Tokens

Validate tokens with proper error handling.

```javascript
import jwt from "jsonwebtoken";

function verifyToken(token, secret = SECRET) {
  try {
    const decoded = jwt.verify(token, secret, {
      algorithms: ["HS256"],
      issuer: "myapp",
      audience: "myapp-api"
    });
    
    return { valid: true, data: decoded };
  } catch (error) {
    if (error.name === "TokenExpiredError") {
      return {
        valid: false,
        error: "Token expired",
        expiredAt: error.expiredAt
      };
    }
    
    if (error.name === "JsonWebTokenError") {
      return {
        valid: false,
        error: "Invalid token",
        details: error.message
      };
    }
    
    return {
      valid: false,
      error: "Token verification failed"
    };
  }
}

// Express middleware
function authenticateToken(req, res, next) {
  const authHeader = req.headers["authorization"];
  const token = authHeader && authHeader.split(" ")[1];
  
  if (!token) {
    return res.status(401).json({ error: "Access token required" });
  }
  
  const result = verifyToken(token);
  
  if (!result.valid) {
    return res.status(403).json({ error: result.error });
  }
  
  req.user = result.data;
  next();
}
```

### 3. Implement Token Refresh

Handle token refresh flow.

```javascript
import jwt from "jsonwebtoken";

async function refreshAccessToken(refreshToken) {
  const result = verifyToken(refreshToken, REFRESH_SECRET);
  
  if (!result.valid) {
    throw new Error("Invalid refresh token");
  }
  
  const user = await getUserById(result.data.id);
  
  if (!user) {
    throw new Error("User not found");
  }
  
  const newAccessToken = generateAccessToken(user);
  const newRefreshToken = generateRefreshToken(user);
  
  return {
    accessToken: newAccessToken,
    refreshToken: newRefreshToken,
    expiresIn: 900 // 15 minutes
  };
}

// Express route
app.post("/auth/refresh", async (req, res) => {
  const { refreshToken } = req.body;
  
  if (!refreshToken) {
    return res.status(400).json({ error: "Refresh token required" });
  }
  
  try {
    const tokens = await refreshAccessToken(refreshToken);
    res.json(tokens);
  } catch (error) {
    res.status(403).json({ error: "Invalid refresh token" });
  }
});
```

## Common Scenarios

### Scenario 1: Multi-tenant JWT

Handle different secrets per tenant:

```javascript
const secrets = {
  tenant1: process.env.JWT_SECRET_TENANT1,
  tenant2: process.env.JWT_SECRET_TENANT2
};

function verifyTenantToken(token, tenantId) {
  const secret = secrets[tenantId];
  
  if (!secret) {
    throw new Error("Unknown tenant");
  }
  
  return jwt.verify(token, secret, {
    algorithms: ["HS256"]
  });
}
```

### Scenario 2: JWT with Roles

Include authorization in token:

```javascript
function generateAdminToken(user) {
  return jwt.sign(
    {
      id: user.id,
      role: "admin",
      permissions: ["read", "write", "delete"]
    },
    SECRET,
    { expiresIn: "1h" }
  );
}

function authorize(allowedRoles) {
  return (req, res, next) => {
    const result = verifyToken(req.user.token);
    
    if (!result.valid) {
      return res.status(403).json({ error: "Invalid token" });
    }
    
    if (!allowedRoles.includes(result.data.role)) {
      return res.status(403).json({ error: "Insufficient permissions" });
    }
    
    req.tokenData = result.data;
    next();
  };
}

// Usage
app.get("/admin", authenticateToken, authorize(["admin"]), (req, res) => {
  res.json({ data: "admin content" });
});
```

## Prevent It

- Use strong, random secrets (at least 256 bits)
- Always specify algorithms explicitly when verifying
- Set appropriate token expiration times (15min for access, 7d for refresh)
- Store refresh tokens securely (httpOnly cookies)
- Validate `iss` and `aud` claims for multi-service architectures