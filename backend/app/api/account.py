from flask import Blueprint, jsonify, request
from app.model.account import Account, AccountStatus
from app.model import db
from app.services import auth

blueprint = Blueprint('api_account', __name__, url_prefix='/api/account')

@blueprint.route('/list')
@auth.login_required
def list_accounts():
    results = Account.query.all()
    return jsonify(status='ok', result=results)



@blueprint.route('/create', methods=['POST'])
@blueprint.route('/new/update', methods=['POST'])
@auth.login_required
def create_account():
    form = request.json or request.form.to_dict()
    account = Account(**form)
    db.session.add(account)
    db.session.commit()
    return jsonify(status='ok', result=account.id)


@blueprint.route('/<account_id>')
@auth.login_required
def get_account(account_id):
    return jsonify(status='ok', result=Account.query.get_or_404(account_id))


@blueprint.route('/<account_id>/remove')
@auth.login_required
def remove_account(account_id):
    account = Account.query.get_or_404(account_id)
    db.session.remove(account)
    db.session.commit()
    return jsonify(status='ok')


@blueprint.route('/<account_id>/update', methods=['POST'])
@auth.login_required
def update_account(account_id):
    account = Account.query.get_or_404(account_id)
    form = request.json or request.form.to_dict()
    # Now, update status cuz it's enum
    status = form.pop('status', None)
    if status:
        account.status = AccountStatus[status]
    # And update all the other things
    for i in form.keys():
        if hasattr(account, i):
            setattr(account, i, form[i])
    db.session.commit()
    return jsonify(status='ok')


@blueprint.route('/<account_id>/rebalance')
@auth.login_required
def refresh_account_balance(account_id):
    account = Account.query.get_or_404(account_id)
    # TODO: Refresh balance with transactions
    return jsonify(status='ok')