#!/bin/bash
# Ģenerē issue indeksu

set -e

echo "🔍 Ģenerē issue indeksu..."

OUTPUT_FILE="ISSUE_INDEX.md"

# Sāk veidot indeksa failu
cat > "$OUTPUT_FILE" << 'EOF'
# Issue indekss

Šis fails tiek automātiski ģenerēts un satur pārskatu par pieejamajiem issue šabloniem.

*Pēdējoreiz atjaunots: TIMESTAMP*

## 📋 Pieejamie issue šabloni

EOF

# Pievieno timestamp
sed -i "s/TIMESTAMP/$(date '+%Y-%m-%d %H:%M:%S UTC')/" "$OUTPUT_FILE"

TEMPLATE_DIR=".github/ISSUE_TEMPLATE"

if [ ! -d "$TEMPLATE_DIR" ]; then
    echo "⚠️  Issue šablonu direktorija nav atrasta"
    echo "Nav pieejami issue šabloni." >> "$OUTPUT_FILE"
    exit 0
fi

# Apstrādā katru šablonu
for template_file in "$TEMPLATE_DIR"/*.yml; do
    if [ -f "$template_file" ]; then
        filename=$(basename "$template_file")
        
        # Iegūst name un description no YAML
        name=$(grep "^name:" "$template_file" | cut -d':' -f2- | sed 's/^ *//' | sed 's/^"//' | sed 's/"$//')
        description=$(grep "^description:" "$template_file" | cut -d':' -f2- | sed 's/^ *//' | sed 's/^"//' | sed 's/"$//')
        
        if [ -n "$name" ] && [ -n "$description" ]; then
            {
                echo "### $name"
                echo ""
                echo "**Apraksts:** $description"
                echo ""
                echo "**Fails:** \`$filename\`"
                echo ""
                echo "---"
                echo ""
            } >> "$OUTPUT_FILE"
            
            echo "✅ Pievienots indeksam: $name"
        else
            echo "⚠️  Nevar iegūt informāciju no: $filename"
        fi
    fi
done

# Pievieno footer
cat >> "$OUTPUT_FILE" << 'EOF'

## 📚 Papildu informācija

- [CI-bota norādes](AGENT_GUIDELINES.md)
- [Workflow apraksts](WORKFLOW.md)
- [Dokumentācija](docs/index.md)

*Šis indekss tiek automātiski atjaunots ar katru commit.*
EOF

echo "🎉 Issue indekss ģenerēts: $OUTPUT_FILE"