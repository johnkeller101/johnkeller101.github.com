---
layout: page
current: about
title: Binary Bomb Lab (All Phases Solved)
navigation: true
class: page-template
subclass: 'post page'
cover:
cover-height: 400

date: 2018-10-22 20:50:00

---

#### Getting Started
----------

First, setup your bomb directory. Untar your specific file and let's get started!

```
jupyter:~$ cd Labs
jupyter:~/Labs$ tar -xvf bomb439.tar
bomb439/README
bomb439/bomb.c
bomb439/bomb
jupyter:~/Labs$ cd bomb439
jupyter:~/Labs/bomb439$ ls
bomb  bomb.c  README
jupyter:~/Labs/bomb439$
```

#### Getting Strings and Objdump
----------

Run the following commands to create text files which we will look at later:


```
strings bomb > strings.txt
objdump -d bomb > assembly.txt
```

You should now have two files: `strings.txt` and `assembly.txt`. Now let's get started with Phase 1!

### Phase 1
----------

```
jupyter:~/Labs/bomb439$ gdb bomb
```

Let's create our breakpoints to make sure nothing get's set to the gradebook!

```
    (gdb) b explode_bomb
	Breakpoint 1 at 0x4013ea
	(gdb) b phase_1
	Breakpoint 2 at 0x400e2d
```

Let's run it and test things out:

```
    (gdb) run
	Starting program: /home/jovyan/Labs/bomb439/bomb
	Welcome to my fiendish little bomb. You have 6 phases with
	which to blow yourself up. Have a nice day!
```

Okay, we know it works. Let's enter a test string to let the program hit our break point. You can enter any string, but I used `TEST`.

```
    TEST

	Breakpoint 2, 0x0000000000400e2d in phase_1 ()
```

Now let's take a quick look at the disassebly to see what variables are being used. Enter `disas` and you will get a chunk of assembly for the function `phase_1` which we put our breakpoint at.

```
(gdb) disas
Dump of assembler code for function phase_1:
=> 0x0000000000400e2d <+0>:     sub    $0x8,%rsp
   0x0000000000400e31 <+4>:     mov    $0x402310,%esi
   0x0000000000400e36 <+9>:     callq  0x401213 <strings_not_equal>
   0x0000000000400e3b <+14>:    test   %eax,%eax
   0x0000000000400e3d <+16>:    je     0x400e44 <phase_1+23>
   0x0000000000400e3f <+18>:    callq  0x4013ea <explode_bomb>
   0x0000000000400e44 <+23>:    add    $0x8,%rsp
   0x0000000000400e48 <+27>:    retq
End of assembler dump.
```

We can see that the `<strings_not_equal>` function is being called which as the name implies compares two strings. The variable being used in this comparison is `$eax`. We can see one line above that `$esi` is also involved. Let's use that address in memory and see what it contains as a string.


```
(gdb) x/25c 0x402310
0x402310:       73 'I'  32 ' '  99 'c'  97 'a'  110 'n' 32 ' '  115 's' 101 'e'
0x402318:       101 'e' 32 ' '  82 'R'  117 'u' 115 's' 115 's' 105 'i' 97 'a'
0x402320:       32 ' '  102 'f' 114 'r' 111 'o' 109 'm' 32 ' '  109 'm' 121 'y'
0x402328:       32 ' '
```

Based on the output, our input string is being run into the `<strings_not_equal>` function with the string **"I can see Russia from my "**. We can open our `strings.txt` file and see that the string we found in memory is the beginning of the full string: **"I can see Russia from my house!"**

```
Welcome to my fiendish little bomb. You have 6 phases with
which to blow yourself up. Have a nice day!
I can see Russia from my house!
Phase 1 defused. How about the next one?
```

### Phase 2
----------

Let's get started by creating both a breakpoint for `explode_bomb` and `phase_2`. This second phase deals with numbers so let's try to enter the array of numbers `0 1 2 3 4 5`. It is important to step the test numbers in some way so you know which order they are in.
```
Phase 1 defused. How about the next one?
0 1 2 3 4 5

Breakpoint 2, 0x0000000000400e49 in phase_2 ()
```
Let's do the standard `disas` command to see the assembly of the function. 
```
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
```
Also run the command `i r` to see what the values of the variables are.
```
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
```

It also might be easier to visualize the operations by using an online disambler like https://onlinedisassembler.com/ to see a full graph.

As we can see, it is fairly obvious that there is a **loop** somewhere in this function (by following the arrows). In the first block of code, the function `read_six_numbers` is called which essentially confirms that it is six numbers which are seperated by a space (as we entered in the first part of this phase). If that function fails, it calls `explode_bomb` to the left. If the function succeeds, it follows the green arrow on the right to the third box.

In order to determine the comparisons used, it will be useful to look up or know "Jumps Based on Signed Comparisons".

### Phase 3
----------
not 0, 1, 5, 6, 7, 8, 9, 10, 11, 12, 898, 1587

-1587

1 5
```
0000000000400e8c <phase_3>:
  400e8c:   48 83 ec 18             sub    $0x18,%rsp
  400e90:   48 8d 4c 24 08          lea    0x8(%rsp),%rcx
  400e95:   48 8d 54 24 0c          lea    0xc(%rsp),%rdx
  400e9a:   be a3 25 40 00          mov    $0x4025a3,%esi
  400e9f:   b8 00 00 00 00          mov    $0x0,%eax
  400ea4:   e8 a7 fc ff ff          callq  400b50 <__isoc99_sscanf@plt>
  400ea9:   83 f8 01                cmp    $0x1,%eax
  400eac:   7f 05                   jg     400eb3 <phase_3+0x27>
  400eae:   e8 37 05 00 00          callq  4013ea <explode_bomb>
  400eb3:   83 7c 24 0c 07          cmpl   $0x7,0xc(%rsp)
  400eb8:   77 66                   ja     400f20 <phase_3+0x94>
  400eba:   8b 44 24 0c             mov    0xc(%rsp),%eax
  400ebe:   ff 24 c5 60 23 40 00    jmpq   *0x402360(,%rax,8)
  400ec5:   b8 35 00 00 00          mov    $0x35,%eax
  400eca:   eb 05                   jmp    400ed1 <phase_3+0x45>
  400ecc:   b8 00 00 00 00          mov    $0x0,%eax
  400ed1:   2d ce 03 00 00          sub    $0x3ce,%eax
  400ed6:   eb 05                   jmp    400edd <phase_3+0x51>
  400ed8:   b8 00 00 00 00          mov    $0x0,%eax
  400edd:   05 1d 01 00 00          add    $0x11d,%eax
  400ee2:   eb 05                   jmp    400ee9 <phase_3+0x5d>
  400ee4:   b8 00 00 00 00          mov    $0x0,%eax
  400ee9:   2d 82 03 00 00          sub    $0x382,%eax
  400eee:   eb 05                   jmp    400ef5 <phase_3+0x69>
  400ef0:   b8 00 00 00 00          mov    $0x0,%eax
  400ef5:   05 82 03 00 00          add    $0x382,%eax
  400efa:   eb 05                   jmp    400f01 <phase_3+0x75>
  400efc:   b8 00 00 00 00          mov    $0x0,%eax
  400f01:   2d 82 03 00 00          sub    $0x382,%eax
  400f06:   eb 05                   jmp    400f0d <phase_3+0x81>
  400f08:   b8 00 00 00 00          mov    $0x0,%eax
  400f0d:   05 82 03 00 00          add    $0x382,%eax
  400f12:   eb 05                   jmp    400f19 <phase_3+0x8d>
  400f14:   b8 00 00 00 00          mov    $0x0,%eax
  400f19:   2d 82 03 00 00          sub    $0x382,%eax
  400f1e:   eb 0a                   jmp    400f2a <phase_3+0x9e>
  400f20:   e8 c5 04 00 00          callq  4013ea <explode_bomb>
  400f25:   b8 00 00 00 00          mov    $0x0,%eax
  400f2a:   83 7c 24 0c 05          cmpl   $0x5,0xc(%rsp)
  400f2f:   7f 06                   jg     400f37 <phase_3+0xab>
  400f31:   3b 44 24 08             cmp    0x8(%rsp),%eax
  400f35:   74 05                   je     400f3c <phase_3+0xb0>
  400f37:   e8 ae 04 00 00          callq  4013ea <explode_bomb>
  400f3c:   48 83 c4 18             add    $0x18,%rsp
  400f40:   c3                      retq   
```
### Phase 4
----------

two number "%d %d"

not 99,45,13,7,2,5,3,10,4,6,8,11,12


number is between 0 and 14 using comparison statement
0,1,2,3,4,5,6,7,8,9,10,11,12,13,14
output of func4 should be 45

 45    13
$0x2d,%eax

eax = 13
esi = 2
edi = 2
edx = 2

0-14

9,10,11,12,13

14 45

2 0

exit function if edi =< ebx

values to look at: edi + ebx

edi = 2
ebx = 7

edi = 2
ebx = 3

edi = 2
ebx = 1

edi = 2
ebx = 2

### Phase 5
------------

Based on this line in the compiler, we know that the final comparison needed should be 72. $ecx is the output of the loop
```
0x0000000000400ff8 <+53>:    cmp    $0x48,%ecx                   // final comparison; 0x48 = 72
0x0000000000400ffb <+56>:    je     0x401002 <phase_5+63>
```
Values attached to letters based on testing:
a = 10
b = 6
c = 1
d = 12
e = 16
f = 9

Since we know the final value is 6 letters/numbers, we know 72/6 = 12. So we can plug in 6 'd' characters and get a valid comparison!
```
Dump of assembler code for function phase_5:
   0x0000000000400fc3 <+0>:     push   %rbx
   0x0000000000400fc4 <+1>:     mov    %rdi,%rbx
   0x0000000000400fc7 <+4>:     callq  0x4011f5 <string_length>
   0x0000000000400fcc <+9>:     cmp    $0x6,%eax
   0x0000000000400fcf <+12>:    je     0x400fd6 <phase_5+19>
   0x0000000000400fd1 <+14>:    callq  0x4013ea <explode_bomb>
   0x0000000000400fd6 <+19>:    mov    %rbx,%rax
   0x0000000000400fd9 <+22>:    lea    0x6(%rbx),%rdi
   0x0000000000400fdd <+26>:    mov    $0x0,%ecx
   0x0000000000400fe2 <+31>:    movzbl (%rax),%edx
   0x0000000000400fe5 <+34>:    and    $0xf,%edx
   0x0000000000400fe8 <+37>:    add    0x4023a0(,%rdx,4),%ecx
   0x0000000000400fef <+44>:    add    $0x1,%rax
   0x0000000000400ff3 <+48>:    cmp    %rdi,%rax
=> 0x0000000000400ff6 <+51>:    jne    0x400fe2 <phase_5+31>
   0x0000000000400ff8 <+53>:    cmp    $0x48,%ecx                   // final comparison; 0x48 = 72
   0x0000000000400ffb <+56>:    je     0x401002 <phase_5+63>
   0x0000000000400ffd <+58>:    callq  0x4013ea <explode_bomb>
   0x0000000000401002 <+63>:    pop    %rbx
   0x0000000000401003 <+64>:    retq
End of assembler dump.
```


### Phase 6
------------

```
Dump of assembler code for function phase_6:
=> 0x0000000000401004 <+0>:     push   %r13
   0x0000000000401006 <+2>:     push   %r12
   0x0000000000401008 <+4>:     push   %rbp
   0x0000000000401009 <+5>:     push   %rbx
   0x000000000040100a <+6>:     sub    $0x58,%rsp
   0x000000000040100e <+10>:    lea    0x30(%rsp),%rsi
   0x0000000000401013 <+15>:    callq  0x401420 <read_six_numbers>   // verifies that the input is "%d %d %d %d %d %d"
   0x0000000000401018 <+20>:    lea    0x30(%rsp),%r12
   0x000000000040101d <+25>:    mov    $0x0,%r13d
   0x0000000000401023 <+31>:    mov    %r12,%rbp
   0x0000000000401026 <+34>:    mov    (%r12),%eax
   0x000000000040102a <+38>:    sub    $0x1,%eax
   0x000000000040102d <+41>:    cmp    $0x5,%eax
   0x0000000000401030 <+44>:    jbe    0x401037 <phase_6+51>
   0x0000000000401032 <+46>:    callq  0x4013ea <explode_bomb>
   0x0000000000401037 <+51>:    add    $0x1,%r13d
   0x000000000040103b <+55>:    cmp    $0x6,%r13d
   0x000000000040103f <+59>:    je     0x40107e <phase_6+122>
   0x0000000000401041 <+61>:    mov    %r13d,%ebx
   0x0000000000401044 <+64>:    movslq %ebx,%rax                  // loop start
   0x0000000000401047 <+67>:    mov    0x30(%rsp,%rax,4),%eax
   0x000000000040104b <+71>:    cmp    %eax,0x0(%rbp)
   0x000000000040104e <+74>:    jne    0x401055 <phase_6+81>
   0x0000000000401050 <+76>:    callq  0x4013ea <explode_bomb>
   0x0000000000401055 <+81>:    add    $0x1,%ebx
   0x0000000000401058 <+84>:    cmp    $0x5,%ebx
   0x000000000040105b <+87>:    jle    0x401044 <phase_6+64>     // loop end
   0x000000000040105d <+89>:    add    $0x4,%r12
   0x0000000000401061 <+93>:    jmp    0x401023 <phase_6+31>
   0x0000000000401063 <+95>:    mov    0x8(%rdx),%rdx          // while start
   0x0000000000401067 <+99>:    add    $0x1,%eax
   0x000000000040106a <+102>:   cmp    %ecx,%eax
   0x000000000040106c <+104>:   jne    0x401063 <phase_6+95>   // while end
   0x000000000040106e <+106>:   mov    %rdx,(%rsp,%rsi,2)
   0x0000000000401072 <+110>:   add    $0x4,%rsi
   0x0000000000401076 <+114>:   cmp    $0x18,%rsi
   0x000000000040107a <+118>:   jne    0x401083 <phase_6+127>
   0x000000000040107c <+120>:   jmp    0x401098 <phase_6+148>
   0x000000000040107e <+122>:   mov    $0x0,%esi
   0x0000000000401083 <+127>:   mov    0x30(%rsp,%rsi,1),%ecx
   0x0000000000401087 <+131>:   mov    $0x1,%eax
   0x000000000040108c <+136>:   mov    $0x6032e0,%edx
   0x0000000000401091 <+141>:   cmp    $0x1,%ecx
   0x0000000000401094 <+144>:   jg     0x401063 <phase_6+95>
   0x0000000000401096 <+146>:   jmp    0x40106e <phase_6+106>
   0x0000000000401098 <+148>:   mov    (%rsp),%rbx
   0x000000000040109c <+152>:   mov    %rsp,%rax
   0x000000000040109f <+155>:   lea    0x28(%rsp),%rsi
   0x00000000004010a4 <+160>:   mov    %rbx,%rcx
   0x00000000004010a7 <+163>:   mov    0x8(%rax),%rdx          // while start
   0x00000000004010ab <+167>:   mov    %rdx,0x8(%rcx)
   0x00000000004010af <+171>:   add    $0x8,%rax
   0x00000000004010b3 <+175>:   mov    %rdx,%rcx
   0x00000000004010b6 <+178>:   cmp    %rsi,%rax
   0x00000000004010b9 <+181>:   jne    0x4010a7 <phase_6+163>  // while end
   0x00000000004010bb <+183>:   movq   $0x0,0x8(%rdx)
   0x00000000004010c3 <+191>:   mov    $0x5,%ebp
   0x00000000004010c8 <+196>:   mov    0x8(%rbx),%rax
   0x00000000004010cc <+200>:   mov    (%rax),%eax
   0x00000000004010ce <+202>:   cmp    %eax,(%rbx)
   0x00000000004010d0 <+204>:   jle    0x4010d7 <phase_6+211>
   0x00000000004010d2 <+206>:   callq  0x4013ea <explode_bomb> // last
   0x00000000004010d7 <+211>:   mov    0x8(%rbx),%rbx          // add 0x8 to rbx
   0x00000000004010db <+215>:   sub    $0x1,%ebp               // checking
   0x00000000004010de <+218>:   jne    0x4010c8 <phase_6+196>  // here
   0x00000000004010e0 <+220>:   add    $0x58,%rsp
   0x00000000004010e4 <+224>:   pop    %rbx
   0x00000000004010e5 <+225>:   pop    %rbp
   0x00000000004010e6 <+226>:   pop    %r12
   0x00000000004010e8 <+228>:   pop    %r13
---Type <return> to continue, or q <return> to quit---
   0x00000000004010ea <+230>:   retq


                        // node value (x)
                                       // node number
                                                      // pointer to next node
(gdb) x/3x $rbx
0x6032e0 <node1>:       0x000002f2      0x00000001      0x006032f0
(gdb) x/3x *($rbx + 8)
0x6032f0 <node2>:       0x000000c3      0x00000002      0x00603300
(gdb) x/3x *(*($rbx + 8)+8)
0x603300 <node3>:       0x0000006f      0x00000003      0x00603310
(gdb) x/3x *(*(*($rbx + 8)+8)+8)
0x603310 <node4>:       0x000001c1      0x00000004      0x00603320
(gdb) x/3x *(*(*(*($rbx + 8)+8)+8)+8)
0x603320 <node5>:       0x000000fe      0x00000005      0x00603330
(gdb) x/3x *(*(*(*(*($rbx + 8)+8)+8)+8)+8)
0x603330 <node6>:       0x00000338      0x00000006      0x00000000
```

|node # |    hex   |    dec|
|-----|-----|----|
|3|        `0x0000006f`  |111|
|2|        `0x000000c3`  |195|
|5|        `0x000000fe`  |254|
|4|        `0x000001c1`  |449|
|1|        `0x000002f2`  |754|
|6|        `0x00000338`  |824|

(sorted smallest to largest gives you the answer)

See also: [getSubSequenceCount Interview Question](/pages/get-subsequence-count)