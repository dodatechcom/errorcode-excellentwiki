---
title: "[Solution] PHP SYMFONY_CONSOLE_ERROR — Symfony Console Command Error"
description: "Fix PHP Symfony Console command errors. Check command definition, verify input/output, and handle exceptions. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 126
---

# PHP SYMFONY_CONSOLE_ERROR — Symfony Console Command Error

A Symfony Console command failed during execution. This error occurs when command definitions are invalid, input arguments are missing, output formatting fails, or the command throws an unhandled exception.

## Common Causes

### Missing required argument

```php
<?php
class CreateUserCommand extends Command
{
    protected static $defaultName = 'app:create-user';

    protected function configure(): void
    {
        $this
            ->addArgument('email', InputArgument::REQUIRED)
            ->addArgument('name', InputArgument::REQUIRED);
    }

    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $email = $input->getArgument('email');
        // php bin/console app:create-user (no arguments)
        // RuntimeException: Not enough arguments
    }
}
?>
```

### Wrong input type

```php
<?php
protected function execute(InputInterface $input, OutputInterface $output): int
{
    $limit = $input->getOption('limit'); // should be getArgument
    // Returns null instead of the value
}
?>
```

### Command not registered

```php
<?php
class MyCommand extends Command
{
    protected static $defaultName = 'app:my-command';
}

// Command class not in src/Command/ or not autoconfigured
// LogicException: The command defined in "MyCommand" cannot have an empty name
?>
```

### Invalid return type

```php
<?php
protected function execute(InputInterface $input, OutputInterface $output): int
{
    $output->writeln('Done');
    return 'success'; // should be int, not string
    // TypeError: Return value must be of type int
}
?>
```

### Table formatting error

```php
<?php
$table = $output->getTableStyle();
$table = new Table($output);
$table->setHeaders(['Name', 'Email']);
$table->addRow(['Alice', 'alice@example.com']);
$table->render();
// Throws if output is not a console output instance
?>
```

## How to Fix

### Fix 1: Define Arguments and Options Correctly

```php
<?php
namespace App\Command;

use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputArgument;
use Symfony\Component\Console\Input\InputOption;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;

class CreateUserCommand extends Command
{
    protected static $defaultName = 'app:create-user';

    protected function configure(): void
    {
        $this
            ->setDescription('Create a new user')
            ->addArgument('email', InputArgument::REQUIRED, 'User email')
            ->addArgument('name', InputArgument::REQUIRED, 'User name')
            ->addOption('admin', null, InputOption::VALUE_NONE, 'Make user admin')
            ->addOption('role', null, InputOption::VALUE_REQUIRED, 'User role', 'user')
            ->setHelp('This command creates a new user with the given email and name');
    }

    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $email = $input->getArgument('email');
        $name = $input->getArgument('name');
        $isAdmin = $input->getOption('admin');
        $role = $input->getOption('role');

        $output->writeln("Creating user: {$name} ({$email})");

        // Create user logic
        $output->writeln('<info>User created successfully</info>');
        return Command::SUCCESS;
    }
}
?>
```

### Fix 2: Handle Input Validation

```php
<?php
protected function execute(InputInterface $input, OutputInterface $output): int
{
    $email = $input->getArgument('email');

    // Validate email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $output->writeln('<error>Invalid email address: ' . $email . '</error>');
        return Command::FAILURE;
    }

    // Validate option values
    $role = $input->getOption('role');
    $validRoles = ['user', 'admin', 'editor'];
    if (!in_array($role, $validRoles)) {
        $output->writeln('<error>Invalid role. Must be one of: ' . implode(', ', $validRoles) . '</error>');
        return Command::FAILURE;
    }

    // Check required option combination
    if ($input->getOption('admin') && $role !== 'admin') {
        $output->writeln('<warning>--admin flag overrides --role option</warning>');
    }

    return Command::SUCCESS;
}
?>
```

### Fix 3: Use Proper Output Formatting

```php
<?php
use Symfony\Component\Console\Helper\Table;
use Symfony\Component\Console\Helper\ProgressBar;

protected function execute(InputInterface $input, OutputInterface $output): int
{
    // Simple output
    $output->writeln('Processing...');
    $output->writeln('<info>Success message</info>');
    $output->writeln('<error>Error message</error>');
    $output->writeln('<comment>Warning message</comment>');

    // Table output
    $table = new Table($output);
    $table->setHeaders(['ID', 'Name', 'Email']);
    $table->addRows([
        [1, 'Alice', 'alice@example.com'],
        [2, 'Bob', 'bob@example.com'],
    ]);
    $table->render();

    // Progress bar
    $progress = new ProgressBar($output, 100);
    for ($i = 0; $i < 100; $i++) {
        $progress->advance();
    }
    $progress->finish();
    $output->writeln('');

    return Command::SUCCESS;
}
?>
```

### Fix 4: Handle Exceptions in Commands

```php
<?php
protected function execute(InputInterface $input, OutputInterface $output): int
{
    try {
        $this->doWork($input, $output);
        return Command::SUCCESS;
    } catch (\Exception $e) {
        $output->writeln('<error>Command failed: ' . $e->getMessage() . '</error>');

        if ($output->isVerbose()) {
            $output->writeln('<error>' . $e->getTraceAsString() . '</error>');
        }

        return Command::FAILURE;
    }
}

private function doWork(InputInterface $input, OutputInterface $output): void
{
    $io = new SymfonyStyle($input, $output);
    $io->title('Processing');

    $io->section('Step 1: Validation');
    // ...

    $io->section('Step 2: Processing');
    // ...
}
?>
```

### Fix 5: Register Commands Properly

```php
<?php
// services.yaml
services:
    _defaults:
        autowire: true
        autoconfigure: true

    App\Command\:
        resource: '../src/Command/'

// Or manually register in Kernel
protected function configureCommands(CommandLoaderInterface $commandLoader): void
{
    $commandLoader->set('app:create-user', CreateUserCommand::class);
}

// Or use #[AsCommand] attribute (Symfony 5.3+)
use Symfony\Component\Console\Attribute\AsCommand;

#[AsCommand(name: 'app:create-user', description: 'Create a new user')]
class CreateUserCommand extends Command
{
    // ...
}
?>
```

## Examples

### Complete Command Example

```php
<?php
namespace App\Command;

use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;
use Symfony\Component\Console\Style\SymfonyStyle;

#[AsCommand(name: 'app:import-users', description: 'Import users from CSV')]
class ImportUsersCommand extends Command
{
    public function __construct(
        private readonly UserImporter $importer
    ) {
        parent::__construct();
    }

    protected function configure(): void
    {
        $this
            ->addArgument('file', InputArgument::REQUIRED, 'CSV file path')
            ->addOption('dry-run', null, InputOption::VALUE_NONE, 'Preview without saving');
    }

    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $io = new SymfonyStyle($input, $output);
        $file = $input->getArgument('file');
        $dryRun = $input->getOption('dry-run');

        if (!file_exists($file)) {
            $io->error("File not found: {$file}");
            return Command::FAILURE;
        }

        $rows = array_map('str_getcsv', file($file));
        $io->title("Importing " . count($rows) . " users");

        foreach ($rows as $index => $row) {
            $io->text("Processing row " . ($index + 1) . ": " . $row[0]);
            if (!$dryRun) {
                $this->importer->import($row);
            }
        }

        $io->success('Import complete');
        return Command::SUCCESS;
    }
}
?>
```

## Related Errors

- [Symfony HttpKernel Error]({{< relref "/languages/php/symfony-http-kernel-error" >}})
- [Symfony DependencyInjection Error]({{< relref "/languages/php/symfony-dependency-injection-error" >}})
- [Laravel Queue Worker Error]({{< relref "/languages/php/laravel-queue-worker-error" >}})
