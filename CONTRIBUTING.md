# Contributing to Trojan

Thank you for your interest in contributing to the Trojan project! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Pull Request Process](#pull-request-process)
- [Validation Steps](#validation-steps)
- [Getting Help](#getting-help)
- [Code Style Guidelines](#code-style-guidelines)

## Getting Started

### Prerequisites

- Git installed on your system
- Bash shell (Linux/macOS/WSL)
- Basic familiarity with markdown and shell scripting

### Setting Up Your Development Environment

1. **Fork the repository** on GitHub

2. **Clone your fork:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Trojan.git
   cd Trojan
   ```

3. **Make scripts executable:**
   ```bash
   chmod +x scripts/*.sh
   ```

4. **Create a new branch for your changes:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Workflow

### Making Changes

1. **Start with documentation:** Update relevant documentation first
2. **Write or update scripts:** Ensure all scripts have proper `--help` functionality
3. **Test your changes:** Run validation scripts before committing

### Before Committing

Always run the validation scripts to ensure your changes don't break anything:

```bash
# Make scripts executable (if you've added new ones)
chmod +x scripts/*.sh

# Validate all documentation links
./scripts/validate-links.sh

# Get help for any script
./scripts/validate-links.sh --help
```

## Pull Request Process

### 1. Prepare Your Changes

- Ensure all scripts are executable (`chmod +x scripts/*.sh`)
- Run validation scripts and fix any issues
- Update documentation to reflect your changes
- Write clear, descriptive commit messages

### 2. Submit Your Pull Request

1. **Push your branch:**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request** on GitHub with:
   - Clear title describing the change
   - Detailed description of what you've changed and why
   - Reference any related issues
   - Include validation results

### 3. Pull Request Requirements

Your PR must:
- [ ] Pass all validation scripts
- [ ] Include updated documentation if applicable
- [ ] Have clear commit messages
- [ ] Follow the project's code style
- [ ] Include proper `--help` functionality for any new scripts

### 4. Review Process

- Maintainers will review your PR
- Address any feedback promptly
- Be prepared to make revisions
- Once approved, your PR will be merged

## Validation Steps

Before submitting any changes, run these validation steps:

### 1. Script Validation
```bash
# Ensure scripts are executable
chmod +x scripts/*.sh

# Test script help functionality
./scripts/validate-links.sh --help

# Run link validation
./scripts/validate-links.sh --verbose
```

### 2. Documentation Validation
- Ensure all relative links work correctly
- Verify markdown formatting is correct
- Check that examples are accurate and up-to-date

### 3. Manual Testing
- Clone a fresh copy of your branch
- Follow quickstart instructions in `docs/index.md`
- Verify all documented workflows function correctly

## Getting Help

If you need help or have questions:

### Documentation
- Read the [Quickstart Guide](docs/index.md)
- Check existing [Issues](https://github.com/skrastins58-source/Trojan/issues)
- Review [Pull Requests](https://github.com/skrastins58-source/Trojan/pulls)

### Communication
- **For questions:** Open a GitHub issue with the "question" label
- **For bugs:** Open a GitHub issue with the "bug" label
- **For feature requests:** Open a GitHub issue with the "enhancement" label

### Script Help
All scripts support the `--help` flag:
```bash
./scripts/validate-links.sh --help
```

## Code Style Guidelines

### Shell Scripts
- Use `#!/bin/bash` shebang
- Include usage headers with script description
- Implement `--help` flag for all scripts
- Use proper error handling with `set -e`
- Include meaningful comments
- Use consistent variable naming (UPPER_CASE for constants, lower_case for variables)

### Documentation
- Use clear, concise language
- Include code examples where appropriate
- Always mention making scripts executable (`chmod +x`)
- Follow markdown best practices
- Keep line lengths reasonable (80-100 characters)

### Commit Messages
- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- First line should be 50 characters or less
- Include detailed description if needed

## Script Requirements

When adding new scripts:

1. **Include proper shebang:** `#!/bin/bash`
2. **Add usage header:** Description of what the script does
3. **Implement --help flag:** Show usage information
4. **Use error handling:** Include `set -e` for proper error handling
5. **Add to validation:** Ensure new scripts are included in validation workflows
6. **Make executable:** Remember to `chmod +x` the script
7. **Document usage:** Update documentation to reference the new script

Example script template:
```bash
#!/bin/bash

# script-name.sh
# Brief description of what this script does
# Usage: ./script-name.sh [OPTIONS]

set -e

show_help() {
    cat << EOF
script-name.sh - Brief description

USAGE:
    ./script-name.sh [OPTIONS]

OPTIONS:
    -h, --help    Show this help message and exit

NOTE:
    Make sure this script is executable: chmod +x scripts/script-name.sh
EOF
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            show_help
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            echo "Use --help for usage information."
            exit 1
            ;;
    esac
done

# Main script logic here
```

## Thank You

Your contributions help make Trojan better for everyone. Thank you for taking the time to contribute!