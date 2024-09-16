# This is the assembly code with O3 optimization:
<truncate_number>:
endbr64
cvttss2si %xmm0,%eax
pxor   %xmm1,%xmm1
cvtsi2ss %eax,%xmm1
subss  %xmm1,%xmm0
ret
# What is the source code?
