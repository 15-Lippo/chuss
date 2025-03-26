from app import db
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    wallets = db.relationship('Wallet', backref='user', lazy=True)
    mining_sessions = db.relationship('MiningSession', backref='user', lazy=True)

class Wallet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255), unique=True, nullable=False)
    balance = db.Column(db.Float, default=0.0)
    currency = db.Column(db.String(10), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    transactions = db.relationship('Transaction', backref='wallet', lazy=True)

class MiningSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, default=datetime.utcnow)
    end_time = db.Column(db.DateTime)
    hashrate = db.Column(db.Float, default=0.0)
    status = db.Column(db.String(20), default='active')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    pool_id = db.Column(db.Integer, db.ForeignKey('mining_pool.id'), nullable=False)

class MiningPool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    algorithm = db.Column(db.String(50), nullable=False)
    fee = db.Column(db.Float, default=0.0)
    status = db.Column(db.String(20), default='active')
    mining_sessions = db.relationship('MiningSession', backref='pool', lazy=True)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), default='pending')
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    wallet_id = db.Column(db.Integer, db.ForeignKey('wallet.id'), nullable=False)
    tx_hash = db.Column(db.String(255), unique=True)