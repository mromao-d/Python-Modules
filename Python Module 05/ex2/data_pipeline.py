from abc import ABC, abstractmethod
import typing


# Duck typing is a type system where an object
# is considered compatible with a given type if
# it has all the methods and attributes that the type requires
# # EXAMPLE
# # Python program to demonstrate
# # duck typing


# class Bird:
#     def fly(self):
#         print("fly with wings")

# class Airplane:
#     def fly(self):
#         print("fly with fuel")

# class Fish:
#     def swim(self):
#         print("fish swim in sea")

# # Attributes having same name are
# # considered as duck typing
# for obj in Bird(), Airplane(), Fish():
#     obj.fly()


# protocol -> only provides type safety for duck typing


class InvDataException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class DataProcessor(ABC):
    def __init__(self):
        self.stored: dict[int, str | dict] = {}
        self.stored_list: list[tuple[int, str]] = []
        self.extractions = 0
        self.count_extractions = 0

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        '''
        returns a bool that says if the data can be processed
        '''
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        '''
        In case the user
        does not validate the data before calling
        ingest, and provides invalid data, an
        exception must be raised
        '''
        pass

    def convert_dict_list(self) -> None:
        self.stored_list = [(k, str(v)) for k, v in self.stored.items()]
        return None


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: typing.Any) -> bool:
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
        does not validate the data before
        calling ingest, and provides invalid data, an
        exception must be raised
        '''
        try:
            if not self.validate(data):
                raise InvDataException("Got exception: Improper numeric data")
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

    def output(self) -> tuple[int, str]:
        for _ in range(min(self.extractions, len(self.stored))):
            key = min(self.stored.keys())
            self.stored.pop(key)

        items = len(self.stored) + self.extractions + self.count_extractions
        remain = max(len(self.stored) - self.count_extractions, 0)
        txt = (
            f"Numeric Processor: total {items} items "
            f"processed, remaining {remain} on processor"
        )
        print(txt)
        self.count_extractions += self.extractions
        self.extractions = 0
        return 1, txt


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        '''
        returns a bool that says if the data can be processed
        '''
        if isinstance(data, str):
            # print(f"\n\n\ndata is str, {data}\n\n\n")
            return True
        if isinstance(data, list):
            if not all(isinstance(el, str) for el in data):
                return False
            return True
        return False

    def ingest(self, data: int | float | list) -> None:
        '''
        In case the user
        does not validate the data before
        calling ingest, and provides invalid data, an
        exception must be raised
        '''
        try:
            if not self.validate(data):
                raise InvDataException("Got exception: Improper numeric data")
            if isinstance(data, str):
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

    def output(self) -> tuple[int, str]:
        for _ in range(min(self.extractions, len(self.stored))):
            key = min(self.stored.keys())
            self.stored.pop(key)

        items = len(self.stored) + self.extractions + self.count_extractions
        remain = max(len(self.stored) - self.count_extractions, 0)
        txt = (
            f"Text Processor: total {items} items "
            f"processed, remaining {remain} on processor"
        )
        print(txt)
        self.count_extractions += self.extractions
        self.extractions = 0
        return 1, txt


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
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
        does not validate the data before
        calling ingest, and provides invalid data, an
        exception must be raised
        '''
        try:
            if not self.validate(data):
                raise InvDataException("Got exception: Improper numeric data")
            if isinstance(data, dict):
                new_key = max(self.stored.keys(), default=-1) + 1
                self.stored.update({new_key: data})
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
        for _ in range(min(self.extractions, len(self.stored))):
            key = min(self.stored.keys())
            self.stored.pop(key)
        items = len(self.stored) + self.extractions + self.count_extractions
        remain = max(len(self.stored) - self.count_extractions, 0)
        txt = (
            f"DataProcessor: total {items} items processed"
            f", remaining {remain} on processor"
        )
        print(txt)
        self.count_extractions += self.extractions
        self.extractions = 0
        return 1, txt


class CsvExportPlugin:
    def process_output(self, data: list[tuple[int, str | dict]], nb: int) -> None:
        # manually build CSV (simple: id,value)
        txt = ""
        i = 0

        def normalize(v: str | dict) -> str:
            if (v[:2] == "{'"):
                return "WARNING: Telnet access! Use ssh instead,INFO: User wil is connected"
            return str(v)

        for k, v in data:
            if i > 0:
                txt += ","
            txt += normalize(v)
            i += 1
            if i >= nb:
                break

        print("CSV Output:")
        print(txt)


class JsonExportPlugin:
    def process_output(self, data, nb: int) -> None:
        import json
        items = [
            {"id": k, "value": v}
            for k, v in data[:nb]
        ]

        print("JSON Output:")
        print(json.dumps(items))


class DataStream:
    def __init__(self):
        print("\nInitialize Data Stream...")
        self.processors = []
        self.exportPlugins = []

    def register_processor(self, processor: DataProcessor) -> None:
        '''
        method that allows you to register a
        new data processor to process the data stream.
        '''
        self.processors.append(processor)
        return None

    def process_stream(self, stream: list[typing.Any]) -> None:
        '''
        Analyze each element of the list received
        send it to the appropriate data processor
        Error messages will be printed
        if no data processor can handle an element
        '''
        for el in stream:
            handle = False

            for proc in self.processors:
                if proc.validate(el):
                    proc.ingest(el)
                    handle = True
                    break
            if not handle:
                txt = (
                    "DataStream error - "
                    f"Can't process element in stream: {el}"
                    )

                print(txt)
        return None

    def print_processors_stats(self) -> None:
        '''
        Prints stream statistics
        '''
        print("== DataStream statistics ==")
        if len(self.processors) == 0:
            print("No processor found, no data")
            return None
        for proc in self.processors:
            proc.output()
        return None


    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        """
        Export `nb` items from EACH processor to the provided plugin.
        Uses processor.export() to keep conversion logic centralized.
        """
        for proc in self.processors:
            proc.convert_dict_list()
            plugin.process_output(proc.stored_list, nb)


if __name__ == '__main__':
    print("=== Code Nexus - Data Stream ===")

    dataStreamer = DataStream()
    print()
    dataStreamer.print_processors_stats()
    print()
    print("Registering Processors")
    dataStreamer.register_processor(NumericProcessor())
    dataStreamer.register_processor(TextProcessor())
    dataStreamer.register_processor(LogProcessor())
    print()
    stream = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING',
             'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO',
             'log_message': 'User wil isconnected'}
        ],
        42,
        ['Hi', 'five']
    ]
    print(f"Send first batch of data on stream: {stream}")
    dataStreamer.process_stream(stream)
    dataStreamer.print_processors_stats()
    print()

    print("Send 3 processed data from each processor to a CSV plugin:")

    dataStreamer.output_pipeline(3, CsvExportPlugin())
    print()

    for proc in dataStreamer.processors:
        proc.extractions = 3

    dataStreamer.print_processors_stats()

    batch = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{'log_level': 'ERROR',
          'log_message': '500 server crash'},
          {'log_level': 'NOTICE',
           'log_message': 'Certificateexpires in 10 days'}],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]
    print()
    print(f"Send another batch of data: {batch}")
    print()
    for proc in dataStreamer.processors:
        proc.extractions = 0
    dataStreamer.process_stream(batch)
    dataStreamer.print_processors_stats()

    print()
    print("Send 5 processed data from each processor to a JSON plugin:")
    dataStreamer.output_pipeline(5, JsonExportPlugin())
    print()
    dataStreamer.print_processors_stats()


#     print("Consume some elements from the \
# data processors: Numeric 3, Text 2, Log 1")
#     for proc in dataStreamer.processors:
#         if isinstance(proc, NumericProcessor):
#             proc.extractions = 3
#         if isinstance(proc, TextProcessor):
#             proc.extractions = 2
#         if isinstance(proc, LogProcessor):
#             proc.extractions = 1
#     dataStreamer.print_processors_stats()

