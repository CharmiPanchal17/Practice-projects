#include <stdio.h>

int stack[100], p = 0;  // Stack array and pointer

// Push function
void push(int x) {
    if (p < 100) {
        stack[p++] = x;
    }
}

// Check if stack is empty
int isEmpty() {
    return (p == 0); // Returns 1 (true) if empty, 0 (false) otherwise
}

// Pop function
int pop() {
    if (isEmpty()) {
        return -1; // Return -1 to indicate stack underflow
    } else {
        return stack[--p];
    }
}

// Peek function (view top element without popping)
int peek() {
    if (isEmpty()) {
        return -1; // Return -1 if stack is empty
    } else {
        return stack[p - 1];
    }
}

int main(void) {
    // Push numbers 0 to 9 onto the stack
    for (int i = 0; i < 10; i++) {
        push(i);
    }

    // Pop and print numbers in LIFO order
    for (int i = 0; i < 10; i++) {
        printf("%d ", pop());
    }
    
    printf("\n");  // Move to the next line after printing all elements

    return 0;
}
