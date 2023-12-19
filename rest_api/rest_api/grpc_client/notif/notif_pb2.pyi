from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Notif(_message.Message):
    __slots__ = ("id", "description", "date", "from_user_id", "to_user_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    FROM_USER_ID_FIELD_NUMBER: _ClassVar[int]
    TO_USER_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    description: str
    date: str
    from_user_id: int
    to_user_id: int
    def __init__(self, id: _Optional[int] = ..., description: _Optional[str] = ..., date: _Optional[str] = ..., from_user_id: _Optional[int] = ..., to_user_id: _Optional[int] = ...) -> None: ...

class SendNotifRequest(_message.Message):
    __slots__ = ("from_user_id", "to_user_id", "description", "date")
    FROM_USER_ID_FIELD_NUMBER: _ClassVar[int]
    TO_USER_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    from_user_id: int
    to_user_id: int
    description: str
    date: str
    def __init__(self, from_user_id: _Optional[int] = ..., to_user_id: _Optional[int] = ..., description: _Optional[str] = ..., date: _Optional[str] = ...) -> None: ...

class SendNotifResponse(_message.Message):
    __slots__ = ("id", "description", "date", "from_user_id", "to_user_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    FROM_USER_ID_FIELD_NUMBER: _ClassVar[int]
    TO_USER_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    description: str
    date: str
    from_user_id: int
    to_user_id: int
    def __init__(self, id: _Optional[int] = ..., description: _Optional[str] = ..., date: _Optional[str] = ..., from_user_id: _Optional[int] = ..., to_user_id: _Optional[int] = ...) -> None: ...

class GetNotifsRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class GetNotifsResponse(_message.Message):
    __slots__ = ("notifs",)
    NOTIFS_FIELD_NUMBER: _ClassVar[int]
    notifs: _containers.RepeatedCompositeFieldContainer[Notif]
    def __init__(self, notifs: _Optional[_Iterable[_Union[Notif, _Mapping]]] = ...) -> None: ...

class DeleteNotifRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class DeleteNotifResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...
