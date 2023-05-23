# Copyright (C) 2023  Pawan Rai <pawanrai9999@gmail.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from urllib.parse import urljoin

import requests

from shlinkcli import __app_name__, __version__


# create a class client to reuse requests Session for whole package.
# Class should have X-Api-Key header with get, post, patch, delete methods.
class Client:
    def __init__(self, url: str, api_key: str) -> None:
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update(
            {
                "X-Api-Key": self.api_key,
                "User-Agent": f"{__app_name__}/v{__version__}",
                "Accept": "application/json",
                "Origin": f"{url}",
            }
        )
        self.host = url

    def get(self, url: str, params=None) -> requests.Response:
        return self.session.get(urljoin(self.host, url), params=params)

    def post(self, url: str, json=None) -> requests.Response:
        return self.session.post(urljoin(self.host, url), json=json)

    def patch(self, url: str, json=None) -> requests.Response:
        return self.session.patch(urljoin(self.host, url), json=json)

    def put(self, url: str, json=None) -> requests.Response:
        return self.session.put(urljoin(self.host, url), json=json)

    def delete(self, url: str) -> requests.Response:
        return self.session.delete(urljoin(self.host, url))

    def close(self) -> None:
        self.session.close()
