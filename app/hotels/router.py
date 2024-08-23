from datetime import date, datetime, timedelta
from typing import List, Optional

from fastapi import APIRouter, Depends, Query
from fastapi_cache.decorator import cache

from app.exceptions import CannotBookHotelForLongPeriod, DateFromCannotBeAfterDateTo
from app.hotels.dao import HotelDAO
from app.hotels.schemas import HotelsSearchArgs, SHotel, SHotelInfo

router = APIRouter(
    prefix="/hotels", 
    tags=["Отели"],
)


@router.get("/{location}")
@cache(expire=30)
async def get_hotels_by_location_and_time(
    location: str,
    date_from: Optional[date] = Query(None),
    date_to: Optional[date] = Query(None),
) -> List[SHotelInfo]:
    if date_from > date_to:
        raise DateFromCannotBeAfterDateTo
    if (date_to - date_from).days > 31:
        raise CannotBookHotelForLongPeriod 
    hotels = await HotelDAO.find_all(location, date_from, date_to)
    return hotels


@router.get("/hotels")
def get_hotels(
    search_args: HotelsSearchArgs = Depends()
):
    return search_args




