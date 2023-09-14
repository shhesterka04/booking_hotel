from datetime import date

from fastapi import APIRouter, Depends

from app.exceptions import RoomCannotBooked
from app.users.models import Users
from app.bookings.dao import BookingDAO
from app.users.dependencies import get_current_user

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)


@router.get("")
async def get_booking(user: Users = Depends(get_current_user)):
    return await BookingDAO.find_all(user_id=user.id)


@router.post("")
async def add_booking(room_id: int, date_from: date, date_to: date, user: Users = Depends(get_current_user)):
    booking = await BookingDAO.add(user.id, room_id, date_from, date_to)
    if not booking:
        raise RoomCannotBooked
