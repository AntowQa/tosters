from clients.mtt_client import MTTClient
from helpers.base_helper import get_all_pronouns, get_all_personal_pronouns, get_personal_pronouns_of_the_1st_person
from hamcrest import assert_that

mtt = MTTClient()


def test_there_are_more_personal_pronouns_of_the_1st_person_than_other_personal_pronouns():
    # Получить html страницу
    html_doc = mtt.get_start_page()
    # Получить все личные местоимения
    pronouns = get_all_pronouns(html_doc)
    all_personal_pronouns = get_all_personal_pronouns(pronouns)
    # Проверить, что колличество личных местоимений 1-го лица больше, чем колличество остальных личных местоимений
    assert_that(
        actual_or_assertion=len(get_personal_pronouns_of_the_1st_person(pronouns)) > len(all_personal_pronouns),
        reason="Местоимений первого лица меньше либо равно, чем всех остальных"
    )
