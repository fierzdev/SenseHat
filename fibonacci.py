class Fibonacci:
	def fib(self,x):
		if(x<0):
			print("Invalid option")
			return
		if(x==0):
			return 0
		if(x==1):
			return 1
		return self.fib(x-1) + self.fib(x-2) 


	def factorial(self,n):
	    if n == 1:
	        return 1
	    else:
	        return n * self.factorial(n-1)
