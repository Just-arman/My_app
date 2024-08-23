from fastapi import FastAPI, Query, Depends
from fastapi.staticfiles import StaticFiles
from typing import Optional
from datetime import date
from pydantic import BaseModel

from app.bookings.router import router as router_bookings
from app.hotels.router import router as router_hotels
from app.hotels.rooms.router import router as router_rooms
from app.users.router import router_users, router_auth

from app.pages.router import router as router_pages
from app.images.router import router as router_images

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), "static")

app.include_router(router_auth)
app.include_router(router_users)
app.include_router(router_hotels)
app.include_router(router_rooms)
app.include_router(router_bookings)

app.include_router(router_pages)
app.include_router(router_images)


