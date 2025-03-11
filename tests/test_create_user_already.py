def test_create_user_already_exists():
    username = "test_user"
    password = "test_password"
    db = SessionLocal()
    User.create_user(username, password, db)
    db.close()


    try:
        db = SessionLocal()
        User.create_user(username, password, db)
        db.close()
        assert False, "Deveria ter levantado uma exceção de usuário já existente"
    except Exception as e:
        assert str(e) == "Usuário já existe"
