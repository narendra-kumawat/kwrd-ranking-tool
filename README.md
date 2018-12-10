# kwrd-ranking-tool
It is a `search engine optimization tool` that help to optimize the indexing on google search result page. This tool is buillt using python `selenium`, `beautifulsoup`, 
`scrappy` that is best library in scrapping using python and a proxy rotating service using proxy rotator server.
## Getting Started
Setup the virutal environment using virtualenv
```
#createing virtual environment with python3.5
virtualenv venv -p python3.5

#activate the virtual environment
source venv/bin/activate

#install the required python modules 
pip install selenium beautifulsoup scrappy

```
Now download the `chromedriver` for the appropreate OS
> https://sites.google.com/a/chromium.org/chromedriver/downloads

Set the path to the chrome driver by editing the file `/kwrd-ranking-tool/scr/keywordranking.py` as follows.
```
executable_path = "/path/to/your/chromedriver"

```
Once the path is set, add the competitor inside the `kwrd-ranking-tool/src/competitor/competitorList.py` file as follows
```
competitor=['www.datamintelligence.com','www.mordorintelligence.com','www.marketsandmarkets.com','www.alliedmarketresearch.com','www.transparencymarketresearch.com','www.grandviewresearch.com','www.futuremarketinsights.com','www.globaldata.com','www.thebusinessresearchcompany.com']

```
Its time to run the Scrapper
```
python keywordranking.py
```
Once the scrapper is finished its scarpping it will generate a final CSV with all the ranks of the keywords
