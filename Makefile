install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
    PYTHONPATH=./mylib pytest --nbval *.ipynb && python -m pytest -cov=mylib test_main.py mylib/test_lib.py

format:	
	black *.py 

lint:
	#disable comment to test speed
	#pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py
	#ruff linting is 10-100X faster than pylint
	ruff check *.py mylib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

#generate_and_push:
# python main.py
# git config --local user.email "action@github.com"
#	git config --local user.name "GitHub Action"
#	git add bar.png bar2.png MTA.md
#	git commit -m "Generate stats and plots" || true
#	git push https://x-access-token:${{ secrets.GH_TOKEN }}@github.com/tursunait/Individual_Project_Tursunai_DE.git
		
all: install lint test format deploy
