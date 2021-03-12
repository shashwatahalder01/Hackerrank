# Complete the solve function below.
def solve(s):
    s=s.split(" ")
    s=[x.capitalize() for x in s]
    return " ".join(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
