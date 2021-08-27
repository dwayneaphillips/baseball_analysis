from abc import ABC, abstractmethod

from pymongo import MongoClient


class AbstractRepository(ABC):

    @abstractmethod
    def get_by_id(self, pid):
        pass

    @abstractmethod
    def get_all(self):
        pass
