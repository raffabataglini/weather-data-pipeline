Weather Data Pipeline 🌦️
This is an ETL (Extract, Transform, Load) data pipeline developed in Python. The project automates the collection of weather data from a public API, processes the information using Pandas, and stores the results both locally and in the cloud (AWS S3).

🚀 Project Architecture
The pipeline follows a traditional data engineering workflow:

Extract: Retrieves hourly temperature data from the Open-Meteo API for specific geographic coordinates.

Transform: Cleans and structures the raw JSON data into a tabular format (DataFrames) using Pandas, including datetime conversion.

Load:

Local: Saves the processed data as a CSV file in the data/processed directory.

Cloud: Uploads the raw JSON files to an Amazon S3 bucket to maintain a Data Lake structure.

📁 Project Structure
src/: Contains the core pipeline modules (extract.py, transform.py, load.py).

data/: Local storage divided into raw and processed layers (ignored by git).

main.py: The orchestrator script that executes the entire pipeline in sequence.

requirements.txt: List of all Python dependencies required to run the project.

🛠️ Technologies Used
Language: Python 3.x.

Libraries:

Pandas: Data manipulation and analysis.

Requests: For consuming the external API.

Boto3: AWS SDK for Python to interact with S3.

Python-dotenv: Management of environment variables and credentials.

⚙️ Setup and Execution
Prerequisites
Python installed on your machine.

AWS credentials configured locally (typically in ~/.aws/credentials).

Installation
Clone the repository.

Install the necessary dependencies:

Bash
pip install -r requirements.txt
Running the Pipeline
To execute the full automated workflow, run:

Bash
python main.py
📝 Technical Details
Data Versioning: Files in the data/raw folder are saved with a unique timestamp (YYYYMMDD_HHMMSS) to prevent overwriting historical data.

Security: The .gitignore file is configured to ensure that virtual environments (venv/), sensitive configuration files (.env, .aws/), and local logs are not exposed on GitHub.

This project was developed as part of my Data Engineering studies.