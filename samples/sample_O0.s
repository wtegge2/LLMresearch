
/home/wtegge2/LLM4Decompile/samples/sample_O0.o:     file format elf64-x86-64


Disassembly of section .text:

0000000000000000 <truncate_number>:
   0:	f3 0f 1e fa          	endbr64 
   4:	55                   	push   %rbp
   5:	48 89 e5             	mov    %rsp,%rbp
   8:	f3 0f 11 45 fc       	movss  %xmm0,-0x4(%rbp)
   d:	f3 0f 10 45 fc       	movss  -0x4(%rbp),%xmm0
  12:	f3 0f 2c c0          	cvttss2si %xmm0,%eax
  16:	66 0f ef c9          	pxor   %xmm1,%xmm1
  1a:	f3 0f 2a c8          	cvtsi2ss %eax,%xmm1
  1e:	f3 0f 10 45 fc       	movss  -0x4(%rbp),%xmm0
  23:	f3 0f 5c c1          	subss  %xmm1,%xmm0
  27:	5d                   	pop    %rbp
  28:	c3                   	ret    
