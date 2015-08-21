import os
import sys
import fileinput
import re
import codecs
import time

#this methode replace some string with new string
def replace_word(infile,old_word,new_word):
    if not os.path.isfile(infile):
        print ("Error on replace_word, not a regular file: "+infile)
        sys.exit(1)
    f1=open(infile,'r').read()
    f2=open(infile,'w')
    m=f1.replace(old_word,new_word)
    f2.write(m)

#this methode replace value in config file if the value is set as: property="value"
def replace_value_in_config_file(infile,fproperty,fvalue):
    if not os.path.isfile(infile):
        print ("Error on replace_word, not a regular file: "+infile)
        sys.exit(1)
    f1=open(infile,'r').read()
    #f2=open(infile,'w')
    f2 = codecs.open(infile, 'w', encoding='utf-8')
    f1=f1.decode('utf-8')
    pattern = re.compile(fproperty+"=\"(.+?)\"")
    print f1
    m=pattern.sub(fproperty+"=\""+fvalue+"\"",f1)
    f2.write(m)

#this methode return first string searched with regular expression 
def extraxtRegEx(text_string,regex_pattern):
    try:
        found = re.search(regex_pattern, text_string).group(1)
        return found
    except AttributeError:
             found = '' # apply your error handling
             return found

#this methode return if the file on remote address contains searched string
def check_remote_file_for_string(ip_address,remote_path,local_path,filename,find_string,try_time):
    for check in range(0, int(try_time)):
        os.system("NET USE \\\\"+ip_address+ " /u:Administrator 111111")
        os.system("robocopy "+"\\\\"+ip_address+"\\"+remote_path+" "+local_path+" "+filename)
        check_test = open(local_path+"\\"+filename, 'rb').read().find(find_string)
        if check_test>-1:
            print check
            print "exist"
            return True
            break
        else:
            print check
            print "not exist"
            time.sleep(10)
    return False



