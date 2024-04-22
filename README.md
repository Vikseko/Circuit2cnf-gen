# Circuit2cnf-gen
CNF generator encoding LEC and inversion problems (for multipliers, summators and sortings by now).

Supported multiplication algorithms:
1. Column;
2. Dadda algorithm;
3. Karatsuba decomposition;
4. Wallace tree.

Supported addition algorithms:
1. Simple;
2. LogHeight.

Supported sorting algorithms:
1. Bubble;
2. Pancake;
3. Selection.

CNF generation follows one of two schemes:
1. TA-program -> aag/aig -> CNF for inversion problem (with output corresponding to random input);
2. Aag + aag -> LEC CNF.


## Requirements:
### Python packages:
1. toposort from https://pypi.org/project/toposort/.

### Additional used apps:
1. Aigtoaig from https://github.com/arminbiere/aiger;
2. Transalg from https://gitlab.com/transalg/transalg/-/tree/develop?ref_type=heads;
3. A version of transalg that supports selecting an addition and multiplication algorithm from https://gitlab.com/transalg/transalg/-/tree/cmake?ref_type=heads;
4. SAT solver kissat from https://github.com/arminbiere/kissat.

All binaries should be located in the ./Apps/ folder.
Binary file for transalg, that supports selecting an addition and multiplication algorithm, must be named as "transalg_for_mults_and_sums".

## Usage
### Basic usage:

For multipliers:

> ./create_tests_mults.sh *first_number_size* *second_number_size*

For sortings:

> ./create_tests_sorts.sh *number_of_numbers* *single_number_size*

For summators:

> ./create_tests_sums.sh *first_number_size* *second_number_size*

This scripts creates aags, aigs, inversion CNFs and LEC CNFs for all considered algorithms of chosen class of problems.

Constructed CNFs can be found in *problemdir*/cnfs/ (*problemdir* is "Summators", "Multipliers", "Sortings", "Summators_LEC", "Multipliers_LEC" or "Sortings_LEC").

### For inversion problems only

Inside ./Multipliers/ or ./Summators/ directory:

> ./create_tests.sh N M

where N is the size of the first integer in bytes, M is the size of the second integer in bytes.

Inside ./Sortings/:

> ./create_tests.sh N M

where N is the number of numbers to sort, M is the size of the single number in bytes.

### For LEC problems only

Inside ./Multipliers_LEC/ or ./Summators_LEC/ directory:

> ./create_lec_tests.sh N M

where N is the size of the first integer in bytes, M is the size of the second integer in bytes.

Inside ./Sortings/:

> ./create_tests.sh N M

where N is the number of numbers to sort, M is the size of the single number in bytes.

To create a LEC problem, both source aags must be pre-created and located in ./*problemclass*/aags/ (*problemclass* is "Summators", "Multipliers", "Sortings").
