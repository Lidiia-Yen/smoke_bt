from datetime import datetime
from selene import browser
import utilities.api_config
import requests


class MyUniversesSteps:

    def __init__(self, access_token, data_service, extract_bonds_json, internal_universe, user_id):
        self.browser = browser
        self.token = access_token
        self.asset_summary_url = f'{data_service}?'
        self.extract_bonds_json = extract_bonds_json
        self.create_internal_universe_url = internal_universe
        self.user_id = user_id
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

    def extract_bonds(self):
        outer = list(requests.post(self.asset_summary_url,
                                   headers=self.headers,
                                   json=self.extract_bonds_json).json()["values"])
        new_list = [item for sublist in outer for item in sublist]
        return new_list

    def create_universe(self):
        universe_name = datetime.today()
        return requests.post(self.create_internal_universe_url,
                             headers=self.headers,
                             json={
                                 "items": [
                                     {"bondit_super_id": self.extract_bonds()[0]},
                                     {"bondit_super_id": self.extract_bonds()[1]},
                                     {"bondit_super_id": self.extract_bonds()[2]}
                                 ],
                                 "method": "static",
                                 "owner_id": self.user_id,
                                 "type": "user",
                                 "universe_description": f"Universe Lidiia{universe_name}",
                                 "universe_name": "CU Lidiia test",
                                 "universe_source": "csv"
                             }
                             ).json()['universe_id']

    def find_universe_name(self):
        pass

    def delete_universe(self):
        pass
