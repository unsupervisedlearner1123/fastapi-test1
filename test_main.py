from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest
from main import app

client = TestClient(app)

def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message":"hELLO, wELCOME tO cOINtOSS", "Drumroll...it's :": "HEADS!"} or response.json() == {"Message":"hELLO, wELCOME tO cOINtOSS", "Drumroll...it's :": "TAILS!"}
    
test_main()