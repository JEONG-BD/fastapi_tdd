from fastapi import FastAPI
from app.routers.category_router import router as cate_router

import logging.config

#logging.basicConfig(level=logging.DEBUG)

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

app = FastAPI()
app.include_router(cate_router, prefix='/api')
#


@app.get('/')
def root():
    try:
        raise Exception('Simulated debug error occurred')
    except Exception as e:
        logging.debug(f"An exception occurred")
        logging.debug(f"Exception traceback : ", exc_info=True)

    return {"root": "root"}


@app.get('/hello')
def hello():
    return {"hello": "hello fastapi"}