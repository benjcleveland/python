#!/usr/bin/python

import urllib2
from os import mkdir
from BeautifulSoup import BeautifulSoup

CLASS_URL = 'http://briandorsey.info/uwpython/Internet_Programming_in_Python.html'

def get_html( url ):
    '''
    Download the html from the given url
    Returns html
    '''

    req = urllib2.Request( url )
    response = urllib2.urlopen( req )

    return response.read()

def get_weeks_urls( html ):
    '''
    Return a list of the urls for the week
    Also returns the name of the week
    '''

    week_name = ''
    week = html.findAll('td')
    links = []

    for table_section in week:
        # get the week name - this will be used for the directory structure
        if table_section.has_key('id'): 
            week_name = table_section['id']
     #       print week_name

        for link in table_section.findAll('a'):
            # get all the links
            if link.has_key('href'):
                # save the link and its name
                links.append( (link['href'],link.text ) )
    #            print link['href'], link.text

    return week_name, links

def download_links(directory, links ):    
    '''
    Downloads all the links into the given directory
    '''

    # create the directory
    mkdir(directory)

    for (link,name) in links:
        # get the html
        if link.lower().endswith('.html'):
            html = get_html( link )
            #open the file
            file = open( directory + '/' + name.replace(' ','_').replace('/','_').lower(),'w')
            file.write( html )
            file.close()

def main():

    print 'Getting the class webpage...'
    class_html = get_html( CLASS_URL )
    
    soup = BeautifulSoup( class_html )

    tr = soup.findAll('tr')
    
    #print tr
    #print tr[1].findNext('td').findNext('td').findNext('td').findNext('td').findNext('td')
    #print tr[2].findAll('id')
    #week2= tr[2].findAll('td')
    #print week2[2]['id']
    #print week2[3].findAll('a')[0]['href']

    for week in tr:
        urls = []
        # get the weeks urls        
        week_name,urls = get_weeks_urls( week )
        if week_name != '' and urls != []:
            print 'Downloading links from', week_name
            download_links( week_name, urls ) 
        elif week_name != '' and urls == []:
            print 'Nothing to download for', week_name
if __name__ == '__main__':
   main() 





