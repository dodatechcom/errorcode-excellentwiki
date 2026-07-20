---
title: "[Solution] PHP SYMFONY_FORM_ERROR — Form Validation Failed"
description: "Fix PHP SYMFONY_FORM_ERROR by checking validation constraints, handling form errors, and using error collectors. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 110
---

# PHP SYMFONY_FORM_ERROR — Form Validation Failed

A Symfony form validation failed or the form configuration is incorrect. This error occurs when validation constraints are violated, form types are misconfigured, or form error handling is missing.

## Common Causes

```php
// Missing validation constraints in form type
class UserType extends AbstractType
{
    public function buildForm(FormBuilderInterface $builder, array $options): void
    {
        $builder
            ->add('name', TextType::class) // no constraints defined
            ->add('email', EmailType::class); // no NotBlank constraint
    }
}
```

```php
// Entity validation annotations missing
class User
{
    // No Assert annotations
    private $name;
    private $email;
}
```

```php
// Form submitted but errors not checked in controller
public function new(Request $request): Response
{
    $form = $this->createForm(UserType::class);
    $form->handleRequest($request);

    if ($form->isSubmitted()) {
        // missing $form->isValid() check
        $this->getDoctrine()->getManager()->flush();
    }
}
```

```php
// Wrong form type used for field
$builder->add('age', TextType::class); // should be IntegerType
```

```php
// Custom validation constraint class not found
use App\Validator\CustomConstraint; // class doesn't exist
```

## How to Fix

### Fix 1: Add Validation Constraints

Define constraints directly in the form type or entity.

```php
// Option A: Constraints in form type
use Symfony\Component\Form\Extension\Core\Type\TextType;
use Symfony\Component\Form\Extension\Core\Type\EmailType;
use Symfony\Component\Form\Extension\Core\Type\SubmitType;
use Symfony\Component\Validator\Constraints\NotBlank;
use Symfony\Component\Validator\Constraints\Length;
use Symfony\Component\Validator\Constraints\Email;

class UserType extends AbstractType
{
    public function buildForm(FormBuilderInterface $builder, array $options): void
    {
        $builder
            ->add('name', TextType::class, [
                'constraints' => [
                    new NotBlank(['message' => 'Name is required']),
                    new Length([
                        'min' => 2,
                        'max' => 50,
                        'minMessage' => 'Name must be at least {{ limit }} characters',
                        'maxMessage' => 'Name cannot exceed {{ limit }} characters',
                    ]),
                ],
            ])
            ->add('email', EmailType::class, [
                'constraints' => [
                    new NotBlank(['message' => 'Email is required']),
                    new Email(['message' => 'Please enter a valid email address']),
                ],
            ])
            ->add('save', SubmitType::class);
    }

    public function configureOptions(OptionsResolver $resolver): void
    {
        $resolver->setDefaults([
            'data_class' => User::class,
        ]);
    }
}
```

### Fix 2: Add Entity Validation Annotations

```php
// src/Entity/User.php
use Symfony\Component\Validator\Constraints as Assert;

/**
 * @ORM\Entity(repositoryClass=UserRepository::class)
 */
class User
{
    /**
     * @ORM\Id
     * @ORM\GeneratedValue
     * @ORM\Column(type="integer")
     */
    private $id;

    /**
     * @ORM\Column(type="string", length=255)
     * @Assert\NotBlank(message="Name is required")
     * @Assert\Length(
     *     min=2,
     *     max=255,
     *     minMessage="Name must be at least {{ limit }} characters",
     *     maxMessage="Name cannot exceed {{ limit }} characters"
     * )
     */
    private $name;

    /**
     * @ORM\Column(type="string", length=255, unique=true)
     * @Assert\NotBlank(message="Email is required")
     * @Assert\Email(message="Please enter a valid email address")
     */
    private $email;

    /**
     * @ORM\Column(type="string", length=20, nullable=true)
     * @Assert\Choice(
     *     choices={"ROLE_USER", "ROLE_ADMIN", "ROLE_EDITOR"},
     *     message="Invalid role selected"
     * )
     */
    private $role;
}
```

### Fix 3: Handle Form Errors in Controller

```php
// src/Controller/UserController.php
class UserController extends AbstractController
{
    #[Route('/user/new', name: 'user_new')]
    public function new(Request $request, EntityManagerInterface $em): Response
    {
        $user = new User();
        $form = $this->createForm(UserType::class, $user);
        $form->handleRequest($request);

        if ($form->isSubmitted() && $form->isValid()) {
            $em->persist($user);
            $em->flush();

            $this->addFlash('success', 'User created successfully');
            return $this->redirectToRoute('user_index');
        }

        // Get form errors for display
        $errors = $form->getErrors(true);

        return $this->render('user/new.html.twig', [
            'form' => $form->createView(),
            'errors' => $errors,
        ]);
    }
}
```

### Fix 4: Use Error Collector for Debugging

```php
// In Twig template
{{ form_start(form) }}
    {% for child in form.children %}
        <div class="form-group">
            {{ form_label(child) }}
            {{ form_widget(child) }}
            {% if child.vars.errors|length > 0 %}
                <div class="form-error">
                    {% for error in child.vars.errors %}
                        <span class="error">{{ error.message }}</span>
                    {% endfor %}
                </div>
            {% endif %}
        </div>
    {% endfor %}
    {{ form_widget(form.save) }}
{{ form_end(form) }}

{# Or render the entire form with errors #}
{{ form(form) }}
```

```php
// Debug form errors programmatically
$form = $this->createForm(UserType::class);
$form->submit($data);

if (!$form->isValid()) {
    $errors = $form->getErrors(true, false);
    foreach ($errors as $error) {
        dump($error->getMessage(), $error->getCause());
    }
}
```

## Examples

```php
// Complete form handling example
class OrderController extends AbstractController
{
    #[Route('/order', name: 'order_new')]
    public function new(Request $request, EntityManagerInterface $em): Response
    {
        $order = new Order();
        $form = $this->createForm(OrderType::class, $order);
        $form->handleRequest($request);

        if ($form->isSubmitted()) {
            if ($form->isValid()) {
                $em->persist($order);
                $em->flush();

                $this->addFlash('success', 'Order placed!');
                return $this->redirectToRoute('order_show', ['id' => $order->getId()]);
            }

            $this->addFlash('error', 'Please correct the errors below');
        }

        return $this->render('order/new.html.twig', [
            'form' => $form->createView(),
        ]);
    }
}
```

## Related Errors

- [Symfony Validator Error](/languages/php/symfony-validator-error)
- [Laravel Validation Error](/languages/php/laravel-validation-error)
- [Symfony Route Error](/languages/php/symfony-route-error)
- [PHP InvalidArgumentError](/languages/php/invalidargumentexception)
