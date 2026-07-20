---
title: "[Solution] PHP SYMFONY_HTTP_KERNEL_ERROR — Symfony HttpKernel Error"
description: "Fix PHP Symfony HttpKernel errors. Check controller, verify request, and handle response. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 127
---

# PHP SYMFONY_HTTP_KERNEL_ERROR — Symfony HttpKernel Error

The Symfony HttpKernel failed to process a request. This error occurs when the controller is not found, the request is malformed, the response is invalid, or the kernel event lifecycle encounters an exception.

## Common Causes

### Controller method does not exist

```php
<?php
class UserController extends AbstractController
{
    // Route references show() but method is named view()
    #[Route('/user/{id}', name: 'user_show')]
    public function view(int $id): Response
    {
        return $this->render('user/show.html.twig');
    }
}
// Symfony\Component\HttpKernel\Exception\NotFoundHttpException
?>
```

### Missing required controller argument

```php
<?php
class UserController extends AbstractController
{
    #[Route('/user/{id}', name: 'user_show')]
    public function show(int $id, EntityManagerInterface $em): Response
    {
        // $em must be autowirable
        // If EntityManagerInterface is not configured → ServiceNotFoundException
    }
}
?>
```

### Controller returns wrong type

```php
<?php
class UserController extends AbstractController
{
    #[Route('/user/{id}')]
    public function show(int $id): string // should return Response
    {
        return "User {$id}"; // TypeError: must return Response
    }
}
?>
```

### Request attribute missing

```php
<?php
class ShowController extends AbstractController
{
    #[Route('/show/{slug}')]
    public function show(Request $request, string $slug): Response
    {
        $extra = $request->attributes->get('extra_field'); // null if not set
    }
}
?>
```

### Exception in controller

```php
<?php
class ApiController extends AbstractController
{
    #[Route('/api/data')]
    public function data(): JsonResponse
    {
        $data = null;
        return $this->json($data['key']); // trying to access key of null
        // TypeError or Notice
    }
}
?>
```

## How to Fix

### Fix 1: Verify Controller Configuration

Ensure route names match controller method names.

```php
<?php
namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

class UserController extends AbstractController
{
    #[Route('/users', name: 'user_index', methods: ['GET'])]
    public function index(): Response
    {
        $users = $this->getDoctrine()->getRepository(User::class)->findAll();
        return $this->render('user/index.html.twig', [
            'users' => $users,
        ]);
    }

    #[Route('/users/{id}', name: 'user_show', methods: ['GET'], requirements: ['id' => '\d+'])]
    public function show(int $id): Response
    {
        $user = $this->getDoctrine()->getRepository(User::class)->find($id);
        if (!$user) {
            throw $this->createNotFoundException('User not found');
        }
        return $this->render('user/show.html.twig', [
            'user' => $user,
        ]);
    }

    #[Route('/users', name: 'user_create', methods: ['POST'])]
    public function create(Request $request): Response
    {
        $form = $this->createForm(UserType::class);
        $form->handleRequest($request);

        if ($form->isSubmitted() && $form->isValid()) {
            $user = $form->getData();
            $this->getDoctrine()->getManager()->flush();
            return $this->redirectToRoute('user_show', ['id' => $user->getId()]);
        }

        return $this->render('user/create.html.twig', [
            'form' => $form->createView(),
        ]);
    }
}
?>
```

### Fix 2: Return Proper Response Types

Always return a Response object from controllers.

```php
<?php
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Response;

class ApiController extends AbstractController
{
    #[Route('/api/users', methods: ['GET'])]
    public function index(): JsonResponse
    {
        $users = $this->getDoctrine()->getRepository(User::class)->findAll();
        return $this->json($users);
    }

    #[Route('/api/users/{id}', methods: ['GET'])]
    public function show(int $id): JsonResponse
    {
        $user = $this->getDoctrine()->getRepository(User::class)->find($id);
        if (!$user) {
            return $this->json(['error' => 'Not found'], 404);
        }
        return $this->json($user);
    }

    #[Route('/download/{id}')]
    public function download(int $id): Response
    {
        $file = $this->getParameter('kernel.project_dir') . '/public/files/report.pdf';
        return $this->file($file, 'report.pdf', ResponseHeaderBag::DISPOSITION_INLINE);
    }
}
?>
```

### Fix 3: Handle Request Properly

```php
<?php
use Symfony\Component\HttpFoundation\Request;

class OrderController extends AbstractController
{
    #[Route('/orders', name: 'order_create', methods: ['POST'])]
    public function create(Request $request): Response
    {
        // Get JSON content
        $data = json_decode($request->getContent(), true);
        if (json_last_error() !== JSON_ERROR_NONE) {
            return $this->json(['error' => 'Invalid JSON'], 400);
        }

        // Get form data
        $name = $request->request->get('name');

        // Get query parameters
        $page = $request->query->getInt('page', 1);

        // Get request headers
        $contentType = $request->headers->get('Content-Type');

        // Validate required fields
        if (empty($data['product_id'])) {
            return $this->json(['error' => 'product_id is required'], 422);
        }

        return $this->json(['success' => true]);
    }
}
?>
```

### Fix 4: Configure Kernel Error Handling

```php
<?php
namespace App\EventListener;

use Symfony\Component\HttpKernel\Event\ExceptionEvent;
use Symfony\Component\HttpFoundation\JsonResponse;

class KernelErrorListener
{
    public function onKernelException(ExceptionEvent $event): void
    {
        $exception = $event->getThrowable();
        $request = $event->getRequest();

        if ($request->getPathInfo() !== '/api/') {
            return; // only handle API errors
        }

        $response = new JsonResponse([
            'error' => $exception->getMessage(),
            'code' => $exception->getCode() ?: 500,
        ], 500);

        $event->setResponse($response);
    }
}

// services.yaml
App\EventListener\KernelErrorListener:
    tags:
        - { name: kernel.event_listener, event: kernel.exception }
?>
```

### Fix 5: Debug Kernel Errors

```php
<?php
// Check route matches
// php bin/console debug:router

// Check controller exists and is autowirable
// php bin/console debug:container App\Controller\UserController

// Check event listeners
// php bin/console debug:event-dispatcher kernel.exception

// In test environment
$client = static::createClient();
$client->request('GET', '/users/1');
$statusCode = $client->getResponse()->getStatusCode();
$content = $client->getResponse()->getContent();
echo "Status: {$statusCode}" . PHP_EOL;
echo $content;
?>
```

## Examples

### Complete API Controller

```php
<?php
namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/api/v1')]
class ApiUserController extends AbstractController
{
    #[Route('/users', methods: ['GET'])]
    public function index(Request $request): JsonResponse
    {
        $page = $request->query->getInt('page', 1);
        $limit = $request->query->getInt('limit', 20);

        $users = $this->getDoctrine()
            ->getRepository(User::class)
            ->findBy([], ['created_at' => 'DESC'], $limit, ($page - 1) * $limit);

        return $this->json([
            'data' => $users,
            'meta' => ['page' => $page, 'limit' => $limit],
        ]);
    }

    #[Route('/users/{id}', methods: ['GET'], requirements: ['id' => '\d+'])]
    public function show(int $id): JsonResponse
    {
        $user = $this->getDoctrine()->getRepository(User::class)->find($id);

        if (!$user) {
            return $this->json(['error' => 'User not found'], 404);
        }

        return $this->json($user);
    }
}
?>
```

## Related Errors

- [Symfony DependencyInjection Error]({{< relref "/languages/php/symfony-dependency-injection-error" >}})
- [Symfony EventDispatcher Error]({{< relref "/languages/php/symfony-event-dispatcher-error" >}})
- [Symfony Route Error]({{< relref "/languages/php/symfony-route-error" >}})
