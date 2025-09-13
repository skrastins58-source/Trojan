# Sourcery Integration Guide

This document explains how to use [Sourcery](https://sourcery.ai/) for code quality improvements and automated refactoring in the Trojan project.

## What is Sourcery?

Sourcery is an AI-powered code review tool that:
- Provides automatic code refactoring suggestions
- Identifies code quality issues
- Suggests performance improvements  
- Helps maintain consistent coding standards
- Supports Python, JavaScript, TypeScript, and more

## Setup and Configuration

### 1. Sourcery Token Setup

To enable Sourcery analysis in CI/CD:

1. **Get a Sourcery token:**
   - Visit [Sourcery Dashboard](https://sourcery.ai/dashboard)
   - Sign up/log in with your GitHub account
   - Copy your personal access token

2. **Add token to GitHub Secrets:**
   - Go to repository Settings → Secrets and variables → Actions
   - Click "New repository secret"
   - Name: `SOURCERY_TOKEN`
   - Value: Your Sourcery token
   - Click "Add secret"

### 2. Configuration File

Sourcery is configured via `.sourcery.yaml` in the repository root. Key settings:

```yaml
# Minimum quality score (1-5 scale)
min_quality: 3

# File patterns to analyze
include:
  - "**/*.py"
  - "**/*.js" 
  - "**/*.ts"
  - "scripts/*.sh"

# Files to exclude
exclude:
  - ".git/**"
  - "node_modules/**"
  - "dist/**"
```

## How Sourcery Works

### Automatic Analysis

Sourcery runs automatically on:
- **Pull Requests**: Provides inline suggestions
- **Push to main/develop**: Generates quality reports
- **Manual workflow runs**: Via GitHub Actions

### Code Review Integration

When you create a pull request:
1. Sourcery analyzes changed files
2. Posts suggestions as PR comments
3. Provides refactoring recommendations
4. Highlights potential issues

### Example Suggestions

Sourcery might suggest improvements like:

**Before:**
```python
items = []
for item in source_list:
    if item.is_valid():
        items.append(item.name)
```

**After:**
```python
items = [item.name for item in source_list if item.is_valid()]
```

## Local Development

### Install Sourcery CLI

```bash
# Install Sourcery CLI
pip install sourcery-cli

# Login with your token
sourcery login

# Analyze current directory
sourcery review .

# Get suggestions for specific file
sourcery review path/to/file.py
```

### IDE Integration

**VS Code:**
1. Install "Sourcery" extension
2. Sign in with your Sourcery account
3. Get real-time suggestions while coding

**PyCharm:**
1. Install Sourcery plugin from marketplace
2. Configure with your Sourcery token
3. Enable automatic suggestions

## Current Repository Status

### Supported Files

Currently, the repository contains:
- ✅ **Shell scripts** (`scripts/*.sh`) - Analyzed via ShellCheck
- 🔄 **Future code files** - Ready for Python, JavaScript, TypeScript

### Workflow Status

The Sourcery workflow (`.github/workflows/sourcery.yml`) includes:
- Sourcery analysis for supported languages
- ShellCheck analysis for shell scripts
- Graceful handling when no token is configured

## Shell Script Quality

Since this repository currently contains shell scripts, we also run **ShellCheck** for shell script quality:

```bash
# Manually check shell scripts
shellcheck scripts/*.sh

# Common issues ShellCheck finds:
# - Unquoted variables
# - Missing error handling
# - Potential security issues
```

## Best Practices

### 1. Review Suggestions Carefully
- Not all suggestions need to be applied
- Consider readability vs. performance
- Maintain consistency with existing code

### 2. Configure Quality Threshold
- Adjust `min_quality` in `.sourcery.yaml`
- Higher values = fewer but higher-quality suggestions
- Lower values = more suggestions but may include minor improvements

### 3. Use in Development Workflow
- Enable IDE integration for real-time feedback
- Review Sourcery suggestions during code review
- Run locally before pushing changes

### 4. Team Guidelines
- Establish team standards for accepting suggestions
- Document project-specific preferences
- Regular review of Sourcery configuration

## Troubleshooting

### Common Issues

**"SOURCERY_TOKEN not set"**
- Add token to GitHub repository secrets
- Verify token is valid at [Sourcery Dashboard](https://sourcery.ai/dashboard)

**"No files to analyze"**
- Check file patterns in `.sourcery.yaml`
- Ensure supported file types exist in repository

**Suggestions not appearing on PRs**
- Verify GitHub App permissions
- Check workflow execution in Actions tab
- Ensure Sourcery token has necessary permissions

### Getting Help

- 📖 [Sourcery Documentation](https://docs.sourcery.ai/)
- 💬 [Sourcery Community](https://github.com/sourcery-ai/sourcery/discussions)  
- 🐛 [Report Issues](https://github.com/sourcery-ai/sourcery/issues)

## Future Enhancements

As the repository grows, consider:

1. **Language-specific rules** for Python/JavaScript
2. **Custom refactoring patterns** for project-specific code
3. **Integration with other tools** (ESLint, Prettier, Black)
4. **Code quality metrics** tracking over time
5. **Team-specific configuration** for different coding standards

---

**Note**: This setup prepares the repository for code development while providing immediate value for existing shell scripts through ShellCheck integration.