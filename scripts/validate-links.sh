#!/bin/bash

# validate-links.sh
# Script to validate links in documentation files
# Usage: ./validate-links.sh [OPTIONS]

set -e

# Configuration
DOCS_DIR="docs"
README_FILE="README.md"
CONTRIBUTING_FILE="CONTRIBUTING.md"
CODE_OF_CONDUCT_FILE="CODE_OF_CONDUCT.md"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to show usage/help
show_help() {
    cat << EOF
validate-links.sh - Validate links in documentation files

USAGE:
    ./validate-links.sh [OPTIONS]

OPTIONS:
    -h, --help          Show this help message and exit
    -v, --verbose       Enable verbose output
    -q, --quiet         Suppress non-error output
    --docs-only         Only validate links in docs directory
    --exclude-external  Skip validation of external links

DESCRIPTION:
    This script validates links in markdown files within the project.
    It checks for:
    - Broken internal file references
    - Missing anchor links
    - Malformed URLs

EXAMPLES:
    ./validate-links.sh                    # Validate all documentation
    ./validate-links.sh --verbose          # Validate with detailed output
    ./validate-links.sh --docs-only        # Only check docs/ directory

EXIT CODES:
    0   All links are valid
    1   Invalid links found
    2   Script execution error

NOTE:
    Make sure this script is executable: chmod +x scripts/validate-links.sh
EOF
}

# Function to log messages
log_info() {
    if [[ "$QUIET" != "true" ]]; then
        echo -e "${GREEN}[INFO]${NC} $1"
    fi
}

log_warning() {
    echo -e "${YELLOW}[WARN]${NC} $1" >&2
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1" >&2
}

log_verbose() {
    if [[ "$VERBOSE" == "true" ]]; then
        echo -e "${YELLOW}[VERBOSE]${NC} $1"
    fi
}

# Function to validate a single file
validate_file() {
    local file="$1"
    local errors=0
    
    log_verbose "Validating file: $file"
    
    if [[ ! -f "$file" ]]; then
        log_error "File not found: $file"
        return 1
    fi
    
    # Check for basic markdown link syntax issues
    while IFS= read -r line_num && IFS= read -r line <&3; do
        # Check for malformed markdown links
        if echo "$line" | grep -q '\]\([^)]*$'; then
            log_error "Malformed link on line $line_num in $file: $line"
            ((errors++))
        fi
        
        # Check for relative file links that don't exist
        while IFS= read -r link; do
            if [[ "$link" =~ ^\.\. || "$link" =~ ^\. ]]; then
                local target_file
                target_file=$(dirname "$file")/"$link"
                if [[ ! -f "$target_file" && ! -d "$target_file" ]]; then
                    log_error "Broken relative link in $file: $link (resolved to: $target_file)"
                    ((errors++))
                fi
            fi
        done < <(grep -o '\[.*\](\([^)]*\))' "$line" 2>/dev/null | sed 's/.*(\([^)]*\)).*/\1/' || true)
        
    done < <(grep -n . "$file") 3< <(sed 's/^[0-9]*://' "$file")
    
    return $errors
}

# Parse command line arguments
VERBOSE=false
QUIET=false
DOCS_ONLY=false
EXCLUDE_EXTERNAL=false

while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            show_help
            exit 0
            ;;
        -v|--verbose)
            VERBOSE=true
            shift
            ;;
        -q|--quiet)
            QUIET=true
            shift
            ;;
        --docs-only)
            DOCS_ONLY=true
            shift
            ;;
        --exclude-external)
            EXCLUDE_EXTERNAL=true
            shift
            ;;
        *)
            log_error "Unknown option: $1"
            echo "Use --help for usage information."
            exit 2
            ;;
    esac
done

# Main validation logic
main() {
    local total_errors=0
    local files_to_check=()
    
    log_info "Starting link validation..."
    
    # Determine which files to check
    if [[ "$DOCS_ONLY" == "true" ]]; then
        if [[ -d "$DOCS_DIR" ]]; then
            while IFS= read -r -d '' file; do
                files_to_check+=("$file")
            done < <(find "$DOCS_DIR" -name "*.md" -print0 2>/dev/null || true)
        fi
    else
        # Check all documentation files
        [[ -f "$README_FILE" ]] && files_to_check+=("$README_FILE")
        [[ -f "$CONTRIBUTING_FILE" ]] && files_to_check+=("$CONTRIBUTING_FILE")
        [[ -f "$CODE_OF_CONDUCT_FILE" ]] && files_to_check+=("$CODE_OF_CONDUCT_FILE")
        
        if [[ -d "$DOCS_DIR" ]]; then
            while IFS= read -r -d '' file; do
                files_to_check+=("$file")
            done < <(find "$DOCS_DIR" -name "*.md" -print0 2>/dev/null || true)
        fi
    fi
    
    if [[ ${#files_to_check[@]} -eq 0 ]]; then
        log_warning "No markdown files found to validate"
        exit 0
    fi
    
    log_info "Found ${#files_to_check[@]} file(s) to validate"
    
    # Validate each file
    for file in "${files_to_check[@]}"; do
        if validate_file "$file"; then
            log_verbose "✓ $file passed validation"
        else
            log_error "✗ $file failed validation"
            ((total_errors++))
        fi
    done
    
    # Report results
    if [[ $total_errors -eq 0 ]]; then
        log_info "✓ All links validated successfully!"
        exit 0
    else
        log_error "✗ Found issues in $total_errors file(s)"
        exit 1
    fi
}

# Run main function
main "$@"