#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<math.h>
#include<time.h>
#include<string.h>
#include<assert.h>
#include<locale.h>
#include<signal.h>
#include<ctype.h>
#include<errno.h>
#include<stdarg.h>
#include<wctype.h>
#include<limits.h>
#include<float.h>
#include<complex.h>
#include<stdbool.h>
#include<stdalign.h>
#include<stdnoreturn.h>
#include<stdatomic.h>

int main(){
    printf("Cat\n");
    printf("Hallo\n");
    for(int i=1;i<=7;i++){
        printf("%d",i);
    }
    printf("\nMultiplication of 93\n");
    for (int j=1;j<=10;j++){
        printf("93 X %d = %d\n",j,93*j);
    }
 
    int k=93,z = pow(k,3);
    printf("\nCube of %d is equal to %d\n",k,z);
    printf("Hello World\nHanuman\n");
 
    int wa=64, d=2;
    if (wa%d == 0){
        printf("It is even number");
    }
    else{
        printf("It is Not even number");
    }
    printf("\nThe Number of Module is %d\n",wa%d);
 
    float length=23.7,breadth=21.3,rad=7, height = 12,pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513280664709384460955058223172;
    printf("\nPerimeter of Rectangle %f",2*length+2*breadth);
    printf("\nArea of Rectangle %f",length*breadth);
    printf("\nArea of Cuboid %f",length*breadth);
    printf("\nCircumference of Circle %f",2*pi*rad);
    printf("\nArea of Circle %f",pi*rad*rad);
    printf("\nVolume of Cylinder %f",2*pi*rad*rad*height);
    printf("\nVolume of Sphere %f",4/3*pi*rad*rad*rad);
    printf("\nVolume of Cone %f",1.0/3*pi*rad*rad*rad);
    printf("\nArea of TSA of Cuboid %f",2*length*breadth+2*breadth*height+2*length*height);
    printf("\nArea of CSA of Cuboid %f\n\n",2*length*breadth+height);


 
    int a0ht,a0wd,a1ht,a1wd,a2ht,a2wd,a3ht,a3wd,a4ht,a4wd,a5ht,a5wd,a6ht,a6wd,a7ht,a7wd,a8ht,a8wd;
    a0ht = 1189,a0wd = 841;
    printf("Size of A0 paper Height = %d Width = %d\n",a0ht,a0wd);
    a1ht = a0wd,a1wd = a0ht/2;
    printf("Size of A1 paper Height = %d Width = %d\n",a1ht,a1wd);
    a2ht = a1wd,a2wd = a1ht/2;
    printf("Size of A2 paper Height = %d Width = %d\n",a2ht,a2wd);
    a3ht = a2wd,a3wd = a2ht/2;
    printf("Size of A3 paper Height = %d Width = %d\n",a3ht,a3wd);
    a4ht = a3wd,a4wd = a3ht/2;
    printf("Size of A4 paper Height = %d Width = %d\n",a4ht,a4wd);
    a5ht = a4wd,a5wd = a4ht/2;
    printf("Size of A5 paper Height = %d Width = %d\n",a5ht,a5wd);
    a6ht = a5wd,a6wd = a5ht/2;
    printf("Size of A6 paper Height = %d Width = %d\n",a6ht,a6wd);
    a7ht = a6wd,a7wd = a6ht/2;
    printf("Size of A7 paper Height = %d Width = %d\n",a7ht,a7wd);
    a8ht = a7wd,a8wd = a7ht/2;
    printf("Size of A8 paper Height = %d Width = %d\n",a8ht,a8wd);
 
    float bp = 100000,da,hra,grpay;
    da = 0.4*bp,hra = 0.2*bp,grpay = bp + hra + da;
    printf("\nBasic pay of Employee :%f",bp);
    printf("\nDearness Allowance : %f",da);
    printf("\nHouse Rent Allowance : %f",hra);
    printf("\nGross pay of Employee : %f",grpay);
 
    int m1 = 96,m2 = 97,m3 = 98,m4 = 99,m5 =100,total;
    total = (m1+m2+m3+m4+m5)/5;
    if((total<40)||m1<33||m2<33||m3<33||m4<33||m5<33){
        printf("\nYour Total Percentage is %d and You are Fail",total);
    }
    else{
        printf("\nYour Total Percentage is %d and You are Pass",total);
    }
    int fr = 98.7,cent,kelvin;
    cent = 5.0/9.0*(fr - 32);
    kelvin = cent + 373;
    printf("\nIn Kelvin Temperature %d K",kelvin);
    printf("\nIn Celsius Temperature %d C",cent);
 
    float s,a = 5.3,b = 6.6,c = 7.8,area;               // Heron's Formula
    s = (a + b + c)/2;
    area = sqrt(s*(s-a)*(s-b)*(s-c));
    printf("\nArea of a Triangle is %f",area); 
 
   float amt,ci,rt = 3.5,yr = 2,pri = 10000;            // Compound Interest
    ci = pri*(pow(1 + rt/100,yr));
    printf("\nCompound Interest = %f",ci);
    amt = pri + ci;
    printf("\nAmount of CI = %f",amt);
 
    float si,amt2,rt2 = 3.5,yr2 = 2,pri2 = 10000;        // Simple Interest
    si = (pri2*rt2*yr2)/100;
    printf("\nSimple Interest = %f",si);
    amt2 = pri2 + si;
    printf("\nAmount of SI = %f",amt2);
 
    float cm,m,km,ft,inch,mil = 1;
    km = mil*1.609344,m = km*1000,ft = m*3.280839895013123,inch = ft*12,cm = inch*2.54;
    printf("\nDistance Between two Point in Kilometer is %f Km",km);
    printf("\nDistance Between two Point in Meter is %f M",m);
    printf("\nDistance Between two Point in Centimeter is %f cm",cm);
    printf("\nDistance Between two Point in Inch is %f inch",inch);
 
    float dam = 99;
    printf("%f \n\n",sqrt(a));
 
    int j,i;
    for (int i = 1; i<10; i++){
        j = pow(i,i);
        printf("Exponential of %d and %d is %d \n",i,i,j);
    }
 
    float g,kg,pound,ounce,carat,stone,ton = 1;
    stone  = ton*157.4730444177697,kg = stone*6.35029318,pound = kg*2.204622621848776,ounce = pound*16,carat = ounce*141.747615625,g = carat*0.2;
    printf("\n%f",stone);
    printf("\n%f",kg);
    printf("\n%f",pound);
    printf("\n%f",ounce);
    printf("\n%f",carat);
    printf("\n%f",g);

    float weight = 59,height = 1.6256,bmi;
    bmi = (weight)/(height*height);
    printf("Your BMI is %f\n",bmi);

    float bmr,w = 59,h = 162.56,age = 23;
    float bmr = 1384;
    // bmr = 66 + (13.73899 * w) + (5 * h) - (6.8*age);
    printf("BMR = %f\n",bmr);
    
    printf("Sedentary BMR - %f\n",bmr*1.2);
    printf("Lightly active BMR - %f\n",bmr*1.375);
    printf("Moderately active BMR - %f\n",bmr*1.55);
    printf("Very active BMR - %f\n",bmr*1.725);
    printf("Highly active BMR - %f\n",bmr*1.9);

    printf("\nCutting | Lean | Fat loss");
    float carb,pro,fat,cal = bmr*1.55;
    carb = cal*0.35,pro = cal*0.5,fat = cal*0.25;
    printf("\nTotal Amount of Calories = %f",cal);
    printf("\nThis amount of Protein = %f",pro);
    printf("\nThis amount of Carbohydrate = %f",carb);
    printf("\nThis amount of Fat = %f",fat);

    printf("\n\nMaintain | Lean and Fit");
    carb = cal*0.30,pro = cal*0.4,fat = cal*0.3;
    printf("\nTotal Amount of Calories = %f",cal);
    printf("\nThis amount of Protein = %f",pro);
    printf("\nThis amount of Carbohydrate = %f",carb);
    printf("\nThis amount of Fat = %f",fat);

    printf("\n\nBulking | Bodybuilding | Muscular");
    carb = cal*0.5,pro = cal*0.35,fat = cal*0.25;
    printf("\nTotal Amount of Calories = %f",cal);
    printf("\nThis amount of Protein = %f",pro);
    printf("\nThis amount of Carbohydrate = %f",carb);
    printf("\nThis amount of Fat = %f",fat);

    printf("\n\nCalories Needs in our body at daily basis")

    printf("\nTotal Amount of Calories = %f",cal);
    printf("\nThis amount of Protein = %f",pro);
    printf("\nThis amount of Carbohydrate = %f",carb);
    printf("\nThis amount of Fat = %f",fat);

    printf("\n\nMacro Nutrient Need Daily in our body At daily Basis")
    float gpro = pro/4,gcarb = carb/4,gfat = fat/9;
    printf("\n\nProtein = %f g",gpro);
    printf("\nCarbohydrates = %f g",gcarb);
    printf("\nFats = %f g",gfat);

    printf("%u",&weight);
    printf("\n%u",&heigh);
    printf("\n%u",&bmi);
    printf("\n%u",&age);
    printf("\n%u",&bmr);
    printf("\n%u",&bmi);


    int x=6,y=3;
    printf("\nYour X and Y Co-ordinate\n");
    if(x>0 && y>0){
        printf("You are in First Quadrant\n");
        printf("You are in (+,+)");
    }
    if(x<0 && y>0){
        printf("You are in Second Quadrant\n");
        printf("You are in (-,+)\n");
    }
    if(x>0 && y<0){
        printf("You are in Fourth Quadrant\n");
        printf("You are in (+,-)\n");
    }
    if(x<0 && y<0){
        printf("You are in Third Quadrant\n");
        printf("You are in (-,-)\n");
    }
    printf("Your Co-ordinate is %d and %d",x,y);

    int jac = 2;
    int mac = 3;
    int *jill = &jac;
    int**kate = &jill;
    int***let = &kate;
    ***let = 7;

    printf("%u\n",&jac);
    printf("%u\n",&mac);
    printf("%u\n",jill);
    printf("%u\n",kate);
    printf("%u\n",let);
    printf("%u\n",jac);
    printf("%u\n",*jill);
    printf("%u\n",*kate);
    printf("%u\n",*let);
    printf("%u\n",&jill);
    printf("%u\n",&kate);
    printf("%u\n",let);
    printf("%u\n",jill+1);
    
    char name [] = "Sourav";
    printf("%s",name);
    char name[] = {'S','o','u','r','a','v','\0'};
    printf("%s",name);

    int m;
    for (int i = 1; i <= 64; i++){
        m = pow(2,i);
    }
    printf("Sum of Num is %d\n",m);
    return 0;
}

