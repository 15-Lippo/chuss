# Cloud Mining Application

A secure and scalable cloud mining application that enables users to manage mining operations, wallets, and pool connections through a RESTful API.

## Features

- User authentication and account management
- Mining pool integration and management
- Real-time mining session monitoring
- Wallet management with deposit/withdrawal functionality
- Transaction history tracking
- System resource monitoring (CPU, Memory)

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables in `.env` file:
```
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///mining.db
```

4. Initialize the database:
```bash
python
>>> from app import db
>>> db.create_all()
```

5. Run the application:
```bash
python app.py
```

## API Endpoints

### Authentication
- POST `/register` - Register new user
- POST `/login` - User login
- GET `/logout` - User logout
- GET `/profile` - Get user profile

### Mining Operations
- GET `/pools` - List available mining pools
- POST `/start` - Start mining session
- POST `/stop/<session_id>` - Stop mining session
- GET `/status/<session_id>` - Get session status
- GET `/earnings` - Get mining earnings

### Wallet Management
- POST `/wallet` - Create new wallet
- POST `/wallet/<wallet_id>/deposit` - Deposit funds
- POST `/wallet/<wallet_id>/withdraw` - Withdraw funds
- GET `/transactions` - Get transaction history

### Mining Pool Management
- POST `/mining-pools` - Create new mining pool

## Security

- Password hashing using Werkzeug
- Session management with Flask-Login
- JWT token authentication
- Secure wallet operations
- Rate limiting and request validation

## Monitoring

The application provides real-time monitoring of:
- Mining session status
- Hashrate performance
- System resource usage
- Wallet balances and transactions