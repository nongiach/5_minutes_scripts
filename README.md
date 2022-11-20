# 5 minutes scripts
Reusable scripts written in 5 minutes for fun and no profit.

# 1: Script parsing /proc/net/tcp for pentest : ./parse_proc_net_tcp.py
# 2: Script anonymizing hashes for pentest to delegate the bruteforce : ./anonymize_hash_files.py
# 3: Script generating a wordcloud that is contained within a form : ./masked_word_cloud.py
# 4: Script to delete all Tweets of a given user : ./delete_all_tweet.py

## TCP connexions

/proc/net/tcp contains informations about all TCP connexions.

Parsing /proc/net/tcp is useful for example when you exploit SSRF :), enjoy.

```sh
$ ./parse_proc_net_tcp.py /proc/net/tcp
          sl local_address   local_port  rem_address     rem_port           st     tx_queue     rx_queue           tr      tm_when     retrnsmt          uid      timeout        inode 
           0    10.0.2.15        38522 34.255.6.193          443           01     00000000     00000000           02     000086EB     00000000            0            0        63871 

```
// TODO: tcp6, udp, udp6, raw

## Anonymize hashfiles like ntds
Sometimes no you need to anonymize hashes files like ntds dump to share them for cracking. This script replace all usernames with fake names.

```sh
$ ./anonymize_hash_files.py input_hashes.txt anonymized_hash.txt link_hashes.txt
```
* param 1: [INPUT] the input hashfiles
* param 2: [OUTPUT] the anonymize hashfiles output
* param 3: [OUTPUT] the file link between anonymized name and real names

## Delete all tweets

Update the ./delete_all_tweet.py to contain your Twitter API tokens and run to delete the tweets.
The code deletes only lastest 10 Tweets for security purpose, adapt it if you wish to delete all.
