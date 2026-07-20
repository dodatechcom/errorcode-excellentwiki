---
title: "[Solution] JavaScript Gatsby Build Error — How to Fix"
description: "Fix JavaScript Gatsby GraphQL schema errors, page creation failures, plugin conflicts, and static generation issues."
languages: ["javascript"]
error-types: ["runtime"]
severities: ["error"]
comments: true
weight: 809
---

# JavaScript Gatsby Build Error

A `GatsbyError`, `GraphQLError`, or `WebpackError` occurs when Gatsby's GraphQL schema cannot infer types, page creation in `gatsby-node.js` fails, plugins conflict during bootstrap, or static HTML generation encounters runtime errors.

## Why It Happens

Gatsby errors arise from missing or conflicting GraphQL schema types, incorrect `createPage` API usage, plugin version incompatibilities, missing `gatsby-source-*` plugins for data fetching, and browser APIs used during SSR.

## Common Error Messages

- `Error: There was an error in your GraphQL query: Cannot query field "xxx"`
- `Error: Page data for page "xxx" looks like it's empty`
- `Error: Plugin "xxx" is not compatible with your Gatsby version`
- `Error: document is not defined during build`
- `Error: gatsby-node.js: createPage must be called with a valid path`

## How to Fix It

### Fix 1: Define GraphQL schema types

```javascript
// gatsby-node.js
exports.createSchemaCustomization = ({ actions }) => {
  const { createTypes } = actions
  const typeDefs = `
    type MarkdownRemark implements Node {
      frontmatter: Frontmatter
    }
    type Frontmatter {
      title: String!
      date: Date @dateformat
      tags: [String!]
    }
  `
  createTypes(typeDefs)
}
```

### Fix 2: Create pages correctly

```javascript
// ❌ Wrong - missing required fields
// exports.createPages = async ({ graphql, actions }) => {
//   const result = await graphql(`...`)
//   result.data.allMarkdownRemark.nodes.forEach(node => {
//     actions.createPage({}) // missing path, component, context
//   })
// }

// ✅ Correct
exports.createPages = async ({ graphql, actions }) => {
  const { createPage } = actions
  const result = await graphql(`
    query {
      allMarkdownRemark {
        nodes {
          id
          frontmatter { slug }
        }
      }
    }
  `)

  result.data.allMarkdownRemark.nodes.forEach(node => {
    createPage({
      path: `/blog/${node.frontmatter.slug}`,
      component: require.resolve('./src/templates/blog-post.tsx'),
      context: { id: node.id }
    })
  })
}
```

### Fix 3: Handle SSR browser APIs

```jsx
// ❌ Wrong - direct browser API access
// const width = window.innerWidth

// ✅ Correct - check for window
const width = typeof window !== 'undefined' ? window.innerWidth : 1024

// Or use useEffect
useEffect(() => {
  const width = window.innerWidth
  setWidth(width)
}, [])
```

### Fix 4: Resolve plugin conflicts

```javascript
// gatsby-config.js
module.exports = {
  plugins: [
    // ❌ Wrong - duplicate source plugins for same source
    // 'gatsby-source-filesystem',
    // 'gatsby-source-filesystem',

    // ✅ Correct - single source with options
    {
      resolve: 'gatsby-source-filesystem',
      options: { name: 'blog', path: `${__dirname}/content/blog` }
    },
    'gatsby-transformer-remark'
  ]
}
```

## Examples

GraphQL query with missing field fallback:

```graphql
query BlogQuery {
  allMarkdownRemark {
    nodes {
      frontmatter {
        title
        # ❌ Wrong - 'author' might not exist in schema
        # ✅ Correct - use default values
        date(formatString: "MMMM DD, YYYY")
      }
    }
  }
}
```

## Related Errors

- [Nuxt Error](/languages/javascript/nuxt-error)
- [Remix Error](/languages/javascript/remix-error)
- [JavaScript GraphQL Error](/languages/javascript/graphql-error)
