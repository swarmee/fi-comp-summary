from datetime import date
from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum



class ReportType(str, Enum):
    internationalFundsTransferInstruction = "internationalFundsTransferInstruction"
    crossBorderMovementReport             = "crossBorderMovementReport"
    suspiciousMatterReport                = "suspiciousMatterReport"
    thresholdTransactionReport            = "thresholdTransactionReport"        


class Summary(BaseModel):
    reportCount: int
    totalAmount: float  # Use float for dollar amounts with cents
    reporter: str
    reportType: ReportType
    transactionMonth: date

    class Config:
        schema_extra = {
            "example": {
                "reportCount": 374,
                "totalAmount": 686568.91,
                "reporter": "paypal",
                "reportType": "internationalFundsTransferInstruction",
                "transactionMonth": "2019-12-01",
            }
        }


app = FastAPI(title="FI-Comp Summary Data API", version="0.0.1")

@app.get("/fi-comp-summary/data/", response_model=list[Summary], tags=["Summary Data"])
def return_summary_data():
    return [
        {
            "reportCount": 374,
            "totalAmount": 686568.91,
            "reporter": "paypal",
            "reportType": "internationalFundsTransferInstruction",
            "transactionMonth": "2019-12-01",
        }
    ]

@app.get("/fi-comp-summary/", tags=["Summary Data"], response_class=HTMLResponse)
def return_summary_html_page(reporter: str = None, reportType: ReportType = None, transactionMonth : date = None):
    return """"""
