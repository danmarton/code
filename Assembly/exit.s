.global _start		# Preserve the symbol "_start" for linker!

.section .text		# Code starts here (data section omitted)

_start:
   mov $1, %eax		# Opcode of Exit, read from here at system call
   mov $0, %ebx		# Exit status goes here (0 means success)
  
   int $0x80     # System call
