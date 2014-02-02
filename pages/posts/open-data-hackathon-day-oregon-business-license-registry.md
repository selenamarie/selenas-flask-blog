title: "Open Data Hackathon Day: Oregon Business License Registry"
slug: open-data-hackathon-day-oregon-business-license-registry
id: 2287
date: 2010-12-04 16:38:38
tags: 
- odhd
- open data hackathon day
- pdx
- scraperwiki
categories: 
- portland

[![](http://www.chesnok.com/daily/wp-content/uploads/2010/12/IMG_0213-300x168.jpg "IMG_0213")](http://www.chesnok.com/daily/wp-content/uploads/2010/12/IMG_0213.jpg)

At the [Portland Software Summit on Thursday](http://www.chesnok.com/daily/2010/12/02/pdx11-the-software-summit-wrapup/), a couple people mentioned that it was hard to keep track of new businesses that pop up, and that merger and acquisition activity wasn't being sufficiently publicised. 

I thought - maybe we could get this information in an automated way!

I started with the [state of Oregon's business registry search site](http://egov.sos.state.or.us/br/pkg_web_name_srch_inq.login). Unfortunately, they limit search results for business searches to 1000, and they don't paginate their results. So, we kicked ScraperWiki into gear, and wrote a very simple scraper with @[maxogden](http://twitter.com/maxogden): [http://scraperwiki.com/scrapers/oregon_business_registry/](http://scraperwiki.com/scrapers/oregon_business_registry/)

Next, I wanted to find out information about businesses specifically in Portland. The City releases information about this, but in PDF form: [http://www.portlandonline.com/omf/index.cfm?c=32192](http://www.portlandonline.com/omf/index.cfm?c=32192)

I wrote a quick and dirty Python script to scrape out information, and am getting probably 250 of the 300+ businesses in the November release. Next, I want to cross reference this data with what's in the Oregon site. I'll be publishing the Python scripts over the weekend.  Hopefully ScraperWiki will add pyPDF to their Python repo support and I will be able to publish the transform there so it can be easily linked to the Oregon data.

Two lessons today: 

*   Governments: Please don't publish data in PDFs. YUCK.
*   Governments: Please paginate results from your site! Hard limits are just kinda lame.

The alternative to scraping the state of Oregon's site is to order a CD-ROM for $50\. I think this is such a stupid profit center for the state. I'd be interested to know how much money they're really making off of it, and whether they could take a page out of Metro's book and find a way to share the data with a different, more useful service.
