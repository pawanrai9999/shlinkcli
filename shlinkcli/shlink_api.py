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

from typing import Any

import requests

from shlinkcli import __api_version__


class ShlinkApi:
    def __init__(self, session: requests.Session):
        self.session = session

    # method to check for error in response and raise exception if any
    @staticmethod
    def check_for_error(response: requests.Response) -> None:
        if response.status_code != requests.codes.ok:
            raise Exception(response.json()["detail"])
        # if header Content-Type: application/problem+json exits raise exception
        if (
            "Content-Type" in response.headers
            and response.headers["Content-Type"] == "application/problem+json"
        ):
            raise Exception(response.json()["detail"])

    def create_short_url(
        self,
        longUrl: str,
        deviceLongUrls: dict[str, str] | None = None,
        validSince: str | None = None,
        validUntil: str | None = None,
        maxVisits: int = 0,
        tags: list[str] | None = None,
        title: str | None = None,
        crawlable: bool = True,
        forwardQuery: bool = True,
        customSlug: str | None = None,
        domain: str | None = None,
        findIfExists: bool = True,
        shortCodeLength: int = 0,
    ) -> Any:
        reqBody: dict[str, Any] = {}
        reqBody["longUrl"] = longUrl
        if deviceLongUrls:
            if deviceLongUrls.get("android"):
                reqBody["deviceLongUrls"]["android"] = deviceLongUrls.get("android")
            if deviceLongUrls.get("ios"):
                reqBody["deviceLongUrls"]["ios"] = deviceLongUrls.get("ios")
            if deviceLongUrls.get("desktop"):
                reqBody["deviceLongUrls"]["desktop"] = deviceLongUrls.get("desktop")
        if validSince:
            reqBody["validSince"] = validSince
        if validUntil:
            reqBody["validUntil"] = validUntil
        reqBody["maxVisits"] = maxVisits
        if tags:
            reqBody["tags"] = tags
        if title:
            reqBody["title"] = title
        reqBody["crawlable"] = crawlable
        reqBody["forwardQuery"] = forwardQuery
        if customSlug:
            reqBody["customSlug"] = customSlug
        if domain:
            reqBody["domain"] = domain
        reqBody["findIfExists"] = findIfExists
        reqBody["shortCodeLength"] = shortCodeLength

        res = self.session.post(
            url=f"/rest/v{__api_version__}/short-urls", json=reqBody
        )

        self.check_for_error(response=res)

        return res.json()

    def delete_short_url(self, shortCode: str) -> None:
        res = self.session.delete(
            url=f"/rest/v{__api_version__}/short-urls/{shortCode}"
        )

        self.check_for_error(response=res)
