---
title: "[Solution] dgrijalva/jwt-go Token Expired Fix"
description: "Fix Go JWT token expired errors. Handle token validation, signing, and refresh logic."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# dgrijalva/jwt-go Token Expired

The JWT token library (`github.com/dgrijalva/jwt-go` or `github.com/golang-jwt/jwt`) fails when the token is expired, the signing method does not match, the secret key is wrong, or the token claims are invalid. JWT validation is a critical security step that must be done on every authenticated request.

## Common Causes

```go
// Cause 1: Token expired
token, err := jwt.Parse(tokenString, func(t *jwt.Token) (interface{}, error) {
    return signingKey, nil
})
// token is expired — Claims.Expiry < time.Now()

// Cause 2: Wrong signing method
token, _ := jwt.Parse(tokenString, func(t *jwt.Token) (interface{}, error) {
    if _, ok := t.Method.(*jwt.SigningMethodHMAC); !ok {
        return nil, fmt.Errorf("unexpected signing method: %v", t.Header["alg"])
    }
    return signingKey, nil
})
// alg: none attack — token signed with "none" algorithm

// Cause 3: Secret key mismatch
// Signed with "secret-1", verified with "secret-2"
// signature is invalid

// Cause 4: Token format invalid
// "not.a.jwt.token"
// token contains an invalid number of segments

// Cause 5: Claims validation fails
// Token has valid signature but invalid claims
// (missing required fields, wrong issuer, etc.)
```

## How to Fix

### Fix 1: Validate token with proper claims

```go
import (
    "fmt"
    "os"
    "time"

    "github.com/golang-jwt/jwt/v5"
)

type Claims struct {
    UserID string `json:"user_id"`
    Role   string `json:"role"`
    jwt.RegisteredClaims
}

func validateToken(tokenString string) (*Claims, error) {
    secretKey := []byte(os.Getenv("JWT_SECRET"))

    claims := &Claims{}
    token, err := jwt.ParseWithClaims(tokenString, claims, func(t *jwt.Token) (interface{}, error) {
        if _, ok := t.Method.(*jwt.SigningMethodHMAC); !ok {
            return nil, fmt.Errorf("unexpected signing method: %v", t.Header["alg"])
        }
        return secretKey, nil
    })

    if err != nil || !token.Valid {
        return nil, fmt.Errorf("invalid token: %w", err)
    }

    return claims, nil
}
```

### Fix 2: Create tokens with proper expiry

```go
func createToken(userID, role string) (string, error) {
    secretKey := []byte(os.Getenv("JWT_SECRET"))

    claims := &Claims{
        UserID: userID,
        Role:   role,
        RegisteredClaims: jwt.RegisteredClaims{
            ExpiresAt: jwt.NewNumericDate(time.Now().Add(24 * time.Hour)),
            IssuedAt:  jwt.NewNumericDate(time.Now()),
            Issuer:    "myapp",
        },
    }

    token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
    return token.SignedString(secretKey)
}
```

### Fix 3: Use refresh tokens for long-lived sessions

```go
func refreshAccessToken(refreshToken string) (string, error) {
    claims, err := validateToken(refreshToken)
    if err != nil {
        return "", fmt.Errorf("invalid refresh token: %w", err)
    }

    // Create new access token
    return createToken(claims.UserID, claims.Role)
}
```

## Examples

```go
package main

import (
    "fmt"
    "log"
    "os"
    "time"

    "github.com/golang-jwt/jwt/v5"
)

type Claims struct {
    UserID string `json:"user_id"`
    jwt.RegisteredClaims
}

func main() {
    secretKey := []byte(os.Getenv("JWT_SECRET"))

    // Create token
    claims := &Claims{
        UserID: "user-123",
        RegisteredClaims: jwt.RegisteredClaims{
            ExpiresAt: jwt.NewNumericDate(time.Now().Add(1 * time.Hour)),
        },
    }

    token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
    tokenString, err := token.SignedString(secretKey)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println("Token:", tokenString)

    // Validate token
    parsedClaims := &Claims{}
    _, err = jwt.ParseWithClaims(tokenString, parsedClaims, func(t *jwt.Token) (interface{}, error) {
        return secretKey, nil
    })
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("User: %s\n", parsedClaims.UserID)
}
```

## Related Errors

- [http-status-401]({{< relref "/languages/go/http-status-401" >}}) — HTTP 401 when JWT is invalid
- [go-oauth-error]({{< relref "/languages/go/go-oauth-error" >}}) — OAuth token exchange similar flow
- [go-vault-error]({{< relref "/languages/go/go-vault-error" >}}) — Vault token validation similar pattern
