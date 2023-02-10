from typing import Dict, List, Tuple
from .classifier_interface import ClassifierInterface
from src.datasets.dataset_interface import DatasetInterface
import numpy as np
import collections


class NearestCentroidClassifier(ClassifierInterface):
    def __init__(self) -> None:
        super().__init__()
        self.train_data = None
        self.train_labels = None
        self.centroids = {}

    def train(self, train_dataset: DatasetInterface) -> None:
        """ calcular os centroides por classe """
        List = []
        for idx in range(train_dataset.size()):
            img_vector, label = train_dataset.get(idx)
            List.append((img_vector, label))

        self.train_data = np.array([d for d, _ in List])
        self.train_labels = [l for _, l in List]

        unique_labels = set(self.train_labels)
        for label in unique_labels:
            label_indices = np.where(np.array(self.train_labels) == label)[0]
            samples = self.train_data[label_indices, :]
            self.centroids[label] = np.mean(samples, axis=0)

    def predict(self, test_dataset: DatasetInterface) -> List[str]:
        """ para cada amostra no dataset, buscar o centroide mais proximo e respectiva retornar a classe """
        List = []
        for idx in range(test_dataset.size()):
            img_vector, _ = test_dataset.get(idx)
            List.append(img_vector)

        predictions = []
        for sample in List:
            distances = [np.sum((sample - centroid)**2)**0.5 for centroid in self.centroids.values()]
            nearest_index = np.argmin(distances)
            nearest_label = list(self.centroids.keys())[nearest_index]
            predictions.append(nearest_label)

        return predictions