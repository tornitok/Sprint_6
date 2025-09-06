import pytest
from tests.conf.main_page_q_and_a_conf import params as q_and_a_params

@pytest.mark.parametrize("accordion_locator, text_locator, expected_attr", q_and_a_params)
def test_main_page_q_and_a(main_page, accordion_locator, text_locator, expected_attr):
    locators = main_page.locators
    expected_text = getattr(main_page.questions, expected_attr)
    main_page.check_question_text(
        getattr(locators, accordion_locator),
        getattr(locators, text_locator),
        expected_text
    )
