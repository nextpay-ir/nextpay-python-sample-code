import glob
import os

if __name__ == "__main__":
    print "test"
    os.chdir("/var/www/html/grameasy")
    for root, dirs, files in os.walk("/var/www/html/grameasy"):
        for _file in files:
            if _file.endswith(".php"):
                with open(os.path.join(root, _file)) as f:
                    for line in f:
                        if "slimscroll" in line:
                            print root + '/' + _file
                            print line
                    contents = f.read()
                if 'slimscroll' in contents:
                    print root + '/' + _file
    # for _file in glob.glob('*.php'):
    #     print _file
    #     # print 'DEBUG: file=>{0}<'.format(_file)
    #     with open(_file) as f:
    #         contents = f.read()
    #     if 'purchase' in contents:
    #         print _file