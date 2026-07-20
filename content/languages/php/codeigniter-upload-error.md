---
title: "[Solution] PHP CODEIGNITER_UPLOAD_ERROR — File Upload Failed"
description: "Fix PHP CODEIGNITER_UPLOAD_ERROR by checking upload config, directory permissions, file types, and size limits. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 103
---

# PHP CODEIGNITER_UPLOAD_ERROR — File Upload Failed

A file upload operation failed in CodeIgniter. This error occurs when the upload configuration is incorrect, the target directory is not writable, the file type is not allowed, or the file exceeds size limits.

## Common Causes

```php
// Upload directory does not exist or is not writable
$config['upload_path'] = './uploads/documents/'; // directory doesn't exist
$config['allowed_types'] = 'gif|jpg|png|pdf';
```

```php
// Wrong allowed_types format
$config['allowed_types'] = 'gif,jpg,png'; // should use pipe separator
```

```php
// File exceeds max_size limit
$config['max_size'] = 2048; // 2MB, but uploading 5MB file
```

```php
// Missing form field name
echo form_upload('file'); // form field named 'file'
$this->upload->do_upload('image'); // expecting 'image' — mismatch
```

```php
// File extension not in allowed list
$config['allowed_types'] = 'gif|jpg|png';
// User uploads a .webp or .svg file
```

## How to Fix

### Fix 1: Check Upload Configuration

Configure upload settings properly in controller or config.

```php
// application/config/upload.php or inline in controller
$config['upload_path']          = FCPATH . 'uploads/images/';
$config['allowed_types']        = 'gif|jpg|jpeg|png|webp|pdf|doc|docx';
$config['max_size']             = 5120; // 5MB in KB
$config['max_width']            = 2048;
$config['max_height']           = 2048;
$config['encrypt_name']         = TRUE; // randomize file name
$config['remove_spaces']        = TRUE;
$config['xss_clean']            = TRUE;
$config['file_name']            = ''; // empty = use original name

$this->load->library('upload', $config);

if (!$this->upload->do_upload('userfile')) {
    $error = array('error' => $this->upload->display_errors());
    $this->load->view('upload_form', $error);
} else {
    $data = $this->upload->data();
    echo 'File uploaded: ' . $data['file_name'];
}
```

### Fix 2: Verify Directory Permissions

```php
// Create upload directory structure
$upload_path = FCPATH . 'uploads/images/';

if (!is_dir($upload_path)) {
    mkdir($upload_path, 0755, true);
}

// Check and fix permissions
if (!is_writable($upload_path)) {
    chmod($upload_path, 0755);
    log_message('error', "Upload path not writable: {$upload_path}");
}

// Verify path exists before upload
if (!file_exists($upload_path) || !is_dir($upload_path)) {
    show_error('Upload directory does not exist: ' . $upload_path);
}

// Alternative: use absolute path
$config['upload_path'] = '/var/www/html/uploads/images/';
```

### Fix 3: Validate File Type

```php
// Extended allowed types with MIME mapping
$config['allowed_types'] = 'gif|jpg|jpeg|png|webp|pdf|doc|docx|xls|xlsx';

// Add MIME type validation
$config['mime_detect'] = 'fileinfo'; // or 'finfo' for PHP 5.3+

$this->load->library('upload', $config);

if (!$this->upload->do_upload('userfile')) {
    $error = $this->upload->display_errors();

    // Common errors:
    // "The filetype you are attempting to upload is not allowed."
    // "The filetype you are attempting to upload is not permitted for security reasons."

    $this->session->set_flashdata('error', $error);
    redirect('upload');
} else {
    $upload_data = $this->upload->data();

    // Additional validation after upload
    $allowed_mimes = ['image/jpeg', 'image/png', 'image/gif', 'application/pdf'];

    if (!in_array($upload_data['file_type'], $allowed_mimes)) {
        unlink($upload_data['full_path']); // remove invalid file
        show_error('Invalid file type detected');
    }
}
```

### Fix 4: Handle Size Limits

```php
// Configure size limits
$config['max_size'] = 10240; // 10MB

// Validate before upload
$file = $_FILES['userfile'];

if ($file['size'] > $config['max_size'] * 1024) {
    $error = 'File is too large. Maximum size is ' . ($config['max_size'] / 1024) . 'MB.';
    $this->session->set_flashdata('error', $error);
    redirect('upload');
}

// Multiple file upload
$files = $this->upload->do_upload('userfile');
if (!$files) {
    $errors = $this->upload->display_errors();
}

// Upload multiple files at once
$files = $_FILES;
$count = count($_FILES['userfile']['name']);

for ($i = 0; $i < $count; $i++) {
    $_FILES['userfile']['name']     = $files['userfile']['name'][$i];
    $_FILES['userfile']['type']     = $files['userfile']['type'][$i];
    $_FILES['userfile']['tmp_name'] = $files['userfile']['tmp_name'][$i];
    $_FILES['userfile']['error']    = $files['userfile']['error'][$i];
    $_FILES['userfile']['size']     = $files['userfile']['size'][$i];

    if (!$this->upload->do_upload('userfile')) {
        $errors[] = $this->upload->display_errors();
    } else {
        $uploads[] = $this->upload->data();
    }
}
```

## Examples

```php
// Complete upload controller
class Upload extends CI_Controller {

    public function __construct() {
        parent::__construct();
        $this->load->helper(['form', 'url']);
        $this->load->library(['upload', 'session']);
    }

    public function index() {
        $this->load->view('upload_form');
    }

    public function do_upload() {
        $config['upload_path']   = FCPATH . 'uploads/';
        $config['allowed_types'] = 'gif|jpg|jpeg|png|pdf';
        $config['max_size']      = 5120;
        $config['encrypt_name']  = TRUE;

        $this->upload->initialize($config);

        if (!$this->upload->do_upload('userfile')) {
            $data = [
                'error' => $this->upload->display_errors(),
            ];
            $this->load->view('upload_form', $data);
        } else {
            $data = [
                'upload_data' => $this->upload->data(),
                'success'     => 'File uploaded successfully',
            ];
            $this->load->view('upload_success', $data);
        }
    }
}
```

## Related Errors

- [Upload Error](/languages/php/upload-error)
- [File Permission Error](/languages/php/file-permission-error)
- [File Write Error](/languages/php/file-write-error)
- [Laravel Validation Error](/languages/php/laravel-validation-error)
