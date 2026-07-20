---
title: "[Solution] PHP SYMFONY_ROUTING_ERROR — Route Not Found"
description: "Fix PHP SYMFONY_ROUTING_ERROR by checking route definitions, clearing cache, and verifying controller annotations. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 111
---

# PHP SYMFONY_ROUTING_ERROR — Route Not Found

A route was not found or is invalid in Symfony. This error occurs when route definitions are incorrect, the controller action does not exist, or the route cache is stale.

## Common Causes

```php
// Route attribute missing or wrong path
class BlogController extends AbstractController
{
    #[Route('/blog')] // missing name parameter
    public function index(): Response
    {
        // ...
    }
}
```

```php
// Route path conflict or duplicate
#[Route('/blog', name: 'blog_index')]
#[Route('/blog', name: 'blog_list')] // duplicate path
```

```php
// Controller action return type mismatch
#[Route('/user/{id}', name: 'user_show')]
public function show(int $id): Response
{
    return $this->json(['id' => $id]); // must return Response
}
```

```php
// YAML route definition syntax error
# config/routes.yaml
blog_index:
    path: /blog
    controller: App\Controller\BlogController::index
    # missing controller reference
```

```php
// Parameter requirement not satisfied
#[Route('/user/{id}', name: 'user_show')]
public function show(string $id): Response // expects int, gets string
{
    // ...
}
```

## How to Fix

### Fix 1: Define Routes Properly

Use PHP 8 attributes or YAML configuration.

```php
// PHP 8 Attribute routes
use Symfony\Component\Routing\Attribute\Route;
use Symfony\Component\HttpFoundation\Response;

class BlogController extends AbstractController
{
    #[Route('/blog', name: 'blog_index')]
    public function index(): Response
    {
        return $this->render('blog/index.html.twig');
    }

    #[Route('/blog/{id}', name: 'blog_show', requirements: ['id' => '\d+'])]
    public function show(int $id): Response
    {
        return $this->render('blog/show.html.twig', [
            'post' => $this->getDoctrine()->getRepository(BlogPost::class)->find($id),
        ]);
    }

    #[Route('/blog/new', name: 'blog_new', methods: ['GET', 'POST'])]
    public function new(Request $request): Response
    {
        // ...
    }
}
```

### Fix 2: Clear Route Cache

```bash
# Clear all caches
php bin/console cache:clear

# Clear only route cache
php bin/console cache:clear --env=prod

# Warm up cache for production
php bin/console cache:warmup --env=prod

# Debug routes
php bin/console debug:router

# Debug specific route
php bin/console debug:router blog_show
```

### Fix 3: Verify Controller Annotations

```php
// Correct controller with all route options
use Symfony\Component\Routing\Attribute\Route;
use Symfony\Component\HttpFoundation\Response;

class ProductController extends AbstractController
{
    /**
     * @Route("/products", name="product_index", methods={"GET"})
     */
    #[Route('/products', name: 'product_index', methods: ['GET'])]
    public function index(): Response
    {
        return $this->render('product/index.html.twig');
    }

    /**
     * @Route("/products/{id}", name="product_show", requirements={"id"="\d+"})
     */
    #[Route('/products/{id}', name: 'product_show', requirements: ['id' => '\d+'])]
    public function show(int $id): Response
    {
        $product = $this->getDoctrine()->getRepository(Product::class)->find($id);

        if (!$product) {
            throw $this->createNotFoundException('Product not found');
        }

        return $this->render('product/show.html.twig', [
            'product' => $product,
        ]);
    }

    #[Route('/products/{slug}', name: 'product_by_slug', methods: ['GET'])]
    public function bySlug(string $slug): Response
    {
        // ...
    }
}
```

### Fix 4: Handle Route Not Found

```php
// In config/routes.yaml
controllers:
    resource: ../src/Controller/
    type: attribute

# Custom 404 error handler
# src/Controller/ErrorController.php
class ErrorController extends AbstractController
{
    public function show404(): Response
    {
        return $this->render('error/404.html.twig', [
            'message' => 'Page not found',
        ], new Response('', Response::HTTP_NOT_FOUND));
    }
}
```

```php
// In ExceptionController or kernel
public function configureExceptions(): void
{
    $this->exceptionListener(function (\Throwable $e) {
        if ($e instanceof NotFoundHttpException) {
            return $this->render('error/404.html.twig');
        }
    });
}
```

## Examples

```yaml
# config/routes.yaml — YAML route definitions
app_blog_index:
    path: /blog
    controller: App\Controller\BlogController::index
    methods: [GET]
    requirements:
        _locale: en|fr|de

app_blog_show:
    path: /blog/{id}
    controller: App\Controller\BlogController::show
    methods: [GET]
    requirements:
        id: \d+
    defaults:
        _locale: en

app_blog_new:
    path: /blog/new
    controller: App\Controller\BlogController::new
    methods: [GET, POST]
    requirements:
        _method: GET|POST

app_product:
    resource: routes/product.yaml
    prefix: /products
```

## Related Errors

- [CodeIgniter Routing Error](/languages/php/codeigniter-routing-error)
- [Laravel Route Not Found](/languages/php/laravel-route-not-found)
- [Symfony Security Error](/languages/php/symfony-security-error)
- [PHP Parse Error](/languages/php/parse-error)
