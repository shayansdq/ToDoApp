import uvicorn

if __name__ == '__main__':
    uvicorn.run('config:app', reload=True, port=8000)