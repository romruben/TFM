#Extracted from https://gist.github.com/stevehanson/7462063
#Edited by ruben.romcor@gmail.com

import os
import sys
import json
import urllib2


HOST = 'http://localhost:9200'
INDEX = 'test'
TYPE = 'attachment'
TMP_FILE_NAME = 'tmp.json'

# for supported formats, see apache tika - http://tika.apache.org/1.4/formats.html
INDEX_FILE_TYPES = ['html','pdf', 'doc', 'docx', 'xls', 'xlsx', 'xml', 'txt']

def main():

    indexDirectory = raw_input('Index entire directory [Y/n]: ')

    if not indexDirectory:
        indexDirectory = 'y'

    if indexDirectory.lower() == 'y':
        dir = raw_input('Directory to index (relative to script): ')
        indexDir(dir)

    else:
        fname = raw_input('File to index (relative to script): ')
        createIndexIfDoesntExist()
        indexFile(fname)

def indexFile(fname):
    print '\nIndexing ' + fname
    createEncodedTempFile(fname)
    postFileToTheIndex()
    os.remove(TMP_FILE_NAME)
    print '\n-----------'

def indexDir(dir):

    print 'Indexing dir ' + dir

    createIndexIfDoesntExist()

    for path, dirs, files in os.walk(dir):
        print "files: "+str(len(files))
        for file in files:
            fname = os.path.join(path,file)

            base,extension = file.rsplit('.',1)

            if extension.lower() in INDEX_FILE_TYPES:
                print "Indexing "+fname
                indexFile(fname)
            else:
                'Skipping {}, not approved file type: {}'.format(fname, extension)

def postFileToTheIndex():
    cmd = 'curl -X POST "{}/{}/{}" -d @'.format(HOST,INDEX,TYPE) + TMP_FILE_NAME
    print cmd
    os.system(cmd)


def createEncodedTempFile(fname):

    file64 = open(fname, "rb").read().encode("base64")

    print 'writing JSON with base64 encoded file to temp file {}'.format(TMP_FILE_NAME)

    f = open(TMP_FILE_NAME, 'w')
    data = { 'file': file64, 'title': fname }
    json.dump(data, f) # dump json to tmp file
    f.close()


def createIndexIfDoesntExist():

    class HeadRequest(urllib2.Request):
        def get_method(self):
            return "HEAD"

    # check if type exists by sending HEAD request to index
    try:
        urllib2.urlopen(HeadRequest(HOST + '/' + INDEX + '/'))
    except urllib2.HTTPError, e:
        if e.code == 404:
            print 'Index doesnt exist, creating...'

            call = 'curl -XPOST "{}/{}/" -d'.format(HOST,INDEX) + ''' '{
                  "attachment" : {
                    "properties" : {
                      "file" : {
                        "type" : "attachment",
                        "fields" : {
                          "title" : { "store" : "yes" },
                          "file" : { "term_vector":"with_positions_offsets", "store":"yes" }
                        }
                      }
                    }
                  }
                }' '''
            print call
            os.system(call)
        else:
            print 'Failed to retrieve index with error code - %s.' % e.code

# kick off the main function when script loads
main()