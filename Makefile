# Install dependencies from requirements.txt
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

# Run tests with coverage for .ipynb notebooks and test files
#test:
#	PYTHONPATH=. pytest --nbval *.ipynb &&\
#		python -m pytest --cov=main.py test_main.py

# Format Python files with Black
format:	
	black *.py 

# Lint Python files with Ruff (faster than Pylint)
lint:
    ruff check *.py

# Lint Dockerfile with Hadolint
container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

# Run both formatting and linting
refactor: format lint

# Placeholder for generate_and_push (uncomment for automation in GitHub Actions)
# generate_and_push:
#	python main.py
#	git config --local user.email "action@github.com"
#	git config --local user.name "GitHub Action"
#	git add bar.png bar2.png MTA.md
#	git commit -m "Generate stats and plots" || true
#	git push https://x-access-token:${{ secrets.GH_TOKEN }}@github.com/tursunait/Individual_Project_Tursunai_DE.git

# Run all steps (install, lint, test, format, deploy if defined)
all: install lint test format deploy
