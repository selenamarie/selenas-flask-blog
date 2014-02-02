title: "Customizing the RPMs from pgrpms.org"
slug: customizing-the-rpms-from-pgrpms-org
id: 1862
date: 2010-08-03 18:00:23
tags: 
- pgrpms
- postgres
- rpm
- sysadmin
categories: 
- postgres
- postgresql
- sysadmin

To pick up [where Devrim left off](http://people.planetpostgresql.org/devrim/index.php?/archives/44-How-To-Build-Your-Own-PostgreSQL-and-related-software-RPMs-on-CentOSRHELFedora.html) in customizing RPMs, here are some more tips for getting your very own RPMs built:

*   Create a VM with your favorite operating system (I'm using versions of CentOS). I need both 32-bit OS and 64-bit OS. This is much easier to manage with separate, local VMs. 

*   Install spectool ([available here](http://packages.sw.be/spectool/)), and SVN

*   The other dependancies were: gcc glibc-devel bison flex python-devel tcl-devel readline-devel zlib-devel openssl-devel krb5-devel e2fsprocs-devel libxml2-devel libxslt-devel pam-devel

*   Edit the postgresql-$VERSION.spec file to your liking: If you're adding patches, you need to add them in TWO places - first in the Patch#: group, and then again below where the %patch# series starts. Finally, if you're adding an entirely new package (say in 8.2, pg_standby in contrib), you'll need to also add the binary (or library, or whatever) to the appropriate %files clause later in the spec file.  It's also a good idea to modify 'Release'. Here's a sample diff of my spec file:

`
+++ postgresql-8.2.spec (working copy)
@@ -74,7 +74,7 @@
 Summary:       PostgreSQL client programs and libraries
 Name:          postgresql
 Version:       8.2.17
-Release:       1PGDG%{?dist}
+Release:       1test%{?dist}
 License:       BSD
 Group:         Applications/Databases
 Url:           http://www.postgresql.org/ 
@@ -95,7 +95,9 @@
 Patch4:                postgresql-test.patch
 Patch6:                postgresql-perl-rpath.patch
 Patch8:                postgresql-prefer-ncurses.patch
+Patch7:                postgresql-pgstat-dir.patch
 Patch9:                postgresql-use-zoneinfo.patch
+Patch10:               pg_standby.patch

 Buildrequires: perl glibc-devel bison flex
 Requires:      /sbin/ldconfig initscripts
@@ -282,7 +284,9 @@
 %patch4 -p1
 %patch6 -p1
 %patch8 -p1
+%patch7 -p1
 %patch9 -p1
+%patch10 -p1

 pushd doc
 tar -zcf postgres.tar.gz *.html stylesheet.css
@@ -604,6 +608,7 @@
 %{_bindir}/pg_controldata
 %{_bindir}/pg_ctl
 %{_bindir}/pg_resetxlog
+%{_bindir}/pg_standby
 %{_bindir}/postgres
 %{_bindir}/postmaster
 %{_mandir}/man1/initdb.*
`

How have you customized RPMs using this repo? Share your .spec files!
