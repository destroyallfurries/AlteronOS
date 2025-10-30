; AlteronOS Bootloader with Enhanced Features
bits 16
org 0x7C00

section .text
global _start

_start:
    ; Set video mode - 80x25 text
    mov ax, 0x0003
    int 0x10
    
    ; Print enhanced boot message
    mov si, banner
    call print
    call print_newline
    
    ; Display loading components
    mov si, loading_msg
    call print
    
    ; Load kernel components
    call load_kernel_manager
    call load_native_workers
    call load_compatibility_layer
    
    ; Jump to kernel
    jmp 0x1000:0000

print:
    lodsb
    test al, al
    jz .done
    mov ah, 0x0E
    int 0x10
    jmp print
.done:
    ret

print_newline:
    mov ah, 0x0E
    mov al, 0x0D
    int 0x10
    mov al, 0x0A
    int 0x10
    ret

load_kernel_manager:
    mov si, load_kernel_msg
    call print
    ; Load kernel to 0x1000
    mov ax, 0x1000
    mov es, ax
    mov bx, 0x0000
    mov ah, 0x02
    mov al, 15
    mov ch, 0
    mov cl, 2
    mov dh, 0
    mov dl, 0x80
    int 0x13
    ret

load_native_workers:
    mov si, load_workers_msg
    call print
    ; Load native workers
    ret

load_compatibility_layer:
    mov si, load_compat_msg
    call print
    ; Load compatibility layer
    ret

; Data section
banner db "AlteronOS v2.0 - Universal OS", 0
loading_msg db "Loading components...", 0
load_kernel_msg db " [KERNEL]", 0
load_workers_msg db " [WORKERS]", 0
load_compat_msg db " [COMPAT]", 0

times 510-($-$$) db 0
dw 0xAA55