.type minimal, @function  #Not needed in this case
.global _start

.section .text

_start:
   push $11		#Put the argument on the stack
   call minimal		#Call the function
   add  $4, %esp	#Reset stack pointer
   
   push %ebx		#Save result
   
   push $22		#Second call
   call minimal
   add  $4, %esp

   add  (%esp), %ebx	#Retreive previous result
   
   mov  $1, %eax
   int  $0x80
   
minimal:
   mov  4(%esp), %ebx	#Reach over for argument
   ret			#Return
  