@echo off
echo Building AlteronOS...
make iso
if %errorlevel% equ 0 (
    echo Build successful!
    echo ISO: alteronos.iso
) else (
    echo Build failed!
)
pause