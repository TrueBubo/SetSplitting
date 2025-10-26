# Set Splitting SAT solver
## Problem
According to [wikipedia](https://en.wikipedia.org/wiki/Set_splitting_problem)
> The set splitting problem is the following decision problem: given a family F of subsets of a finite set S, decide whether there exists a partition of S into two subsets $S_1$, $S_2$ such that all elements of F are split by this partition, i.e., none of the elements of F is completely in $S_1$ or $S_2$.

## Usage
### Terminal
```shell
python set-splitting-sat.py [INPUT]
```

Additional options include  
`--only-conversion` - Will print the CNF clauses generated, and will not attempt to solve them
`--verbose` - Prints the clauses, and also solves the problem

## Input
Input file includes the list of subsets of a finite set S. Each subset of new line with elements seperated by spaces.
It will implicitly assume the list goes from 1 to the highest number mentioned. If you have elements not mentioned in
subsets, they can go to both S1 and S2.

Example input:
```
1 2
1 3
1 4
```

## Encoding
Let assume the variable $p_i$ is equivalent to this statement: the $i$-th element lies in $S_1$  
From the problem definition `none of the elements of F is completely in S1 or S2`, we can deduct that for each subset
we cannot have all the element in $S_1$. Let $a_1 \dots a_k$ be the element of subset. Then the following is false
$a_1 \land a_2 \dots \land a_k$. From De Morgan's laws we can rewrite the negation of this statement as $a_1 \lor a_2 
\dots \lor a_k$. It also cannot be entirely in $S_2$, not lying in $S_1$ means lying in $S_2$, hence the $i$-th element
lying in $S_1$ will be denoted as $\lnot p_1$. And using the same principles as before we can get clause 
$\lnot a_1 \lor \lnot a_2 \dots \lnot a_k$. This must be true for every set, hence the clauses will be anded together.

The example DIMACS CNF of the above input
```s
1 2 0
1 3 0
1 4 0
-1 -2 0
-1 -3 0
-1 -4 0
```

## Experiments
In [inputs/](inputs)

### Human readable
- [input-sat-small](inputs/input-sat-small)
- [input-unsat-small](inputs/input-unsat-small)

### Medium
- [input-sat-medium-100-1k](inputs/input-sat-medium-100-1k) - Set size = 100, Subset count = 1000, takes 0.04s
- [input-sat-medium-100-10k](inputs/input-sat-medium-100-10k) - Set size = 100, Subset count = 10000, takes 1.4s

### Big
**Satisfiable**
- [input-sat-large-300-10k](inputs/input-sat-large-300-10k) - Set size = 300, Subset count = 10000, takes 56s

**Unsatisfiable**
- [input-unsat-large-20-80k](inputs/input-unsat-large-20-80k) - Set size = 20, Subset count = 80k, takes 14s