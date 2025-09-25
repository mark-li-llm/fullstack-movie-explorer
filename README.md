# Full-Stack Movie Explorer on GCP: Flask API, React Client, PostgreSQL, CI/CD

[![Python CI](https://github.com/mark-li-llm/fullstack-movie-explorer/actions/workflows/monorepo-python.yml/badge.svg)](https://github.com/mark-li-llm/fullstack-movie-explorer/actions/workflows/monorepo-python.yml)
[![React CI](https://github.com/mark-li-llm/fullstack-movie-explorer/actions/workflows/monorepo-react.yml/badge.svg)](https://github.com/mark-li-llm/fullstack-movie-explorer/actions/workflows/monorepo-react.yml)
[![CodeQL](https://github.com/mark-li-llm/fullstack-movie-explorer/actions/workflows/codeql.yml/badge.svg)](https://github.com/mark-li-llm/fullstack-movie-explorer/actions/workflows/codeql.yml)

This repository consolidates three previously separate projects into a single monorepo while preserving full Git history:

- `project1-yli3466/` — Movie Explorer (Flask + TMDB/Wikipedia, Cloud Run)
- `milestone2-yli3466/` — Movie Review App (Flask + Auth + Postgres, App Engine)
- `milestone3-yli3466/` — Full‑stack SPA (Flask API + React client)

Structure was created using `git subtree` so each subdirectory contains its original commit history, authorship, and tags (if any).

Common tasks:
- Backend (Flask): see each subproject's README for setup and env vars.
- Frontend (React): `cd milestone3-yli3466/client && npm install && npm start`.

Notes:
- Future updates from the original repos can be pulled via `git subtree pull --prefix=<subdir> <remote> <branch>`.
- Issues/PRs from the original repositories are not migrated automatically.

CI
- Automated quality gates via GitHub Actions:
  - Python: Ruff + Black (check) + MyPy + pip-audit
  - React: ESLint (Airbnb) + production build
  - Security: CodeQL (Python & JavaScript)
- Triggers: push/PR (path filtered), weekly schedule, and manual dispatch.
- Dependabot keeps pip/npm dependencies up to date with weekly PRs.
