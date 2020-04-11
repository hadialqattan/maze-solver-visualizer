if [[ $1 == "" ]]; then 
    python3 -m src
elif [[ $1 == "tests" ]]; then
    pytest -vv tests/a01_datastructure_tests.py tests/b02_algorithm_tests.py
else
    echo "Usage: ./run.sh [tests]"
fi
