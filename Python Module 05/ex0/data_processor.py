from abc import ABC, abstractmethod
from typing import Any

class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: Any) -> bool:
        '''
        returns a bool that says if the data can be processed
        '''
        return True

    @abstractmethod
    def ingest(self, data: Any) -> None:
        '''
        In case the user
        does not validate the data before calling ingest, and provides invalid data, an
        exception must be raised
        '''
        return None

    def output() -> tuple[int, str]:
        print("output ingested data")


class NumericProcessor(DataProcessor):
    pass


class TextProcessor(DataProcessor):
    pass


class LogProcessor(DataProcessor):
    pass


if __name__ == '__main__':
    DataProcessor()
