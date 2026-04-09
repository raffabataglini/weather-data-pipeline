Multi-City Weather Data Pipeline 🌦️
This is an automated ETL (Extract, Transform, Load) pipeline built with Python. The project has been scaled to monitor weather conditions across multiple cities in the Paraíba Valley and Alto Tietê regions (Guararema, Mogi das Cruzes, Jacareí, and São José dos Campos).

🚀 Project Architecture
The pipeline follows a modular data engineering workflow:

Extract: Dynamically fetches hourly temperature data for multiple coordinates using the Open-Meteo API.

Transform: Processes the raw JSON response for each city using Pandas, structuring it into a unified tabular format with proper timestamp conversions.

Load:

Local: Stores individual city data and a consolidated master file in CSV format.

Cloud: Syncs the raw data to an Amazon S3 bucket, maintaining a versioned Data Lake structure.

📍 Monitored Locations
The pipeline currently tracks:

Guararema, SP

Mogi das Cruzes, SP

Jacareí, SP

São José dos Campos, SP

📁 Project Structure
src/extract.py: Handles API requests and saves raw JSON files with city-specific tags.

src/transform.py: Cleans data and generates DataFrames.

src/load.py: Manages the integration with AWS S3 using boto3.

main.py: The orchestrator that iterates through the city list and runs the full pipeline.

🛠️ Technologies Used
Python 3.x

Pandas: For data manipulation and transformation.

Boto3: AWS SDK for Python (S3 integration).

Requests: For API consumption.

Python-dotenv: Secure management of environment variables.

⚙️ Setup and Execution
Prerequisites
Python installed.

AWS credentials configured in ~/.aws/credentials.

Installation
Clone the repository.

Install dependencies:

Bash
pip install -r requirements.txt
Running
To process data for all cities:

Bash
python main.py
📝 Technical Features
Dynamic File Naming: Files are saved as weather_city_timestamp.json to ensure data traceability.

Data Lake Best Practices: Raw data is preserved in its original format before transformation.

Scalability: The modular design allows adding new cities simply by updating the coordinate dictionary in the code.

Project developed as part of my Data Engineering internship preparation.