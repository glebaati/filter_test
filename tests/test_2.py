import pytest
from steamtest.pages.home_page import HomePage
from steamtest.pages.search_result_page import SearchResultPage
import json

with open('test_data.json', 'r') as f:
    data = json.load(f)


@pytest.mark.parametrize('game_name, n', [(data['FIRST_TUPLE']), (data['SECOND_TUPLE'])])
@pytest.mark.parametrize('driver', ['ru', 'en'], indirect=True)
def test_first(driver, game_name, n):
    home_page = HomePage(driver)
    search_result_page = SearchResultPage(driver)

    home_page.search_game(game_name)
    search_result_page.apply_filter()
    games_list = search_result_page.get_games_list(n)
    prices = search_result_page.get_prices(n)

    assert len(games_list) == n, f"Ожидалось {n} игр, но найдено {len(games_list)}"
    assert prices == sorted(prices, reverse=True), f"Фильтр работает некорректно. Получено: {prices}"
