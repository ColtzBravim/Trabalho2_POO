
from typing import Any
import argparse

class DummyArgs:
    """ Essa classe eh so para exemplo e nao devera existir
    na versao final do codigo. Ela foi criada porque a forma
    de usar os argumentos de linha de comando depois sera
    similar.
    """
    def __init__(self,configs='',reports=''):
        self.config_path = configs
        self.report_path = reports


def parse_args() -> Any:
    parser = argparse.ArgumentParser(description='Alguma coisa digitada!!')
    
    #Adicionar os argumentos com o metodo add_argument():
    parser.add_argument('configs', type=str, help= 'Arquivo JSON com as configurações')
    parser.add_argument('reports',type=str, help= 'Arquivo .txt com os reports')
    args = parser.parse_args()
    # Exemplo. Utilizar o argparse na versao final
    configs = f'/data/configs/{args.configs}'
    reports = f'/data/configs/{args.reports}'
    return DummyArgs(configs,reports)
