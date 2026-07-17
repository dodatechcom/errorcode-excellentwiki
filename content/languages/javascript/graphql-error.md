---
title: "[Solution] GraphQL Error: Cannot return null Fix"
description: "Fix GraphQL 'Cannot return null for non-nullable field' errors. Handle null values, required fields, and resolver errors in GraphQL."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["graphql", "null", "resolver", "schema", "non-nullable"]
weight: 5
---

# GraphQL Error — Cannot return null

This error occurs when a GraphQL resolver returns `null` for a non-nullable field. The schema requires a value, but the resolver produces none.

## What This Error Means

Common error messages:

- `Cannot return null for non-nullable field Query.user`
- `Cannot return null for non-nullable field User.email`
- `GraphQL error: Field "..." must not have a selection since type "..." has no subfields`

Non-nullable fields (`!` in schema) must always return a value. Returning null causes the error to bubble up.

## Common Causes

```graphql
# Cause 1: Resolver returns null
type User {
  id: ID!
  email: String!  # non-nullable
}

# Resolver
const resolvers = {
  User: {
    email: (user) => user.email || null,  # null = error
  },
};
```

```javascript
// Cause 2: Database returns null
const user = await db.users.findById(id);
// user.email is null in database

// Cause 3: Missing field in response object
return { id: 1 }; // missing required 'email'

// Cause 4: Incorrect field name in resolver
const resolvers = {
  User: {
    name: (user) => user.fullName, // field is 'name' not 'fullName'
  },
};
```

## How to Fix

### Fix 1: Return fallback values

```javascript
const resolvers = {
  User: {
    email: (user) => user.email || 'unknown@example.com',
    name: (user) => user.name ?? 'Anonymous',
  },
};
```

### Fix 2: Make fields nullable in schema

```graphql
type User {
  id: ID!
  email: String   # nullable - can return null
  name: String    # nullable
}
```

### Fix 3: Validate data before returning

```javascript
const resolvers = {
  Query: {
    user: async (_, { id }) => {
      const user = await db.users.findById(id);
      if (!user) {
        throw new Error('User not found');
      }
      return user;
    },
  },
};
```

### Fix 4: Use error handling in resolvers

```javascript
const resolvers = {
  User: {
    email: (user) => {
      if (!user.email) {
        throw new Error('Email not available');
      }
      return user.email;
    },
  },
};
```

## Examples

```graphql
# Schema
type Query {
  user(id: ID!): User!
}

type User {
  id: ID!
  email: String!  # non-nullable
}

# Query
query {
  user(id: "1") {
    email
  }
}

# If user.email is null:
# Error: Cannot return null for non-nullable field User.email
```

## Related Errors

- [Apollo Error]({{< relref "/languages/javascript/apollo-error" >}}) — Apollo Client network error
- [Mongoose Validation]({{< relref "/languages/javascript/mongoose-validation" >}}) — validation error
- [Express Route 404]({{< relref "/languages/javascript/express-route" >}}) — route not found
