import os
import json

from fastapi import FastAPI
import uvicorn


app = FastAPI()

# @app.get("/")
# async def read_root():
#     return {"message": "欢迎使用 FastAPI!"}

@app.get("/get_news")
async def read_item(query: str):
    file_name = f'{query}.json'

    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf8') as f:
            data = json.load(f)
            return data
    else:
        from duckducksearch import duck_search, save_search_res
        search_res = duck_search(query=query)
        save_search_res(query=query, data=search_res)
        return search_res



if __name__ == '__main__':
    server_ip = '0.0.0.0'
    server_port = 8900
    uvicorn.run(app, host=server_ip, port=server_port)