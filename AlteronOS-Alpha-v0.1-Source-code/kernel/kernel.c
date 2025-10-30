#include <stdint.h>

uint16_t* vga_buffer = (uint16_t*)0xB8000;

void print(const char* str) {
    static int cursor = 0;
    while (*str) {
        vga_buffer[cursor++] = (uint16_t)(0x07 << 8) | *str++;
    }
}

extern void rust_kernel_init();
extern void cpp_kext_init();
extern void go_kext_init();

void kernel_main() {
    for (int i = 0; i < 80 * 25; i++) {
        vga_buffer[i] = (uint16_t)0x0720;
    }
    
    print("AlteronOS Kernel v2.0");
    print("\nInitializing Rust components...");
    rust_kernel_init();
    
    print("\nLoading kernel extensions...");
    cpp_kext_init();
    go_kext_init();
    
    print("\nStarting Python kernel manager...");
    
    while(1) {
        asm("hlt");
    }
}