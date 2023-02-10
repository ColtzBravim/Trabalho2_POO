
from typing import Dict, List,Tuple
from .classifier_interface import ClassifierInterface
from src.datasets.dataset_interface import DatasetInterface
import numpy as np
import collections


class KnnClassifier(ClassifierInterface):
    def __init__(self) -> None:
        super().__init__()
        self.train_data = None
        self.train_labels = None


    def train(self, train_dataset:DatasetInterface) -> None:
        List = []
        for idx in range(train_dataset.size()):
            base_vector, label = train_dataset.get(idx)
            List.append((base_vector, label))

        self.train_data = np.array([d for d, _ in List])
        self.train_labels = [l for _, l in List]
        

    def predict(self, test_dataset:DatasetInterface, k:int = 5) -> List[str]:
        List=[]
        for idx in range(test_dataset.size()):
            base_vector, _ = test_dataset.get(idx)
            List.append(base_vector)

        predictions = []

        def dist(a, b):
            a = a.astype(np.float)
            b = b.astype(np.float)
            return np.sum((a - b)**2)**0.5

        for sample in List:

            distances = [dist(sample, t) for t in self.train_data]

            nearest_indices = np.argsort(distances)[:k].tolist()

            nearest_labels = []
            for i in nearest_indices:
                nearest_labels.append(self.train_labels[i])


            prediction = collections.Counter(nearest_labels).most_common(1)[0][0]
            predictions.append(prediction)
       
        return predictions