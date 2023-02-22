import math
import re

repeat=1
while repeat==1:
    x = input('Value for x or enter pi for input containing pi: ')
    if 'pi' in x.lower():
        piStr=input("Enter the expression using format a*pi/b: ")

        #split and assign internal pi value to string 'pi'

        valueList=re.split('\*|\/',piStr) 
        #convert from str to float for calculation
        coefficient= float(valueList[0])
        #print(type(valueList[0]))
        #print(type(valueList[2]))
        fractional= float(valueList[2])
        x=coefficient*math.pi/fractional
        print('x =',x)  
    else:
        x=float(x)
        x=x%(2*math.pi)
        print("x =",x)

    sum=0
    for i in range (0,10000):
        term=(((-1)**i)*(x**(2*i+1)))/(math.factorial((2*i)+1))
        #b+=a
        #print(
        #term=(-1)*term*(x*x)/(2*i*(2*i+1))
        sum+=term
        print("Estimated value of sequence sin(x):",sum)
        print("True value of sequence sin(x):",math.sin(x))
        
        #Conditional for accuracy check
        if abs(sum-math.sin(x)) < 0.000001:
            break

    else:
        print("Sequence not convergent after 10000 iteration")
    #run until user choose to quit
    repeat=int(input("Enter 1 to run again or 2 to quit:\n"))
    if repeat==2:
        print("Exit program")
        break

'''Output
Value for x or enter pi for input containing pi: 1*pi/3
Enter the expression using format a*pi/b: 1*pi/3
1.0471975511965976
Estimated value of sequence sin(x): 1.0471975511965976
True value of sequence sin(x): 0.8660254037844386
Estimated value of sequence sin(x): 0.8558007815651173
True value of sequence sin(x): 0.8660254037844386
Estimated value of sequence sin(x): 0.8662952837868347
True value of sequence sin(x): 0.8660254037844386
Estimated value of sequence sin(x): 0.8660212716563725
True value of sequence sin(x): 0.8660254037844386
Estimated value of sequence sin(x): 0.8660254450997811
True value of sequence sin(x): 0.8660254037844386
Enter 1 to run again or 2 to quit:
1
Value for x or enter pi for input containing pi: -1*pi/6
Enter the expression using format a*pi/b: -1*pi/6
-0.5235987755982988
Estimated value of sequence sin(x): -0.5235987755982988
True value of sequence sin(x): -0.49999999999999994
Estimated value of sequence sin(x): -0.49967417939436376
True value of sequence sin(x): -0.49999999999999994
Estimated value of sequence sin(x): -0.5000021325887924
True value of sequence sin(x): -0.49999999999999994
Estimated value of sequence sin(x): -0.4999999918690232
True value of sequence sin(x): -0.49999999999999994
Enter 1 to run again or 2 to quit:
1
Value for x or enter pi for input containing pi: 0.112
Estimated value of sequence sin(x): 0.112
True value of sequence sin(x): 0.11176599215128519
Estimated value of sequence sin(x): 0.11176584533333334
True value of sequence sin(x): 0.11176599215128519
Enter 1 to run again or 2 to quit:
1
Value for x or enter pi for input containing pi: pi
Enter the expression using format a*pi/b: 1*pi/1
3.141592653589793
Estimated value of sequence sin(x): 3.141592653589793
True value of sequence sin(x): 1.2246467991473532e-16
Estimated value of sequence sin(x): -2.0261201264601763
True value of sequence sin(x): 1.2246467991473532e-16
Estimated value of sequence sin(x): 0.5240439134171688
True value of sequence sin(x): 1.2246467991473532e-16
Estimated value of sequence sin(x): -0.07522061590362306
True value of sequence sin(x): 1.2246467991473532e-16
Estimated value of sequence sin(x): 0.006925270707505135
True value of sequence sin(x): 1.2246467991473532e-16
Estimated value of sequence sin(x): -0.00044516023820921277
True value of sequence sin(x): 1.2246467991473532e-16
Estimated value of sequence sin(x): 2.1142567558399565e-05
True value of sequence sin(x): 1.2246467991473532e-16
Estimated value of sequence sin(x): -7.727858894306387e-07
True value of sequence sin(x): 1.2246467991473532e-16
Enter 1 to run again or 2 to quit:
1
Value for x or enter pi for input containing pi: 1*pi/2
Enter the expression using format a*pi/b: 1*pi/2
1.5707963267948966
Estimated value of sequence sin(x): 1.5707963267948966
True value of sequence sin(x): 1.0
Estimated value of sequence sin(x): 0.9248322292886504
True value of sequence sin(x): 1.0
Estimated value of sequence sin(x): 1.0045248555348174
True value of sequence sin(x): 1.0
Estimated value of sequence sin(x): 0.9998431013994987
True value of sequence sin(x): 1.0
Estimated value of sequence sin(x): 1.0000035425842861
True value of sequence sin(x): 1.0
Estimated value of sequence sin(x): 0.999999943741051
True value of sequence sin(x): 1.0
Enter 1 to run again or 2 to quit:
1
Value for x or enter pi for input containing pi: 0.5
Estimated value of sequence sin(x): 0.5
True value of sequence sin(x): 0.479425538604203
Estimated value of sequence sin(x): 0.4791666666666667
True value of sequence sin(x): 0.479425538604203
Estimated value of sequence sin(x): 0.47942708333333334
True value of sequence sin(x): 0.479425538604203
Estimated value of sequence sin(x): 0.479425533234127
True value of sequence sin(x): 0.479425538604203
Enter 1 to run again or 2 to quit:
1
Value for x or enter pi for input containing pi: 7.3
Estimated value of sequence sin(x): 7.3
True value of sequence sin(x): 0.8504366206285644
Estimated value of sequence sin(x): -57.536166666666674
True value of sequence sin(x): 0.8504366206285644
Estimated value of sequence sin(x): 115.21979941666666
True value of sequence sin(x): 0.8504366206285644
Estimated value of sequence sin(x): -103.97461564478172
True value of sequence sin(x): 0.8504366206285644
Estimated value of sequence sin(x): 58.259695169448605
True value of sequence sin(x): 0.8504366206285644
Estimated value of sequence sin(x): -20.335454133190794
True value of sequence sin(x): 0.8504366206285644
Estimated value of sequence sin(x): 6.512850394614677
True value of sequence sin(x): 0.8504366206285644
Estimated value of sequence sin(x): -0.3002265019889103
True value of sequence sin(x): 0.8504366206285644
Estimated value of sequence sin(x): 1.0345855120552263
True value of sequence sin(x): 0.8504366206285644
Estimated value of sequence sin(x): 0.8265968213288754
True value of sequence sin(x): 0.8504366206285644
Estimated value of sequence sin(x): 0.8529866244927021
True value of sequence sin(x): 0.8504366206285644
Estimated value of sequence sin(x): 0.8502073505587093
True value of sequence sin(x): 0.8504366206285644
Estimated value of sequence sin(x): 0.8504541964052801
True value of sequence sin(x): 0.8504366206285644
Estimated value of sequence sin(x): 0.8504354579221408
True value of sequence sin(x): 0.8504366206285644
Estimated value of sequence sin(x): 0.8504366876927892
True value of sequence sin(x): 0.8504366206285644
Enter 1 to run again or 2 to quit:
1
Value for x or enter pi for input containing pi: 133221
Estimated value of sequence sin(x): 4.905117178412709
True value of sequence sin(x): -0.9814853367334335
Estimated value of sequence sin(x): -14.764545391942715
True value of sequence sin(x): -0.9814853367334335
Estimated value of sequence sin(x): 8.89823033139934
True value of sequence sin(x): -0.9814853367334335
Estimated value of sequence sin(x): -4.657258093875628
True value of sequence sin(x): -0.9814853367334335
Estimated value of sequence sin(x): -0.12743285213697586
True value of sequence sin(x): -0.9814853367334335
Estimated value of sequence sin(x): -1.1182363605421308
True value of sequence sin(x): -0.9814853367334335
Estimated value of sequence sin(x): -0.9654228647659295
True value of sequence sin(x): -0.9814853367334335
Estimated value of sequence sin(x): -0.9829310522874528
True value of sequence sin(x): -0.9814853367334335
Estimated value of sequence sin(x): -0.9813823388773751
True value of sequence sin(x): -0.9814853367334335
Estimated value of sequence sin(x): -0.9814912930146545
True value of sequence sin(x): -0.9814853367334335
Estimated value of sequence sin(x): -0.9814850514537995
True value of sequence sin(x): -0.9814853367334335
Enter 1 to run again or 2 to quit:
2
Exit program
'''