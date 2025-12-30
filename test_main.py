from main import get_weather
import pytest

def test_get_weather():
    assert get_weather(30) =="Hot"
    assert get_weather(20) == "Normal"
    assert get_weather(15) == "Cold"
