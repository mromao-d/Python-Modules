from abc import ABC, abstractmethod
from typing import Any


class InvDataException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class DataProcessor(ABC):
    def __init__(self):
        self.stored: dict[int, str | dict] = {}
        self.extractions = 0

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
        does not validate the data before calling ingest,
        and provides invalid data, an
        exception must be raised
        '''
        pass

    def output(self) -> tuple[int, str]:
        if len(self.stored) == 0:
            return 0, ""
        extractions = min(len(self.stored), self.extractions)
        extractions = max(extractions, 0)
        print(f"Extracting {extractions} values...")
        for i in range(0, extractions):
            min_val = min(list(self.stored.keys()))
            txt = self.stored[min_val]
            print(f"Numeric Value {min_val}: {txt}")
            self.stored.pop(min_val)
        return 1, "text"


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        '''
        returns a bool that says if the data can be processed
        '''
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            if not all(isinstance(el, (int, float)) for el in data):
                return False
            return True
        return False

    def ingest(self, data: int | float | list) -> None:
        '''
        In case the user
        does not validate the data before calling ingest,
        and provides invalid data, an
        exception must be raised
        '''
        try:
            if not self.validate(data):
                raise InvDataException("Got exception: Improper numeric data")
            print(f"processing data: {data}")
            if isinstance(data, (int, float)):
                new_key = max(self.stored.keys(), default=-1) + 1
                self.stored.update({new_key: str(data)})
                return None
            else:
                i = 0
                for el in data:
                    new_key = max(self.stored.keys(), default=-1) + 1
                    self.stored.update({new_key: str(el)})
                    i += 1
                return None

        except InvDataException as e:
            print(e)


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        '''
        returns a bool that says if the data can be processed
        '''
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            if not all(isinstance(el, str) for el in data):
                return False
            return True
        return False

    def ingest(self, data: int | float | list) -> None:
        '''
        In case the user
        does not validate the data before calling ingest,
        and provides invalid data, an
        exception must be raised
        '''
        try:
            if not self.validate(data):
                raise InvDataException("Got exception: Improper numeric data")
            print(f"processing data: {data}")
            if isinstance(data, data):
                new_key = max(self.stored.keys(), default=-1) + 1
                self.stored.update({new_key: str(data)})
                return None
            else:
                i = 0
                for el in data:
                    new_key = max(self.stored.keys(), default=-1) + 1
                    self.stored.update({new_key: str(el)})
                    i += 1
                return None

        except InvDataException as e:
            print(e)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        '''
        returns a bool that says if the data can be processed
        '''
        if isinstance(data, dict):
            return True
        if isinstance(data, list):
            if not all(isinstance(el, dict) for el in data):
                return False
            return True
        return False

    def ingest(self, data: dict) -> None:
        '''
        In case the user
        does not validate the data before calling ingest,
        and provides invalid data, an
        exception must be raised
        '''
        try:
            if not self.validate(data):
                raise InvDataException("Got exception: Improper numeric data")
            print(f"processing data: {data}")
            if isinstance(data, dict):
                new_key = max(self.stored.keys(), default=-1) + 1
                self.stored.update({new_key: str(data)})
                return None
            else:
                i = 0
                for el in data:
                    new_key = max(self.stored.keys(), default=-1) + 1
                    self.stored.update({new_key: el})
                    i += 1
                return None

        except InvDataException as e:
            print(e)

    def output(self) -> tuple[int, str]:
        if len(self.stored) == 0:
            return 0, ""
        extractions = min(len(self.stored), self.extractions)
        extractions = max(extractions, 0)
        print(f"Extracting {extractions} values...")
        for i in range(0, extractions):
            min_val = min(list(self.stored.keys()))
            txt = self.stored[min_val]
            print(f"Numeric Value {min_val}:\
{txt.get('log_level')}: {txt.get('log_message')}")
            self.stored.pop(min_val)
        return 1, "text"


if __name__ == '__main__':
    print("=== Code Nexus - Data Processor ===")
    print("\nTesting Numeric Processor...")
    testNumeric = NumericProcessor()
    for el in [42, 'Hello', [1, 2, 4, 5], [1, "2", 4, 5]]:
        print(f"Trying to validate input {el}: {testNumeric.validate(el)}")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    testNumeric.ingest("fo")
    testNumeric.ingest(1)
    testNumeric.extractions = 3
    testNumeric.ingest([1, 2, 3, 4, 5])
    testNumeric.output()

    print()

    print("\nTesting Text Processor...")
    testString = TextProcessor()
    for el in [42, 'Hello', ['Hello', 'Nexus', 'World'], [1, "2", 4, 5]]:
        print(f"Trying to validate input {el}: {testString.validate(el)}")
    testString.ingest(['Hello', 'Nexus', 'World'])
    testString.extractions = 1
    testString.output()

    print()

    print("\nTesting Log Processor...")
    testLog = LogProcessor()
    elements = ['Hello', {'log_level': 'NOTICE',
                          'log_message': 'Connection to server'},
                [{'log_level': 'NOTICE',
                  'log_message': 'Connection to server'},
                {'log_level': 'ERROR',
                 'log_message': 'Unauthorized access!!'}]]
    for el in elements:
        print(f"Trying to validate input {el}: {testLog.validate(el)}")
    testLog.ingest([{'log_level': 'NOTICE',
                     'log_message': 'Connection to server'},
                    {'log_level': 'ERROR',
                     'log_message': 'Unauthorized access!!'}])
    testLog.extractions = 2
    testLog.output()
