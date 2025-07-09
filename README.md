# diy api

This repo contains material delivered at the NCAS 2025 annual staff meeting. It aims to help you take the first steps towards creating and understanding (web) application programming interfaces (APIs).

### What's in the repo?

- `diy-api-slides.pdf` contains the slides that were delivered during the session.
- `main.py` contains the FastAPI application and the definition of its endpoints.
- `create-timeseries.py` creates a temperature timeseries netcdf (randomly generated data) for use in our FasAPI API endpoints.
- `requirements.txt` contains the names and versions of pip packages needed to run this repo.
- `plot.html` contains a very simple html web page that accesses some of the FastAPI endpoints.

### Getting started

This practical parts of this session were delivered using the linux terminal.

```
git clone git@github.com:lrrmar/diy-api.git
cd diy-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements
uvicorn main:app --reload
```

Here we have:
- cloned the repo
- navigated into the rep
- created a python virtual environment
- activated the python virtual environment
- installed dependencies
- started a `uvicorn` http/https server



### Exploring FastAPI

In a new terminal window, open `main.py` in a text editor and in your browser navigate to `localhost:8000/docs`. Here you can see the python definition of our API endpoints in the script and information and testing facilities in the web page.



### Using the endpoints

In your browser, navigate to `file://{path to repo}/diy-api/plot.html`. This is a very simple web page that interacts with two of our endpoints using javascript and html. Open the `plot.html` file in a text editor and figure out what is going on.
