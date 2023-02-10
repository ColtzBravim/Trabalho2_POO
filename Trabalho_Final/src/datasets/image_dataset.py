
from typing import Tuple, Any, Dict
from .dataset_interface import DatasetInterface
import cv2,os
import numpy as np

class ImageDataset(DatasetInterface):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        #ler arquivo contendo os nomes das imagens e as classes e armazenar
        #em uma lista
        self.list = self.readPath(path)

    def size(self) -> int:
        return len(self.list)


    def get(self, idx: int) -> Tuple[np.ndarray, str]:
        # ler a i-esima imagem do disco usando a biblioteca cv2 e retornar
        # a imagem e a respectiva classe
  
        img = cv2.imread(self.list[idx][0], cv2.IMREAD_GRAYSCALE)
        #vetorizar a imagem utilizando flattening
        base_vector = img.flatten()
        
        
        return base_vector, self.list[idx][1]




    def readPath(self,path):
        caminho = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
        filename = caminho + self.path
        dataset = os.path.abspath(os.path.join(os.path.dirname(filename)))
        data = []
        try:
            txt_file = open(filename, 'r')
            lines = txt_file.readlines()
            for i in lines:
                img_class = i.split()
                img_class = [dataset+img_class[0],img_class[1]]
                data.append(img_class)
                
        except(FileNotFoundError):
            print(f'Arquivo não foi encontrado no diretório {filename} ')
            return 0
        return data
