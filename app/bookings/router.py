from fastapi import APIRouter
from sqlalchemy import select

from app.bookings.models import Bookings
from app.bookings.schemas import SBooking
from app.database import async_session_maker
from app.bookings.dao import BookingDAO

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"]
)


@router.get("")
async def get_booking() -> list[SBooking]:
    async with async_session_maker() as session:
        return await BookingDAO.find_all()
