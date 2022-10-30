from hamcrest import assert_that

from clients.site_client import SiteClient
from helpers.base_helper import get_personal_pronouns, get_personal_pronouns_of_the_1st_person, \
    get_second_and_third_person_pronouns

site = SiteClient()


def test_there_are_more_personal_pronouns_of_the_1st_person_than_other_personal_pronouns():
    html_doc = site.get_start_page()
    personal_pronouns = get_personal_pronouns(html_doc)
    first_person_pronouns = get_personal_pronouns_of_the_1st_person(personal_pronouns)
    second_and_third_person_pronouns = get_second_and_third_person_pronouns(personal_pronouns)
    assert_that(
        actual_or_assertion=len(first_person_pronouns) > len(second_and_third_person_pronouns),
        reason="Местоимений первого лица меньше либо равно, чем всех остальных"
    )
