# cadweb-api

Die **cadweb‑API** ist das zentrale, modulare Framework des cadweb‑Ökosystems.  
Sie stellt einheitliche Schnittstellen für:

- CAD‑Adapter (FreeCAD, Blender, weitere Engines)
- LLM‑Backends (OpenAI, GPT4All, Ollama, lokale Modelle)
- Tools & Workflows
- Agenten‑Logik
- Datei‑IO und Utility‑Funktionen

Die API bildet die Grundlage für:

- **cadweb‑runtime**
- **cadweb‑education**
- **cadweb‑maker**
- **cadweb‑enterprise**
- **cadweb‑agent**
- **cadweb‑cli**
- **cadweb‑ui**

---

## 📁 Projektstruktur

cadweb-api/

│

├── core/       # Config, Logging, Basisklassen

├── llm/        # LLM-Client, Registry

├── cad/        # CAD-Adapter, Registry

├── tools/      # Tool-Basis + Registry

├── agent/      # Agent-Framework + Workflows

├── io/         # Datei-IO

└── utils/      # Hilfsfunktionen, Pfade


---

## 🚀 Ziele

- Einheitliche API für alle cadweb‑Module  
- Portabel, modular, auditierbar  
- Erweiterbar für Education/Maker/Enterprise  
- Klare, dokumentierte Schnittstellen  
- Saubere Trennung von Runtime und Source‑Code  

---

## 🔧 Installation (lokale Entwicklung)

1. Python‑Interpreter auswählen (portable Python empfohlen)
2. Repository klonen: git clone https://github.com/cadweb-ecosystem/cadweb-api
3. Abhängigkeiten installieren (optional, sobald vorhanden): pip install -r requirements.txt

---

## 🧪 Tests

Tests folgen in einem späteren Schritt (pytest‑Struktur wird ergänzt).

---

## 📄 Lizenz

MIT License  
(c) cadweb‑ecosystem
