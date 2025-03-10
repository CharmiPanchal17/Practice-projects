#include <stdio.h>

// Function to calculate factorial using recursion
int factorial(int n) {
    if (n < 0)
        return -1;  // Return -1 for negative numbers (invalid input)
    else if (n == 0)
        return 1;   // Base case: factorial of 0 is 1
    else
        return n * factorial(n - 1);  // Recursive case
}

int main() {
    int num;
    
    // Taking input from the user
    printf("Enter a number: ");
    scanf("%d", &num);
    
    int result = factorial(num);
    
    if (result == -1)
        printf("Factorial of negative numbers is not defined.\n");
    else
        printf("Factorial of %d is %d\n", num, result);

    return 0;
}

//The function factorial takes an integer n as input.
//Inside the function, there are three cases:
// If n is less than 0, the function returns -1. This is because the factorial of negative numbers is not defined.
// If n is equal to 0, the function returns 1. This is the base case of the recursion, where the factorial of 0 is 1.
// If n is greater than 0, the function calls itself with the argument n - 1 and multiplies the result by n. 
//This is the recursive case, where the factorial of n is calculated by multiplying n with the factorial of n - 1.
// The function continues to call itself recursively until it reaches the base case (when n is 0), 
//and then it starts returning the results back up the call stack, multiplying each result by the corresponding n value until it reaches the original call.
//This process calculates the factorial of the input number.