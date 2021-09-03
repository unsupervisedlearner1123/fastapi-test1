from fastapi import FastAPI
import uvicorn
import random

app = FastAPI()

@app.get("/")
async def root():
    result = random.choice(["Heads!", "Tails!"])
    return {"Message":"hELLO, wELCOME tO cOINtOSS", "Drumroll...it's :": result}
    
if __name__=="__main__":
    uvicorn.run(app,port=8080, host='0.0.0.0')
