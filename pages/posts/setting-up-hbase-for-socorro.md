title: "Setting up HBase for Socorro"
slug: setting-up-hbase-for-socorro
id: 4582
date: 2013-01-20 19:57:17
tags: 
categories: 
- socorro

Setting up HBase for use with [Socorro](http://github.com/mozilla/socorro) is a bit of a [bear](https://i.chzbgr.com/maxW500/516933888/h7E25C981/)!  The default Vagrant config sets up a VM with filesystem-only. For those that want to try out the HBase support, or are on a path toward setting up a production instance, these instructions might help you along the way. 

You may also be interested in Lars' recent blog posts about Socorro: 

*   [Socorro Modular Design](http://www.twobraids.com/2012/12/socorro-modular-design.html)
*   [Socorro Crash Storage System](http://www.twobraids.com/2012/12/the-socorro-crash-storage-system.html)
*   [Socorro File System Storage](http://www.twobraids.com/2012/12/socorro-file-system-storage.html)
*   [More Socorro File System Storage](http://www.twobraids.com/2013/01/more-socorro-file-system-storage.html)
*   [What's next for Socorro File System](http://www.twobraids.com/2013/01/whats-next-for-socorro-file-system.html)
*   [HBase as Socorro Crash Storage](http://www.twobraids.com/2013/01/hbase-as-socorro-crash-storage.html)

Here's how I got it all working on an Ubuntu Precise (12.04) system, along with some scripts for launching important processes and putting test crashes into the system so you can tell that it is working. Ultimately, my goal is to incorporate all of this into some setup scripts to help new users out.

## Set up HBase and Thrift

Socorro uses the Thrift API to insert new crashes and retrieve them through the middleware layer. These [Quickstart instructions](http://hbase.apache.org/book.html#quickstart) are pretty helpful for getting HBase installed.

Then, you need to edit <pre>/etc/hosts</pre> and remove the '127.0.1.1' entry, and add your hostname to the localhost '127.0.0.1' line. Also, it's helpful for the defaults to add '`crash-stats`' and '`crash-reports`' as host aliases. Your final config line for localhost would look like: 

<pre>
127.0.0.1       localhost wuzetian crash-reports crash-stats
</pre>

(where `wuzetian` is your hostname)

You also need to add configuration for HBase. Here's an example: 

    &lt;?xml version=&quot;1.0&quot;?&gt;
    &lt;?xml-stylesheet type=&quot;text/xsl&quot; href=&quot;configuration.xsl&quot;?&gt;
    &lt;configuration&gt;
      &lt;property&gt;
        &lt;name&gt;hbase.rootdir&lt;/name&gt;
        &lt;value&gt;file:///var/tmp/hbase&lt;/value&gt;
      &lt;/property&gt;
      &lt;property&gt;
        &lt;name&gt;hbase.zookeeper.property.dataDir&lt;/name&gt;
        &lt;value&gt;/var/tmp/zookeeper&lt;/value&gt;
      &lt;/property&gt;
    &lt;/configuration&gt;

That sets the location for your HBase files for and zookeeper. This setup is for testing, so I put the directories in a location can easily clear out.

Then, to start HBase and Thrift up: 

<pre>
/etc/init.d/hadoop-hbase-master start
/etc/init.d/hadoop-hbase-thrift start
</pre>

## Setting up processor tools

The processor that looks at raw crashes runs two tools by default: `minidump_stackwalk` and `exploitable`.

You can build these from the socorro source tree with: 
<pre>
`make minidump_stackwalk`
</pre>

Then `make install` should put these files into a useful location.

You can also just copy the binaries from the stackwalk/bin directory and the other is exploitable/exploitable.

The paths for these are configured in `config/processor.ini`: `exploitability_tool_pathname` and `minidump_stackwalk_pathname`

There's also a symbols resolver configured, but I am not setting this up in my test.

## Disable LZO compression for HBase (unless you have it configured

Our hbase schema is configured to use LZO compression by default. Change that to 'NONE' and load the schema into hbase: 

<pre>
/bin/cat /home/socorro/dev/socorro/analysis/hbase_schema | sed 's/LZO/NONE/g' | /usr/bin/hbase shell
</pre>

## Set up crashmover

Update two lines in scripts/config/collectorconfig.py:

<pre>
localFS.default = '/home/socorro/primaryCrashStore'
fallbackFS.default = '/home/socorro/fallback'
</pre>

Set those to directories that you can store crash dumps.

## Configure processor and monitor to use HBase

You need to set the processor up to use HBase instead of local crash storage. 

The easiest way to do this is as follows: 

<pre>
PYTHONPATH=. python socorro/processor/processor_app.py --admin.conf=./config/processor.ini --source.crashstorage_class=socorro.external.hbase.crashstorage.HBaseCrashStorage --admin.dump_conf=config/processor2.ini
PYTHONPATH=. python socorro/processor/monitor_app.py --admin.conf=./config/monitor.ini --source.crashstorage_class=socorro.external.hbase.crashstorage.HBaseCrashStorage --admin.dump_conf=config/monitor2.ini
</pre>

Then edit both files to reflect your HBase configuration.

## Starting up

The [docs suggest starting up four daemons in screen sessions.](http://socorro.readthedocs.org/en/latest/installation.html#run-socorro-in-dev-mode) I mocked up [a shell script and a screenrc](https://gist.github.com/4583487) to get you started.

And that's it! You should now have a working system, with crashes being submitted and stashed into HBase, and the monitor and processor picking up crashes as they arrive and running the stackwalk and exploitable tools against the crashes.

Please let me know if these instructions work, or don't work, for you.
