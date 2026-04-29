# assistente_giochi_di_carte_alexa

## Descrizione
**Game Guru** è una skill Alexa che funge da assistente per giochi di carte.

Include le seguenti funzionalità:
- Sorteggiare un gioco
- Spiegazione delle regole
- Risposte alle domande sulle regole tramite AI
- Gestione partita e turni
- Classifica giocatori
- Fine partita con vincitore
- Storico vincitori

---

## 👥 Autore
- Andrea Tito — https://github.com/And0503

---

## ⚙️ Tecnologie
- Amazon Developer Console
- Python
  - boto3 1.28.78
  - ask-sdk-core 1.19.0
  - ask-sdk-dynamodb-persistence-adapter

---

## 📁 Struttura del progetto

| File / Cartella | Descrizione |
|----------------|-------------|
| `ai/ai_service.py` | Interfaccia servizi AI |
| `ai/gemini_service.py` | Integrazione con Gemini |
| `errors.py` | Gestione errori custom |
| `game_service.py` | Logica di business |
| `helper_functions.py` | Funzioni di supporto |
| `interactionModel.json` | Modello Alexa (intents e slot) |
| `lambda_function.py` | Entry point AWS Lambda |
| `models.py` | Dataclass |
| `requirements.txt` | Dipendenze Python |
| `storage/repository.py` | Interfaccia persistenza |
| `storage/dynamo_repository.py` | DynamoDB persistence |
| `storage/testing/in_memory_repository.py` | Repository test (session-based) |

---

## 🚀 Come eseguire il progetto
1. Creare account su Amazon Developer Console
2. Creare nuova skill Alexa
3. Impostare invocation name: *game guru*
4. Importare interaction model
5. Deploy su AWS Lambda
6. Abilitare modalità test
7. Usare su dispositivi Alexa

---

## ⚠️ Nota
- Skill progettata per uso personale
- Non garantita conformità completa alle linee guida di pubblicazione Alexa Store
