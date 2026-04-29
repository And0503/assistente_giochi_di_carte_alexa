# alexa_skill

---

## DESCRIZIONE
**Game Guru** è una skill alexa che svolge il compito di assistente per giochi di carte. 
Include le seguenti funzionalità:
- Sorteggiare un gioco
- Spiegazione delle regole
- Rispondere a domande sulle regole mediante AI
- Avviare una partita e ricordare chi deve dare carte
- Segnare e riportare la classifica
- Fine turno
- Fine gioco con vincitore
- Storico vincitori
---

---

👥 Autori - Progetto personale
- Andrea Tito - https://github.com/And0503

---

---

⚙️ Guida tecnica

---

---

🛠️ Tecnologie
- Amazon developer console
- Python
  - boto3 1.28.78
  - ask-sdk-core 1.19.0
  - ask-sdk-dynamodb-persistence-adapter

---

### 📁 Struttura del repo

| File / Cartella | Descrizione |
|----------------|-------------|
| `ai/ai_service.py` | Interfaccia per servizi AI |
| `ai/gemini_service.py` | Integrazione con Gemini per risposte sulle regole dei giochi |
| `errors.py` | Gestione errori custom |
| `game_service.py` | Logica di business |
| `helper_functions.py` | Funzioni di supporto |
| `interactionModel.json` | Modello di interazione Alexa (intents, slot, sample utterances e dialog management) |
| `lambda_function.py` | Entry point della AWS Lambda per la skill Alexa con gestione degli intent |
| `models.py` | Modelli dati (dataclass) |
| `requirements.txt` | Dipendenze Python del progetto |
| `skill-package/skill.json` | Manifest della skill Alexa: configurazione generale, endpoint Lambda, metadata e impostazioni di pubblicazione |
| `storage/dynamo_repository.py` | Persistenza su AWS DynamoDB tramite Alexa Persistence Adapter |
| `storage/in_memory_repository.py` | Repository per testing con session_attributes (senza DynamoDB) |
| `storage/repository.py` | Interfaccia per i repository di persistenza |

---

---

### 🚀 Come eseguire il progetto
1. Creare account amazon developer console
2. Aprire online la amazon developer console
3. Creare la skill con nome di invocazione game guru
4. Importare codice in code
5. Importare modello di interazione in build
6. Fare save, deploy e build
7. Avviare in Test la modalità Development
8. Usare la skill sui propri dispositivi alexa o da amazon developer console

---

