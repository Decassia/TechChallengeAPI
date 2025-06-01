from fastapi import FastAPI

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.v1 import api
from api.v1.api import api_router
from core.settings import settings

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou coloque domínios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




app = FastAPI(title='API - Tech Challenge_01 - Viticultura')
app.include_router(api_router, prefix=settings.API_V1_STR)



if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                log_level='info', reload=True)
