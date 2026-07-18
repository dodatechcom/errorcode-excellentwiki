---
title: "[Solution] Scala Play Framework — Action Not Found Error"
description: "Fix Play Framework action not found errors. Learn about routing configuration, controller binding, and request handling in Play."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A "Action not found" error in Play Framework means the router could not match the incoming HTTP request to any defined route. The error page shows the request method, path, and a list of possible routes that were considered but rejected.

## Why It Happens

The most common cause is a typo or mismatch in the route definition. The path parameters in `conf/routes` must exactly match the method parameters in the controller. If the route says `/users/:id` but the controller method expects `id: String`, the types must align.

Another frequent cause is incorrect HTTP method matching. If a route is defined with `POST` but the request uses `GET`, it will not match. This is especially common when testing with browsers that default to GET requests.

Missing controller method bindings occur when the routes file references a method that does not exist or has been renamed. Play generates a router class at compile time, and if the routes file does not match the controller, compilation fails silently or the route is omitted.

Wildcard routes and catch-all patterns can also cause issues. A route like `/*path` may match too broadly or not at all depending on the URL structure.

Finally, query parameters are not part of route matching. If you are relying on query parameters to distinguish routes, you need to handle them inside the action.

## How to Fix It

### Verify routes file syntax

```conf
# conf/routes
GET  /users         controllers.UserController.list()
GET  /users/:id     controllers.UserController.get(id: Long)
POST /users         controllers.UserController.create()
```

### Match controller parameter types exactly

```scala
class UserController @Inject()(cc: ControllerComponents) extends AbstractController(cc) {
  // Route: GET /users/:id — id must be parseable as Long
  def get(id: Long) = Action { implicit request =>
    Ok(s"User $id")
  }
}
```

### Add a catch-all route for SPA or 404 handling

```conf
GET  /*path  controllers.Application.index()
```

### Use the routes documentation tool

```bash
# List all routes
sbt "playRoutes"

# Show route compilation errors
sbt compile
```

### Check for conflicting routes

```conf
# These conflict — more specific route must come first
GET  /users/admin   controllers.UserController.admin()
GET  /users/:id     controllers.UserController.get(id: Long)
```

## Common Mistakes

- Placing wildcard routes before specific routes in the routes file
- Using `String` for route parameters that should be `Long` or other types
- Forgetting that route paths are case-sensitive
- Not restarting the application after changing the routes file
- Using `Action` without `Action { implicit request =>` when form binding is needed

## Related Pages

- [Scala Akka Timeout](/languages/scala/scala-akka-timeout/)
- [Scala MatchError](/languages/scala/match-error/)
- [Scala Option.get Error](/languages/scala/scala-option-get-error/)
