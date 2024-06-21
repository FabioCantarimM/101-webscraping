import json

from mitmproxy import ctx, http
from mitmproxy.connection import Server
from mitmproxy.http import HTTPFlow
from mitmproxy.utils import strutils
from mitmproxy.net.server_spec import ServerSpec

class ProxyControllerAddon:
    def request(self, flow: HTTPFlow):
        if flow.request.pretty_url == "https://api.linximpulse.com/engage/search/v3/search?apikey=paodeacucar&origin=https://www.paodeacucar.com&page=1&resultsPerPage=100&terms=azeite&allowRedirect=true&salesChannel=461&salesChannel=catalogmkp&sortBy=relevance":
            flow.request.query["terms"] = "pudim"
        if flow.request.pretty_url == 'https://www.codechef.com/api/codechef/login':
            print(flow.request.text)

    def response(self, flow: HTTPFlow):
        if flow.request.pretty_url  == "https://api.linximpulse.com/engage/search/v3/search?apikey=paodeacucar&origin=https://www.paodeacucar.com&page=1&resultsPerPage=100&terms=azeite&allowRedirect=true&salesChannel=461&salesChannel=catalogmkp&sortBy=relevance":
            flow.response.content=bytes("Oi eu assumi seu computador e as respostas serão minhas! Hahahah","UTF-8")



addons = [ProxyControllerAddon()]
