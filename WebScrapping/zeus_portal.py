#!/usr/bin/python

from bs4 import BeautifulSoup

soup = BeautifulSoup(open("https://zeus.uk.eu.org/wallboard/#/"))
print (soup)

