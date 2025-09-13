# Workflow konfigurāciju apraksts

Šis dokuments apraksta CI/CD workflow konfigurācijas un to funkcionalitāti.

## 🔄 GitHub Actions Workflows

### Validācijas workflow

Automātiski validē:
- Markdown sintaksi un saturu
- YAML konfigurācijas failus
- GitHub Actions workflows
- Issue šablonu struktūru

### Dokumentācijas ģenerēšana

- Atjauno dokumentācijas indeksus
- Ģenerē PDF/EPUB eksportus (ja konfigurēts)
- Validē iekšējās saites

### CI-bot operācijas

CI-bots veic šādas darbības:
1. **Validācija** - Pārbauda failu sintaksi un struktūru
2. **Indeksēšana** - Atjauno `ISSUE_INDEX.md` failus
3. **Paziņošana** - Nosūta paziņojumus kanālos (ja konfigurēts)
4. **Žurnālēšana** - Reģistrē visas veiktās izmaiņas

## 🏷️ Labeling sistēma

- `ci-bot` - Automātiski ģenerēti pull requesti
- `documentation` - Dokumentācijas izmaiņas
- `workflow` - CI/CD konfigurāciju izmaiņas

## 🚨 Drošības prasības

- Sensitīvi dati nedrīkst būt logs failos
- Automātiskās izmaiņas jāvalidē pirms sapludināšanas
- Neizdošanās gadījumā process jāaptur un jāpaziņo komandai

## 📝 Konfigurācijas faili

- `.github/workflows/` - GitHub Actions workflows
- `scripts/` - Validācijas un automatizācijas skripti
- `.github/ISSUE_TEMPLATE/` - Issue šabloni

---

*Sīkāka informācija par katru workflow atrodama attiecīgajos YAML failos.*