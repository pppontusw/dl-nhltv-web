# dl-nhltv-web

This is a web interface for presenting download data from the dl-nhltv application.

To run this, you need to install the requirements from requirements.txt

Ex: `pip install -r requirements.txt`

Then set the DATABASE_URL to the path to your nhltv database (will be in your target
download folder) `EXPORT DATABASE_URL=sqlite:////path/to/download/folder/nhltv_database`

After that you can run the application with `python run.py` and the web interface will
respond at http://*ipaddress*:5000
