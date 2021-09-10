from fastapi import FastAPI
# from fastapi.testclient import TestClient
import uvicorn
import random
import pytest

app = FastAPI()

@app.get("/")
async def root():
    result = random.choice(["HEADS!", "TAILS!"])
    return {"Message":"hELLO, wELCOME tO cOINtOSS", "Drumroll...it's :": result}

# client = TestClient(app)

# def test_root():
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"Message":"hELLO, wELCOME tO cOINtOSS", "Drumroll...it's :": "Heads!"} or response.json() == {"Message":"hELLO, wELCOME tO cOINtOSS", "Drumroll...it's :": "Tails!"}
    
if __name__=="__main__":
    uvicorn.run(app,port=8080, host='0.0.0.0')
