import pytest
from config import URL
from tests.conf.order_flow_conf import params as order_params
import allure

@allure.feature('Order flow')
class TestOrderFlow:

    @pytest.mark.parametrize('entry_index', [0, -1])
    @pytest.mark.parametrize('data', order_params)
    def test_create_order_and_check_logos(self, order_page, data, entry_index):
        """Positive scenario: open order (top/bottom), fill forms, confirm order, check logos."""
        with allure.step('Open order modal by entry point'):
            order_page.open_order_by_index(entry_index)

        with allure.step('Fill personal information and go to next'):
            order_page.fill_personal_info(
                name=data['name'],
                surname=data['surname'],
                address=data['address'],
                metro=data['metro'],
                phone=data['phone']
            )

        with allure.step('Fill rental info and place order'):
            order_page.fill_rental_info(
                date=data['date'],
                rental_period_index=data['rental_index'],
                color=data['color'],
                comment=data['comment']
            )

        with allure.step('Confirm the order and check confirmation message'):
            confirm_text = order_page.confirm_order()
            assert confirm_text and len(confirm_text.strip()) > 0
            assert 'заказ' in confirm_text.lower() or 'оформлен' in confirm_text.lower()

        with allure.step('Click scooter logo and verify navigation to main site'):
            scooter_url = order_page.click_logo_scooter_and_check()
            assert URL.BASE_URL in scooter_url

        with allure.step('Click Yandex logo, switch to new tab and verify redirect to Dzen'):
            yandex_url = order_page.click_logo_yandex_and_switch()
            assert ('dzen' in yandex_url.lower()) or ('zen' in yandex_url.lower())
