def test_login_incorrect_credentials():
    username = "test_user"
    password = "test_password"
    db = SessionLocal()
    user = User.create_user(username, password, db)
    db.close()


    response = client.post("/auth/login", data={"username": username, "password": "wrong_password"})


    assert response.status_code == 400
    assert response.json() == {"detail": "Credenciais inválidas"}
