import json
import urllib.request
import urllib.error
import logging
from .ai_service import AIService
from errors import AiServiceError
from config import GEMINI_API_KEY

logger = logging.getLogger(__name__)

class GeminiService(AIService):

    def __init__(self, api_key, model = "gemini-2.5-flash-lite"):
        self.url = (
            f"https://generativelanguage.googleapis.com/v1beta/models/"
            f"{model}:generateContent?key={api_key}"
        )

    def ask_rules(self, gioco, regole, domanda):
        payload = self._build_payload(gioco, regole, domanda)
        try:
            data = json.dumps(payload).encode("utf-8")
            req = urllib.request.Request(
                self.url,
                data=data,
                headers={"Content-Type": "application/json"},
                method="POST"
            )
            with urllib.request.urlopen(req, timeout=10) as response:
                result = json.loads(response.read().decode("utf-8"))
            return result["candidates"][0]["content"]["parts"][0]["text"].strip()
            
        except urllib.error.HTTPError as e:
            logger.error(f"Gemini HTTP error: {e.code} - {e.read().decode()}")
            raise AiServiceError(f"Errore HTTP: {e.code}")
        except Exception as e:
            logger.error(f"Errore chiamata Gemini: {e}")
            raise AiServiceError(f"Errore generico: {e}")

    def _build_payload(self, gioco, regole, domanda):
        return {
            "system_instruction": {
                "parts": [{"text": (
                    "Sei un assistente esperto di regole di giochi di carte. "
                    "Rispondi SOLO a domande sulle regole dei giochi di carte. "
                    "Hai a disposizione SOLO le regole fornite: non inventare. "
                    "Rispondi in italiano, conciso, adatto alla lettura ad alta voce."
                )}]
            },
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": (
                        f"Gioco: {gioco}\n\n"
                        f"Regole disponibili:\n{regole}\n\n"
                        f"Domanda: {domanda}"
                    )}]
                }
            ],
            "generationConfig": {
                "maxOutputTokens": 300,
                "temperature": 0.2
            }
        }

def create_ai_service():
    return GeminiService(api_key = GEMINI_API_KEY)
