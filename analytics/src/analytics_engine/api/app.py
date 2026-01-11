from fastapi import FastAPI

app = FastAPI()

# FastAPI app entrypoint
@app.get("/health")
def health(): return {"status":"ok"}
@app.get("/ready")
def ready(): return {"ready":True}
