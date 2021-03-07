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

```console
/tmp$ mipsel-linux-gnu-gcc -v
Using built-in specs.
COLLECT_GCC=mipsel-linux-gnu-gcc
COLLECT_LTO_WRAPPER=/usr/lib/gcc-cross/mipsel-linux-gnu/7/lto-wrapper
Target: mipsel-linux-gnu
Configured with: ../src/configure -v --with-pkgversion='Ubuntu 7.5.0-3ubuntu1~18.04' --with-bugurl=file:///usr/share/doc/gcc-7/README.Bugs --enable-languages=c,ada,c++,go,d,fortran,objc,obj-c++ --prefix=/usr --with-gcc-major-version-only --program-suffix=-7 --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --libdir=/usr/lib --enable-nls --with-sysroot=/ --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --with-default-libstdcxx-abi=new --enable-gnu-unique-object --disable-libitm --disable-libsanitizer --disable-libquadmath --disable-libquadmath-support --enable-plugin --with-system-zlib --enable-multiarch --disable-werror --enable-multilib --with-arch-32=mips32r2 --with-fp-32=xx --with-madd4=no --with-lxc1-sxc1=no --enable-targets=all --with-arch-64=mips64r2 --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=mipsel-linux-gnu --program-prefix=mipsel-linux-gnu- --includedir=/usr/mipsel-linux-gnu/include
Thread model: posix
gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04) 
```
```console
/tmp$ uname -a
Linux desktop 5.4.0-66-generic #74~18.04.2-Ubuntu SMP Fri Feb 5 11:17:31 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
```

You may need to install the [gcc-mipsel-linux-gnu] package.
Tested with binary ninja 1.3.2015 personal.

## Samples
![custom_main](https://i.ibb.co/zbWrt0H/custom-plugin-main.jpg "custom")
![buildin](https://i.ibb.co/gDscMgp/buildin-main.jpg "buildin")

[ILL]:https://docs.binary.ninja/dev/bnil-llil.html
[capstone]:https://www.capstone-engine.org/
[gcc-mipsel-linux-gnu]:https://packages.debian.org/unstable/gcc-mipsel-linux-gnu
