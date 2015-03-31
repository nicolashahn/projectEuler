-- Project Euler
-- Nicolas Hahn
-- Problem 17

removeSpace :: String -> String
removeSpace "" = ""
removeSpace (x:xs) = if x == ' ' then removeSpace xs else x:(removeSpace xs)

solution = length (removeSpace (concatMap sayNum [1..1000]))

main = print solution


-- code below is from an old homework assignment



--helper for sayNum
--x: takes the integer, 
--m: a multiple of 1000 that is 1/1000th the "illion", 
--s: the "illion" string of that, 
--and returns the whole number in string form
illion :: Integer -> Integer -> String -> String
illion x m s = sayNum (div x m) ++ s ++ if ((mod x m) /= 0)
                                        then sayNum (mod x m)
                                        else ""

sayNum :: Integer -> String
sayNum 0 = "zero "
sayNum 1 = "one "
sayNum 2 = "two "
sayNum 3 = "three "
sayNum 4 = "four "
sayNum 5 = "five "
sayNum 6 = "six "
sayNum 7 = "seven "
sayNum 8 = "eight "
sayNum 9 = "nine "
sayNum 10 = "ten "
sayNum 11 = "eleven "
sayNum 12 = "twelve "
sayNum 13 = "thirteen "
sayNum 14 = "fourteen "
sayNum 15 = "fifteen "
sayNum 16 = "sixteen "
sayNum 17 = "seventeen "
sayNum 18 = "eighteen "
sayNum 19 = "nineteen "
sayNum 20 = "twenty "
sayNum 30 = "thirty "
sayNum 40 = "forty "
sayNum 50 = "fifty "
sayNum 60 = "sixty "
sayNum 70 = "seventy "
sayNum 80 = "eighty "
sayNum 90 = "ninety "
sayNum x 
    | x < 100 = 
        sayNum ((div x 10) * 10) ++ sayNum (mod x 10)
    | (mod x 100 == 0) && (x < 1000) = 
    	sayNum (div x 100) ++ "hundred "
    | x < 1000 = 
        sayNum (div x 100) ++ "hundred and " ++ if ((mod x 100) /= 0) 
                                            then sayNum (mod x 100) 
                                            else ""
    | x < 1000000 = 
        sayNum (div x 1000) ++ "thousand" ++ if ((mod x 1000) /= 0) 
                                              then sayNum (mod x 1000) 
                                              else ""
