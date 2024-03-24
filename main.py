from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import drop_tables, create_tables

from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_tables()
    print('Dropping tables...')
    await create_tables()
    print('Creating tables...')
    yield
    print('Reloading apps...')


app = FastAPI(title='Trading App', lifespan=lifespan)
app.include_router(tasks_router)
