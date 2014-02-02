title: "PostgreSQL security releases now available: versions 9.2.4, 9.1.9, 9.0.13 and 8.4.17"
slug: postgresql-security-releases-now-available-versions-9-2-4-9-1-9-9-0-13-and-8-4-17
id: 4744
date: 2013-04-04 05:43:39
tags: 
categories: 
- postgresql

PostgreSQL Global Development Group has [just released updates](http://www.postgresql.org/about/news/1456/) for all currently supported versions of PostgreSQL.

From the release announcement:

> The PostgreSQL Global Development Group has released a security update to all current versions of the PostgreSQL database system, including versions 9.2.4, 9.1.9, 9.0.13, and 8.4.17\. This update fixes a high-exposure security vulnerability in versions 9.0 and later. All users of the affected versions are strongly urged to apply the update immediately.
> 
> A major security issue fixed in this release, CVE-2013-1899, makes it possible for a connection request containing a database name that begins with "-" to be crafted that can damage or destroy files within a server's data directory. Anyone with access to the port the PostgreSQL server listens on can initiate this request. This issue was discovered by Mitsumasa Kondo and Kyotaro Horiguchi of NTT Open Source Software Center.

I wanted to highlight a couple things from the [FAQ](http://www.postgresql.org/support/security/faq/2013-04-04/) we developed for this release.

1.  There are no known exploits for the major security issue fixed by this release. The vulnerability was discovered through security testing conducted by NTT.
2.  Only users of 9.0 PostgreSQL and higher are affected by the major vulnerability.
3.  Affected users are those who allow unrestricted access to the network port PostgreSQL listens on. If you allow anyone, without IP address whitelisting, firewalling or some other kind of network-based access control, to connect to your network port, you are especially vulnerable.

Upgrading from minor version (9.2.3 to 9.2.4, for example) only requires that you install the new binaries and then restart PostgreSQL.

Additionally, if you are using GiST indexes, read the detailed notes in the release announcement to see if you are using features that require you to REINDEX your GiST indexes.

Please update as soon as possible!

Many thanks to our volunteer packagers who worked hard for the past several weeks to make this release possible. All PostgreSQL software releases are managed by volunteers.
