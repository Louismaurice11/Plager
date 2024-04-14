#include <stdio.h>

int get_factorial(int n) {
    if (n == 0) {
        return 1;
    }
    int result = 1;
    int i = 1;
    while (i <= n) {
        result *= i;
        i++;
    }
    return result;
}

double get_power_of(double base, double exponent) {
    double result = 1.0;
    int i = 0;
    while (i < exponent) {
        result *= base;
        i++;
    }
    return result;
}

double find_square_root_of(double n) {
    double x = n;
    double y = 1.0;
    double epsilon = 0.000001;
    for (; x - y > epsilon; ) {
        x = (x + y) / 2.0;
        y = n / x;
    }
    return x;
}

int find_sum_of(int arr[], int n) {
    int sum = 0;
    int i = 0;
    while (i < n) {
        sum += arr[i];
        i++;
    }
    return sum;
}

int main (int argc, char *argv[]) {
    int n = 5;
    int arr[] = {1, 2, 3, 4, 5};
    int sum = find_sum_of(arr, n);
    double square_root = find_square_root_of(sum);
    double power = get_power_of(square_root, n);
    int factorial = get_factorial(n);
    printf("Sum: %d\nSquare Root of Sum: %f\nPower: %f\nFactorial: %d\n", sum, square_root, power, factorial);
    return 0;
}