"""The _extract_ phase of the ETL pipeline."""
import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()


def fetch_a_true_grit(year: int) -> None:
    """Fetch one of the True Grit movies from the oMDB API.

    Args:
    ----
        year (int): The year of the movie to fetch. Must be 1969 or 2010.
    """
    data = requests.get(
        f"http://www.omdbapi.com/?t=True+Grit&y={year}&apikey={os.environ['OMDB_API_KEY']}",
        timeout=10,
    ).json()

    with Path(f"data/true_grit_{year}.json").open("w") as f:
        json.dump(data, f, indent=2)
