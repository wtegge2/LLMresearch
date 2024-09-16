#include <stdio.h>
#include <stdio.h>
#include <assert.h>

static void func0(int n, int m, int *a, int *b) {
    *b = 0;
    while (n < m) {
        if (n % 10) {
            a[*b] = n;
            (*b)++;
        }
        n++;
    }
}