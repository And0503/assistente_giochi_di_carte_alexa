from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class GameInfo:
    regole: str
    min_giocatori: int
    max_giocatori: int
    
@dataclass
class Match:
    gioco: str
    turno: int
    data_inizio: str
    giocatori: Dict[str, int]
    ordine: List[str]
    mazziere_index: int = 0
    
@dataclass
class HistoryEntry:
    data: str
    gioco: str
    vincitore: str
    punteggi: Dict[str, int]
