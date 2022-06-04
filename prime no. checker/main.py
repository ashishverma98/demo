def prime_num_checker(x,y):
    for num in range(x,y):
        is_prime = True
        for i in range(2,num):
            if num%i==0:
                is_prime=False
        if is_prime:
            print(f"{num} prime")
        else:
            print(f"{num} not prime")
            
        
prime_num_checker(1,100)