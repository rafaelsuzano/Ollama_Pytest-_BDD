Feature: Testes de API de usuários no ReqRes

  Scenario: Listar usuários
    When eu faço uma requisição GET para "/users?page=2"
    Then a resposta deve ter status 200
    And a resposta deve conter o campo "data"

  Scenario: Criar usuário válido
    Given que eu gero um payload de usuário válido
    When eu faço uma requisição POST para "/users" com esse payload
    Then a resposta deve ter status 201
    And a resposta deve conter o campo "id"

  Scenario: Login inválido
    When eu faço uma requisição POST para "/login" com payload inválido
    Then a resposta deve ter status 401
    And a resposta deve conter o campo "error"
