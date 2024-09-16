
/home/wtegge2/LLM4Decompile/samples/sample_O1.o:     file format elf64-x86-64


Disassembly of section .text:

0000000000000000 <truncate_number>:
   0:	f3 0f 1e fa          	endbr64 
   4:	f3 0f 2c c0          	cvttss2si %xmm0,%eax
   8:	66 0f ef c9          	pxor   %xmm1,%xmm1
   c:	f3 0f 2a c8          	cvtsi2ss %eax,%xmm1
  10:	f3 0f 5c c1          	subss  %xmm1,%xmm0
  14:	c3                   	ret    
