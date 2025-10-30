# AlteronOS MSYS2 Makefile
PYTHON = python
CC = gcc
CXX = g++
RUSTC = rustc
GO = go
NASM = nasm

all: iso

iso: kernel.bin grub.cfg
	mkdir -p build/isodir/boot/grub
	cp kernel.bin build/isodir/boot/
	cp grub.cfg build/isodir/boot/grub/
	grub-mkrescue -o alteronos.iso build/isodir

kernel.bin: boot.bin loader.bin
	cat boot.bin loader.bin > kernel.bin

boot.bin: boot.asm
	nasm -f bin boot.asm -o boot.bin

loader.bin: loader.asm
	nasm -f bin loader.asm -o loader.bin

libc_worker.so: c_worker.c
	$(CC) -shared -fPIC -o libc_worker.so c_worker.c

librust_worker.so: rust_worker.rs
	$(RUSTC) --crate-type cdylib -o librust_worker.so rust_worker.rs

libgo_worker.so: go_worker.go
	$(GO) build -buildmode=c-shared -o libgo_worker.so go_worker.go

libcpp_worker.so: cpp_worker.cpp
	$(CXX) -shared -fPIC -o libcpp_worker.so cpp_worker.cpp

run: iso
	qemu-system-x86_64 -cdrom alteronos.iso

clean:
	rm -rf build *.bin *.so *.iso

.PHONY: all iso run clean