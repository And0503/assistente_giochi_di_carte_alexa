from abc import ABC, abstractmethod

class AIService(ABC):
    @abstractmethod
    def ask_rules(self, gioco, regole, domanda):
        pass
