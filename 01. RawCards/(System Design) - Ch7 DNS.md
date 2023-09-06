---
source: System Design
tags:
- programming/systemDesign
---
# Domain name system
> [!example]+ Resource
> - [Domain name system](https://github.com/donnemartin/system-design-primer/blob/2d8231663fd0800720d25b9ac82dec3cda7e5a89/README.md#domain-name-system)
> - [DNS architecture](https://technet.microsoft.com/en-us/library/dd197427(v=ws.10).aspx)
> - [Wikipedia](https://en.wikipedia.org/wiki/Domain_Name_System)
> - [DNS articles](https://support.dnsimple.com/categories/dns/)

- Translate: **domain name → IP address**
- Cache: by browser, OS for period of time - [time to live (TTL)](https://en.wikipedia.org/wiki/Time_to_live)
- Disadvantages:
	- Slight delay 
	- could be complex -   [governments, ISPs, and large companies](http://superuser.com/questions/472695/who-controls-the-dns-servers/472729)
	- Come under [DDoS attack](http://dyn.com/blog/dyn-analysis-summary-of-friday-october-21-attack/)

- **NS record**
	- NS - name server
	- Specifies the *DNS servers*
- **MX record**
	- MX - mail exchange
	- Specified the *mail servers*
- **A record**
	- mapping to an *IP address*
- **CNAME**
	- C - canonical, 典範
	- mapping to *another name or CNAME or A record* 
	- example.com → www.example.com

- Managed DNS services:
	- [[Amazon Route 53 (p. 68)|Route53]]
	- [CloudFlare](https://www.cloudflare.com/dns/)
	- ...
- Various routing methods:
	- [Weighted round robin](https://www.jscape.com/blog/load-balancing-algorithms)
	    -   Prevent traffic from going to servers under maintenance
	    -   Balance between varying cluster sizes
	    -   A/B testing
	-   [Latency-based](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-latency)
	-   [Geolocation-based](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-geo)
