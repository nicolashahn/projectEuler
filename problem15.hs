-- Project Euler
-- Nicolas Hahn
-- Problem 15

import Data.List

solution = length (nub (permutations [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]))

main = print solution