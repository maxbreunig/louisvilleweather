"Louisville Weather" 
* This program shows the current weather forecast as well as visualizes the month of 3/2022 in Louisville, KY thorugh a plot graph.

Please run in a virtual environment using:
* python3 -m venv /path/new_env_name
* source path/new_env_name/bin/activate
* pip install -r requirements.txt 

REQUIREMENTS (pip install "_____") INSTALL in CMD Prompt and VS Studio:
* pip install pandas
* pip install matplotlib
* pip install requests




Also must have the latest version of Python downloaded as of 3.10.4 at https://www.python.org/downloads/

Must have latest version of Microsoft Virtual Studio Code downloaded. Can find at https://visualstudio.microsoft.com/downloads/


Requirement category 1: Calculate and display data based on an external factor (ex: get the current date, and display how many days remain until some event).

        * lines 30 through 33

Requirement category 2: Read data from an external file, such as text, JSON, CSV, etc, and use that data in your application.

        * lines 8 through 20 (not sure if this counts, pulls from url and visualizes current forecast, just thought it was cool.)
        * line 38 (Read) / lines 38 through 47 (Use)
        
Requirement category 3: Visualize data in a graph, chart, or other visual representation of data.

        * lines 38 through 47



INSTRUCTIONS TO RUN:
Download file from git respository and extraxt the files.

Open louisvilleforecast folder contents in visual studio.

Run in the terminal in visual studio using CMD prompt style terminal:
*C:\Users\Max\Documents\louisvilleforecast>louisvilleforecast.py

*Please ensure python or any other package extensions are install in Visual Studio as well*



About:
    This project starrted as a forecast predictor, but I could not harness neuralprohet because I was not working with Juypter Notebook and got too far behind to fix it. This project is the result. 

    Works with accurate monthly data for March 2022 in Louisville, KY