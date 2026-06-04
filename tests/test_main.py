from __future__ import annotations

from io import BytesIO, TextIOWrapper

from src.main import _configure_stream_encoding


def test_configure_stream_encoding_switches_gbk_stream_to_utf8() -> None:
    stream = TextIOWrapper(BytesIO(), encoding="gbk")

    _configure_stream_encoding(stream)

    assert stream.encoding.lower().replace("-", "") == "utf8"
