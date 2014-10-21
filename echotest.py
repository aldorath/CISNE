from pyechonest import artist
from pyechonest import config



def test():
    x = artist.Artist('fourtet')
    print x.id
    print "Artists similar to: %s:" % (x.name,)
    for similar_artist in x.similar: 
        print "\t%s" % (similar_artist.name,)

if __name__ == "__main__":
    config.ECHO_NEST_API_KEY="FDO0XWTDUWDSWI3DL "
    print test()