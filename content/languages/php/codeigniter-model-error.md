---
title: "[Solution] PHP CODEIGNITER_MODEL_ERROR — Model Operation Failed"
description: "Fix PHP CODEIGNITER_MODEL_ERROR by verifying model config, checking database connection, and handling validation errors. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 102
---

# PHP CODEIGNITER_MODEL_ERROR — Model Operation Failed

A model operation failed in CodeIgniter. This error occurs when the model class cannot be loaded, the database table does not exist, or a CRUD operation encounters an invalid state.

## Common Causes

```php
// Model not loaded before use
class Blog extends CI_Controller {
    public function index() {
        // $this->post_model is undefined — forgot to load model
        $posts = $this->post_model->get_all();
    }
}
```

```php
// Model class name doesn't match file name
// File: application/models/post_model.php
// But class is named Posts (should be Post_model)
class Posts extends CI_Model { } // wrong
```

```php
// Table does not exist or wrong table name
class Post_model extends CI_Model {
    public function __construct() {
        parent::__construct();
        $this->table = 'posts'; // table 'posts' doesn't exist in database
    }
}
```

```php
// Missing parent::__construct() call
class Post_model extends CI_Model {
    public function __construct() {
        // parent::__construct(); // forgot this — $this->db will be null
    }
}
```

```php
// Validation failure not handled
public function create_post() {
    $this->form_validation->set_rules('title', 'Title', 'required');
    $this->form_validation->run(); // result not checked
    $this->db->insert('posts', $this->input->post()); // proceeds anyway
}
```

## How to Fix

### Fix 1: Verify Model Configuration

Ensure the model file name, class name, and constructor are correct.

```php
// application/models/Post_model.php
<?php
defined('BASEPATH') || exit('No direct script access allowed');

class Post_model extends CI_Model {

    protected $table = 'posts';
    protected $primaryKey = 'id';

    public function __construct() {
        parent::__construct(); // always call parent constructor
        $this->load->database();
    }

    public function get_all() {
        $query = $this->db->get($this->table);
        return $query->result_array();
    }

    public function get_by_id($id) {
        $query = $this->db->get_where($this->table, [$this->primaryKey => $id]);
        return $query->row_array();
    }

    public function create($data) {
        return $this->db->insert($this->table, $data);
    }

    public function update($id, $data) {
        $this->db->where($this->primaryKey, $id);
        return $this->db->update($this->table, $data);
    }

    public function delete($id) {
        $this->db->where($this->primaryKey, $id);
        return $this->db->delete($this->table);
    }

    public function count_all() {
        return $this->db->count_all($this->table);
    }
}
```

### Fix 2: Check Database Connection in Model

```php
// In model constructor
public function __construct() {
    parent::__construct();

    // Load database explicitly
    $this->load->database();

    // Verify connection
    if (!$this->db->conn_id) {
        log_message('error', 'Database connection failed in model');
    }

    // Check if table exists
    if (!$this->db->table_exists($this->table)) {
        log_message('error', "Table {$this->table} does not exist");
        throw new RuntimeException("Table {$this->table} not found");
    }
}

// Verify table schema
public function verify_table() {
    $fields = $this->db->list_fields($this->table);
    log_message('debug', 'Table fields: ' . implode(', ', $fields));
    return $fields;
}
```

### Fix 3: Handle Validation Errors

```php
// In model or controller
public function create_post() {
    $this->load->library('form_validation');

    $this->form_validation->set_rules('title', 'Title', 'required|max_length[255]');
    $this->form_validation->set_rules('content', 'Content', 'required|min_length[10]');
    $this->form_validation->set_rules('status', 'Status', 'in_list[draft,published]');

    if ($this->form_validation->run() === FALSE) {
        // Return validation errors
        return [
            'success' => false,
            'errors'  => $this->form_validation->error_array(),
        ];
    }

    $data = [
        'title'    => $this->input->post('title'),
        'content'  => $this->input->post('content'),
        'status'   => $this->input->post('status'),
        'created'  => date('Y-m-d H:i:s'),
    ];

    if ($this->db->insert('posts', $data)) {
        return [
            'success' => true,
            'id'      => $this->db->insert_id(),
        ];
    }

    return [
        'success' => false,
        'errors'  => ['Database error: ' . $this->db->error()['message']],
    ];
}
```

### Fix 4: Use Proper Model Loading

```php
// Load model in controller constructor
class Blog extends CI_Controller {

    public function __construct() {
        parent::__construct();
        $this->load->model('post_model');
        $this->load->model('user_model');
        // Load multiple models at once
        $this->load->model(['post_model', 'user_model', 'category_model']);
    }

    public function index() {
        $data['posts'] = $this->post_model->get_all();
        $this->load->view('blog/index', $data);
    }
}

// Load model in controller method
public function view($id) {
    $this->load->model('post_model');
    $post = $this->post_model->get_by_id($id);

    if (!$post) {
        show_404();
    }

    $this->load->view('blog/view', ['post' => $post]);
}
```

## Examples

```php
// Complete model with relationships
class Post_model extends CI_Model {

    protected $table = 'posts';

    public function __construct() {
        parent::__construct();
    }

    public function get_posts_with_users() {
        $this->db->select('posts.*, users.name as author_name');
        $this->db->from($this->table);
        $this->db->join('users', 'users.id = posts.user_id');
        $this->db->where('posts.status', 'published');
        $query = $this->db->get();
        return $query->result_array();
    }

    public function get_post_with_category($id) {
        $this->db->select('posts.*, categories.name as category_name');
        $this->db->from($this->table);
        $this->db->join('categories', 'categories.id = posts.category_id');
        $this->db->where('posts.id', $id);
        $query = $this->db->get();
        return $query->row_array();
    }

    public function get_paginated($limit, $offset) {
        $query = $this->db->get($this->table, $limit, $offset);
        return $query->result_array();
    }
}
```

## Related Errors

- [PDO Error](/languages/php/pdo-error)
- [Laravel Model Not Found](/languages/php/laravel-model-not-found)
- [Laravel Validation Error](/languages/php/laravel-validation-error)
- [Symfony Form Error](/languages/php/symfony-form-error)
