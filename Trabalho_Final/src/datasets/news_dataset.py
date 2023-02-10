from typing import Tuple, Any, Dict
from .dataset_interface import DatasetInterface
import os
from collections import Counter
import nltk
#nltk.download('punkt')
#nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import numpy as np



class NewsDataset(DatasetInterface):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        # ler arquivo contendo os nomes dos arquivos de noticias e as classes
        self.list = self.readPath(path)
        self.vocab = None
        self.vocab_to_int = None

    def size(self) -> int:
        # retornar o numero de noticias no dataset (numero de linhas no arquivo)
        size = len(self.list)
        return size

    def get(self, idx: int) -> Tuple[Any, str]:
        # ler a i-esima noticia do disco e retornar o texto como uma string e
        # a classe
        with open(self.list[idx][0], 'r') as file:
            text = file.read()
        
        # converte o texto pra representação numerica 
        tokens = self.tokenize(text)
        base_vector = self.text_to_vector(tokens)
        
        
        return base_vector, self.list[idx][1]
        
    def readPath(self, path):
        caminho = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
        filename = caminho + self.path
        dataset = os.path.abspath(os.path.join(os.path.dirname(filename)))
        data = []
        try:
            txt_file = open(filename, 'r')
            lines = txt_file.readlines()
            for i in lines:
                article_class = i.split()
                article_class = [dataset + article_class[0], article_class[1]]
                data.append(article_class)
        except (FileNotFoundError):
            print(f'arquivo nao foi encontrado no diretorio {filename}')
            return 0
        return data

    def tokenize(self, text):
        # Tokeniza o texto
        tokens = word_tokenize(text)
        
        # Converte pra minuscula caso tenha
        tokens = [word.lower() for word in tokens]
        
        # Remove pontuações
        table = str.maketrans('', '', string.punctuation)
        tokens = [word.translate(table) for word in tokens]
        
        # Remove o que não é letra
        tokens = [word for word in tokens if word.isalpha()]
        
        # Remove stop words
        stop_words = set(stopwords.words("portuguese"))
        tokens = [word for word in tokens if not word in stop_words]

        return tokens

    def text_to_vector(self, tokens):
        if not self.vocab:
            word_counts = Counter(tokens)
            self.vocab = sorted(word_counts, key=word_counts.get, reverse=True)
            self.vocab_to_int = {word: ii for ii, word in enumerate(self.vocab)}

        # Converte acrescenta os tokens de palavras em um vetor
        vector = np.zeros(len(self.vocab), dtype=np.int32)
        if tokens:
            for word in tokens:
                if word in self.vocab_to_int:
                    vector[self.vocab_to_int[word]] += 1
        #O classificador nao conseguir fazer a expressão matematica com arrays diferentes
        #então implementei essas duas linhas seguintes pros arrays terem o mesmo tamanho, 
        #e os espaços vazios eu preenchi com zeros
        max_len = 400
        vector = np.pad(vector, (0, max_len - len(vector)), 'constant')
        return vector