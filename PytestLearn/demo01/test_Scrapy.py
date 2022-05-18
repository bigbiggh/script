import scrapy,builtwith,whois
url = 'http://www.baidu.com/'
func = builtwith.parse(url)
who = whois.whois(url)
print(func)
print(who)