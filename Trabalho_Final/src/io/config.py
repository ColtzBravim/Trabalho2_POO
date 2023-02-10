from typing import Dict
import json,os

def load_config(path: str) -> Dict:
    """ le o arquivo json e retorna como um dicionario """

    caminho = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
    filename = caminho + path
    
    data = None
    with open(filename) as json_file:
        data = json.load(json_file)

    return data
