---
title: "[Solution] GraphQL: Error Response from Server Fix"
description: "Fix GraphQL server errors including validation errors, resolver errors, and malformed query responses. Handle error arrays and partial data."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# GraphQL: Error Response from Server

This error occurs when a GraphQL server returns an error in its `errors` array. Unlike REST, GraphQL often returns a 200 status with errors in the response body, making them easy to miss.

## What This Error Means

Common error messages:

- `"message": "Cannot query field 'email' on type 'User'."`
- `"message": "Field 'createUser' is missing required arguments: name, email"`
- `"message": "Not authorized to perform this action"`
- `"message": "Internal server error"`
- `{ errors: [...], data: null }` or `{ errors: [...], data: { partial: "data" } }`

GraphQL servers always return a JSON object with an `errors` array (when errors occur) and optionally a `data` field. HTTP status is usually 200.

## Common Causes

```javascript
// Cause 1: Querying a field that doesn't exist in the schema
const query = `
  query {
    user(id: 1) {
      name
      email
      nonExistentField  // ERROR
    }
  }
`;

// Cause 2: Missing required arguments
const query = `
  mutation {
    createUser {
      id
    }
  }
`;
// Error: Field 'createUser' is missing required argument 'input'

// Cause 3: Resolver throws an error
const resolvers = {
  User: {
    posts: (parent) => {
      throw new Error('Database connection failed'); // becomes GraphQL error
    },
  },
};

// Cause 4: Authorization error in middleware
const resolvers = {
  Query: {
    adminData: (_, __, context) => {
      if (!context.user?.isAdmin) {
        throw new Error('Not authorized'); // GraphQL error
      }
    },
  },
};
```

## How to Fix

### Fix 1: Check the errors array in the response

```javascript
async function graphqlRequest(query, variables = {}) {
  const res = await fetch('/graphql', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query, variables }),
  });
  const json = await res.json();

  if (json.errors) {
    json.errors.forEach(err => {
      console.error('GraphQL Error:', err.message);
      if (err.locations) {
        console.error('At line:', err.locations[0].line);
      }
    });
  }

  return json.data;
}
```

### Fix 2: Use `allErrors` option in Apollo Server

```javascript
const server = new ApolloServer({
  typeDefs,
  resolvers,
  includeStacktraceInErrorMessages: process.env.NODE_ENV !== 'production',
});
```

### Fix 3: Handle errors in client queries

```javascript
// Apollo Client
const { data, error, loading } = useQuery(GET_USER, {
  variables: { id: 1 },
  onError: (err) => {
    err.graphQLErrors.forEach(e => {
      console.error('GraphQL Error:', e.message);
    });
  },
});

if (error) {
  return <div>Error: {error.message}</div>;
}
```

### Fix 4: Add proper error types in resolvers

```javascript
class AuthenticationError extends Error {
  constructor(message = 'Not authenticated') {
    super(message);
    this.extensions = { code: 'UNAUTHENTICATED' };
  }
}

const resolvers = {
  Query: {
    secretData: (_, __, ctx) => {
      if (!ctx.user) throw new AuthenticationError();
      return getSecretData();
    },
  },
};
```

## Examples

```json
{
  "errors": [
    {
      "message": "Cannot query field 'posts' on type 'User'. Did you mean 'post'?",
      "locations": [{ "line": 4, "column": 7 }],
      "path": ["user", "posts"],
      "extensions": {
        "code": "GRAPHQL_VALIDATION_FAILED",
        "exception": {}
      }
    }
  ],
  "data": null
}
```

```graphql
# Fix: use the correct field name
query {
  user(id: 1) {
    name
    post {       # correct field name
      title
    }
  }
}
```

## Related Errors

- [GraphQL Error]({{< relref "/languages/javascript/graphql-error" >}}) — basic GraphQL error
- [Apollo Error V2]({{< relref "/languages/javascript/apollo-error-v2" >}}) — Apollo Client network error
- [Axios Error V2]({{< relref "/languages/javascript/axios-error-v2" >}}) — HTTP request failed
