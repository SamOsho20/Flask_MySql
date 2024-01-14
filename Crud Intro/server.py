from flask import Flask, render_template, request, redirect
# import the class from friend.py
from friend import Friend

@app.route('/friends/create', methods=['POST'])
def create():
    Friend.save(request.form)
    return redirect('/')

@app.route('/')
def get_all_friends():
    list_friends = Friend.get_all_friends()
    return render_template("index.html", list_friends = list_friends)

@app.route('/friends/<int:friend_id>')
def get_one_friend(friend_id):
    #we must enter in teh id as a variable
    one_friend = Friend.get_one_friend(friend_id)
    #setting this variable to equal the friend_id
    return render_template('index.html', one_friend = one_friend)
    


@app.route('/friends/update',methods=['POST'])
def update():
    Friend.update(request.form)
    return redirect('/')


@app.route('/friends/delete/<int:friend_id>')
def delete(friend_id):
    Friend.delete(friend_id)
    return redirect('/')

