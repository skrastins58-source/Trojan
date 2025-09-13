#!/bin/bash
# Validē dokumentācijas saites

set -e

echo "🔍 Validē dokumentācijas saites..."

# Meklē visus .md failus
md_files=$(find . -name "*.md" -not -path "./.git/*")

if [ -z "$md_files" ]; then
    echo "⚠️  Nav atrasti Markdown faili"
    exit 0
fi

echo "📄 Atrasti Markdown faili:"
echo "$md_files"

broken_links=0

# Pārbauda katru .md failu
for file in $md_files; do
    echo ""
    echo "🔍 Pārbauda failu: $file"
    
    # Atrod visas relatīvās saites
    relative_links=$(grep -E '\[.*\]\([^)]+\)' "$file" | sed 's/.*(\([^)]*\)).*/\1/' | grep -v '^http' | grep -v '^#' || true)
    
    if [ -z "$relative_links" ]; then
        echo "  ℹ️  Nav relatīvu saišu"
        continue
    fi
    
    for link in $relative_links; do
        # Noņem fragment identifikatorus (#section)
        clean_link=$(echo "$link" | cut -d'#' -f1)
        
        if [ -z "$clean_link" ]; then
            continue
        fi
        
        # Izveido pilnu ceļu
        if [[ "$clean_link" == /* ]]; then
            # Absolūts ceļš no repo saknes
            full_path=".$clean_link"
        else
            # Relatīvs ceļš no faila direktorijas
            file_dir=$(dirname "$file")
            full_path="$file_dir/$clean_link"
        fi
        
        # Normalizē ceļu
        full_path=$(realpath -m "$full_path" 2>/dev/null || echo "$full_path")
        
        if [ ! -f "$full_path" ] && [ ! -d "$full_path" ]; then
            echo "  ❌ Salauzta saite: $link"
            broken_links=$((broken_links + 1))
        else
            echo "  ✅ Saite OK: $link"
        fi
    done
done

echo ""
if [ $broken_links -eq 0 ]; then
    echo "🎉 Visas dokumentācijas saites ir validētas veiksmīgi!"
else
    echo "❌ Atrasts $broken_links salauztu saišu"
    exit 1
fi