from datetime import date
from fastapi import APIRouter, BackgroundTasks, Depends, Request
from pydantic import TypeAdapter
from typing import List

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking, SBookingInfo, SNewBooking
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.exceptions import RoomCannotBeBooked

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


@router.get("/")
async def get_bookings(
    user: Users = Depends(get_current_user)
) -> List[SBookingInfo]:
    return await BookingDAO.find_all(user_id=user.id)


@router.post("/")
async def add_booking(
    room_id: int, 
    date_from: date, 
    date_to: date,
    user: Users = Depends(get_current_user)
) -> List[SBookingInfo]:
    booking = await BookingDAO.add(
        user.id,
        room_id,
        date_from,
        date_to,
    )
    if not booking:
        raise RoomCannotBeBooked
    return booking
