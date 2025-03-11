def test_login_correct_credentials():
    username = "test_user"
    password = "test_password"
    db = SessionLocal()
    user = User.create_user(username, password, db)
    db.close()

    response = client.post("/auth/login", data={"username": username, "password": password})

    assert response.status_code == 200
    assert "access_token" in response.json()
