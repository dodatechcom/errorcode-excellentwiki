---
title: "[Solution] PHP CODEIGNITER_ROUTING_ERROR — Route Not Found"
description: "Fix PHP CODEIGNITER_ROUTING_ERROR by checking route definitions, controller methods, and 404 handling. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 101
---

# PHP CODEIGNITER_ROUTING_ERROR — Route Not Found

A route was not found or is invalid in CodeIgniter. This happens when the requested URL does not match any defined route, the controller or method does not exist, or the route configuration is incorrect.

## Common Causes

```php
// Incorrect route definition in application/config/routes.php
$route['user/profile'] = 'users/profile'; // missing controller prefix issue
$route['blog/(:any)'] = 'blog/view/$1'; // missing closing parenthesis
```

```php
// Controller method does not exist
// URL: /users/delete
// But Users controller has no delete() method
class Users extends CI_Controller {
    public function index() { }
    public function view($id) { }
    // no delete() method defined
}
```

```php
// Case sensitivity issue in controller/method names
// URL: /Users/View/1 but method is named view()
class Users extends CI_Controller {
    public function View($id) { } // Capital V may cause issues on Linux
}
```

```php
// Wrong default controller
$route['default_controller'] = 'welcome'; // controller 'welcome' doesn't exist
```

```php
// Missing controller file
// application/controllers/User.php expected but file is named users.php
```

## How to Fix

### Fix 1: Check Route Definition

Verify route patterns in `application/config/routes.php`.

```php
// application/config/routes.php
$route['default_controller'] = 'home';
$route['404_override'] = 'errors/show_404';

// Simple routes
$route['about'] = 'pages/about';
$route['contact'] = 'pages/contact';

// Routes with parameters
$route['blog/(:any)'] = 'blog/view/$1';
$route['blog/(:num)'] = 'blog/view/$1';

// Routes with multiple parameters
$route['user/(:num)/post/(:num)'] = 'user/post/$1/$2';

// Custom regex routes
$route['news/([a-z-]+)'] = 'news/view/$1';
$route['product/([0-9]+)/([a-z-]+)'] = 'catalog/view/$1/$2';

// Redirect routes
$route['old-page'] = 'new-page';
$route['old-url'] = 'new-url';
```

### Fix 2: Verify Controller and Method Existence

Ensure the controller file and methods are properly defined.

```php
// application/controllers/User.php
<?php
defined('BASEPATH') || exit('No direct script access allowed');

class User extends CI_Controller {

    public function __construct() {
        parent::__construct();
        $this->load->model('user_model');
    }

    // GET /user/index or /user
    public function index() {
        $data['users'] = $this->user_model->get_all_users();
        $this->load->view('user/index', $data);
    }

    // GET /user/view/5
    public function view($id = null) {
        if ($id === null) {
            show_404();
        }
        $data['user'] = $this->user_model->get_user($id);
        $this->load->view('user/view', $data);
    }

    // GET /user/create
    public function create() {
        $this->load->view('user/create');
    }

    // POST /user/store
    public function store() {
        $this->user_model->create_user();
        redirect('user');
    }

    // GET /user/edit/5
    public function edit($id) {
        $data['user'] = $this->user_model->get_user($id);
        $this->load->view('user/edit', $data);
    }

    // POST /user/update/5
    public function update($id) {
        $this->user_model->update_user($id);
        redirect('user/view/' . $id);
    }

    // GET /user/delete/5
    public function delete($id) {
        $this->user_model->delete_user($id);
        redirect('user');
    }
}
```

### Fix 3: Handle 404 Errors Properly

Configure a custom 404 error handler.

```php
// application/config/routes.php
$route['404_override'] = 'errors/show_404';

// application/controllers/Errors.php
class Errors extends CI_Controller {

    public function show_404() {
        $data = [
            'title'  => '404 Page Not Found',
            'error'  => $this->uri->uri_string(),
            'status' => 404,
        ];

        $this->output->set_status_header(404);
        $this->load->view('errors/404', $data);
    }
}

// In controller methods, trigger 404 manually
public function view($id) {
    $user = $this->user_model->get_user($id);

    if (!$user) {
        show_404(); // triggers 404 error page
    }

    $data['user'] = $user;
    $this->load->view('user/view', $data);
}
```

### Fix 4: Enable Route Debugging

```php
// application/config/config.php
$config['permitted_uri_chars'] = 'a-z 0-9~%.:_\-';
$config['enable_query_strings'] = TRUE; // if using query strings

// Debug routes in controllers
public function debug_routes() {
    echo '<pre>';
    print_r($this->router->routes);
    echo '</pre>';
    echo 'Current route: ' . $this->router->fetch_class() . '/' . $this->router->fetch_method();
}

// Check available routes
$this->load->helper('url');
echo site_url('user/view/5'); // verify URL generation
```

## Examples

```php
// application/config/routes.php — complete example
$route['default_controller'] = 'home';
$route['404_override'] = 'errors/show_404';
$route['translate_uri_dashes'] = FALSE;

// Auth routes
$route['login'] = 'auth/login';
$route['logout'] = 'auth/logout';
$route['register'] = 'auth/register';

// API routes
$route['api/users'] = 'api/user/index';
$route['api/users/(:num)'] = 'api/user/view/$1';
$route['api/posts'] = 'api/post/index';
$route['api/posts/(:num)'] = 'api/post/view/$1';

// Admin routes
$route['admin/(:any)'] = 'admin/dashboard/$1';
$route['admin/users/(:any)'] = 'admin/users/$1';
```

## Related Errors

- [Symfony Routing Error](/languages/php/symfony-route-error)
- [Laravel Route Not Found](/languages/php/laravel-route-not-found)
- [PHP Parse Error](/languages/php/parse-error)
- [Twig Error](/languages/php/twig-error)
