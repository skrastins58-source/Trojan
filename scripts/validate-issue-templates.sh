#!/bin/bash
# Validē issue šablonu struktūru

set -e

echo "🔍 Validē issue šablonus..."

TEMPLATE_DIR=".github/ISSUE_TEMPLATE"

if [ ! -d "$TEMPLATE_DIR" ]; then
    echo "❌ Issue šablonu direktorija nav atrasta: $TEMPLATE_DIR"
    exit 1
fi

# Pārbauda, vai eksistē pamata šabloni
required_templates=("bug_report.yml" "feature_request.yml" "documentation.yml")

for template in "${required_templates[@]}"; do
    if [ ! -f "$TEMPLATE_DIR/$template" ]; then
        echo "❌ Trūkst obligātā šablona: $template"
        exit 1
    fi
    echo "✅ Atrasts šablons: $template"
done

# Validē YAML sintaksi šablonos
echo "🔍 Validē YAML sintaksi šablonos..."
for template_file in "$TEMPLATE_DIR"/*.yml; do
    if [ -f "$template_file" ]; then
        if ! python3 -c "import yaml; yaml.safe_load(open('$template_file'))" 2>/dev/null; then
            echo "❌ YAML sintakses kļūda failā: $template_file"
            exit 1
        fi
        echo "✅ YAML sintakse OK: $(basename "$template_file")"
    fi
done

# Pārbauda obligātos laukus
echo "🔍 Pārbauda obligātos laukus šablonos..."
for template_file in "$TEMPLATE_DIR"/*.yml; do
    if [ -f "$template_file" ]; then
        # Pārbauda, vai eksistē name un description
        if ! grep -q "^name:" "$template_file"; then
            echo "❌ Trūkst 'name' lauka failā: $template_file"
            exit 1
        fi
        if ! grep -q "^description:" "$template_file"; then
            echo "❌ Trūkst 'description' lauka failā: $template_file"
            exit 1
        fi
        echo "✅ Obligātie lauki OK: $(basename "$template_file")"
    fi
done

echo "🎉 Visi issue šabloni ir validēti veiksmīgi!"