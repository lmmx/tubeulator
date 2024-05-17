name: Build and Test

on:
  push:
    branches: [master]
  pull_request:
    branches: [master]

jobs:
  test-setup:
    runs-on: ubuntu-latest
    outputs:
      test-matrix: ${{ steps.set-matrix.outputs.test_matrix }}
    steps:
      - uses: actions/checkout@v4

      - id: set-matrix
        run: |
          ALL_TEST_TARGETS=$(find tests -mindepth 1 -type d -name *_test.py -exec realpath --relative-to=tests {} \;)
          PACKAGE_MATRIX_JSON=$(echo "$ALL_TEST_TARGETS" | sort | jq -R -s -c 'split("\n")[:-1] | map({testtarget: .})')
          echo "Setting test_matrix to: $PACKAGE_MATRIX_JSON"
          echo "test_matrix=$PACKAGE_MATRIX_JSON" >> $GITHUB_OUTPUT

  test:
    runs-on: ubuntu-latest
    needs: test-setup
    env:
      TFL_API_KEY_ID: ${{ secrets.TFL_API_KEY_ID }}
      TFL_API_PRIMARY_ACCESS_KEY: ${{ secrets.TFL_API_PRIMARY_ACCESS_KEY }}
      TFL_API_SECONDARY_ACCESS_KEY: ${{ secrets.TFL_API_SECONDARY_ACCESS_KEY }}
    strategy:
      fail-fast: false
      matrix:
        include: ${{ fromJson(needs.test-setup.outputs.test-matrix) }}
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install PDM
        run: |
          python -m pip install --user pdm
          pdm config install.cache on

      - name: Install package dependencies and run unit tests
        timeout-minutes: 5
        run: |
          set -ex
          test_target=tests/${{ matrix.testtarget }}
          target_dir=$(dirname "$test_target")

          INSTALL_START_TIME=$(date +%s)
          echo "- Installing tubeulator :: $(date)"
          if [[ ! -f "pyproject.toml" ]]; then
            echo "pyproject.toml does not exist"
            exit 1
          fi
          # This would become useful if .venv caching was introduced
          if [[ ! -d ".venv" ]]; then
            echo "Creating new venv from the test group of 'pyproject.toml'"
            pdm install -dG test
          fi
          INSTALL_END_TIME=$(date +%s)
          INSTALL_ELAPSED_TIME=$(($INSTALL_END_TIME - $INSTALL_START_TIME))
          echo "- Finished installing $service, now running tests :: $(date)"

          TEST_START_TIME=$(date +%s)
          pdm run python -m pytest $test_target -m "not skiponci" -n auto -qq --disable-warnings --suppress-no-test-exit-code
          TEST_END_TIME=$(date +%s)

          TEST_ELAPSED_TIME=$(($TEST_END_TIME - $TEST_START_TIME))
          echo "- Installed tubeulator (target: <code>$test_target</code>) in $INSTALL_ELAPSED_TIME seconds, tests passed in $TEST_ELAPSED_TIME seconds," >> $GITHUB_STEP_SUMMARY