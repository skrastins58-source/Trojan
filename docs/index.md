# Trojan Documentation

Welcome to the Trojan project documentation.

## Quickstart

Follow these steps to get started with the Trojan project:

### Prerequisites

- Git installed on your system
- Bash shell (Linux/macOS/WSL)

### Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/skrastins58-source/Trojan.git
   cd Trojan
   ```

2. **Make scripts executable:**
   ```bash
   chmod +x scripts/*.sh
   ```

3. **Run validation scripts:**
   ```bash
   # Validate links in documentation
   ./scripts/validate-links.sh
   
   # Get help for any script
   ./scripts/validate-links.sh --help
   ```

### Next Steps

- Read the [Contributing Guide](../CONTRIBUTING.md) to learn how to contribute
- Review the [Code of Conduct](../CODE_OF_CONDUCT.md) for community guidelines
- Check the main [README](../README.md) for project overview

## Project Structure

```
Trojan/
├── docs/           # Documentation files
├── scripts/        # Utility and validation scripts
├── CONTRIBUTING.md # Contribution guidelines
├── CODE_OF_CONDUCT.md # Community standards
└── README.md       # Project overview
```

## Script Usage

All scripts in the `scripts/` directory support the `--help` flag for usage information:

```bash
./scripts/validate-links.sh --help
```

Remember to make scripts executable after cloning:
```bash
chmod +x scripts/*.sh
```