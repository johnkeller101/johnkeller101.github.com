---
layout: page
current: about
title: Binary Bomb Lab Phase 1
navigation: true
class: page-template
subclass: 'post page'
cover: /assets/images/about-header.jpg
cover-height: 400
---

#### Getting Started

First, setup your bomb directory. Untar your specific file and let's get started!

<pre>
  <code class="ruby">
    jovyan@jupyter-joke1008:~$ cd Labs
	jovyan@jupyter-joke1008:~/Labs$ tar -xvf bomb439.tar
	bomb439/README
	bomb439/bomb.c
	bomb439/bomb
	jovyan@jupyter-joke1008:~/Labs$ cd bomb439
	jovyan@jupyter-joke1008:~/Labs/bomb439$ ls
	bomb  bomb.c  README
	jovyan@jupyter-joke1008:~/Labs/bomb439$
  </code>
</pre>

#### Getting Strings and Objdump

Run the following commands to create text files which we will look at later:

<pre>
  <code class="ruby">
    strings bomb > strings.txt
    objdump -d bomb > assembly.txt
  </code>
</pre>

You should now have two files: `strings.txt` and `assembly.txt`. Now let's get started with Phase 1!

#### Phase 1 Solution

<pre>
  <code class="ruby">
    jovyan@jupyter-joke1008:~/Labs/bomb439$ gdb bomb
  </code>
</pre>

Let's create our breakpoints to make sure nothing get's set to the gradebook!

<pre>
  <code class="ruby">
    (gdb) b explode_bomb
	Breakpoint 1 at 0x4013ea
	(gdb) b phase_1
	Breakpoint 2 at 0x400e2d
  </code>
</pre>

Let's run it and test things out:

<pre>
  <code class="ruby">
    (gdb) run
	Starting program: /home/jovyan/Labs/bomb439/bomb
	Welcome to my fiendish little bomb. You have 6 phases with
	which to blow yourself up. Have a nice day!
  </code>
</pre>

Okay, we know it works. Let's enter a test string to let the program hit our break point. You can enter any string, but I used `TEST`.

<pre>
  <code class="ruby">
    TEST

	Breakpoint 2, 0x0000000000400e2d in phase_1 ()
  </code>
</pre>

Now let's take a quick look at the disassebly to see what variables are being used. Enter `disas` and you will get a chunk of assembly for the function `phase_1` which we put our breakpoint at.

<pre>
  <code class="ruby">
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
  </code>
</pre>

We can see that the `<strings_not_equal>` function is being called which as the name implies compares two strings. The variable being used in this comparison is `$eax`. We can see one line above that `$esi` is also involved. Let's use that address in memory and see what it contains as a string.


<pre>
  <code class="ruby">
(gdb) x/25c 0x402310
0x402310:       73 'I'  32 ' '  99 'c'  97 'a'  110 'n' 32 ' '  115 's' 101 'e'
0x402318:       101 'e' 32 ' '  82 'R'  117 'u' 115 's' 115 's' 105 'i' 97 'a'
0x402320:       32 ' '  102 'f' 114 'r' 111 'o' 109 'm' 32 ' '  109 'm' 121 'y'
0x402328:       32 ' '
  </code>
</pre>

Based on the output, our input string is being run into the `<strings_not_equal>` function with the string **"I can see Russia from my "**. We can open our `strings.txt` file and see that the string we found in memory is the beginning of the full string: **"I can see Russia from my house!"**

<pre>
  <code class="ruby">
Welcome to my fiendish little bomb. You have 6 phases with
which to blow yourself up. Have a nice day!
I can see Russia from my house!
Phase 1 defused. How about the next one?
  </code>
</pre>

Now, onto ![Phase 2](/phase2.html)
