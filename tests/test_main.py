import time
import pytest
from hamcrest import assert_that, equal_to, is_in

from steps.alerts_steps import AlertsSteps
from steps.app_mix_steps import BonditAppMenuSteps
from steps.edit_steps import EditSteps
from steps.generate_steps import GenerateSteps
from steps.my_portfolios_steps import MyPortfoliosSteps
from steps.my_universes_steps import MyUniversesSteps
from steps.portfolio_view_steps import PortfolioViewSteps
from steps.search_steps import SearchSteps
from test_data.test_data import TestData

# py.test --html=report.html
# py.test -v -m search
# py.test -v -m "not GeneratePage"
bondit_app_menu = BonditAppMenuSteps()


@pytest.mark.usefixtures("setup_login")
class TestSmoke:

    def test_login(self):
        my_portfolios = MyPortfoliosSteps()
        assert_that(my_portfolios.get_page_name_label(), equal_to("My Portfolios"))

    # @pytest.mark.parametrize('gen_data', [*TestData.gen_data])
    # def test_generate(self, gen_data):  # gen_data is fixture to pass data
    #     bondit_app_menu.open_generate_page()
    #     generate = GenerateSteps()
    #     generate.wait_on_element(GenerateSteps.port_name)
    #     generate.enter_port_name(gen_data["port_name"])
    #     generate.enter_amount(gen_data['amount'])
    #     generate.navigate_constraints_tab()
    #     generate.expand_all_sections()
    #     generate.click_upgrade_probability()
    #     generate.click_senior()
    #     generate.click_subordinated()
    #     generate.click_144a()
    #     generate.click_regs()
    #     generate.submit_generate_portfolio()
    #     time.sleep(7)
    #     assert_that(generate.get_toaster_text(), equal_to(gen_data["toaster_text"]))

    # @pytest.mark.parametrize('st_data', [*TestData.st_data])
    # def test_switch_trade(self, st_data):
    #     bondit_app_menu.open_my_portfolios_page()
    #     portfolio_view = PortfolioViewSteps()
    #     portfolio_view.open_portfolio_view_page()
    #     time.sleep(5)
    #     portfolio_view.open_switch_trade()
    #     portfolio_view.select_issuer(st_data["issuer_name"])
    #     portfolio_view.apply_filters()
    #     portfolio_view.wait_on_element(portfolio_view.switch_trade_idea)
    #     time.sleep(5)
    #     portfolio_view.submit_switch_trade()
    #     time.sleep(5)
    #     assert_that("Switch Trade", is_in(portfolio_view.get_portfolio_name()))

    # @pytest.mark.parametrize('edit_data', [*TestData.edit_data])
    # def test_edit(self, edit_data):
    #     bondit_app_menu.open_my_portfolios_page()
    #     edit = EditSteps()
    #     edit.open_portfolio_view_page()
    #     edit.open_portfolio_design_page()
    #     edit.wait_on_element(EditSteps.table_header)
    #     edit.unselect_all_columns()
    #     edit.select_isin_column()
    #     edit.buy_bond(edit_data["buy_amount"])
    #     edit.sell_bond(edit_data["sell_amount"])
    #     edit.save_portfolio_as(edit_data["port_name"])
    #     edit.navigate_transaction_list()
    #     assert_that(edit_data["port_name"], is_in(edit.get_portfolio_name()))

    # @pytest.mark.parametrize('search_data', [*TestData.search_data])
    # def test_search(self, search_data):
    #     bondit_app_menu.open_search_page()
    #     search = SearchSteps()
    #     search.wait_on_element(search.side_dropdown)
    #     search.select_ask()
    #     search.select_corporate_asset_type()
    #     #  search.select_usd_currency() no bonds in universe
    #     search.select_issuer(search_data["issuer_name"])
    #     search.select_country(search_data["country"])
    #     search.select_ytw()
    #     search.do_search()
    #     search.wait_on_element(search.search_table_body)
    #     search.select_two_rows()
    #     search.go_to_compare_bonds()
    #     time.sleep(5)
    #     assert_that("Bonds Comparison Table", is_in(search.get_table_name()))

    # def test_alerts(self):
    #     bondit_app_menu.open_alerts_page()
    #     alerts = AlertsSteps()
    #     alerts.wait_on_element(AlertsSteps.table_body)
    #     assert_that(alerts.take_last_alert_date()), is_in(alerts.select_three_past_days())

    # @pytest.mark.parametrize('extract_bonds_json', [TestData.extract_bonds_json])
    # def test_my_universes(self, receive_access_token, config, extract_bonds_json):
    #     my_universes = MyUniversesSteps(receive_access_token, config["data_service"], extract_bonds_json,
    #                                     config["internal_universe"], config["user_id"])
    #     print(my_universes.create_universe())
