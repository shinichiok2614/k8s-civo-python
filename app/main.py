# from typing import Union

from fastapi import FastAPI
import os
app = FastAPI()
@app.get("/")
def read_root():
    # return{
    #     "Hello": "Youtube"
    #        }

    #bien env, nếu k có thì gt mặc định DEFAULT_ENV
    return {"Hello": f"From: {os.environ.get('ENV','DEFAULT_ENV')}"}


# @app.get("/items/{item_id}")
# def read_item(item_id:int, q: Union[str, None]=None):
#     return{"item_id": iteam_id, "q": q}