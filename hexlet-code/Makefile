install:
		uv sync
brain-games:
		uv run brain-games
brain-even:
		uv run brain-even
		
brain-calc:
	uv run brain-calc

brain-gcd:
	uv run brain-gcd

	
build:
		uv build

package-install:
		uv tool install --force dist/*.whl
		

clean:
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info/
	rm -rf __pycache__/
	rm -rf brain_games/__pycache__/
	rm -rf brain_games/games/__pycache__/
	rm -rf brain_games/scripts/__pycache__/
	

lint:
		uv run ruff check brain_games
fix:
		uv run ruff check --fix
force:
	uv tool install --force dist/*.whl
	

format:
	uv run ruff format brain_games

check-format:
	uv run ruff format --check brain_games
	
reinstall: clean install build package-install
