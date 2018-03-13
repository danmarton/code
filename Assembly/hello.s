.global _start

.section .data
hello:
   .ascii "Hello World!\n"
length:
   .long . -hello

.section .text
_start:
   mov $4, %eax		#Opcode for Write
   mov $1, %ebx		#File descriptor for standard output
   mov $hello, %ecx	#Start address of the thing to write
   mov length, %edx	#Number of bytes to write
   
   int $0x80
   
   mov %eax, %ebx
   mov $1, %eax
   
   int $0x80
   