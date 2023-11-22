import uvicorn
from fastapi import FastAPI

app = FastAPI()

d = {}
datei = open("Uebung_07/PLZO_CSV_LV95.csv", encoding="utf-8")
next(datei)

for line in datei:
    data = line.strip().split(";")
    ortschaftsname = data[0]
    plz = data[1]
    zusatzziffer = data[2]
    gemeinde = data[3]
    bfs_nr = data[4]
    kanton = data[5]
    e_koord = data[6]
    n_koord = data[7]
    sprache = data[8]
    d[gemeinde] = {
        "ortschaftsname": ortschaftsname,
        "plz": plz,
        "zusatzziffer": zusatzziffer,
        "gemeindename": gemeinde,
        "bfs-nr": bfs_nr,
        "kantonskuerzel": kanton,
        "E": e_koord,
        "N": n_koord,
        "Sprache": sprache
    }
datei.close()


@app.get("/search")
async def search(gemeinde: str):
    if gemeinde in d:
        return d[gemeinde]
    else:
        return {"error": "not found"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


