# 5_minutes_scripts
Scripts written in 5 minutes or so, might be useful.

Parsing /proc/net/tcp is useful for example when exploit ssrf :), enjoy.
```sh
$ ./parse_proc_net_tcp.py /proc/net/tcp
          sl local_address   local_port  rem_address     rem_port           st     tx_queue     rx_queue           tr      tm_when     retrnsmt          uid      timeout        inode 
           0    10.0.2.15        38522 34.255.6.193          443           01     00000000     00000000           02     000086EB     00000000            0            0        63871 

```
