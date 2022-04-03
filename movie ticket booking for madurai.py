
global f
f = 0 
#this t_movie function is used to select movie name
def movies():
    global f
    f = f+1
    print("which movie do you want to watch?")
    print("1,beast 1 ")
    print("2,kgf 2 2 ")
    print("3,valimai 3")
    print("4, kaathu vaakula rendu kadhal")
    print("5, RRR")
    print("4,back")
    movie = int(input("choose your movie: "))
    if movie == 6:
      # in this it goes to center function and from center it goes to movie function and it comes back here and then go to theater
      center()
      theater()
      return 0
    if f == 1:
      theater()
# this theater function used to select screen
def theater():
    print("which screen do you want to watch movie: ")
    print("1,SCREEN 1")
    print("2,SCREEN 2")
    print("3,SCREEN 3")
    a = int(input("choose your screen: "))
    ticket = int(input("number of ticket do you want "))
    timing(a)
 
# this timing function used to select timing for movie
def timing(a):
    time1 = {
        "1": "10.00-1.00",
        "2": "1.10-4.10",
        "3": "4.20-7.20",
        "4": "7.30-10.30"
    }
    time2 = {
        "1": "10.15-1.15",
        "2": "1.25-4.25",
        "3": "4.35-7.35",
        "4": "7.45-10.45"
    }
    time3 = {
        "1": "10.30-1.30",
        "2": "1.40-4.40",
        "3": "4.50-7.50",
        "4": "8.00-10.45"
    }
    if a == 1:
        print("choose your time:")
        print(time1)
        t = input("select your time:")
        x = time1[t]
        print("booking successful!, enjoy movie at "+x)
    elif a == 2:
        print("choose your time:")
        print(time2)
        t = input("select your time:")
        x = time2[t]
        print("booking successful!, enjoy movie at "+x)
    elif a == 3:
        print("choose your time:")
        print(time3)
        t = input("select your time:")
        x = time3[t]
        print("booking successful!, enjoy movie at "+x)
    return 0
 
 
def movie(theater):
    if theater == 1:
        movies()
    elif theater == 2:
        movies()
    elif theater == 3:
        movies()  
    elif theater == 4:
        movies()
    elif theater == 5:
        movies() 
    elif theater == 6:
        region()         
    else:
        print("wrong choice")
def center():
    print("select theatre to see movie ")
    print("1,vetri cinemas")
    print("2,thangareegal")
    print("3,priya complex")
    print("4,inox")
    print("5,ambiga cinemas")
    print("6,back")
    a = int(input("choose your option: "))
    movie(a)
    return 0
 
# this function is used to select city
def region():
    print(" welcome to book your tickets ")
    print("choose theatre to watch movie:")
    print("1,kk nagar 1")
    print("2,villapuram 2 ")
    print("3,periyar bus stand 3 ")
    print("4, thallakulam")
    print("5,anna nagar")
    place = int(input("choose your option: "))
    if place == 1:
      center()
    elif place == 2:
      center()
    elif place == 3:
      center()
    elif place == 4:
      center() 
    elif place == 5:
      center()     
    else:
      print("wrong choice")
region()