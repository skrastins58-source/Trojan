# 🤖 CI-bota norādes – Kā darboties ar šo starter-pack

Šīs vadlīnijas paredzētas CI/bota skriptiem un operatoriem, kas darbojas šajā šablonu/dokumentācijas repozitorijā.

---

## ✅ Principi

1. **Izpildi tikai dokumentētos un apstiprinātos workflow.**
   - Nedrīkst veikt izmaiņas ārpus CI/CD skriptos noteiktā.
2. **Strādā tikai ar šablonu un dokumentācijas direktorijiem:**
   - `.github/ISSUE_TEMPLATE/`
   - `docs/`
   - `scripts/`
   - Citi norādīti repozitorija dokumentācijā.
3. **Automatizētās darbības:**
   - Validē Markdown, YAML un CI konfigurācijas sintaksi.
   - Ģenerē vai atjauno indeksus (`ISSUE_INDEX.md`) tikai ar apstiprinātiem skriptiem.
   - Eksportē dokumentāciju uz PDF/EPUB tikai ar norādītajiem rīkiem (pandoc, marp, utt.).
   - Veic paziņojumus uz Slack/Teams/Discord tikai, ja saņemts apstiprinājums vai trigger.
   - Nelabo vai neizvieto failus ārpus iepriekš definētajām vietām.

---

## 🛡️ Drošība un kvalitāte

- Nekad neievieto sensitīvus datus log failos, publiskajos artefaktos vai paziņojumos.
- Pull requestus, kas ģenerēti automātiski, atzīmē ar `ci-bot` label.
- Pirms sapludināšanas automātiski ģenerētam saturam jāiziet validācija un (ja iespējams) cilvēka pārbaude.
- Ja validācija neizdodas, automātiski apturi procesu un paziņo komandai.

---

## 📝 Darbību soļi

1. Saņem trigger no GitHub Actions vai cita CI/CD servera.
2. Veic tikai dokumentācijā vai workflow definētos uzdevumus.
3. Validē visus automātiski ģenerētos failus.
4. Pievieno nepieciešamos labelus vai statusus pull requestiem.
5. Paziņo atbilstošajos kanālos (Slack/Teams/Email), ja definēts workflow vai notikums.
6. Reģistrē visas izmaiņas žurnālā (logs, workflow summary, u.c.).

---

## ⚡ Noderīgas saites

- [Galvenā dokumentācija](docs/index.md)
- [CI konfigurāciju apraksts](WORKFLOW.md)
- [CHANGELOG un roadmap](CHANGELOG.md)

---

**Šīs norādes jāievēro visiem CI-botiem un to operatoriem šajā repozitorijā.**