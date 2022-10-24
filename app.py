from fastapi import FastAPI, APIRouter
from routers import user_routers

app = FastAPI()
router = APIRouter()

@router.get('/')
def hello_world():
    # btc = requests.get("https://www.mercadobitcoin.net/api/btc/ticker").content
    # return [btc]
    return 'hello world'
app.include_router(router)
app.include_router(user_routers)