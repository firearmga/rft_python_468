def if_prime(num):
    count = 0
    for i in range(1,num+1):
        if num%i == 0:
            count +=1

    if count == 2:
        return True
    return False



print(if_prime(9))


def largest(*args):
    return max(args)
print(largest(1,2,3,4,9))

def student_info(**kwargs):
    for i in kwargs:
        print(f"{i}={kwargs[i]}")

student_info(s_name="Alice", s_age=25, s_branch="AI-ML")

def nums(*args):
        return [f"max = {max(args)}", f"min = {min(args)}",f"mean = {sum(args)/len(args)}",f"sum = {sum(args)}"]
print(nums(1,2,3,4,9))

