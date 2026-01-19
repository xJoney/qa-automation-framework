from api_tests.api_client import ReqresAPI


api = ReqresAPI()

def test_get_users():

    response = api.get_users()

    assert response.status_code == 200

    body = response.json()
    assert "users" in body
    assert len(body["users"]) > 0

def test_get_single_user():

    response = api.get_user(1)
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert "firstName" in data
    assert "lastName" in data


def test_create_user():

    payload = {
        "firstName": "Bob",
        "lastName": "Belcher",
        "age": 30,
        "gender": "male",
        "email": "Bob@example.com",
        "phone": "123-456-7890"
    }

    response = api.create_user(payload)
    assert response.status_code == 201  

    data = response.json()

    assert "id" in data  
    assert data["firstName"] == payload["firstName"]
    assert data["lastName"] == payload["lastName"]


def test_update_user():

    payload = {
        "firstName": "Bob",
        "lastName": "Belcher",
        "age": 43
    }

    response = api.update_user(1, payload)
    assert response.status_code == 200

    data = response.json()
    assert data["firstName"] == payload["firstName"]
    assert data["age"] == payload["age"]


