from django.conf import settings
import pymongo

class WeatherRepository:

    collection = ''

    def __init__(self, collectionName) -> None:
        self.collection = collectionName

# estabelece conexão via pymongo, com mongo client
    def getConnection(self):
        client = pymongo.MongoClient(
            getattr(settings, "MONGO_CONNECTION_STRING"))
        connection = client[
            getattr(settings, "MONGO_DATABASE_NAME")]
        return connection
    
# estabelece conexão com collection 
    def getCollection(self):
        conn = self.getConnection()
        collection = conn[self.collection]
        return collection
    
    # CRUD
    def getAll(self):
        # busca por um JSON
        document = self.getCollection().find({})
        return document
    
    def get_by_id(self, document_id):
        # Retorna um documento pelo seu ID
        document = self.get_collection().find_one({"_id": document_id})
        return document

    def get_by_attribute(self, attribute, value):
        # Retorna documentos com um determinado atributo e valor
        documents = self.get_collection().find({attribute: value})
        return documents

    def insert_document(self, document):
        # Insere um novo documento na coleção
        self.get_collection().insert_one(document)

    def update_document(self, document_id, new_data):
        # Atualiza um documento existente na coleção
        self.get_collection().update_one({"_id": document_id}, {"$set": new_data})

    def delete_document(self, document_id):
        # Deleta um documento da coleção pelo seu ID
        self.get_collection().delete_one({"_id": document_id})

    def post(self, document):
            self.insert_document(document)