from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Project(_message.Message):
    __slots__ = ("id", "title", "description", "user_id", "task_ids", "user_ids")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_IDS_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    description: str
    user_id: int
    task_ids: _containers.RepeatedScalarFieldContainer[int]
    user_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., user_id: _Optional[int] = ..., task_ids: _Optional[_Iterable[int]] = ..., user_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class ProjectListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ProjectListResponse(_message.Message):
    __slots__ = ("projects",)
    PROJECTS_FIELD_NUMBER: _ClassVar[int]
    projects: _containers.RepeatedCompositeFieldContainer[Project]
    def __init__(self, projects: _Optional[_Iterable[_Union[Project, _Mapping]]] = ...) -> None: ...

class ProjectGetRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ProjectResponse(_message.Message):
    __slots__ = ("project",)
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: Project
    def __init__(self, project: _Optional[_Union[Project, _Mapping]] = ...) -> None: ...

class ProjectCreateRequest(_message.Message):
    __slots__ = ("title", "description")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class ProjectCreateResponse(_message.Message):
    __slots__ = ("project",)
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: Project
    def __init__(self, project: _Optional[_Union[Project, _Mapping]] = ...) -> None: ...

class ProjectUpdateRequest(_message.Message):
    __slots__ = ("id", "title", "description", "task_ids")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TASK_IDS_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    description: str
    task_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., task_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class ProjectUpdateResponse(_message.Message):
    __slots__ = ("project",)
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: Project
    def __init__(self, project: _Optional[_Union[Project, _Mapping]] = ...) -> None: ...

class ProjectDeleteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ProjectDeleteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ProjectAddTaskRequest(_message.Message):
    __slots__ = ("project_id", "task_id")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: int
    task_id: int
    def __init__(self, project_id: _Optional[int] = ..., task_id: _Optional[int] = ...) -> None: ...

class ProjectAddTaskResponse(_message.Message):
    __slots__ = ("project",)
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: Project
    def __init__(self, project: _Optional[_Union[Project, _Mapping]] = ...) -> None: ...

class ProjectRemoveTaskRequest(_message.Message):
    __slots__ = ("project_id", "task_id")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: int
    task_id: int
    def __init__(self, project_id: _Optional[int] = ..., task_id: _Optional[int] = ...) -> None: ...

class ProjectRemoveTaskResponse(_message.Message):
    __slots__ = ("project",)
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: Project
    def __init__(self, project: _Optional[_Union[Project, _Mapping]] = ...) -> None: ...

class ProjectAddUserRequest(_message.Message):
    __slots__ = ("project_id", "user_id")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: int
    user_id: int
    def __init__(self, project_id: _Optional[int] = ..., user_id: _Optional[int] = ...) -> None: ...

class ProjectAddUserResponse(_message.Message):
    __slots__ = ("project",)
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: Project
    def __init__(self, project: _Optional[_Union[Project, _Mapping]] = ...) -> None: ...

class ProjectRemoveUserRequest(_message.Message):
    __slots__ = ("project_id", "user_id")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: int
    user_id: int
    def __init__(self, project_id: _Optional[int] = ..., user_id: _Optional[int] = ...) -> None: ...

class ProjectRemoveUserResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GenerateLinkProjectRequest(_message.Message):
    __slots__ = ("project_id",)
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: int
    def __init__(self, project_id: _Optional[int] = ...) -> None: ...

class GenerateLinkProjectResponse(_message.Message):
    __slots__ = ("link",)
    LINK_FIELD_NUMBER: _ClassVar[int]
    link: str
    def __init__(self, link: _Optional[str] = ...) -> None: ...
