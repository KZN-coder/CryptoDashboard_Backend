from fastapi import APIRouter

from .moduls import cmc_client

router = APIRouter(
    prefix="/cryptocurrencies"
)

@router.get("")
async def get_cryptocurrencies():
    return await cmc_client.get_listings()

@router.get("/{currency_id}")
async def get_cryptocyrrecy(currency_id: int):
    return await cmc_client.get_currency(currency_id=currency_id)