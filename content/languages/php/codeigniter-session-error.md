---
title: "[Solution] PHP CODEIGNITER_SESSION_ERROR — Session Handling Failed"
description: "Fix PHP CODEIGNITER_SESSION_ERROR by configuring session driver, checking storage path, and resolving session conflicts. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 104
---

# PHP CODEIGNITER_SESSION_ERROR — Session Handling Failed

Session handling failed in CodeIgniter. This error occurs when the session driver is not configured properly, the storage path is not writable, or session data conflicts with other components.

## Common Causes

```php
// Session driver not configured or unavailable
$config['sess_driver'] = 'files'; // but session save path is not writable
$config['sess_save_path'] = '/tmp/ci_sessions/';
```

```php
// Session class not loaded
class Welcome extends CI_Controller {
    public function index() {
        $this->session->set_userdata('key', 'value'); // session library not loaded
    }
}
```

```php
// Session cookie conflict with other frameworks
// Same domain has Laravel/Symfony app with different session cookie name
$config['sess_cookie_name'] = 'ci_session'; // conflicts with other apps
```

```php
// Session data too large for storage
// Serializing large objects into session data
$this->session->set_userdata('large_data', $huge_array);
```

```php
// Missing session config values in config file
// sess_expiration, sess_expire_on_close not set
```

## How to Fix

### Fix 1: Configure Session Driver

Set up session configuration in `application/config/config.php`.

```php
// application/config/config.php
$config['sess_driver']            = 'database'; // or 'files', 'redis', 'memcached'
$config['sess_cookie_name']       = 'ci_session';
$config['sess_expiration']        = 7200; // 2 hours in seconds
$config['sess_expire_on_close']   = FALSE;
$config['sess_encrypt_cookie']    = TRUE;
$config['sess_use_database']      = TRUE; // required for database driver
$config['sess_table_name']        = 'ci_sessions';
$config['sess_match_ip']          = FALSE;
$config['sess_match_useragent']   = TRUE;
$config['sess_time_to_update']    = 300; // regenerate session ID every 5 min

// Session save path for file driver
$config['sess_save_path'] = FCPATH . 'cache/sessions/';
```

### Fix 2: Create Session Table for Database Driver

```sql
-- SQL for database session driver
CREATE TABLE `ci_sessions` (
    `id` varchar(128) NOT NULL,
    `ip_address` varchar(45) NOT NULL,
    `timestamp` int(10) unsigned NOT NULL DEFAULT 0,
    `data` blob NOT NULL,
    KEY `ci_sessions_timestamp` (`timestamp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- For CodeIgniter 3.1.13+
CREATE TABLE `ci_sessions` (
    `id` varchar(128) NOT NULL,
    `ip_address` varchar(45) NOT NULL,
    `timestamp` int(10) unsigned NOT NULL DEFAULT 0,
    `data` text NOT NULL,
    PRIMARY KEY (`id`),
    KEY `ci_sessions_timestamp` (`timestamp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

```php
// Ensure database config has session table
$db['default'] = [
    // ... other settings
    'sess_table_name' => 'ci_sessions',
];
```

### Fix 3: Ensure Session Directory Permissions

```php
// Verify session save path
$save_path = FCPATH . 'cache/sessions/';

if (!is_dir($save_path)) {
    mkdir($save_path, 0700, true);
}

if (!is_writable($save_path)) {
    chmod($save_path, 0700);
}

// Or use system temp directory
$config['sess_save_path'] = sys_get_temp_dir();

// Verify directory is accessible
if (!is_writable($config['sess_save_path'])) {
    log_message('error', 'Session save path not writable: ' . $config['sess_save_path']);
}
```

### Fix 4: Load Session Library Properly

```php
// Load in controller constructor
class Welcome extends CI_Controller {

    public function __construct() {
        parent::__construct();
        $this->load->library('session');
        $this->load->helper('url');
    }

    public function index() {
        // Set session data
        $this->session->set_userdata([
            'user_id'    => $user_id,
            'username'   => $username,
            'logged_in'  => TRUE,
        ]);

        // Get session data
        $user_id = $this->session->userdata('user_id');

        // Check if data exists
        if ($this->session->has_userdata('user_id')) {
            echo 'User is logged in';
        }

        // Remove specific data
        $this->session->unset_userdata('username');

        // Destroy entire session
        $this->session->sess_destroy();

        // Set flash data
        $this->session->set_flashdata('success', 'Login successful');
        echo $this->session->flashdata('success');
    }
}
```

## Examples

```php
// Session-based authentication example
class Auth extends CI_Controller {

    public function __construct() {
        parent::__construct();
        $this->load->library(['session', 'form_validation']);
        $this->load->model('user_model');
    }

    public function login() {
        $this->form_validation->set_rules('email', 'Email', 'required|valid_email');
        $this->form_validation->set_rules('password', 'Password', 'required');

        if ($this->form_validation->run() === FALSE) {
            $this->load->view('auth/login');
        } else {
            $email = $this->input->post('email');
            $password = $this->input->post('password');

            $user = $this->user_model->check_login($email, $password);

            if ($user) {
                $session_data = [
                    'user_id'   => $user['id'],
                    'email'     => $user['email'],
                    'logged_in' => TRUE,
                ];
                $this->session->set_userdata($session_data);
                redirect('dashboard');
            } else {
                $this->session->set_flashdata('error', 'Invalid credentials');
                redirect('auth/login');
            }
        }
    }

    public function logout() {
        $this->session->sess_destroy();
        redirect('auth/login');
    }

    public function check_login() {
        if (!$this->session->userdata('logged_in')) {
            redirect('auth/login');
        }
    }
}
```

## Related Errors

- [Session Start Error](/languages/php/session-start-error)
- [Session Save Path Error](/languages/php/session-save-path-error)
- [Laravel Token Mismatch](/languages/php/laravel-token-mismatch)
- [Symfony Security Error](/languages/php/symfony-security-error)
