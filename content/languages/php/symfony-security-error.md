---
title: "[Solution] PHP SYMFONY_SECURITY_ERROR — Authentication/Authorization Failed"
description: "Fix PHP SYMFONY_SECURITY_ERROR by checking security config, verifying user providers, and handling access denied. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 112
---

# PHP SYMFONY_SECURITY_ERROR — Authentication/Authorization Failed

An authentication or authorization error occurred in Symfony Security. This happens when security configuration is incorrect, user providers are misconfigured, or access control rules deny the request.

## Common Causes

```yaml
# security.yaml — wrong firewall or provider config
security:
    providers:
        app_user_provider:
            entity:
                class: App\Entity\User
                property: email
                # missing id property
```

```php
// Controller action requires authentication but no login form configured
#[Route('/admin')]
class AdminController extends AbstractController
{
    #[IsGranted('ROLE_ADMIN')] // throws AccessDeniedHttpException
    public function dashboard(): Response
    {
        // ...
    }
}
```

```php
// User entity doesn't implement UserInterface
class User // missing implements UserInterface
{
    // ...
}
```

```php
// Wrong encoder configuration
// security.yaml
encoders:
    App\Entity\User: bcrypt // deprecated in Symfony 6
```

```php
// Access control path pattern doesn't match URL
access_control:
    - { path: ^/admin, roles: ROLE_ADMIN }
    # but admin URL is /admin-panel, doesn't match pattern
```

## How to Fix

### Fix 1: Configure Security Properly

```yaml
# config/packages/security.yaml
security:
    enable_authenticator_manager: true

    password_hashers:
        App\Entity\UserInterface: 'auto'

    providers:
        app_user_provider:
            entity:
                class: App\Entity\User
                property: email

    firewalls:
        dev:
            pattern: ^/(_(profiler|wdt))/
            security: false
        main:
            lazy: true
            provider: app_user_provider
            form_login:
                login_path: app_login
                check_path: app_login
                username_parameter: email
                password_parameter: password
                enable_csrf: true
                default_target_path: /dashboard
            logout:
                path: app_logout
                target: app_login

    role_hierarchy:
        ROLE_ADMIN: ROLE_USER
        ROLE_SUPER_ADMIN: ROLE_ADMIN

    access_control:
        - { path: ^/login, roles: PUBLIC_ACCESS }
        - { path: ^/register, roles: PUBLIC_ACCESS }
        - { path: ^/admin, roles: ROLE_ADMIN }
        - { path: ^/api, roles: ROLE_USER }
        - { path: ^/, roles: PUBLIC_ACCESS }
```

### Fix 2: Implement UserInterface Correctly

```php
// src/Entity/User.php
namespace App\Entity;

use App\Repository\UserRepository;
use Doctrine\ORM\Mapping as ORM;
use Symfony\Component\Security\Core\User\PasswordAuthenticatedUserInterface;
use Symfony\Component\Security\Core\User\UserInterface;

#[ORM\Entity(repositoryClass: UserRepository::class)]
#[ORM\Table(name: '`user`')]
class User implements UserInterface, PasswordAuthenticatedUserInterface
{
    #[ORM\Id]
    #[ORM\GeneratedValue]
    #[ORM\Column(type: 'integer')]
    private $id;

    #[ORM\Column(type: 'string', length: 180, unique: true)]
    private $email;

    #[ORM\Column(type: 'json')]
    private $roles = [];

    #[ORM\Column(type: 'string')]
    private $password;

    public function getId(): ?int
    {
        return $this->id;
    }

    public function getUserIdentifier(): string
    {
        return (string) $this->email;
    }

    public function getRoles(): array
    {
        $roles = $this->roles;
        $roles[] = 'ROLE_USER';
        return array_unique($roles);
    }

    public function setRoles(array $roles): self
    {
        $this->roles = $roles;
        return $this;
    }

    public function getPassword(): string
    {
        return $this->password;
    }

    public function setPassword(string $password): self
    {
        $this->password = $password;
        return $this;
    }

    public function eraseCredentials(): void
    {
        // Clear temporary, sensible data
    }
}
```

### Fix 3: Handle Access Denied

```php
// In controller
use Symfony\Component\Security\Core\Exception\AccessDeniedException;

#[Route('/admin/users')]
#[IsGranted('ROLE_ADMIN')]
class AdminUserController extends AbstractController
{
    public function index(): Response
    {
        // Manual access check
        if (!$this->isGranted('ROLE_SUPER_ADMIN')) {
            throw $this->createAccessDeniedException('Super admin access required');
        }

        return $this->render('admin/users.html.twig');
    }
}

// Twig template access check
{# templates/admin/dashboard.html.twig #}
{% if is_granted('ROLE_ADMIN') %}
    <p>Welcome, admin!</p>
{% else %}
    <p>Access denied.</p>
{% endif %}

// In security controller
class SecurityController extends AbstractController
{
    #[Route('/login', name: 'app_login')]
    public function login(AuthenticationUtils $authenticationUtils): Response
    {
        if ($this->getUser()) {
            return $this->redirectToRoute('dashboard');
        }

        $error = $authenticationUtils->getLastAuthenticationError();
        $lastUsername = $authenticationUtils->getLastUsername();

        return $this->render('security/login.html.twig', [
            'last_username' => $lastUsername,
            'error' => $error,
        ]);
    }

    #[Route('/logout', name: 'app_logout')]
    public function logout(): void
    {
        // Handled by security firewall
    }
}
```

### Fix 4: Configure User Providers

```yaml
# Custom user provider
security:
    providers:
        app_user_provider:
            id: App\Security\UserProvider

        # Database provider
        database_provider:
            entity:
                class: App\Entity\User
                property: email

        # In-memory provider
        in_memory:
            memory:
                users:
                    admin:
                        password: '$2y$12$...'
                        roles: ['ROLE_ADMIN']
```

```php
// Custom user provider
class UserProvider implements UserProviderInterface
{
    public function loadUserByIdentifier(string $identifier): UserInterface
    {
        $user = $this->entityManager->getRepository(User::class)
            ->findOneBy(['email' => $identifier]);

        if (!$user) {
            throw new UserNotFoundException();
        }

        return $user;
    }

    public function refreshUser(UserInterface $user): UserInterface
    {
        if (!$user instanceof User) {
            throw new UnsupportedUserException();
        }

        return $user;
    }

    public function supportsClass(string $class): bool
    {
        return User::class === $class;
    }
}
```

## Examples

```php
// Full security setup example
class DashboardController extends AbstractController
{
    #[Route('/dashboard', name: 'dashboard')]
    public function index(): Response
    {
        // Check authentication
        if (!$this->isGranted('IS_AUTHENTICATED_FULLY')) {
            return $this->redirectToRoute('app_login');
        }

        $user = $this->getUser();

        return $this->render('dashboard/index.html.twig', [
            'user' => $user,
            'is_admin' => $this->isGranted('ROLE_ADMIN'),
        ]);
    }

    #[Route('/admin/settings', name: 'admin_settings')]
    #[IsGranted('ROLE_ADMIN')]
    public function adminSettings(): Response
    {
        return $this->render('admin/settings.html.twig');
    }
}
```

## Related Errors

- [Symfony Form Error](/languages/php/symfony-form-error)
- [Symfony Route Error](/languages/php/symfony-route-error)
- [Laravel Token Mismatch](/languages/php/laravel-token-mismatch)
- [Session Start Error](/languages/php/session-start-error)
