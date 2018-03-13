#int main() { return my_fun(11) + my_fun(22); }
#int my_fun(x) { int i = x; return i; }

.global _start

.section .text

_start:
   
   push $11			#Put Argument on Stack
   call my_fun			#Call Function
   add  $4, %esp		#Remove Argument from Stack
   
   push  %eax			#Save Result
   
   push $22			#Second Call
   call my_fun
   add  $4, %esp
   
   pop %ebx
   add %eax, %ebx		#Return Sum of Results as Exit Code
   
   mov  $1, %eax
   int  $0x80
   
my_fun:
   push %ebp			#Save BP of Caller
   mov  %esp, %ebp		#Set BP for This Function
   
   sub  $4, %esp		#Make room for a Local Variable
   
   mov  8(%ebp), %ebx		#Reach back for Argument
   mov	%ebx, -4(%ebp)		#And store it in Local Variable
   
   #Algorithm goes here
   
   mov  -4(%ebp), %eax		#Return value goes to AX
   
   mov  %ebp, %esp		#Reset Stack Pointer
   pop  %ebp			#Re-load BP for Caller
   
   ret				#Return
   
   