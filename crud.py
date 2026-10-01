from sqlalchemy import or_
from sqlalchemy.orm import Session

from app import models
from app.schemas import PriorityEnum, StatusEnum, TaskCreate, TaskUpdate


def create_task(db: Session, task_data: TaskCreate):
    new_task = models.Task(
        title=task_data.title,
        description=task_data.description,
        priority=task_data.priority.value,
        status=task_data.status.value,
        due_date=task_data.due_date,
        assigned_to=task_data.assigned_to
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


def get_all_tasks(
    db: Session,
    status: StatusEnum | None = None,
    priority: PriorityEnum | None = None,
    assigned_to: str | None = None
):
    query = db.query(models.Task)

    if status is not None:
        query = query.filter(
            models.Task.status == status.value
        )

    if priority is not None:
        query = query.filter(
            models.Task.priority == priority.value
        )

    if assigned_to is not None:
        query = query.filter(
            models.Task.assigned_to.ilike(
                f"%{assigned_to}%"
            )
        )

    return query.order_by(models.Task.task_id).all()


def get_task_by_id(db: Session, task_id: int):
    return (
        db.query(models.Task)
        .filter(models.Task.task_id == task_id)
        .first()
    )


def update_task(
    db: Session,
    task_id: int,
    task_data: TaskUpdate
):
    task = get_task_by_id(db, task_id)

    if task is None:
        return None

    task.title = task_data.title
    task.description = task_data.description
    task.priority = task_data.priority.value
    task.status = task_data.status.value
    task.due_date = task_data.due_date
    task.assigned_to = task_data.assigned_to

    db.commit()
    db.refresh(task)

    return task


def delete_task(db: Session, task_id: int):
    task = get_task_by_id(db, task_id)

    if task is None:
        return None

    db.delete(task)
    db.commit()

    return task