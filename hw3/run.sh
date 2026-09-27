uv run \
  --no-project \
  --python 3.10 \
  --with-requirements requirements.txt \
  main.py 2>&1 | tee run.log
