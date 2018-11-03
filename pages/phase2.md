---
layout: page
current: about
title: Binary Bomb Lab Phase 2
navigation: true
class: page-template
subclass: 'post page'
cover: /assets/images/about-header.jpg
cover-height: 400
---

#### Phase 2 Solution

Let's get started by creating both a breakpoint for `explode_bomb` and `phase_2`. This second phase deals with numbers so let's try to enter the array of numbers `0 1 2 3 4 5`. It is important to step the test numbers in some way so you know which order they are in.

Phase 1 defused. How about the next one?
0 1 2 3 4 5

Breakpoint 2, 0x0000000000400e49 in phase_2 ()

Let's do the standard `disas` command to see the assembly of the function. 

(gdb) disas
Dump of assembler code for function phase_2:
=> 0x0000000000400e49 <+0>:     push   %rbp
   0x0000000000400e4a <+1>:     push   %rbx
   0x0000000000400e4b <+2>:     sub    $0x28,%rsp
   0x0000000000400e4f <+6>:     mov    %rsp,%rsi
   0x0000000000400e52 <+9>:     callq  0x401420 <read_six_numbers>
   0x0000000000400e57 <+14>:    cmpl   $0x0,(%rsp)
   0x0000000000400e5b <+18>:    jns    0x400e62 <phase_2+25>
   0x0000000000400e5d <+20>:    callq  0x4013ea <explode_bomb>
   0x0000000000400e62 <+25>:    mov    %rsp,%rbp
   0x0000000000400e65 <+28>:    mov    $0x1,%ebx
   0x0000000000400e6a <+33>:    mov    %ebx,%eax
   0x0000000000400e6c <+35>:    add    0x0(%rbp),%eax
   0x0000000000400e6f <+38>:    cmp    %eax,0x4(%rbp)
   0x0000000000400e72 <+41>:    je     0x400e79 <phase_2+48>
   0x0000000000400e74 <+43>:    callq  0x4013ea <explode_bomb>
   0x0000000000400e79 <+48>:    add    $0x1,%ebx
   0x0000000000400e7c <+51>:    add    $0x4,%rbp
   0x0000000000400e80 <+55>:    cmp    $0x6,%ebx
   0x0000000000400e83 <+58>:    jne    0x400e6a <phase_2+33>
   0x0000000000400e85 <+60>:    add    $0x28,%rsp
   0x0000000000400e89 <+64>:    pop    %rbx
   0x0000000000400e8a <+65>:    pop    %rbp
   0x0000000000400e8b <+66>:    retq
End of assembler dump.

Also run the command `i r` to see what the values of the variables are.

(gdb) i r
rax            0x603bf0 6306800
rbx            0x0      0
rcx            0xb      11
rdx            0x603bf0 6306800
rsi            0x1      1
rdi            0x603bf0 6306800
rbp            0x402140 0x402140 <__libc_csu_init>
rsp            0x7fffffffdea8   0x7fffffffdea8
r8             0x60567c 6313596
r9             0x7ffff7fe8500   140737354040576
r10            0x7ffff7fe8500   140737354040576
r11            0x246    582
r12            0x400c00 4197376
r13            0x7fffffffdf90   140737488347024
r14            0x0      0
r15            0x0      0
rip            0x400e49 0x400e49 <phase_2>
eflags         0x202    [ IF ]
cs             0x33     51
ss             0x2b     43
ds             0x0      0
es             0x0      0
fs             0x0      0
gs             0x0      0


It also might be easier to visualize the operations by using an online disambler like https://onlinedisassembler.com/ to see a full graph.

As we can see, it is fairly obvious that there is a **loop** somewhere in this function (by following the arrows). In the first block of code, the function `read_six_numbers` is called which essentially confirms that it is six numbers which are seperated by a space (as we entered in the first part of this phase). If that function fails, it calls `explode_bomb` to the left. If the function succeeds, it follows the green arrow on the right to the third box.

In order to determine the comparisons used, it will be useful to look up or know "Jumps Based on Signed Comparisons".