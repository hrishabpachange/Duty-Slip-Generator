from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pandas as pd
import os
from datetime import datetime
import uvicorn

app = FastAPI()

# Mount static files (CSS, HTML form)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

EXCEL_FILE = "duty_slips.xlsx"

# Ensure Excel file exists with headers
if not os.path.exists(EXCEL_FILE):
    df = pd.DataFrame(columns=[
        "Booked By", "User Names", "Cab Number", "Starting Kms", 
        "Closing Kms", "Chauffeur Name", "Trip", "Closing Time", 
        "Reporting Time", "Total Hours", "Date"
    ])
    df.to_excel(EXCEL_FILE, index=False)

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/submit", response_class=HTMLResponse)
async def submit_form(
    request: Request,
    booked_by: str = Form(...),
    user_names: str = Form(...),
    cab_number: str = Form(...),
    starting_kms: int = Form(...),
    closing_kms: int = Form(...),
    chauffeur_name: str = Form(...),
    trip: str = Form(...),
    closing_time: str = Form(...),
    reporting_time: str = Form(...),
    total_hours: float = Form(...)
):
    # Prepare data
    new_data = {
        "Booked By": booked_by,
        "User Names": user_names,
        "Cab Number": cab_number,
        "Starting Kms": starting_kms,
        "Closing Kms": closing_kms,
        "Chauffeur Name": chauffeur_name,
        "Trip": trip,
        "Closing Time": closing_time,
        "Reporting Time": reporting_time,
        "Total Hours": total_hours,
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Append to Excel
    if os.path.exists(EXCEL_FILE):
        try:
            df = pd.read_excel(EXCEL_FILE)
            new_row = pd.DataFrame([new_data])
            df = pd.concat([df, new_row], ignore_index=True)
            df.to_excel(EXCEL_FILE, index=False)
        except PermissionError:
            return HTMLResponse(content="Error: Please close the Excel file 'duty_slips.xlsx' and try again.", status_code=500)
    
    # Render the Duty Slip
    return templates.TemplateResponse("slip.html", {
        "request": request,
        "data": new_data,
        "slip_id": int(datetime.now().timestamp()) # Simple ID generation
    })

@app.get("/download")
async def download_excel():
    if os.path.exists(EXCEL_FILE):
        from fastapi.responses import FileResponse
        return FileResponse(EXCEL_FILE, filename="duty_slips.xlsx", media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    return HTMLResponse("File not found", status_code=404)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
