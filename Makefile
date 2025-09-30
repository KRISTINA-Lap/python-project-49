.PHONY: install brain-games brain-even brain-calc brain-gcd brain-progression brain-prime build package-install clean lint format check-format

install:
	python3 -m pip install -e .

brain-games:
	python3 -m brain_games.scripts.brain_games

brain-even:
	python3 -m brain_games.scripts.brain_even

brain-calc:
	python3 -m brain_games.scripts.brain_calc

brain-gcd:
	python3 -m brain_games.scripts.brain_gcd

brain-progression:
	python3 -m brain_games.scripts.brain_progression

brain-prime:
	python3 -m brain_games.scripts.brain_prime

build:
	python3 -m build

package-install:
	python3 -m pip install --force-reinstall dist/*.whl

clean:
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info/
	rm -rf __pycache__/
	rm -rf brain_games/__pycache__/
	rm -rf brain_games/games/__pycache__/
	rm -rf brain_games/scripts/__pycache__/

lint:
	python3 -m ruff check brain_games

format:
	python3 -m ruff format brain_games

check-format:
	python3 -m ruff format --check brain_games

reinstall: clean install build package-install
