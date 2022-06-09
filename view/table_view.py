from fastapi import APIRouter
from controller import Table
from fastapi.responses import JSONResponse


router = APIRouter()


 
@router.get("/")
async def create_table():
   json_response = await Table.JSONTable()
   return json_response


    