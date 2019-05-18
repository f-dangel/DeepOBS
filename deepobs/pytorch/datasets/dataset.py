# -*- coding: utf-8 -*-
import abc
from .. import config
"""Base class for DeepOBS datasets."""

# pylint: disable=too-many-instance-attributes, too-few-public-methods
class DataSet(abc.ABC):
    """Base class for DeepOBS data sets.

  Args:
    batch_size (int): The mini-batch size to use.

  Methods:
     _make_train_dataloader: Creates a torch data loader for the training data with batches of size batch_size.
     _make_train_eval_dataloader: Creates a torch data loader for the training evaluation data with batches of size batch_size.
     _make_test_dataloader: Creates a torch data loader for the test data with batches of size batch_size.

  """

    def __init__(self, batch_size):
        """Creates a new DataSet instance.

    Args:
      batch_size (int): The mini-batch size to use.
    """
        self._batch_size = batch_size

        if config.get_default_device() == 'cuda':
            self._pin_memory = True
        else:
            self._pin_memory = False

        self._train_dataloader = self._make_train_dataloader()
        self._train_eval_dataloader = self._make_train_eval_dataloader()
        self._test_dataloader = self._make_test_dataloader()

    @abc.abstractmethod
    def _make_train_dataloader(self):
        """Creates the training data loader.

    Returns:
      A torch.utils.data.DataLoader instance with batches of training data.
    """
        pass

    @abc.abstractmethod
    def _make_train_eval_dataloader(self):
        """Creates the train eval data loader.

    Returns:
      A torch.utils.data.DataLoader instance with batches of training eval data.
    """
        pass

    @abc.abstractmethod
    def _make_test_dataloader(self):
        """Creates the test data loader.

    Returns:
      A torch.utils.data.DataLoader instance with batches of test data.
    """
        pass