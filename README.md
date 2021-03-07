### A custom MIPS architecture plugin for Binary Ninja.
This is a naive MIPS architecture plugin without [ILL] or [capstone], so don't expect any symbol resolution.
The basic logic should be working fine, as demonstrated below.

The plugin is for convience seperation into three files.
### mips_instructions.py
Contains the MIPS Instruction Reference.
### mips_plugin_external_functions.py
Generates instructions token for "get_instruction_text" method in the Architecture class.
### Custom_mipsPlugin.py
Holds the Binary Ninja Architecture class. 
### mips.c
Sample C file for testing compiled with
```
mipsel-linux-gnu-gcc mips.c -o mips_out
```
### mips_out
The compiled mips.c file.

```console
/tmp$ file mips_out
mips_out: ELF 32-bit LSB executable, MIPS, MIPS32 rel2 version 1 (SYSV), dynamically linked, interpreter /lib/ld.so.1, for GNU/Linux 3.2.0, BuildID[sha1]=5106ccc260d47efc72a74ee8c302d6b8b3f65097, not stripped
```

You may need to install the [gcc-mipsel-linux-gnu] package.
Tested with binary ninja 1.3.2015 personal.

## Samples
![custom_main](https://i.ibb.co/zbWrt0H/custom-plugin-main.jpg "custom")
![buildin](https://i.ibb.co/gDscMgp/buildin-main.jpg "buildin")

[ILL]:https://docs.binary.ninja/dev/bnil-llil.html
[capstone]:https://www.capstone-engine.org/
[gcc-mipsel-linux-gnu]:https://packages.debian.org/unstable/gcc-mipsel-linux-gnu
