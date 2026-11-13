# Agent Sandbox Shop

A small FastAPI shop (products and carts) that exists so the [AI Dev Agent](https://github.com/MaikonJm/ai-dev-agent) has real work to do. It ships with a known bug, missing tests and a feature request, all tracked as issues.

The agent only works through pull requests: label an issue `agent`, review the plan it comments, reply `/approve`, and review the PR it opens.

## Run locally

```bash
pip install -r requirements-dev.txt
pytest -q
uvicorn shop.main:app --reload
```

## Branch protection

`main` requires a pull request and a passing `CI` check. The agent pushes only to `agent/issue-<number>` branches and never merges.
