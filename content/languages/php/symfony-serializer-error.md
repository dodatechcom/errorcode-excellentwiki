---
title: "[Solution] PHP SYMFONY_SERIALIZER_ERROR — Serialization Failed"
description: "Fix PHP SYMFONY_SERIALIZER_ERROR by checking normalizer config, verifying class metadata, and handling circular references. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 114
---

# PHP SYMFONY_SERIALIZER_ERROR — Serialization Failed

A serialization or deserialization error occurred in Symfony. This happens when normalizer configuration is wrong, class metadata is invalid, or circular references cause infinite loops.

## Common Causes

```php
// Circular reference in entity relationship
class User
{
    #[ORM\OneToMany(mappedBy: 'author', targetEntity: Post::class)]
    private $posts;
}

class Post
{
    #[ORM\ManyToOne(targetEntity: User::class)]
    private $author; // User -> Post -> User -> infinite loop
}
```

```php
// Missing normalizer for custom type
$serializer->serialize($myCustomObject, 'json');
// No normalizer registered for MyCustomObject
```

```php
// Wrong serialization format
$serializer->serialize($data, 'xml'); // object has properties that can't be XML-encoded
```

```php
// Property not accessible (private, no getter)
class User
{
    private $name; // no getter, serializer can't access it
}
```

```php
// Deserialization type mismatch
$json = '{"name": "John", "age": "thirty"}';
$serializer->deserialize($json, User::class, 'json'); // age expects int
```

## How to Fix

### Fix 1: Configure Normalizers

```php
// config/services.yaml
services:
    App\Normalizer\DateTimeNormalizer:
        tags: ['serializer.normalizer']

    App\Normalizer\EntityNormalizer:
        tags: ['serializer.normalizer']
        arguments:
            - '@doctrine.orm.entity_manager'
```

```php
// Custom normalizer for DateTime
namespace App\Normalizer;

use Symfony\Component\Serializer\Normalizer\NormalizerInterface;
use Symfony\Component\Serializer\Normalizer\DenormalizerInterface;

class DateTimeNormalizer implements NormalizerInterface, DenormalizerInterface
{
    public function normalize(mixed $object, ?string $format = null, array $context = []): array
    {
        return [
            'date' => $object->format('Y-m-d'),
            'time' => $object->format('H:i:s'),
            'timestamp' => $object->getTimestamp(),
        ];
    }

    public function denormalize(mixed $data, string $type, ?string $format = null, array $context = []): \DateTime
    {
        if (isset($data['date'])) {
            return new \DateTime($data['date']);
        }

        return new \DateTime();
    }

    public function supportsNormalization(mixed $data, ?string $format = null): bool
    {
        return $data instanceof \DateTime;
    }

    public function supportsDenormalization(mixed $data, string $type, ?string $format = null): bool
    {
        return $type === \DateTime::class;
    }
}
```

### Fix 2: Handle Circular References

```php
// Option A: Use Serializer groups to break cycles
use Symfony\Component\Serializer\Annotation\Groups;

class User
{
    #[Groups(['user:read'])]
    private $name;

    #[Groups(['user:read'])]
    #[ORM\OneToMany(mappedBy: 'author', targetEntity: Post::class)]
    private $posts;
}

class Post
{
    #[Groups(['user:read'])]
    private $title;

    #[Groups(['user:read'])]
    #[ORM\ManyToOne(targetEntity: User::class)]
    private $author;
}

// Use groups to control what gets serialized
$serializer->serialize($user, 'json', ['groups' => ['user:read']]);
```

```php
// Option B: Use MaxDepth
use Symfony\Component\Serializer\Annotation\MaxDepth;

class User
{
    #[MaxDepth(2)]
    #[ORM\OneToMany(mappedBy: 'author', targetEntity: Post::class)]
    private $posts;
}

$serializer->serialize($user, 'json', [
    'circular_reference_handler' => function (mixed $object) {
        return $object->getId();
    },
]);
```

```php
// Option C: Use Serializer configuration
$normalizer = new ObjectNormalizer();
$normalizer->setCircularReferenceHandler(function (mixed $object) {
    return $object->getId();
});

$serializer = new Serializer([$normalizer]);
```

### Fix 3: Add Getters for Private Properties

```php
class User
{
    private string $name;
    private int $age;
    private \DateTime $createdAt;

    // Add getters for serialization
    public function getName(): string
    {
        return $this->name;
    }

    public function getAge(): int
    {
        return $this->age;
    }

    public function getCreatedAt(): \DateTime
    {
        return $this->createdAt;
    }

    // Or use #[Accessor] attribute
    use \Symfony\Component\PropertyAccess\PropertyAccess;

    public function __serialize(): array
    {
        return [
            'name' => $this->name,
            'age' => $this->age,
        ];
    }

    public function __unserialize(array $data): void
    {
        $this->name = $data['name'];
        $this->age = $data['age'];
    }
}
```

### Fix 4: Configure Serializer Metadata

```php
// config/serialization.yaml or attribute-based config
use Symfony\Component\Serializer\Annotation\SerializedPath;

class User
{
    #[SerializedPath('[user][name]')]
    private $name;

    #[SerializedPath('[user][email]')]
    private $email;

    #[Groups(['admin:read'])]
    #[SerializedPath('[admin][roles]')]
    private $roles;
}

// Register metadata factory
// config/services.yaml
services:
    Symfony\Component\Serializer\Mapping\Factory\ClassMetadataFactoryInterface:
        class: Symfony\Component\Serializer\Mapping\Factory\ClassMetadataFactory
        arguments:
            - '@Symfony\Component\Serializer\Mapping\Loader\AnnotationLoader'

    Symfony\Component\Serializer\Normalizer\ObjectNormalizer:
        arguments:
            - '@Symfony\Component\Serializer\Mapping\Factory\ClassMetadataFactoryInterface'
```

## Examples

```php
// Complete serialization example
class ApiController extends AbstractController
{
    #[Route('/api/users', name: 'api_users', methods: ['GET'])]
    public function getUsers(SerializerInterface $serializer): JsonResponse
    {
        $users = $this->getDoctrine()->getRepository(User::class)->findAll();

        $json = $serializer->serialize($users, 'json', [
            'groups' => ['user:read'],
            'circular_reference_handler' => function (mixed $object) {
                return $object->getId();
            },
        ]);

        return new JsonResponse(json_decode($json, true));
    }

    #[Route('/api/users', name: 'api_users_create', methods: ['POST'])]
    public function createUser(Request $request, SerializerInterface $serializer): JsonResponse
    {
        $json = $request->getContent();

        try {
            $user = $serializer->deserialize($json, User::class, 'json', [
                'groups' => ['user:write'],
            ]);

            $errors = $this->get('validator')->validate($user);
            if (count($errors) > 0) {
                return $this->json(['errors' => (string) $errors], 422);
            }

            $em = $this->getDoctrine()->getManager();
            $em->persist($user);
            $em->flush();

            return $this->json($user, 201, [], ['groups' => ['user:read']]);
        } catch (\Throwable $e) {
            return $this->json(['error' => $e->getMessage()], 400);
        }
    }
}
```

## Related Errors

- [Symfony Validator Error](/languages/php/symfony-validator-error)
- [Json Encode Error](/languages/php/json-encode-error)
- [Json Decode Error](/languages/php/json-decode-error)
- [Doctrine Error](/languages/php/doctrine-error)
