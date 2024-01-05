# Circuit2cnf-mults-gen
CNF generator encoding LEC and inversion problems for multipliers.

Repository with multiplier test generator by circuits 
1. TA-program -> aag/aig -> CNF for multiplier inversion problem (with output corresponding to random input);
2. Aag + aag -> LEC CNF.

Additional used apps:
1. Aigtoaig from https://github.com/arminbiere/aiger
2. Transalg from https://gitlab.com/transalg/transalg/-/tree/cmake?ref_type=heads
Both binaries should be located in the ./Apps/ folder.

# Usage
For inversion problem:

./Multipliers/create_tests.sh N M

where N is the size of the first integer in bytes, M is the size of the second integer in bytes.

For LEC problem:

./Multipliers_LEC/create_lec_tests.sh N M

where N is the size of the first integer in bytes, M is the size of the second integer in bytes.

To create a LEC problem, both source aags must be pre-created and located in ./Multipliers/aags/ .
