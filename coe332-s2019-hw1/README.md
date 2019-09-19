# COE332 Fall 2019 Homework 1

### Preliminary Steps

- Make a *private fork* of this repo
- Share it with `ubik10`, `jchuahtacc`, `abkahn`
- Log in to `coe332.tacc.utexas.edu`
- Make a Python 3 virtual environment using the command `python3 -m venv coe332-venv`
- Activate the virtual environment using the command `source ~/coe332-venv/bin/activate`
- Install `coverage` using the command `pip install coverage`
- Clone *your fork* of the repository

### Using the repository

- Make sure your working directory is your local copy of the repository using the command `cd ~/coe332-f2019-hw1` (assuming that's where you cloned it)
- Create a file called `HW1.md` that lists your name and EID
- Stage changed files using the command `git add <filename>` (or to stage all changes from the root of the local repo, `git add .`)
- Commit your staged changes with `git commit`
- Push your changes with `git push origin master`

### Task 0: Running the program and getting coverage

- See what the current output of your program is, by running the command `python main.py`
- You can compare it to the expected output by running the command `python main.py | diff output.txt -`
- _*DO NOT overwrite the output.txt file!*_
- You can run local coverage reports using `coverage run --source=hw1 -m unittest discover -s hw1/ -p "*_test.py"` and `coverage report` or you can simply watch your Pipelines run on Bitbucket

### Task 1: The `read_data` function.

In the `hw1/hw.py` file, make the `read_data` function read in the CSV file `rainfall.csv`. The first line of the file contains column information. Each subsequent line of data has values corresponding with the headers. `read_data` should return a Python list of dictionaries, where each dictionary corresponds to a line of data in the file. For expected output, you may look at the `hw1_test.py` unit test file.

### Task 2: The `dates` function

In the `hw1/hw1.py` file, make the `dates` function filter dictionaries for years of data. It has one required parameter `data`, which should be provided from the returned data from `read_data()`. If the optional `start` parameter is specified, the `dates` function should return a list containing dictionaries where the `year` is greater than or equal to the `start`. If the optional `end` parameter is specified, it should return a list containing dictionaries where the `year` is less than or equal to the `end`. If both are specified, it should return a list containing dictionaries where the year is between `start` and `end`, inclusively. If neither optional parameters are specified, it should return all of the data.

### Task 3: The `paginate` function

In the `hw1/hw1.py` file, make the `paginate` function return a slice of the data passed to it in the `data` parameter, which should be provided from the returned data from `read_data()`. If the optional parameter `offset` is specified, it should skip the first `offset` number of entries and return a list of the remaining entries. If the optional parameter `limit` is provided, it should limit the number of returned list items to the number specified. If both `offset` and `limit` are provided, then `paginate` should skip `offset` entries and return a list of the next `limit` entries. If neither are provided, `paginate` should return the complete list.

### Task 4: Unit Tests

Provided complete coverage for `hw1/hw1.py` by writing additional unit tests in `hw1/hw1_test.py` to cover the `paginate` function.

### How you will be graded

You will be graded on the basis of your Bitbucket Pipeline output. Full credit is awarded to repositories that demonstrate:
- All unit tests passing
- Full coverage of `hw1.py`
- Matching output between `python main.py` and `output.txt`
