import random

def randrange_float(start, stop, step):
    return random.randint(0, int((stop - start) / step)) * step + start



def calculate_values(entrance, max):
    stop_loss = max - (max*0.15)
    stop_gain = entrance + (entrance*0.05)
    return stop_loss, stop_gain

def print_info(paper_value, stop_loss, stop_gain):
    print "Paper value: %.2f, Stop Loss: %.2f, Stop Gain: %.2f" % (paper_value, stop_loss, stop_gain)



entrance = 5000.00#23.83
paper_value = entrance
max = paper_value

stop_loss, stop_gain = calculate_values(entrance, max)
print_info(paper_value, stop_loss, stop_gain)

while True:
    percent = randrange_float(-3, 3, 0.3)
    if percent >= 0:
        paper_value += (paper_value * (abs(percent)/100))
    else:
        paper_value -= (paper_value * (abs(percent)/100))
    #raw_input()
    print "%.2f" % paper_value
    
    if paper_value > max:
        max = paper_value
    
    stop_loss, stop_gain = calculate_values(entrance, max)
    print_info(paper_value, stop_loss, stop_gain)

    if paper_value <= stop_loss or paper_value >= stop_gain:
        print "Finalized at: %.2f" % paper_value
        raw_input("Press any type to restart...")
        entrance = paper_value
        max = entrance
        stop_loss, stop_gain = calculate_values(entrance, max)
        print_info(paper_value, stop_loss, stop_gain)