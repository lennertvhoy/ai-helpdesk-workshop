# Workshop Outline — AI voor je Helpdesk

## Module 1: De Realiteit van AI in Support (15 min)

### Opening Hook
> "Hoeveel van jullie hebben vandaag al ChatGPT, Copilot, of een andere AI tool gebruikt voor werk?"
> (Verwacht: 80%+ heft hand op)
> "En hoeveel van jullie bedrijf heeft daar een beleid voor?"
> (Verwacht: stilte)

### Wat we behandelen
1. **AI Act Article 4** — EU-verplichting sinds februari 2025
   - Alle werknemers die AI gebruiken moeten AI-literate zijn
   - Je bedrijf moet dit kunnen aantonen
   - Boetes bij non-compliance: tot 7% van jaaromzet

2. **De huidige staat** — Cijfers die pijn doen
   - 88% van helpdesks experimenteert met AI
   - 75% heeft geen governance
   - 39% van Belgische werknemers heeft AI-training gehad

3. **Het misverstand** — AI vervangt niet, AI assisteert
   - Human-in-the-loop is niet optioneel, het is verplicht
   - De juiste balans: 70% AI-generated, 100% human-reviewed

## Module 2: Demo — Ticket Classificatie (20 min)

### Live Demo Flow
```
Input: Ruwe ticket (email/chat/vorm)
      ↓
AI: Extractie — wat, wie, urgentie, sentiment
      ↓
Human: Validatie — 1 klik om goed te keuren
      ↓
Output: Geclassificeerde ticket in juiste categorie
```

### Tools die we tonen
1. **Rule-based classificatie** (basis)
2. **LLM-based classificatie** (geavanceerd)
3. **Hybride: AI suggestie + human override** (aanbevolen)

### Hands-on oefening
Deelnemers krijgen 5 voorbeeld tickets. Ze beoordelen:
- Welke categorie?
- Welke prioriteit?
- Welke sentiment?
- Dan tonen we wat de AI suggereerde

## Module 3: Demo — AI-Assisted Responses (20 min)

### Het Probleem
> "Een standaardticket kost 12-15 minuten om te beantwoorden. Met AI: 3-4 minuten. Maar het klinkt vaak als... een robot."

### De Oplossing: Structured AI + Human Polish
```
1. AI genereert DRAFT (structuur + facts)
2. Human voegt TONE toe (empathie, context, bedrijfscultuur)
3. AI checkt COMPLIANCE (geen gevoelige data gelekt?)
4. Human keurt GOED en verzendt
```

### Live Demo
- Voorbeeld 1: Wachtwoord reset (eenvoudig)
- Voorbeeld 2: Bug report (complex)
- Voorbeeld 3: Boze klant (hoog risico)

### Template Library
Deelnemers krijgen:
- 10 response templates (Nederlands/Engels)
- Prompt library voor common scenarios
- Tone-of-voice guidelines

## Module 4: Privacy & Security (15 min)

### De Gouden Regels
1. **Nooit** PII naar publieke LLMs sturen (ChatGPT web, Claude web)
2. **Altijd** gebruik enterprise-grade API's met data processing agreements
3. **Log** alle AI-interacties voor audit trail
4. **Anonimiseer** voor je naar AI stuurt
5. **Review** elke output voor data leakage

### Compliance Checklist (EU AI Act)
- [ ] AI-gebruik geregistreerd in risicoregister
- [ ] Werknemers getraind in AI literacy
- [ ] Human oversight process gedocumenteerd
- [ ] Data retention policy vastgelegd
- [ ] Incident response plan voor AI fouten

## Module 5: Q&A & Next Steps (20 min)

### Vragen die we verwachten
- "Werkt dit met ons [specifieke] ticketing systeem?"
  - Antwoord: Ja, via API of eenvoudige integraties
- "Hoe lang duurt implementatie?"
  - Antwoord: Basis workflow: 1-2 dagen. Volledige governance: 2-4 weken.
- "Wat kost dit?"
  - Antwoord: Workshop €375. Implementatie support op maat.

### Meenemen na de workshop
1. AI Acceptable Use Policy template
2. Prompt library (20+ prompts)
3. Compliance checklist
4. 30-dagen adoptie email sequence
5. Contact voor follow-up vragen

## Sprekersnotities

### Timing Waarschuwingen
- ⏱️ 15 min: Module 1 moet af zijn
- ⏱️ 35 min: Module 2 demo moet draaien
- ⏱️ 55 min: Module 3 hands-on start
- ⏱️ 75 min: Module 4 checklist doorlopen
- ⏱️ 85 min: Begin Q&A

### Technische Setup (vooraf)
- [ ] Demo-omgeving getest
- [ ] Backup internetverbinding
- [ ] Screenshare getest
- [ ] Chat/moderatie klaar
- [ ] Opname ingesteld (indien gewenst)

### Noodscenario's
- **Internet valt uit**: Fallback naar offline demo video's
- **Tool werkt niet**: Altijd 2 tools klaar (bijv. ChatGPT + lokale LLM)
- **Te technische vragen**: "Dat bespreken we graag 1-op-1 na de sessie"
- **Skeptische deelnemer**: Focus op compliance/privacy, niet op "AI is cool"

## Follow-up Sequence

### Dag 1
Email met:
- Workshop opname (indien beschikbaar)
- Alle templates en checklists
- Kalender link voor 1-op-1 gesprek

### Dag 7
Email met:
- Case study van vergelijkbaar bedrijf
- "Hoe start je met je eerste AI workflow"

### Dag 14
Email met:
- Aanbod: 2-uurs implementatie sessie (€950)
- KMO-portefeuille info

### Dag 30
Email met:
- Nieuwe AI ontwikkelingen in helpdesk space
- Uitnodiging voor volgende workshop
