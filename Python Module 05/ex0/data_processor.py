from abc import ABC, abstractmethod
from typing import Any

class DataProcessor(ABC):
    def __init__(self, data: Any):
        self.validate(data)

    @abstractmethod
    def validate(self, data: Any) -> bool:
        '''
        returns a bool that says if the data can be processed
        '''
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        '''
        In case the user
        does not validate the data before calling ingest, and provides invalid data, an
        exception must be raised
        '''
        pass

    def output(self) -> tuple[int, str]:
        print(0, "output ingested data")
        return 0, "output ingested data"


class NumericProcessor(DataProcessor):
    def __init__(self, data: Any):
        super().__init__(data=data)

    def validate(self, data: Any) -> bool:
        '''
        returns a bool that says if the data can be processed
        '''
        print(f"type is {"string" if type(data).__name__ == 'str' else "not string"}")

        return True

    def ingest(self, data: float) -> None:
        '''
        In case the user
        does not validate the data before calling ingest, and provides invalid data, an
        exception must be raised
        '''
        return None


# class TextProcessor(DataProcessor):
#     def validate(self, data: Any) -> bool:
#         '''
#         returns a bool that says if the data can be processed
#         '''
#         return True

#     def ingest(self, data: str) -> None:
#         '''
#         In case the user
#         does not validate the data before calling ingest, and provides invalid data, an
#         exception must be raised
#         '''
#         return None


# class LogProcessor(DataProcessor):
#     def validate(self, data: Any) -> bool:
#         '''
#         returns a bool that says if the data can be processed
#         '''
#         return True



if __name__ == '__main__':
    print("=== Code Nexus - Data Processor ===")
    print("\nTesting Numeric Processor...")
    NumericProcessor("adsad")
