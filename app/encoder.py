import json
from bson import ObjectId

#classe responsável pela configuração da serialização do objeto OBjectId que está presente em alguns objetos Dict. Sem isso não está conseguindo converter o json.
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)