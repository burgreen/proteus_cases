# proteus_cases

Cases for MSU fork of Proteus.

untar case files into the appropriate msu_vv_xxx directory.

For example:

```cd msu_vv_rans2p
tar xfvz ../case_rans2p_cyl.tar.gz 
edit user_param.py accordingly
source <proteus_build_dir>/1-setup-proteus.sh
which parun
./1-run.sh output
```

