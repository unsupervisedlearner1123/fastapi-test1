from fastapi import FastAPI
import uvicorn
import random
import pytest

app = FastAPI()

@app.get("/")
async def root():
    result = random.choice(["HEADS!", "TAILS!"])
    return {"Message":"hELLO, wELCOME tO cOINtOSS", "Drumroll...it's :": result}

if __name__=="__main__":
    uvicorn.run(app,port=8080, host='0.0.0.0')
