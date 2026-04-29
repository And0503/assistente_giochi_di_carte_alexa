#=================
#    TESTING: senza dynamoDB, solo persistenza intra-sessione con session_attr (dati conservati e scambiati nei json di richiesta e risposta)
#=================
from .repository import GameRepository
from game_service import GameService

class InMemoryGameRepository(GameRepository):

    def __init__(self, handler_input):
        self.session_attr = handler_input.attributes_manager.session_attributes

        if "game_data" not in self.session_attr:
            self.session_attr["game_data"] = {
                "partite": [],
                "partita_corrente": None
            }

    def get_data(self):
        return self.session_attr["game_data"]

    def save_data(self, data):
        self.session_attr["game_data"] = data
        
def create_game_service(handler_input):
    return GameService(InMemoryGameRepository(handler_input))
