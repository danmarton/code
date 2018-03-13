; Build: nasm exit_nasm.s -f elf -o exit.o
; Link: ld exit.o -o exit

global _start  ; Reserve _start for linker!

section .text  ; Code starts here (data section omitted)

_start:
   mov eax, 1   ; Opcode of Exit (read by the kernel)
   mov ebx, 0   ; Exit status (also read by the kernel)
  
   int 0x80    ; Kernel call