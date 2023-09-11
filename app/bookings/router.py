from fastapi import APIRouter, Depends
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
