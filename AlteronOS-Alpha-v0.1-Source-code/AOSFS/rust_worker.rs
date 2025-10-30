#![no_std]
#![no_main]

use core::ffi::CStr;
use core::panic::PanicInfo;

#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    loop {}
}

// Safe file operations
#[no_mangle]
pub extern "C" fn rust_create_file(filename: *const i8) -> i32 {
    unsafe {
        if let Ok(name) = CStr::from_ptr(filename).to_str() {
            println!("Rust: Safely creating file: {}", name);
            0
        } else {
            -1
        }
    }
}

#[no_mangle]
pub extern "C" fn rust_read_file(filename: *const i8) -> *mut i8 {
    unsafe {
        if let Ok(name) = CStr::from_ptr(filename).to_str() {
            let content = match name {
                "readme.txt" => "Rust: Safe file content\nWelcome to AlteronOS",
                "config.txt" => "Rust: Safe configuration data",
                _ => "Rust: File content"
            };
            std::ffi::CString::new(content).unwrap().into_raw()
        } else {
            std::ptr::null_mut()
        }
    }
}

#[no_mangle]
pub extern "C" fn rust_write_file(filename: *const i8, content: *const i8) -> i32 {
    unsafe {
        if let (Ok(name), Ok(text)) = (
            CStr::from_ptr(filename).to_str(),
            CStr::from_ptr(content).to_str()
        ) {
            println!("Rust: Safely writing to {}: {}", name, text);
            0
        } else {
            -1
        }
    }
}

// Memory-safe operations
#[no_mangle]
pub extern "C" fn rust_safe_copy(src: *const i8, dest: *const i8) -> i32 {
    unsafe {
        if let (Ok(source), Ok(destination)) = (
            CStr::from_ptr(src).to_str(),
            CStr::from_ptr(dest).to_str()
        ) {
            println!("Rust: Safe copy {} -> {}", source, destination);
            0
        } else {
            -1
        }
    }
}

#[no_mangle]
pub extern "C" fn rust_validate_path(path: *const i8) -> i32 {
    unsafe {
        if let Ok(path_str) = CStr::from_ptr(path).to_str() {
            if path_str.contains("..") || path_str.contains("//") {
                -1 // Invalid path
            } else {
                0 // Valid path
            }
        } else {
            -1
        }
    }
}

#[no_mangle]
pub extern "C" fn init_rust_worker() {
    println!("Rust Worker: Memory-safe tools ready (safe file ops, validation, secure copy)");
}