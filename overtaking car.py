import turtle,time
wn = turtle.Screen()
wn.setup(700,500)
turtle.tracer(2)
image0=[]
for i in range (241):
    i1=str(i)
    image0.append(i1+'.gif')
wn.bgpic(image0[0])
t1=turtle.Turtle()
t1.up()

t2=turtle.Turtle()
t2.up()
t2.goto(-30,-210)

t3=turtle.Turtle()
t3.up()
t3.goto(280,-100)

t4=turtle.Turtle()
t4.up()
t4.goto(-280,-100)


image1=['Bcar1_.gif','Bcar2_.gif','Bcar3_.gif']

image1L=['Bcar1L_.gif','Bcar2L_.gif','Bcar3L_.gif']

image1R=['Bcar1R_.gif','Bcar2_.gif','Bcar3R_.gif']
image2=['Becar1.gif','Becar2.gif','Becar3.gif']
image3=['Kcar1.gif','Kcar2.gif','Kcar2.gif']
image4=['Ccar1.gif','Ccar2.gif','Ccar3.gif']
for j in range (3):
    wn.addshape(image1[j])
    wn.addshape(image1L[j])
    wn.addshape(image1R[j])
    wn.addshape(image2[j])
    wn.addshape(image3[j])
    wn.addshape(image4[j])

while True:
    t1.hideturtle()
    t1.goto(-400,-190)
    X1=t1.xcor()
    t1.showturtle()

    for i in range(241):
        #print(i)
        
        i1=i%3
        i2=i%8
        
        if i<30:
            t1.shape(image1[i1])
        t2.shape(image2[i1])
        t3.shape(image3[i1])
        t4.shape(image4[i1])
       
        if i>=30 and i<=100:
            
            if i2==0:
                t1.shape(image1R[i1])
            if i2==4:
                t1.shape(image1[i1])
                
            
            if i==70:
                t1.setheading(45)
                #t1.shape(image1R[i3])
                t1.fd(90)
                t1.setheading(0)
        if i>100 and i<170:
            if i2==0:
                t1.shape(image1L[i1])
            if i2==4:
                t1.shape(image1[i1])
                
            if i==140:
                t1.setheading(-45)
                #t1.shape(image1L[0])
                t1.fd(90)
                t1.setheading(0)
        #print(i)
        if i>170:
            t1.shape(image1[i1])
                        
        wn.bgpic(image0[i])
        t1.fd(2.9)
        time.sleep(0.02)
