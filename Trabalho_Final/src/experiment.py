
from typing import Union, Dict, List
from src.datasets.dataset_interface import DatasetInterface
from src.classifiers.classifier_interface import ClassifierInterface
from src.metrics import accuracy
import time


class Experiment:
    def __init__(self,
                 train_dataset: DatasetInterface,
                 test_dataset: DatasetInterface):
        self.train_dataset = train_dataset
        self.test_dataset = test_dataset
        self.true_classes = self._get_true_classes_from_dataset(
            self.test_dataset)

    def run(self, classifier: ClassifierInterface) -> Dict[str, float]:
        """ executa o experimento """
        start = time.time()
        classifier.train(self.train_dataset)
        end = time.time()
        training_time = (end - start) / self.train_dataset.size()
        
        
        start = time.time()
        pred_classes = classifier.predict(self.test_dataset)
        end = time.time()
        inference_time = (end - start) / self.test_dataset.size()

        
        

        metrics = {
            "accuracy": accuracy(self.true_classes, pred_classes),
            "training": training_time,
            "inference": inference_time
        }
        
        return metrics

    def _get_true_classes_from_dataset(self, dataset: DatasetInterface) -> List[str]:
        true_classes = []
        for idx in range(dataset.size()):
            _, sample_class = dataset.get(idx)
            true_classes.append(sample_class)
        return true_classes
