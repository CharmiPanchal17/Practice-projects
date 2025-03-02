#include <stdio.h>

int queue[100], p = 0;

void put(int x) {
    if (p < 100) 
        queue[p++] = x;
}

int isEmpty() {
    return (p == 0);
}

int get() {
    if (isEmpty()) 
        return -1;
    else {
        int i = 0, j = queue[0];
        for (; i < p - 1; i++) 
            queue[i] = queue[i + 1];
        p--;
        return j;
    }
}

int main(void) {
    // Push some numbers onto the queue
    for (int i = 0; i < 10; i++) 
        put(i);
    
    // Pop those numbers from the queue
    printf("Queue items:");
    for (int i = 0; i < 10; i++) 
        printf(" %d", get());
    
    printf("\n");
    return 0;
}
