
from typing import List


def accuracy(true_classes: List[str], predicted_classes: List) -> float:
    '''Calcula a porcentagem de acerto """'''
    if predicted_classes:
        correct = sum([1 for t, p in zip(true_classes, predicted_classes) if t == p])
        return correct / len(true_classes) * 100
    else:
        return 0