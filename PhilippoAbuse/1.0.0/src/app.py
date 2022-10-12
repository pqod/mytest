import asyncio
import urllib.request
from bs4 import BeautifulSoup
from walkoff_app_sdk.app_base import AppBase


class GetAbuse(AppBase):
    """
    An example of a Walkoff App.
    Inherit from the AppBase class to have Redis, logging, and console logging set up behind the scenes.
    """
    __version__ = "1.0.0"
    app_name = "PhilippoAbuse"  # this needs to match "name" in api.yaml

    def __init__(self, redis, logger):
        """
        Each app should have this __init__ to set up Redis and logging.
        :param redis:
        :param logger:
        """
        super().__init__(redis, logger)
    async def get_ip(self,url):
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        rawsite = urllib.request.urlopen(req)
        content = rawsite.read().decode('utf-8')
        soup = BeautifulSoup(content, 'html.parser')
        res = soup.find_all("a")
        filtered = map(lambda ip: ip.contents[0], res)
        return(list(filtered))

if __name__ == "__main__":
    asyncio.run(Basics.run())
