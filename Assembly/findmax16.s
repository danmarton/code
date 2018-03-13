.global _start

.section .data

numbers:			#Each number will occupy a 32-bit word
   .short 3,67,34,222,45,75,54,34,44,33,22,11,66,0

.section .text

_start:
   mov $0, %di			#Set starting value for index
   mov numbers(,%edi,2), %bx	#Move first item to Result register
   
loop_start:			
   inc %di			#Increment index
   mov numbers(,%edi,2), %ax	#Move next number to Current register
   cmp $0, %ax			#Compare Current with zero
   je  loop_exit		#Exit if it's zero
   cmp %bx, %ax			#Compare Current with Result
   jle loop_start		#Jump back if it's not greater
   mov %ax, %bx			#Let Current replace Result otherwise
   jmp loop_start		#Restart the loop
   
   # DI must be extended in the memory addressing scheme!
   # Find minimum: Replace "jle" with "jge" on line 19
   
loop_exit:
   mov $1, %ax			#Opcode of Exit read at system call
   int $0x80			#System call
   