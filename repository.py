from sqlalchemy import select

from database import new_session, TaskOrm
from schemas import STask, STaskAdd


class TaskRepository:

    @classmethod
    async def add_task(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def get_all_tasks(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_model = result.scalars().all()
            task_schemas = [STask.model_validate(task_model) for task_model in task_model]
            return task_schemas
