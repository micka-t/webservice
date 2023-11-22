import pyproj
from pyproj import Transformer
import uvicorn
from fastapi import FastAPI

app = FastAPI()


lv95 = "EPSG:2056"
wgs84 = "EPSG:4326"

trans_wgs84lv95 = Transformer.from_crs(wgs84, lv95)
trans_lv95wgs84 = Transformer.from_crs(lv95, wgs84)

@app.get("/wgs84lv95")
async def wgs84lv95(lat: float=0,lng: float=0):
    resultat = trans_wgs84lv95.transform(lat, lng)
    return {"LV95-Koordinaten" : resultat}

@app.get("/lv95wgs84")
async def lv95wgs84(E: float=0,N: float=0):
    resultat = trans_lv95wgs84.transform(E, N)
    return {"WGS84-Koordinaten" : resultat}

uvicorn.run(app, host="127.0.0.1", port=8000)