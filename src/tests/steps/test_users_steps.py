import requests
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from utils.payload_generator import generate_user_payload

scenarios("../features/users.feature")
BASE_URL = "https://reqres.in/api"

@pytest.fixture
def context():
    return {}

@given("que eu gero um payload de usuário válido")
def user_payload():
    return generate_user_payload()

@when(parsers.parse('eu faço uma requisição GET para "{path}"'))
def do_get(context, path):
    resp = requests.get(f"{BASE_URL}{path}")
    context["response"] = resp
    return resp

@when(parsers.parse('eu faço uma requisição POST para "{path}" com esse payload'))
def do_post(context, path, user_payload):
    resp = requests.post(f"{BASE_URL}{path}", json=user_payload)
    context["response"] = resp
    return resp

@when('eu faço uma requisição POST para "/login" com payload inválido')
def do_invalid_login(context):
    resp = requests.post(f"{BASE_URL}/login", json={"email": "invalido"})
    context["response"] = resp
    return resp

@then(parsers.parse("a resposta deve ter status {status:d}"))
def check_status(context, status):
    resp = context.get("response")
    assert resp.status_code == status, f"Esperado {status}, retornado {resp.status_code}"

@then(parsers.parse('a resposta deve conter o campo "{field}"'))
def check_field(context, field):
    resp = context.get("response")
    assert field in resp.json(), f"Campo '{field}' não encontrado na resposta"
