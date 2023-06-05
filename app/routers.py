from fastapi import APIRouter

from app.records.routers import records_router
from app.users.routers import users_router

base_router = APIRouter()

base_router.include_router(users_router)
base_router.include_router(records_router)
