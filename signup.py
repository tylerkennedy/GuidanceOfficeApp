
# -*- coding: UTF-8 -*-

# enable debugging



#print ("Hello World!")


from flask import, request redirect

@app.route('/signup', methods = ['POST'])

def signup():
	email = request.form['firstname']
	print("First name is '" + firstname + "'")
	return redirect('/')