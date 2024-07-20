from fastapi import APIRouter, HTTPException,Request
from .utils import getBlockNumber, getTransactions

router = APIRouter()

@router.post("/block-number")
async def block_number(request: Request):
    try:
        data = await request.json()
        latest_block_number = getBlockNumber(data['block_number'])
        return {"block_number": latest_block_number}
    except Exception as e:
        print(request.block_number)
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/transactions")
async def transactions(request: Request):
    try:
        data = await request.json()
        # block_number = data['block_number']?
        transactions = getTransactions(data['block_number'],data['input_number'])
        return {"transactions": transactions}
    except Exception as e:
        raise HTTPException(status_code=500, details = str(e))
