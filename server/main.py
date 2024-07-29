from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from charts import DataframeManager
import uvicorn

app = FastAPI()

origins = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

df_manager = DataframeManager()
print(df_manager.get_global_indicators())
print(df_manager.main_chart())

@app.get("/")
def read_root():
    return {"message": "OLÁ MUNDO"}

@app.get("/charts")
def read_root():
    try:
        return {
            "results": {
                "globalIndicators": df_manager.get_global_indicators(),
                "mainChart": df_manager.main_chart(),
                "allNaturesChart": df_manager.all_natures_chart(),
                "months": df_manager.get_months(),
            }
        }
    except Exception as e:
        # Log the exception (you can use logging module or print)
        print(f"An error occurred: {e}")
        # Raise an HTTPException with status code 500
        raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)