from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp
import datetime
import time

from helpers import *

# configure application
app = Flask(__name__)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# custom filter
app.jinja_env.filters["usd"] = usd

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

@app.route("/")
@login_required
def index():
    stocks= db.execute("SELECT * FROM portfoglios WHERE user_id=:user_id",user_id=session['user_id'])
    rows=db.execute("SELECT cash FROM users WHERE id=:user_id",user_id=session['user_id'])
    cash=rows[0]['cash']
    total=0
    for stock in stocks:
        total+=stock['price']*stock['shares']
    capital=total+cash
    return render_template("index.html",stocks=stocks, cash=usd(cash),total=usd(total),capital=usd(capital))

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock."""
    #if user reached route via POST(as by submitting a form via POST)
    if request.method =="POST":
        
        #ensure a symbol was submitted
        
        if not request.form.get("symbol"):
            return apology("missing symbol")
        #ensure the symbol is valid
        obj = lookup(request.form.get("symbol"))
        if not obj:
            return apology("invalid symbol")
        if not request.form.get("shares"):
            return apology("missing number of shares")
        
        symbol=request.form.get("symbol")   
        shares = int(request.form.get("shares"))
        if type(shares)!= int:
            apology("not a integer")
            
        # query database for cash
        rows = db.execute("SELECT * FROM users WHERE id = :id", id=session['user_id'])
        cash=rows[0]['cash']
        price=obj['price']
        total=price*shares
        if cash<total:
            return apology("you don't have enough cash")
            
        cash-=total
        date= datetime.datetime.now()
        hour=time.strftime("%H:%M:%S")
       
        rows2 = db.execute("INSERT INTO 'transactions' ('Symbol','Name','Shares','Price','Total','user_id','date','time') VALUES (:symbol,:name,:shares,:price,:total,:user_id,:date,:time)", symbol=symbol,name=obj['name'],price=price,shares=shares,user_id=session['user_id'], total=total,date=date,time=hour)
        rows3 = db.execute("UPDATE 'users' SET cash=:cash WHERE id=:id",cash=cash,id=session["user_id"])
        
        counter = 0
        stocks = db.execute("SELECT * FROM portfoglios WHERE user_id=:user_id",user_id=session['user_id'])

        for stock in stocks:
            if stock['symbol']==symbol:
                counter +=1

        if counter==0:
            rows4= db.execute("INSERT INTO 'portfoglios' ('user_id','symbol','name','shares','price','product') VALUES (:user_id,:symbol,:name,:shares,:price,:product)",user_id=session['user_id'],symbol=symbol,name=obj['name'],price=price,shares=shares,product=total)
        else:
            shares+= stock['shares']
            product= shares*price
            rows6 =db.execute("UPDATE 'portfoglios' SET shares=:shares, price=:price, product=:product WHERE user_id=:user_id AND symbol=:symbol",shares=shares, price=price,user_id=session['user_id'],symbol=symbol,product=product)
        
        return redirect(url_for("index"))
        
    #else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    """Show history of transactions."""
    transactions=db.execute("SELECT * FROM transactions WHERE user_id=:user_id",user_id=session['user_id'])
    return render_template("history.html",transactions=transactions)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""

    # forget any user_id
    session.clear()

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))

        # ensure username exists and password is correct
        if len(rows) != 1 or not pwd_context.verify(request.form.get("password"), rows[0]["hash"]):
            return apology("invalid username and/or password")

        # remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # redirect user to home page
        return redirect(url_for("index"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("login"))


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    #if user reached route via POST(as by submitting a form via POST)
    if request.method =="POST":
        
        #ensure a symbol was submitted
        if not request.form.get("symbol"):
            return apology("missing symbol")
        #ensure the symbol is valid
        obj = lookup(request.form.get("symbol"))
        if not obj:
            return apology("invalid symbol")
        
        return render_template("stock.html",name=obj['name'],price=usd(obj['price']),symbol=obj['symbol'])
        
    #else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("quote.html")

@app.route("/stock",methods=["GET"])
@login_required
def stock():
    return render_template("stock.html")
    
    
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user."""
     # forget any user_id
    session.clear()

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")
        
        elif not request.form.get("password") == request.form.get("password2"):
            return apology("the password are not the same")
        
        encrypted_pwd = pwd_context.hash(request.form.get("password"))

        # query database for username
        result = db.execute("INSERT INTO 'users' (username, hash) VALUES (:username,:hash)", username=request.form.get("username"), hash=encrypted_pwd)
        if not result:
            return apology("this username already exists")
        
        rows = db.execute("SELECT * FROM 'users' WHERE username= :username",username=request.form.get("username"))

        session["user_id"] = rows[0]["id"]

        # redirect user to home page
        return redirect(url_for("index"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock."""
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("missing symbol")
        if not request.form.get("shares"):
            return apology("missing shares")
        obj=lookup(request.form.get("symbol"))
        if not obj:
            return apology("invalid symbol")
        else:
            stocks = db.execute("SELECT * FROM portfoglios WHERE user_id=:user_id",user_id=session['user_id'])
            rows = db.execute("SELECT * FROM users WHERE id = :id", id=session['user_id'])
            
            cash=rows[0]['cash']
            price = obj['price']
            symbol = request.form.get("symbol")
            shares = int(request.form.get("shares"))
            name = obj['name']
            date= datetime.datetime.now()
            hour=time.strftime("%H:%M:%S")
            total=shares*price
            counter=0
            
            db.execute("INSERT INTO 'transactions' ('Symbol','Name','Shares','Price','Total','user_id','date','time') VALUES (:symbol,:name,:shares,:price,:total,:user_id,:date,:time)", symbol=symbol,name=obj['name'],price=price,shares=-shares,user_id=session['user_id'], total=total,date=date,time=hour)
            
            for stock in stocks:
                if stock['symbol']==symbol:
                    counter+=1
                    shares_owned=stock['shares']
                    if shares_owned >= shares:
                        cash+=shares*price
                        shares_owned-=shares
                        
                        db.execute("UPDATE users SET cash=:cash WHERE id=:user_id",cash=cash, user_id=session['user_id'])
                        if shares_owned > 0:
                            db.execute("UPDATE portfoglios SET shares=:shares WHERE user_id=:user_id AND symbol=:symbol",shares=shares_owned,symbol=symbol, user_id=session['user_id'])
                        else:
                            db.execute("DELETE from portfoglios WHERE user_id=:user_id AND symbol=:symbol",user_id=session['user_id'],symbol=symbol)
                        return redirect(url_for("index"))
                    else:
                        return apology("too many shares")
            if counter == 0:
                return apology("symbol not owned")
    else:
        return render_template("sell.html")

