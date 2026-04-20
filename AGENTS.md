# AGENTS.md instructions

## File editing guidelines
- **Never** use `apply_patch` for large or multi‑file changes.
- Use **Python** for file creation or substantial edits: `from pathlib import Path; Path("file.py").write_text(content, encoding="utf-8")`.
- For single small changes, `apply_patch` is acceptable.
- Always ensure the target directory exists before writing.
- Do **not** edit files that are outside the scope of the task unless explicitly instructed.
- If a file contains syntax errors, fix them before committing.

## Test strategy
- Write tests under `backend/api/tests/`.
- Keep tests focused on a single behavior.
- Use Django’s `TestCase` and `Client` for API tests.
- Do not rely on existing data unless it’s created in `setUp`.
- Clean up the database after tests; Django’s test framework handles this automatically.
- Run tests with `python manage.py test`.
