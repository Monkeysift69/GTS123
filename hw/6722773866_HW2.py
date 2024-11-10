import math as m
start = input("Start number: ")
stop = input("End number: ")
step = input("Step number: ")

if start.isnumeric() and stop.isnumeric() and step.isnumeric():
    start = int(start)
    stop = int(stop)
    step = int(step)

    if stop > start and start >= 1 and step >= 1:
        c = 0
        t = 0
        nlist = ""

        for prime in range(start, stop+1, step):
            t += 1
            if prime > 1:
                p = True
                for check in range(2, int(m.sqrt(prime)+1)):
                    if prime % check == 0:
                        p = False
                        break

                if p:
                    nlist += "%s*"%prime
                    c += 1
                else:
                    nlist += "%s"%prime
            else:
                nlist += "%s"%prime
            if prime + step <= stop:
                nlist += ", "
        print("Starting from %d and ending at %d with a step of %d, there are a total of %d numbers." %(start,stop,step,t))
        print("Among them, %d are prime." %c)
        print("Numbers: %s"%nlist)
    else:
        print("Input ERROR!!")
else:
  print("Input ERROR!!")
