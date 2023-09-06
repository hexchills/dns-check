# dns-check

Script that was written with CharGPT for checking security of DNS provider. 
It can read .txt file with list of malicious domains and count if the attempt was succeeded or failed.


**Malicious domains, links for download:**

1. [hole.cert.pl](https://hole.cert.pl/domains/domains.txt)
2. [stamparm/blackbook](https://raw.githubusercontent.com/stamparm/blackbook/master/blackbook.txt)
3. [spamhaus.org](https://www.spamhaus.org/drop/drop.lasso)
4. [emergingthreats.net](https://rules.emergingthreats.net/blockrules/compromised-ips.txt)
5. [zonefiles.io](https://zonefiles.io/compromised-domain-list/)
6. [threatfeeds.io](https://threatfeeds.io/?feed=Malware%20Domains%20List)

From my test: 

- Quad9: 7 resolved from 300 domains

- 1.1.1.1 and Google DNS (8.8.8.8): 100 resolved from 300 domains