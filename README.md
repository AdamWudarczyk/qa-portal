#  QA Portal – Web Application for Test Management

**QA Portal** is a fullstack web application for managing manual and automated tests.  
It's a lightweight alternative to tools like TestRail or Xray, designed for individual testers and small QA teams.

---

##  Tech Stack

| Layer       | Technology                          |
|-------------|--------------------------------------|
| Frontend    | React, Vite, Cypress                 |
| Backend     | FastAPI, SQLAlchemy, Alembic         |
| Database    | PostgreSQL                           |
| E2E Testing | Cypress (JavaScript), Playwright (Python) |
| CI/CD       | GitHub Actions                       |
| DevTools    | Docker + Docker Compose, dotenv, Faker, Allure |

---

##  Project Structure
web-app-project/
│
├── backend/ # FastAPI backend and database logic\
│ ├── app/ # application modules and logic\
│ ├── tests/ # backend unit/integration tests\
│ ├── alembic/ # database migrations\
│ └── requirements.txt\
│\
├── frontend/ # React frontend + Cypress tests\
│ ├── src/ # components, pages, routing\
│ ├── cypress/ # frontend E2E tests\
│ └── package.json\
│\
├── tests-playwright/ # E2E tests using Playwright + Python\
│ ├── tests/ # Playwright test cases\
│ └── requirements.txt\
│\
├── postgres/ # PostgreSQL init scripts\
│ └── init.sql\
│\
├── .env.example # environment variable template\
├── docker-compose.yml # full project orchestration\
├── Makefile # useful shortcuts\
└── .github/workflows/ # CI pipelines (backend, frontend, tests)\

---

##  Key Features

###  For Testers & Users

- User registration and login
- Create and manage test projects
- Add test cases (title, steps, expected results)
- Organize tests into suites
- Track test execution history and status (PASS, FAIL, SKIP, BLOCKED)
- Upload test results from Cypress/Playwright (JSON)

###  For Automation QA Engineers

- API endpoint to push automated test results
- Link test cases to GitHub Actions builds
- Support for test data generation via Faker
- API documentation via Swagger (OpenAPI)

---

##  How to Run Locally

1. Clone the repository:
```bash
git clone https://github.com/your-username/qa-portal.git
cd qa-portal
```
2. Create a .env file based on the .env.example

3. Start the app using Docker Compose:
```bash
docker-compose up --build
```
4. Access the application:
Frontend: http://localhost:5173
Backend (API Docs): http://localhost:8000/docs
PostgreSQL: localhost:5432

Project Status
- [x] Initial project structure
- [ ] Backend setup and DB connection
- [ ] User registration/login
- [ ] Test case & project CRUD
- [ ] Cypress & Playwright integration
- [ ] Dashboard & data export

# License
This project is for educational and portfolio purposes only.
You are free to explore, fork, and contribute.

___
Created by Adam Wudarczyk