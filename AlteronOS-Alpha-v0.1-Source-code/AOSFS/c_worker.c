#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>

// LS - List directory contents
void c_ls(const char* path) {
    printf("drwxr-xr-x 1 root root 4096 Jan 1 00:00 System.dir\n");
    printf("drwxr-xr-x 1 root root 4096 Jan 1 00:00 Programs.dir\n");
    printf("drwxr-xr-x 1 root root 4096 Jan 1 00:00 Users.dir\n");
    printf("drwxr-xr-x 1 root root 4096 Jan 1 00:00 Config.dir\n");
    printf("-rw-r--r-- 1 root root  123 Jan 1 00:00 readme.txt\n");
    printf("-rw-r--r-- 1 root root  456 Jan 1 00:00 version.txt\n");
}

// CAT - Concatenate and print files
void c_cat(const char* filename) {
    if (strstr(filename, "readme")) {
        printf("Welcome to AlteronOS\n");
        printf("Built with C, Rust, Go, C++, Python\n");
    } else if (strstr(filename, "version")) {
        printf("AlteronOS v2.0\n");
        printf("Kernel: Python Manager\n");
        printf("FS: AOSFS\n");
    } else {
        printf("File content: %s\n", filename);
    }
}

// MKDIR - Make directories
int c_mkdir(const char* path) {
    printf("C: Creating directory: %s\n", path);
    return 0; // Success
}

// RM - Remove files/directories
int c_rm(const char* path) {
    printf("C: Removing: %s\n", path);
    return 0;
}

// CP - Copy files
int c_cp(const char* source, const char* dest) {
    printf("C: Copying %s to %s\n", source, dest);
    return 0;
}

// MV - Move files
int c_mv(const char* source, const char* dest) {
    printf("C: Moving %s to %s\n", source, dest);
    return 0;
}

// CHMOD - Change file modes
int c_chmod(const char* path, const char* mode) {
    printf("C: Changing permissions of %s to %s\n", path, mode);
    return 0;
}

// TOUCH - Create files
int c_touch(const char* filename) {
    printf("C: Creating file: %s\n", filename);
    return 0;
}

// ECHO - Display text
void c_echo(const char* text) {
    printf("%s\n", text);
}

// PWD - Print working directory
void c_pwd() {
    printf("A:\\Alteron\n");
}

// INIT - Initialize C worker
void init_c_worker() {
    printf("C Worker: Unix tools ready (ls, cat, mkdir, rm, cp, mv, chmod, touch, echo, pwd)\n");
}