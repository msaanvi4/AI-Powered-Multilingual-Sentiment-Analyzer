"""Tests for CSV text extraction."""

import pandas as pd
import pytest

from src.csv_sources import extract_text_entries


def test_xquik_tweet_text_entries_are_extracted():
    source = pd.DataFrame({"Tweet Text": ["Great launch", "  ", None, "Needs support"]})

    result = extract_text_entries(source)

    assert result == ["Great launch", "Needs support"]


def test_existing_sentence_column_is_supported():
    source = pd.DataFrame({"sentence": ["Bonjour tout le monde"]})

    result = extract_text_entries(source)

    assert result == ["Bonjour tout le monde"]


def test_missing_text_column_raises_clear_error():
    source = pd.DataFrame({"body": ["No supported text column"]})

    with pytest.raises(ValueError, match="text column"):
        extract_text_entries(source)
