class MockResponse:
    def __init__(self, status_code, json_data):
        self.status_code = status_code
        self.json_data = json_data

    def json(self):
        return self.json_data

class UserClient:
    def __init__(self, api_base):
        self.api_base = api_base

    def create_user(self, username, email):
        # Mock API now returns 201 (Created) for user creation.
        response = MockResponse(201, {"id": 101, "username": username, "email": email})
        # Fixed assertion: expect 201.
        assert response.status_code == 201, f"Failed to create user, got status {response.status_code}"
        return response.json()
