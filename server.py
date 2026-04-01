from fastapi import FastAPI

app = FastAPI(
    title="cadweb-api",
    description="Zentrale API des cadweb-Ökosystems",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"status": "cadweb-api running"}

@app.get("/info")
def info():
    return {
        "name": "cadweb-api",
        "version": "0.1.0",
        "modules": [
            "core",
            "llm",
            "cad",
            "tools",
            "agent",
            "io",
            "utils"
        ]
    }
