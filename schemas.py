from datetime import date, datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class PriorityEnum(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class StatusEnum(str, Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"


class TaskBase(BaseModel):
    title: str = Field(
        ...,
        min_length=1,
        max_length=200
    )

    description: str = Field(
        ...,
        min_length=1
    )

    priority: PriorityEnum

    status: StatusEnum

    due_date: date

    assigned_to: str = Field(
        ...,
        min_length=1,
        max_length=100
    )


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    pass


class TaskResponse(TaskBase):
    task_id: int
    created_date: datetime

    model_config = ConfigDict(from_attributes=True)