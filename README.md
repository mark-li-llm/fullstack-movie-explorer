# sf0 Monorepo

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

