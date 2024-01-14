# What does the script do?

This script takes an amount of bytes with a given unit, and then converts it to the given destination unit, i.e., it can convert 4KB to 4000 Bytes, 4096 Bytes to 4KiB, or even 2147483.648KB to 2GiB.

Currently it only supports the following units:

-   B (Bytes)
-   KB
-   KiB
-   MB
-   MiB
-   GB
-   GiB
-   TB
-   TiB

# How does it work?

The script takes 2 arguments: the value to convert with the units, and the destination units.

```
$ ./py-bytes-units.py 2GiB MiB
```

This will convert 2GiB into MiB, the result will be printed to the screen

```
2048MiB
```

# Can I hide the units from the result?

Yes, all you have to do is add the "-h" flag, and it'll print just the resulting number:

```
$ ./py-bytes-units.py 2GiB MiB -h
2048MiB
```

# What version of Python do I need?

Currently it has been tested only on Python 3.12, I can't guarantee compatibility with previous versions or with Python 2.
