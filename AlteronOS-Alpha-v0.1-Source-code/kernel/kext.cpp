#include <stdint.h>

extern "C" {
    void print(const char* str);
}

extern "C" void cpp_kext_init() {
    print("C++: Kernel extensions loaded");
}