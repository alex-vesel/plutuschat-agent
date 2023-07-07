import requests
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from parameters import DB_HOST

class SearchAPI():
    def __init__(self, search_query):
        self.search_query = search_query

    # @staticmethod
    def get_documents(question=None, sentences=[], ticker_list=[], date_start="1990-01-01", date_end="2050-01-01", max_results=5):
        """Get documents from database API.

        :return:
        """
        r = requests.post(f'http://{DB_HOST}:9091/search', params={'q': str(question), 'sentences': sentences, 'ticker_list': ticker_list, 'date_start': date_start, 'date_end': date_end, 'max_results': max_results})
        if r.status_code == 200:
            return r.json()['results']
        else:
            return "No results found."

    def get_references(uuids):
        """Get documents from database API.

        :return:
        """
        r = requests.post(f'http://{DB_HOST}:9091/getreferences', params={'uuids': uuids})
        if r.status_code == 200:
            return r.json()['results']
        else:
            return "No results found."


if __name__ == "__main__":
    search = SearchAPI.get_documents("""Arhaus insider trading.""", ticker_list=["arhs"], date_start="2010-01-01", date_end="2023-01-01", max_results=10)
