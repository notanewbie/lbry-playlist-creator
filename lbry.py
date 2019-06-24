import urllib;
import urllib2;
import json;
import gzip;
import time;
import codecs;
def GetURL2(link):
    req = urllib2.Request(link, None, {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
    response = urllib2.urlopen(req).read()
    return response;
def GetURL(link):
    url = link;
    try:
        txt = urllib.urlopen(link).read();
        return txt;
    except IOError:
        print "File could not be read."

channel = raw_input("Enter channel name: ");
filename = channel + ".m3u8";
search = GetURL2("https://www.google.com/search?safe=active&ei=btcQXZD5MqqIggfWmY_4Bg&q=spee.ch+sitemap19.xml.gz+" + channel + "&oq=spee.ch+sitemap+" + channel + "&gs_l=psy-ab.3..33i160.278360.284271..284547...3.0..0.247.2087.10j8j1......0....1..gws-wiz.......0i71j33i299.l77RvJYoy9Y");
import re;
split1 = re.split(channel + "</b>#", search, flags=re.IGNORECASE)[1];
split1 = re.split("&", split1, flags=re.IGNORECASE)[0];
channelid = split1;
#print "Reading file...";
#print page;
i = 1;
page = GetURL2("https://spee.ch/api/channel/claims/@" + channel + "/" + channelid + "/1");
encoded = json.loads(page);
L = encoded['data']['totalPages'];
channel = raw_input("Channel found. Press enter to continue.");
filestring = str('#EXTM3U\n');
while i <= L:
    page = GetURL2("https://spee.ch/api/channel/claims/@americanlampoon/2326929a70ccf8b4937244fc6cbbc96926db7e14/" + str(i));
    encoded = json.loads(page);
    x = 0;
    while len(encoded['data']['claims']) > x:
        #print "https://spee.ch/" + encoded['data']['channelName'] + "/" + encoded['data']['claims'][x]['name'] + ".mp4";
        #print encoded['data']['claims'][x]['title'];
        #print encoded['data']['claims'][x]['thumbnail'];
        filestring = filestring + '#EXTINF:0, ';
        filestring = filestring + 'tvg-logo="' + encoded['data']['claims'][x]['thumbnail'] + '" '
        filestring = filestring + 'group-title="spee.ch",'
        filestring = filestring + encoded['data']['claims'][x]['title'];
        filestring = filestring + '\n' + "https://spee.ch/" + encoded['data']['channelName'] + "/" + encoded['data']['claims'][x]['name'] + ".mp4 \n";
        x = x + 1;
    i = i + 1;
#print filestring;
#print channel;
file = codecs.open(filename, 'w', 'utf-8')
file.write(filestring);
file.close()
raw_input('To quote my mentor Thanos, "the work is done."\nPress enter to exit.');
#print "Parsing file...";
#url = page.split("https://p-events-delivery.akamaized.net/")[1].split("/");
#print url;
