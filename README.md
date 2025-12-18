# q

Backend API for q

## Tech Stack

- **Frontend**: React
- **Backend**: FastAPI + SQLAlchemy
- **Frontend Source**: GitHub ([Repository](https://github.com/HimaShankarReddyEguturi/Designecommerceproductui.git))

## Project Structure

```
q/
├── frontend/          # Frontend application
├── backend/           # Backend API
├── README.md          # This file
└── docker-compose.yml # Docker configuration (if applicable)
```

## Getting Started

### Prerequisites

- Node.js 18+ (for frontend)
- Python 3.11+ (for Python backends)
- Docker (optional, for containerized setup)

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Backend Setup

```bash
cd backend
# Follow backend-specific setup instructions in backend/README.md
```

## Features

- user accounts
- data storage
- data retrieval
- data manipulation
- search

## API Endpoints

- `POST /api/register` - Create a new user account.
- `POST /api/login` - Log in to an existing user account.
- `GET /api/data` - Retrieve a list of all data for the current user.
- `POST /api/data` - Create new data for the current user.
- `PUT /api/data/{id}` - Update existing data for the current user.
- `DELETE /api/data/{id}` - Delete data for the current user.
- `GET /api/search` - Search for data by keyword.

## License

MIT
