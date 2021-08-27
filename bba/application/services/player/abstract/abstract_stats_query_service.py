from abc import ABC, abstractmethod


class AbstractPlayerStatsQueryService(ABC):

    @abstractmethod
    def get_player_stats_by_id(self,pid):
        pass

