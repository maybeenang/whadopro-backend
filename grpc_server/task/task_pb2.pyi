from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Task(_message.Message):
    __slots__ = ("id", "title", "description", "status", "date", "project_id", "user_ids")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    description: str
    status: str
    date: str
    project_id: int
    user_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., status: _Optional[str] = ..., date: _Optional[str] = ..., project_id: _Optional[int] = ..., user_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class TaskListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TaskListResponse(_message.Message):
    __slots__ = ("tasks",)
    TASKS_FIELD_NUMBER: _ClassVar[int]
    tasks: _containers.RepeatedCompositeFieldContainer[Task]
    def __init__(self, tasks: _Optional[_Iterable[_Union[Task, _Mapping]]] = ...) -> None: ...

class TaskRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class TaskResponse(_message.Message):
    __slots__ = ("task",)
    TASK_FIELD_NUMBER: _ClassVar[int]
    task: Task
    def __init__(self, task: _Optional[_Union[Task, _Mapping]] = ...) -> None: ...

class TaskCreateRequest(_message.Message):
    __slots__ = ("title", "description", "status", "date", "project_id", "user_ids")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    status: str
    date: str
    project_id: int
    user_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., status: _Optional[str] = ..., date: _Optional[str] = ..., project_id: _Optional[int] = ..., user_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class TaskCreateResponse(_message.Message):
    __slots__ = ("task",)
    TASK_FIELD_NUMBER: _ClassVar[int]
    task: Task
    def __init__(self, task: _Optional[_Union[Task, _Mapping]] = ...) -> None: ...

class TaskUpdateRequest(_message.Message):
    __slots__ = ("id", "title", "description", "status", "date", "user_ids")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    description: str
    status: str
    date: str
    user_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., status: _Optional[str] = ..., date: _Optional[str] = ..., user_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class TaskUpdateResponse(_message.Message):
    __slots__ = ("task",)
    TASK_FIELD_NUMBER: _ClassVar[int]
    task: Task
    def __init__(self, task: _Optional[_Union[Task, _Mapping]] = ...) -> None: ...

class TaskDeleteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class TaskDeleteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TaskUpdateStatusRequest(_message.Message):
    __slots__ = ("id", "status")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: int
    status: str
    def __init__(self, id: _Optional[int] = ..., status: _Optional[str] = ...) -> None: ...

class TaskUpdateStatusResponse(_message.Message):
    __slots__ = ("task",)
    TASK_FIELD_NUMBER: _ClassVar[int]
    task: Task
    def __init__(self, task: _Optional[_Union[Task, _Mapping]] = ...) -> None: ...

class TaskGetByProjectRequest(_message.Message):
    __slots__ = ("project_id",)
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: int
    def __init__(self, project_id: _Optional[int] = ...) -> None: ...

class TaskGetByProjectResponse(_message.Message):
    __slots__ = ("tasks",)
    TASKS_FIELD_NUMBER: _ClassVar[int]
    tasks: _containers.RepeatedCompositeFieldContainer[Task]
    def __init__(self, tasks: _Optional[_Iterable[_Union[Task, _Mapping]]] = ...) -> None: ...

class TaskGetByUserRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class TaskGetByUserResponse(_message.Message):
    __slots__ = ("tasks",)
    TASKS_FIELD_NUMBER: _ClassVar[int]
    tasks: _containers.RepeatedCompositeFieldContainer[Task]
    def __init__(self, tasks: _Optional[_Iterable[_Union[Task, _Mapping]]] = ...) -> None: ...
