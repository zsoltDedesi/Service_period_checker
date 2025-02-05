from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    return "Login page"

@auth_bp.route('/logout', methods=['GET'])
def logout():
    return "Logout page"