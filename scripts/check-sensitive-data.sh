#!/bin/bash
# Pārbauda sensitīvos datus

set -e

echo "🔍 Pārbauda sensitīvos datus failos..."

# Sensitīvu datu modeļi
sensitive_patterns=(
    "password"
    "secret"
    "api[_-]?key"
    "access[_-]?token"
    "private[_-]?key"
    "aws[_-]?secret"
    "github[_-]?token"
    "slack[_-]?token"
    "bearer\s+[a-zA-Z0-9]+"
)

found_issues=0

# Meklē visus tekstuālos failus, izņemot .git
files=$(find . -type f \( -name "*.md" -o -name "*.yml" -o -name "*.yaml" -o -name "*.json" -o -name "*.txt" -o -name "*.sh" \) -not -path "./.git/*")

for file in $files; do
    echo "🔍 Pārbauda: $file"
    
    for pattern in "${sensitive_patterns[@]}"; do
        # Meklē modeļus (case-insensitive)
        matches=$(grep -i -n "$pattern" "$file" 2>/dev/null || true)
        
        if [ -n "$matches" ]; then
            # Pārbauda, vai tas nav komentārs vai dokumentācija
            while IFS= read -r match; do
                line_num=$(echo "$match" | cut -d':' -f1)
                line_content=$(echo "$match" | cut -d':' -f2-)
                
                # Izņem komentārus un dokumentācijas paraugus
                if [[ "$line_content" =~ ^[[:space:]]*# ]] || \
                   [[ "$line_content" =~ \`.*$pattern.*\` ]] || \
                   [[ "$line_content" =~ YOUR_.*$pattern ]] || \
                   [[ "$line_content" =~ \<.*$pattern.*\> ]] || \
                   [[ "$line_content" =~ example.*$pattern ]] || \
                   [[ "$line_content" =~ $pattern.*example ]]; then
                    echo "  ℹ️  Izņemts (dokumentācija): līnija $line_num"
                else
                    echo "  ⚠️  Potenciāli sensitīvi dati: līnija $line_num"
                    echo "      $line_content"
                    found_issues=$((found_issues + 1))
                fi
            done <<< "$matches"
        fi
    done
done

# Pārbauda arī failu nosaukumus
echo ""
echo "🔍 Pārbauda failu nosaukumus..."
for pattern in "${sensitive_patterns[@]}"; do
    suspicious_files=$(find . -type f -iname "*$pattern*" -not -path "./.git/*" 2>/dev/null || true)
    if [ -n "$suspicious_files" ]; then
        echo "⚠️  Aizdomīgs faila nosaukums:"
        echo "$suspicious_files"
        found_issues=$((found_issues + 1))
    fi
done

echo ""
if [ $found_issues -eq 0 ]; then
    echo "🎉 Nav atrasti sensitīvi dati!"
else
    echo "❌ Atrasti $found_issues potenciāli sensitīvi elementi"
    echo "⚠️  Lūdzu, pārbaudiet un nodrošiniet, ka nav iekļauti īsti sensitīvi dati"
    # Nav hard failure, jo var būt false positives
    exit 0
fi