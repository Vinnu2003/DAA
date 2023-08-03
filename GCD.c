#include <stdio.h>
int gcd(int num1, int num2) {
    if (num1 < num2) {
        int temp = num1;
        num1 = num2;
        num2 = temp;
    }
    int remainder;
    while (num2 != 0) {
        remainder = num1 % num2;
        num1 = num2;
        num2 = remainder;
    }
    return num1;
}
int main() {
    int num1, num2;
    printf("Enter two numbers to find their GCD: ");
    scanf("%d %d", &num1, &num2);
    int result = gcd(num1, num2);
    printf("The GCD of %d and %d is: %d\n", num1, num2, result);
    return 0;
}
