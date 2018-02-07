# Scrapping from JavaScript rendered web page 

Not all web pages can be scrapped directly. Some are rendered through JavaScript.
This project uses PyQt5 to rendered the page in background and scrapping was done 
using BeautfifulSoup4.

ps: The page rendering is slow. So if you are trying to scrap multiple website. 
The best approach is to use multiprocessing and threading.

## Pre-requisite

Anaconda
 
Python 3.6, BeautfifulSoup4, PyQt5
```
conda install python python=3.6 BeautfifulSoup4 
```
and
```
pip install PyQt5
```

## Creating Conda environment (optional)
If you don't want to install the package one by one, and just wanted to create
an exactly same environment.
```
conda env create -f environment.yml -m myenv
activate myenv
```
Replace 'myenv' with anything you like

## Running the code
```
python scrap.py
```
