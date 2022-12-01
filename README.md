# advent_of_code_2022
Advent of Code 2022 solutions:
[Advent of Code 2022](https://adventofcode.com/2022) daily challenges code solutions.

## Solutions as Jupyter Lab sheet - Python (v3.10)
Using [Python language](https://www.python.org/)

* `aoc_2022.ipynb` - Main Jupyter Lab Notebook for solutions
* `./pylib/aochelper.py` - AoC helper module, imported using `sys.path`
* `./in/day##.in` - store your individual days challenge textfile inputs in those files
* `aoc_2022.py` - jupyter lab sheet exported as executable script

## Solutions as Jupyter Lab sheet - Coconut language (v2.1.1)
Same as above, but using [Coconut language](https://coconut-lang.org/) on top of Python.

* `aoc_2022_coco.ipynb` - Main Jupyter Lab Notebook for solutions
* `./pylib/aochelper.py` - see above
* `./in/day##.in` - see above
* `aoc_2022_coco.coco` - jupyter lab sheet exported as executable script

## Clojure solutions
As script, see individual days in directories `day[dd]`.
Run like:

    clojure -M day01/day01.clj

## Kotlin solutions
As script, see individual days in directories `day[dd]`.
Run like:

    kotlinc day01/day01.kt -d day01/day01.jar && kotlin -classpath day01/day01.jar Day01Kt