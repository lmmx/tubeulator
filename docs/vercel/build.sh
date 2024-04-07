echo "MICROMAMBA VERSION REPORT"
~/micromamba/bin/python --version
echo "MKDOCS BUILD"
~/micromamba/bin/python -m pdm run mkdocs build -v
