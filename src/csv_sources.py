"""Extract analyzable text rows from CSV exports."""

from collections.abc import Iterable

import pandas as pd


TEXT_COLUMN_ALIASES = (
    "text",
    "sentence",
    "review",
    "comment",
    "comment_text",
    "content",
    "Tweet Text",
    "tweet_text",
    "tweetText",
)


def _match_column(columns: Iterable[str], aliases: Iterable[str]) -> str | None:
    normalized = {column.strip().casefold(): column for column in columns}
    for alias in aliases:
        match = normalized.get(alias.casefold())
        if match is not None:
            return match
    return None


def extract_text_entries(dataframe: pd.DataFrame) -> list[str]:
    """Return non-empty text values from a supported CSV text column."""
    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("Expected a pandas DataFrame.")

    text_column = _match_column(dataframe.columns, TEXT_COLUMN_ALIASES)
    if text_column is None:
        raise ValueError("CSV must include a text column such as 'text' or 'Tweet Text'.")

    return [
        value
        for value in dataframe[text_column].fillna("").astype(str).str.strip().tolist()
        if value
    ]
