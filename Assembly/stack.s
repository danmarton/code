.global _start

.section .text

_start:
   push $1
   push $2		
   push $3
   push $4
   
   pop %ebx		
   
   add  (%esp), %ebx	# 4 + 3
   add 4(%esp), %ebx	# 7 + 2
   add 8(%esp), %ebx	# 9 + 1
   
   mov $1, %eax
   
   int $0x80
   