from flask import Blueprint, jsonify, request, abort
from app.model.account import Account
from app.model.transaction import Transaction, TransactionType
from app.model import db
from app.services import auth

blueprint = Blueprint('api_transaction', __name__, url_prefix='/api/transaction')


@blueprint.route('/list')
@auth.login_required
def list_transactions():
    result = Account.query.all()
    return jsonify(status='ok', result=result)


@blueprint.route('/new/update', methods=['POST'])
@blueprint.route('/create', methods=['POST'])
@auth.login_required
def create_transaction():
    form = request.json or request.form.to_json()
    if 'type' in form:
        form['type'] = TransactionType[form['type']]
    transaction = Transaction(**form)
    db.session.add(transaction)
    db.session.commit()
    return jsonify(status='ok', result=transaction.id)


@blueprint.route('/<transaction_id>')
@auth.login_required
def get_transaction(transaction_id):
    transaction = Transaction.query.get_or_404(transaction_id)
    return jsonify(status='ok', result=transaction)


@blueprint.route('/<transaction_id>/update', methods=['POST'])
@auth.login_required
def update_transaction(transaction_id):
    transaction = Transaction.query.get_or_404(transaction_id)
    form = request.json or request.form.to_json()
    if 'type' in form:
        form['type'] = TransactionType[form['type']]
    for k, v in form.items():
        if hasattr(transaction, k):
            setattr(transaction, k, v)
    db.session.commit()
    return jsonify(status='ok')


@blueprint.route('/<transaction_id>/remove')
@auth.login_required
def remove_transaction(transaction_id):
    transaction = Transaction.query.get_or_404(transaction_id)
    db.session.remove(transaction)
    db.session.commit()
    return jsonify(status='ok')
