class TestData:
    gen_data = [
        {'amount': '1000000', 'port_name': 'GeneratePage_smoke', 'toaster_text': "Portfolio Successfully Generated"}
    ]

    edit_data = [
        {'sell_amount': '1000', 'buy_amount': '1000', 'port_name': 'edit'}
    ]

    st_data = [
        {'issuer_name': 'Apple'}
    ]

    search_data = [
        {'issuer_name': 'Apple', 'country': 'united'}
    ]

    extract_bonds_json = {
        "calc_date": "2022-11-18",
        "caller": "search",
        "filters":
            {
                "bond_status": {
                    "in": [19]},
                "bond_class": {
                    "in": [89]},
                "bond_country": {
                    "in": [140]},
                "bond_coupon": {
                    "min": 1,
                    "max": 8},
                "bond_ttm": {
                    "min": 0,
                    "max": 8,
                    "is": f"false"},
                "bond_yield": {
                    "min": 0.00,
                    "max": 0.05}
            },
        "limit": 5,
        "selected_columns": ["bondit_super_id"]
    }
