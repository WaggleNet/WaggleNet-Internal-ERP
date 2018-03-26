from app.services import auth, bcrypt
from app.model.user import User
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from app.model import db
from flask import g, current_app, jsonify, Blueprint, request, abort

blueprint = Blueprint('api_user', __name__, url_prefix='/api/user')


def verify_user_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except SignatureExpired or BadSignature:
        return None
    user = User.query.get(data['user_id'])
    g.user = jsonify(user)
    return user


@auth.verify_password
def authenticate(token_or_username, password):
    if verify_user_token(token_or_username):
        return True
    user = User.query.filter_by(username=token_or_username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        return True
    return False


def generate_user_token(user_id, expiration=3600*24*7):
    # Fetch the thing from DB
    user = User.query.get(user_id)
    if not user: return None
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({'user_id': user_id})


@blueprint.route('/list')
@auth.login_required
def list_users():
    return jsonify(results=User.query.all())


@blueprint.route('/create', methods=['POST'])
@auth.login_required
def create_user():
    kwargs = request.json or request.form.to_dict()
    user = User(**kwargs)
    if User.query.filter_by(username=user.username).first():
        # User is found
        return None
    db.session.add(user)
    db.session.commit()
    return user.id


@blueprint.route('/<user_id>/remove')
@auth.login_required
def remove_user(user_id):
    user = User.query.get(user_id)
    db.session.remove(user)
    db.session.commit()
    return jsonify(status='ok')


@blueprint.route('/<user_id>/update_profile')
@auth.login_required
def update_profile(user_id):
    user = User.query.get_or_404(user_id)
    profile = request.json or request.form.to_dict()
    user.profile = profile
    db.session.commit()
    return jsonify(status='ok')


@blueprint.route('/<user_id>/reset', methods=['POST'])
@auth.login_required
def reset_user_password(user_id):
    user = User.query.get_or_404(user_id)
    form = request.json or request.form
    pwd = form['password']
    user.password = bcrypt.generate_password_hash(pwd)
    db.session.commit()
    return jsonify(status='ok')


@blueprint.route('/login')
@auth.login_required
def handle_login():
    token = generate_user_token(g.user['user_id'])
    return jsonify(status='ok', token=token.decode('ascii'), user=g.user)


@blueprint.route('/register', methods=['POST'])
def handle_register():
    form = request.json or request.form
    inv_code = form.get('inv_code')
    username = form.get('username')
    password = form.get('password')
    if inv_code is None: abort(400)
    user = User.query.filter_by(inv_code=inv_code, username=username).first_or_404()
    user.password = bcrypt.generate_password_hash(password)
    user.inv_code = None
    db.session.commit()
    return jsonify(status='ok', user_id=user.id)