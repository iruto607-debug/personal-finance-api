import bcrypt
from database import db, User

def hash_pw(pw):
    return bcrypt.hashpw(pw.encode(), bcrypt.gensalt()).decode()

def verify_pw(pw, hashed):
    return bcrypt.checkpw(pw.encode(), hashed.encode())

def register_user(username, password):
    if db.query(User).filter(User.username == username).first():
        return False

    user = User(username=username, password=hash_pw(password))
    db.add(user)
    db.commit()
    return True

def login_user(username, password):
    user = db.query(User).filter(User.username == username).first()

    if user and verify_pw(password, user.password):
        return True
    return False