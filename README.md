# Duty Slip Generator

A professional web application for generating vehicle duty slips and maintaining a digital log of trips in Excel format. Built with **FastAPI**, **Pandas**, and **HTML/CSS**.

## 🚀 Features

-   **Digital Duty Slips**: Generate clean, printable duty slips instantly.
-   **Excel Integration**: Automatically saves every trip detail to a local Excel file (`duty_slips.xlsx`).
-   **Data Consistency**: Appends new records row-by-row to the existing Excel sheet.
-   **Calculation**: Automatically calculates total kilometers and total hours.
-   **Responsive Design**: Modern, premium UI that works on desktop and mobile.

## 🛠️ Tech Stack

-   **Backend**: Python (FastAPI)
-   **Data Handling**: Pandas, OpenPyXL
-   **Frontend**: HTML5, CSS3 (Custom Premium Design), Jinja2 Templates

## 📋 Prerequisites

-   Python 3.8 or higher installed on your system.

## ⚙️ Installation & Running Locally

Follow these steps to set up and run the project on your local machine:

1.  **Navigate to the project directory**:
    ```bash
    cd "Duty Slip Generator"
    ```

2.  **Install Dependencies**:
    Install the required Python packages using pip:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Application**:
    Start the local development server:
    ```bash
    uvicorn main:app --reload
    ```
    *Note: `uvicorn` will start the server at `http://127.0.0.1:8000`*

4.  **Access the App**:
    Open your web browser and go to:
    [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 📂 Project Structure

-   `main.py`: The core application logic and API endpoints.
-   `templates/`: Contains HTML files (`index.html` for the form, `slip.html` for the receipt).
-   `static/`: Contains the CSS stylesheet (`style.css`).
-   `duty_slips.xlsx`: The Excel file where records are stored (automatically created if missing).

## 📝 Usage

1.  Fill in the trip details (Booked By, User Names, Cab Number, KMS, Time, etc.).
2.  Click **"Generate Duty Slip"**.
3.  The trip is saved to Excel instantly.
4.  Print the generated slip or create a new one.
5.  Download the full Excel record log from the homepage if needed.
