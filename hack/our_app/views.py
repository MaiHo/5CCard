# views.py

import ast
#from django.shortcuts import render_to_response
#from django.template import RequestContext
#from django.http import HttpResponseRedirect
import mechanize
#import requests
import cookielib
import time
import webbrowser
#from django.conf import settings
#from hack.our_app.models import User, Flex, CCash, NumMeals

def login(request):
    '''
        This handler will handle the login.html page
        It needs to get the username and the password from the form
        and login to the CUC page
        request.GET.get('q')
    '''

    if request.method == 'GET':
        print "hahaha GET"
        return render_to_response('login.html', context_instance = RequestContext(request))

    else:
        print "hahahaha POST!"
        username = request.POST.get('username')
        password = request.POST.get('password')

        br = mechanize.Browser()
        r = br.open("https://cards.cuc.claremont.edu/login.php")
        br.select_form(nr=1)
        br.form['loginphrase'] = username
        br.form['password'] = password
        br.submit()
        #time.sleep(10)
        print "THIS IS THE READ:::::", str(br.response().read())
        response_str = str(br.response().read())
        string = ""
        i=0
        
        for char in response_str:
            if char == '?':
                string = response_str[i:]
                break
            i += 1
        string = string.split('cid=35')[0] + 'cid=35&'
        
        print "STRING STRING STRING: ", string 
        
        print "AND THIS IS THE FUCKING URL: ::: : :", br.response().geturl()
        skey = request.GET.get('skey')
        print "THIS IS THE GEEEEEEEEEEEEEEEEEEEEEEEEEEET PARAM" , skey
        br2 = mechanize.Browser()
        r2 = br.open('https://cards.cuc.claremont.edu/index.php' + string)
        webbrowser.open_new_tab('https://cards.cuc.claremont.edu/index.php' + string)
        return HttpResponseRedirect('https://cards.cuc.claremont.edu/index.php' + string)

        #payload = {'loginphrase': username, 'password': password}
        #r = requests.post('https://cards.cuc.claremont.edu/', data = payload)

        #print r.text
        #return render_to_response('login.html', context_instance = RequestContext(request))
