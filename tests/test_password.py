def test_password_verification():
    username = "test_user"
    password = "test_password"
    db = SessionLocal()
    user = User.create_user(username, password, db)
    db.close()

    assert user.verify_password(password)  
    assert not user.verify_password("wrong_password") 
