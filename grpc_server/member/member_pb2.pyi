from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Member(_message.Message):
    __slots__ = ("id", "name", "email", "password")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    email: str
    password: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class MemberListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MemberListResponse(_message.Message):
    __slots__ = ("members",)
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    members: _containers.RepeatedCompositeFieldContainer[Member]
    def __init__(self, members: _Optional[_Iterable[_Union[Member, _Mapping]]] = ...) -> None: ...

class MemberGetRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class MemberGetResponse(_message.Message):
    __slots__ = ("name", "email", "password")
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    name: str
    email: str
    password: str
    def __init__(self, name: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class MemberCreateRequest(_message.Message):
    __slots__ = ("member",)
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    member: Member
    def __init__(self, member: _Optional[_Union[Member, _Mapping]] = ...) -> None: ...

class MemberCreateResponse(_message.Message):
    __slots__ = ("member",)
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    member: Member
    def __init__(self, member: _Optional[_Union[Member, _Mapping]] = ...) -> None: ...

class MemberUpdateRequest(_message.Message):
    __slots__ = ("member",)
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    member: Member
    def __init__(self, member: _Optional[_Union[Member, _Mapping]] = ...) -> None: ...

class MemberUpdateResponse(_message.Message):
    __slots__ = ("member",)
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    member: Member
    def __init__(self, member: _Optional[_Union[Member, _Mapping]] = ...) -> None: ...

class MemberDeleteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class MemberDeleteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
