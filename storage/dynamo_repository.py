import os
import boto3
from ask_sdk_dynamodb.adapter import DynamoDbAdapter
from .repository import GameRepository
from game_service import GameService
from errors import DBError
import logging
logger = logging.getLogger(__name__)


region = os.environ["DYNAMODB_PERSISTENCE_REGION"]
table = os.environ["DYNAMODB_PERSISTENCE_TABLE_NAME"]

ddb_resource = boto3.resource("dynamodb", region_name=region)
dynamodb_adapter = DynamoDbAdapter(
    table_name=table,
    create_table=False,
    partition_key_name="id",
    dynamodb_resource=ddb_resource
)


class DynamoDbGameRepository(GameRepository):
    
    def __init__(self, handler_input):
        self.handler_input = handler_input
    
    def get_data(self):
        try:
            attr = self.handler_input.attributes_manager.persistent_attributes
            if not attr:
                return {"partite": [], "partita_corrente": None}
            return attr
        except Exception as e:
            logger.error(f"DynamoDB get error: {e}")
            raise DBError(f"Errore lettura DynamoDB: {e}")
    
    def save_data(self, data):
        try:
            self.handler_input.attributes_manager.persistent_attributes = data
            self.handler_input.attributes_manager.save_persistent_attributes()
        except Exception as e:
            logger.error(f"DynamoDB save error: {e}")
            raise DBError(f"Errore scrittura DynamoDB: {e}")
        
        
def create_game_service(handler_input):
    repository = DynamoDbGameRepository(handler_input)
    return GameService(repository)
