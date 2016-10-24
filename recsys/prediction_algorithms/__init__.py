"""
The :mod:`prediction_algorithms` package includes the prediction algorithms
available for recommendation.

The available prediction algorithms are:

.. autosummary::
    :nosignatures:

    random_pred.NormalPredictor
    baseline_only.BaselineOnly
    knns.KNNBasic
    knns.KNNWithMeans
    knns.KNNBaseline
"""

from .bases import AlgoBase
from .random_pred import NormalPredictor
from .baseline_only import BaselineOnly
from .knns import KNNBasic
from .knns import KNNBaseline
from .knns import KNNWithMeans
