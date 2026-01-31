#include <stdio.h>
#include <stdlib.h>

// 这是一个完全良性的程序
int main() {
    printf("[INFO] Service starting...\n");
    printf("[INFO] Loading optimization module v2.4...\n");
    
    //计算操作
    int volatile *ptr = (int *)malloc(sizeof(int));
    *ptr = 42;
    
    if (*ptr == 42) {
        printf("[INFO] Module loaded successfully.\n");
    }
    
    free((void*)ptr);
    return 0;
}