import glob, os

from runipy.notebook_runner import NotebookRunner

for fn in glob.glob('*.ipynb'):
    if not fn.startswith('test'):
        r = NotebookRunner(fn)
        r.run_notebook()