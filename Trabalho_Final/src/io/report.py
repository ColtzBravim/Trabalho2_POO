
from typing import Dict



def write_report(path: str, config: Dict, metrics_values) -> None:
    tipo = config['type']
    caminho = config['train_path']
    classificador = config['classifier']
    tempo_treino = metrics_values['training']
    tempo_test = metrics_values['inference']
    acuracia = metrics_values['accuracy']


    with open("report.txt", 'w') as archive:

        archive.write(f"Dataset: {tipo} \n")
        archive.write(f"Path: {caminho} \n")
        archive.write(f"classificador: {classificador}\n")
        archive.write("Tempo de treino: {:.4f} \n".format(tempo_treino))
        archive.write("Tempo de teste: {:.4f} \n".format(tempo_test))
        archive.write("Acuracia: {:.2f} \n".format(acuracia))
        archive.close()

    