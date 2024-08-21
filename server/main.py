from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from charts import global_indicators, main_chart, natures_chart, month_chart
import uvicorn

app = FastAPI()

origins = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
    "http://127.0.0.1:3001",
    "http://localhost:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    try:
        return {
            "results": {
                "globalIndicators": global_indicators.GlobalIndicators().get_datas(),
                "mainChart": main_chart.MainChart().get_datas(),
                "allNaturesChart": natures_chart.NaturesChart().get_datas(),
                "byMonthChart": month_chart.MonthChart().get_datas(),
                "months": month_chart.MonthChart().get_months(),
            }
        }
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)