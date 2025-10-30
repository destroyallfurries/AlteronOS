package main

/*
#include <stdint.h>
extern void print(const char* str);
*/
import "C"
import "unsafe"

//export go_kext_init
func go_kext_init() {
	msg := C.CString("Go: Concurrent services ready")
	defer C.free(unsafe.Pointer(msg))
	C.print(msg)
}

func main() {}
