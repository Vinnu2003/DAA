#include <stdio.h>
int main() {
    int n, k, i, j;
    printf("Enter the value of n: ");
    scanf("%d", &n);
    printf("Enter the value of k: ");
    scanf("%d", &k);

    if (n < 0 || k < 0 || k > n) {
        printf("Invalid input.\n");
        return 0;
    }

    int dp[10][10];

    for (i = 0; i <= n; i++) {
        for (j = 0; j <= k && j <= i; j++) {
            if (j == 0 || j == i) {
                dp[i][j] = 1;
            } else {
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
            }
        }
    }

    printf("C(%d, %d) = %d\n", n, k, dp[n][k]);

    return 0;
}

