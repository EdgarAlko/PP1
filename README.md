# Scrapy based Project
The code was created to parse cvbankas.lt web page, to give information about job offers for IT specialist in Lithuania.

#!!!PROBLEM in code - start page is 'https://www.cvbankas.lt/?padalinys%5B%5D=76&keyw=',
but also 'https://www.cvbankas.lt/?padalinys%5B%5D=76' have the same data. So spider find 1 page more.
Also data from next pages is obtained chaotically

# Requirements:
1. [Python 3](https://www.python.org/)
2. [Scrapy framework](https://scrapy.org/)

   `pip3 install scrapy`

# Usage:
1. `cd <project directory>`
2. import scrapy
3. import time
4. import logging
5t. `scrapy crawl <cvbankas> -o <cvbankas>.<json>`