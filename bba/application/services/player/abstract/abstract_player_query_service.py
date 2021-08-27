from abc import ABC, abstractmethod


class AbstractPlayerQueryService(ABC):

    @abstractmethod
    def get_player_by_id(self,pid):
        print('abstract')
        pass

    @abstractmethod
    def get_all_players(self):
        pass

    @abstractmethod
    def get_player_detail(self,pid):
        pass