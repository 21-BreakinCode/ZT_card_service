---
source: System Design
tags:
- programming/systemDesign
---
# Content Delivery Network
> [!example]+ Resource
> - [CDN - content delivery network](https://github.com/donnemartin/system-design-primer/blob/2d8231663fd0800720d25b9ac82dec3cda7e5a89/README.md#content-delivery-network)
> -   [Globally distributed content delivery](https://figshare.com/articles/Globally_distributed_content_delivery/6605972)
> -   [The differences between push and pull CDNs](http://www.travelblogadvice.com/technical/the-differences-between-push-and-pull-cdns/)
> -   [Wikipedia](https://en.wikipedia.org/wiki/Content_delivery_network)

- Globally distributed network of *proxy servers*
- content from locations *closer* to user
- Usually static and videos ([[Amazon CloudFront (p. 68)|CloudFront]] can serve dynamic)
- Improve performance:
	- user receive data quicker
	- servers don't have to server requests that CDN fulfills
- Disadvantages:
	- CDN costs could be significant depending on traffic
	- Content might be stale
	- require changing URLs for static content to point to the CDN
- **Push CDNs** 
	- content is *placed on the CDNs once*, instead of being re-pulled at regular intervals
	- update content whenever *changes on server*
	- minimize traffic <--> maximize storage
- **Pull CDNs** 
	- *grab new content* from server when the *1st user requests* the content
	- A [time-to-live (TTL)](https://en.wikipedia.org/wiki/Time_to_live) determines how long content is cached.
	- redundant traffic <--> minimize storage