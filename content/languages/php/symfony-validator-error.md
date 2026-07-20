---
title: "[Solution] PHP SYMFONY_VALIDATOR_ERROR — Validation Constraint Violation"
description: "Fix PHP SYMFONY_VALIDATOR_ERROR by checking constraint definitions, handling validation groups, and using proper assertions. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 113
---

# PHP SYMFONY_VALIDATOR_ERROR — Validation Constraint Violation

A validation constraint violation occurred in Symfony. This error happens when validation constraints are defined incorrectly, the validator is misconfigured, or constraint options are invalid.

## Common Causes

```php
// Invalid constraint option
use Symfony\Component\Validator\Constraints as Assert;

class User
{
    /**
     * @Assert\Length(min="abc") // must be integer, not string
     */
    private $name;
}
```

```php
// Missing use statement for constraint
class Product
{
    /**
     * @Assert\NotBlank() // Assert not imported
     */
    private $title;
}
```

```php
// Wrong constraint class for property type
/**
 * @Assert\Email() // applied to integer field
 */
private $age;
```

```php
// Validation group doesn't exist
$validator->validate($user, ['nonexistent_group']);
```

```php
// Custom constraint class not found
use App\Validator\UniqueEmail; // class doesn't exist or namespace wrong
```

## How to Fix

### Fix 1: Check Constraint Definitions

Use proper constraint syntax and options.

```php
// src/Entity/User.php
use Symfony\Component\Validator\Constraints as Assert;

class User
{
    /**
     * @Assert\NotBlank(message="Name is required")
     * @Assert\Length(
     *     min=2,
     *     max=100,
     *     minMessage="Name must be at least {{ limit }} characters",
     *     maxMessage="Name cannot exceed {{ limit }} characters"
     * )
     */
    private $name;

    /**
     * @Assert\NotBlank
     * @Assert\Email(
     *     mode="strict",
     *     message="The email '{{ value }}' is not a valid email address"
     * )
     */
    private $email;

    /**
     * @Assert\Range(
     *     min=18,
     *     max=120,
     *     minMessage="You must be at least {{ limit }} years old",
     *     maxMessage="You cannot be older than {{ limit }} years"
     * )
     */
    private $age;

    /**
     * @Assert\Positive
     */
    private $price;

    /**
     * @Assert\Count(
     *     min=1,
     *     max=5,
     *     minMessage="At least one item is required",
     *     maxMessage="Cannot have more than {{ limit }} items"
     * )
     */
    private $tags;

    /**
     * @Assert\Valid
     */
    private $address; // validates nested object
}
```

### Fix 2: Handle Validation Groups

```php
// Define validation groups
use Symfony\Component\Validator\Constraints as Assert;

/**
 * @Assert\GroupSequence({"Default", "strict"})
 */
class User
{
    /**
     * @Assert\NotBlank(groups={"registration", "profile"})
     */
    private $name;

    /**
     * @Assert\NotBlank(groups={"registration"})
     * @Assert\Email(groups={"registration"})
     */
    private $email;

    /**
     * @Assert\NotBlank(groups={"profile"})
     */
    private $bio;

    /**
     * @Assert\IsTrue(
     *     message="You must agree to the terms",
     *     groups={"registration"}
     * )
     */
    private $agreeTerms;
}

// Validate with specific groups
$validator = $this->get('validator');

$errors = $validator->validate($user, ['registration']);
// Only validates fields with groups={"registration"}

$errors = $validator->validate($user, ['Default', 'strict']);
// Uses group sequence

if (count($errors) > 0) {
    $errorString = (string) $errors;
}
```

### Fix 3: Validate Programmatically

```php
use Symfony\Component\Validator\Validator\Constraints as Assert;
use Symfony\Component\Validator\Validation;

// Standalone validation
$validator = Validation::createValidator();

// Validate a scalar value
$violations = $validator->validate(
    'hello@example.com',
    [
        new Assert\NotBlank(),
        new Assert\Email(),
    ]
);

if (count($violations) > 0) {
    foreach ($violations as $violation) {
        echo $violation->getMessage() . "\n";
    }
}

// Validate an object
$violations = $validator->validate($user);

if (count($violations) > 0) {
    $errors = [];
    foreach ($violations as $violation) {
        $errors[$violation->getPropertyPath()][] = $violation->getMessage();
    }
    return new JsonResponse(['errors' => $errors], 422);
}
```

### Fix 4: Custom Validation Constraints

```php
// src/Validator/UniqueEmail.php
namespace App\Validator;

use Symfony\Component\Validator\Constraint;

/**
 * @Annotation
 */
class UniqueEmail extends Constraint
{
    public string $message = 'The email "{{ value }}" is already registered.';
    public string $service = 'app.validator.unique_email';

    public function validatedBy(): string
    {
        return static::class . 'Validator';
    }
}

// src/Validator/UniqueEmailValidator.php
namespace App\Validator;

use App\Repository\UserRepository;
use Symfony\Component\Validator\Constraint;
use Symfony\Component\Validator\ConstraintValidator;

class UniqueEmailValidator extends ConstraintValidator
{
    public function __construct(private UserRepository $userRepository)
    {
    }

    public function validate(mixed $value, Constraint $constraint): void
    {
        if (!$constraint instanceof UniqueEmail) {
            throw new UnexpectedTypeException($constraint, UniqueEmail::class);
        }

        if (null === $value || '' === $value) {
            return;
        }

        $existingUser = $this->userRepository->findOneBy(['email' => $value]);

        if ($existingUser) {
            $this->context->buildViolation($constraint->message)
                ->setParameter('{{ value }}', $value)
                ->addViolation();
        }
    }
}
```

## Examples

```php
// Full validation example
class RegistrationController extends AbstractController
{
    #[Route('/register', name: 'register')]
    public function register(Request $request, ValidatorInterface $validator): Response
    {
        $user = new User();
        $form = $this->createForm(RegistrationType::class, $user);
        $form->handleRequest($request);

        if ($form->isSubmitted()) {
            $errors = $validator->validate($user, ['registration']);

            if (count($errors) > 0) {
                $errorMessages = [];
                foreach ($errors as $error) {
                    $errorMessages[] = $error->getMessage();
                }

                $this->addFlash('error', implode(' ', $errorMessages));
            } else {
                // Proceed with registration
                // ...
            }
        }

        return $this->render('registration/register.html.twig', [
            'form' => $form->createView(),
        ]);
    }
}
```

## Related Errors

- [Symfony Form Error](/languages/php/symfony-form-error)
- [Laravel Validation Error](/languages/php/laravel-validation-error)
- [InvalidArgumentError](/languages/php/invalidargumentexception)
- [Symfony Serializer Error](/languages/php/symfony-serializer-error)
