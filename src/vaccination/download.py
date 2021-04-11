import requests

URL_SOURCE_BUNDSWEIT = 'https://impfdashboard.de/static/data/germany_vaccinations_timeseries_v2.tsv'

class Download():        

    def download_bundesweit(self, path):
        r = requests.get(URL_SOURCE_BUNDSWEIT)
        with open(path + "germany_vaccinations_timeseries_v2.tsv", 'wb') as f:
            f.write(r.content)