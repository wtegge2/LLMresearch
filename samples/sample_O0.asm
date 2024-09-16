# This is the assembly code with O0 optimization:
<truncate_number>:
endbr64
push   %rbp
mov    %rsp,%rbp
movss  %xmm0,-0x4(%rbp)
movss  -0x4(%rbp),%xmm0
cvttss2si %xmm0,%eax
pxor   %xmm1,%xmm1
cvtsi2ss %eax,%xmm1
movss  -0x4(%rbp),%xmm0
subss  %xmm1,%xmm0
pop    %rbp
ret
# What is the source code?
