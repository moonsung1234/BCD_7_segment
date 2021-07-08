
// BCD-to-7 segments display
// 0~4 inputs (4 bits)

#include <stdio.h>

int getBit(int number, int hex) {
    if(number & hex) {
        return 1;
    }

    return 0;
}

int main() {
    int input;

    scanf_s("%d", &input, sizeof(int));

    //decimal, A(MSB), B(second bit), C(third bit), D(LSB) => a
    // 0, 0, 0, 0, 0 => 1
    // 1, 0, 0, 0, 1 => 0
    // 2, 0, 0, 1, 0 => 1
    // 3, 0, 0, 1, 1 => 1
    // 4, 0, 1, 0, 0 => 0
    // 논리식(K-map 추론) : a = A`B`C + A`B`D`

    int a = (!getBit(input, 0x8) * !getBit(input, 0x4) * getBit(input, 0x2)) | (!getBit(input, 0x8) * !getBit(input, 0x4) * !getBit(input, 0x1));

    //decimal, A(MSB), B(second bit), C(third bit), D(LSB) => f
    // 0, 0, 0, 0, 0 => 1
    // 1, 0, 0, 0, 1 => 0
    // 2, 0, 0, 1, 0 => 0
    // 3, 0, 0, 1, 1 => 0
    // 4, 0, 1, 0, 0 => 1
    // 논리식(K-map 추론) : f = A`C`D`

    int f = !getBit(input, 0x8) * !getBit(input, 0x2) * !getBit(input, 0x1);

    //decimal, A(MSB), B(second bit), C(third bit), D(LSB) => b
    // 0, 0, 0, 0, 0 => 1
    // 1, 0, 0, 0, 1 => 1
    // 2, 0, 0, 1, 0 => 1
    // 3, 0, 0, 1, 1 => 1
    // 4, 0, 1, 0, 0 => 1
    // 논리식(K-map 추론) : b = A`B` + A`C`D`

    int b = (!getBit(input, 0x8) * !getBit(input, 0x4)) | (!getBit(input, 0x8) * !getBit(input, 0x2) * !getBit(input, 0x1)); 

    //decimal, A(MSB), B(second bit), C(third bit), D(LSB) => g
    // 0, 0, 0, 0, 0 => 0
    // 1, 0, 0, 0, 1 => 0
    // 2, 0, 0, 1, 0 => 1
    // 3, 0, 0, 1, 1 => 1
    // 4, 0, 1, 0, 0 => 1
    // 논리식(K-map 추론) : g = B + A`B`C

    int g = getBit(input, 0x4) | (!getBit(input, 0x8) * !getBit(input, 0x4) * getBit(input, 0x2)); 

    //decimal, A(MSB), B(second bit), C(third bit), D(LSB) => e
    // 0, 0, 0, 0, 0 => 1
    // 1, 0, 0, 0, 1 => 0
    // 2, 0, 0, 1, 0 => 1
    // 3, 0, 0, 1, 1 => 0
    // 4, 0, 1, 0, 0 => 0
    // 논리식(K-map 추론) : e = A'B'D'

    int e = !getBit(input, 0x8) * !getBit(input, 0x4) * !getBit(input, 0x1); 
    
    //decimal, A(MSB), B(second bit), C(third bit), D(LSB) => c
    // 0, 0, 0, 0, 0 => 1
    // 1, 0, 0, 0, 1 => 1
    // 2, 0, 0, 1, 0 => 0
    // 3, 0, 0, 1, 1 => 1
    // 4, 0, 1, 0, 0 => 1
    // 논리식(K-map 추론) : c = A`C`D` + A`B`D

    int c = (!getBit(input, 0x8) * !getBit(input, 0x2) * !getBit(input, 0x1)) | (!getBit(input, 0x8) * !getBit(input, 0x4) * getBit(input, 0x1)); 

    //decimal, A(MSB), B(second bit), C(third bit), D(LSB) => d
    // 0, 0, 0, 0, 0 => 1
    // 1, 0, 0, 0, 1 => 0
    // 2, 0, 0, 1, 0 => 1
    // 3, 0, 0, 1, 1 => 1
    // 4, 0, 1, 0, 0 => 0
    // 논리식(K-map 추론) : c = A`C`D` + A`B`C

    int d = (!getBit(input, 0x8) * !getBit(input, 0x2) * !getBit(input, 0x1)) | (!getBit(input, 0x8) * !getBit(input, 0x4) * getBit(input, 0x2)); 

    printf("%d %d %d %d %d %d %d", a, f, b, g, e, c, d);

    return 0;
}