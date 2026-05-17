#!/usr/bin/env python3
"""
Ticket Classificatie Demo
Eenvoudig script om te tonen hoe AI tickets kan classificeren.
Usage: python3 ticket-classifier.py < ticket.txt
"""
import sys, json, re
from datetime import datetime

# Simpele rule-based classifier (voor demo zonder API keys)
CATEGORIES = {
    "password_reset": ["wachtwoord", "password", "login", "inloggen", "account locked"],
    "bug_report": ["bug", "fout", "error", "crashed", "werkt niet", "not working"],
    "feature_request": ["feature", "enhancement", "wens", "zou fijn zijn", "could you add"],
    "network_issue": ["internet", "netwerk", "wifi", "verbinding", "connection", "slow"],
    "hardware": ["laptop", "monitor", "printer", "muis", "toetsenbord", "device"],
    "access_request": ["toegang", "access", "rechten", "permissions", "share", "folder"]
}

PRIORITY_SIGNALS = {
    "critical": ["urgent", "critical", "down", "offline", "everyone", "allemaal", "nood", "emergency"],
    "high": ["snel", "quickly", "asap", "important", "belangrijk", "manager", "director"],
    "low": ["when you have time", "geen haast", "not urgent", "someday"]
}

SENTIMENT_WORDS = {
    "positive": ["bedankt", "thanks", "great", "geweldig", "fijn", "goed"],
    "negative": ["frustrating", "terrible", "slecht", "waardeloos", "stupid", "idiot", "klaag", "complaint"],
    "urgent": ["nu", "now", "immediately", "meteen", "asap"]
}

def classify_ticket(text):
    text_lower = text.lower()
    
    # Category detection
    category_scores = {cat: 0 for cat in list(CATEGORIES.keys()) + ["general"]}
    for cat, keywords in CATEGORIES.items():
        for kw in keywords:
            if kw in text_lower:
                category_scores[cat] += 1
    
    category = max(category_scores, key=category_scores.get)
    if category_scores[category] == 0:
        category = "general"
    
    # Priority detection
    priority = "medium"
    for p, signals in PRIORITY_SIGNALS.items():
        if any(s in text_lower for s in signals):
            priority = p
            break
    
    # Sentiment analysis (simple)
    sentiment = "neutral"
    neg_count = sum(1 for w in SENTIMENT_WORDS["negative"] if w in text_lower)
    pos_count = sum(1 for w in SENTIMENT_WORDS["positive"] if w in text_lower)
    
    if neg_count > pos_count:
        sentiment = "negative"
    elif pos_count > neg_count:
        sentiment = "positive"
    
    if any(w in text_lower for w in SENTIMENT_WORDS["urgent"]):
        sentiment = "urgent"
    
    # Extract entities (simple)
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    
    return {
        "category": category,
        "priority": priority,
        "sentiment": sentiment,
        "confidence": min(category_scores[category] * 0.3 + 0.5, 0.95),
        "extracted_emails": emails,
        "word_count": len(text.split()),
        "timestamp": datetime.now().isoformat()
    }

def print_demo():
    demo_tickets = [
        {
            "subject": "Wachtwoord reset",
            "body": "Hallo, ik kan niet meer inloggen op mijn account. Mijn wachtwoord werkt niet meer. Kan je me helpen? - Jan from Finance"
        },
        {
            "subject": "Printer werkt niet",
            "body": "De printer op de 3de verdieping geeft constant een foutmelding. Ik moet dringend een rapport afdrukken voor de directeur. ASAP please!"
        },
        {
            "subject": "Feature request",
            "body": "Het zou fijn zijn als we tickets konden sorteren op urgentie in plaats van alleen op datum. Nu moet ik alles handmatig doen."
        },
        {
            "subject": "Boze klant",
            "body": "Dit systeem is waardeloos! Voor de 3e keer deze week loopt alles vast. Ik verlies hier klanten door. Ik wil dit NU opgelost zien!"
        }
    ]
    
    print("=" * 60)
    print("AI TICKET CLASSIFICATIE DEMO")
    print("=" * 60)
    
    for i, ticket in enumerate(demo_tickets, 1):
        full_text = f"{ticket['subject']}\n{ticket['body']}"
        result = classify_ticket(full_text)
        
        print(f"\n🎫 Ticket #{i}: {ticket['subject']}")
        print(f"   Text: {ticket['body'][:80]}...")
        print(f"   ├─ Categorie: {result['category']}")
        print(f"   ├─ Prioriteit: {result['priority']}")
        print(f"   ├─ Sentiment: {result['sentiment']}")
        print(f"   ├─ Confidence: {result['confidence']:.0%}")
        print(f"   └─ Emails gevonden: {len(result['extracted_emails'])}")
    
    print(f"\n{'=' * 60}")
    print("In een echte implementatie:")
    print("• Gebruik je een LLM (GPT-4, Claude, of lokale model)")
    print("• Confidence < 70% → human review verplicht")
    print("• Negatief sentiment + hoge prioriteit → escaleren naar team lead")
    print("• Alle classificaties gelogd voor audit trail")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        print_demo()
    else:
        print("Usage: python3 ticket-classifier.py --demo")
        print("   Of pipe een ticket file: cat ticket.txt | python3 ticket-classifier.py")
        print("\nRun de demo met: python3 ticket-classifier.py --demo")
