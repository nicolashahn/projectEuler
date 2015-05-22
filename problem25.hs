memoized_fib :: Int -> Integer
memoized_fib = (map fib [0 ..] !!)
   where fib 0 = 0
         fib 1 = 1
         fib n = memoized_fib (n-2) + memoized_fib (n-1)

solution n = if length (show (memoized_fib n)) == 1000 then n 
				else solution (n+1)

main = do
	let result = solution 1
	print result