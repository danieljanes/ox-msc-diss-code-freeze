# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from numproto.protobuf.ndarray_pb2 import (
    NDArray as numproto___protobuf___ndarray_pb2___NDArray,
)

from typing import (
    Optional as typing___Optional,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class NumProtoRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def arr(self) -> numproto___protobuf___ndarray_pb2___NDArray: ...

    def __init__(self,
        *,
        arr : typing___Optional[numproto___protobuf___ndarray_pb2___NDArray] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> NumProtoRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"arr"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"arr"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"arr",b"arr"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"arr",b"arr"]) -> None: ...

class NumProtoReply(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def arr(self) -> numproto___protobuf___ndarray_pb2___NDArray: ...

    def __init__(self,
        *,
        arr : typing___Optional[numproto___protobuf___ndarray_pb2___NDArray] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> NumProtoReply: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"arr"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"arr"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"arr",b"arr"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"arr",b"arr"]) -> None: ...
