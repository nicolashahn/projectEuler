-- Project Euler
-- Nicolas Hahn
-- Problem 4

palindromic :: String -> Bool
palindromic "" = True
palindromic i = case length i of
					1		-> True
					_		-> if (head i) == (last i)
								then palindromic (tail (init i))
								else False

intPalindromic :: Int -> Bool
intPalindromic i = palindromic (show i)

-- Takes a maximum int, and multiplies all ints from 1 to the max by all ints from 1 to max
-- and returns the largest palindromic product
solution :: Int -> Int
solution i = maximum ( filter intPalindromic [ (x*y) | x <- [1..i], y <- [1..i] ] ) 

main = putStr (show (solution 999))