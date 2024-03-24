from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId

router = APIRouter(prefix='/tasks', tags=['Tasks'])


@router.post("")
async def create_task(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    task_id = await TaskRepository.add_task(task)
    return {"message": "Task added", "task_id": task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.get_all_tasks()
    return tasks
