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

from typing import Annotated

import typer

app = typer.Typer()


@app.command()
def create_short_url(
    long_url: Annotated[str, typer.Option(help="Long URL to shorten")]
) -> None:
    """
    Creates a short url for the given long url

    Args:
        long_url (str): long url
    """
    typer.echo(f"Creating short url for {long_url}")


if __name__ == "__main__":
    app()
