.global _start

.section .data

numbers:			#Each number will occupy a 32-bit word
   .long 3,67,34,222,45,75,54,34,44,33,22,11,66,0

.section .text

_start:
   mov $0, %edi			#Set starting value for index
   mov numbers(,%edi,4), %ebx	#Move first item to Result register
   
loop_start:			
   inc %edi			#Increment index
   mov numbers(,%edi,4), %eax	#Move next number to Current register
   cmp $0, %eax			#Compare Current with zero
   je  loop_exit		#Exit if it's zero
   cmp %ebx, %eax		#Compare Current with Result
   jle loop_start		#Jump back if it's not greater
   mov %eax, %ebx		#Let Current replace Result otherwise
   jmp loop_start		#Restart the loop
   
   # Find minimum: Replace "jle" with "jge" on line 19
   
loop_exit:
   mov $1, %eax			#Opcode of Exit read at system call
   int $0x80			#System call
   