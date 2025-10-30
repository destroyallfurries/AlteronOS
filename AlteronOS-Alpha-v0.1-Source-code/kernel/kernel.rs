#![no_std]
#![no_main]

use core::panic::PanicInfo;

#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    loop {}
}

#[no_mangle]
pub extern "C" fn rust_kernel_init() {
    unsafe {
        super::print(b"Rust: Kernel components ready\0".as_ptr() as *const i8);
    }
}b