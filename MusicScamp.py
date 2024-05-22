from scamp import *
from math import *
import random
import time
s = Session().run_as_server()
n = s.new_part("Cello")
# n = s.new_part("Bagpipe")
# n = s.new_part("Flute")
n.set_max_pitch_bend(100)
cresc = Envelope.from_levels([0.6,0.8,1.0])

def chrom (start, end, time):
    step = ((start-end)/time)
    return [start - (step * x) for x in range(0,time+1)]

def osci (start, end, time):
    step = ((start-end)/time)*2
    returnable = [start]
    p = start
    while p > end:
        p = p + step
        returnable.append(p)
        p = p - step*2
        returnable.append(p)
    #returnable.append(end)
    return returnable

def tenuto (start, end, time):
    step = 3*((start-end)/time)
    p = start
    returnable = []
    while p > end:
        returnable.append(p)
        returnable.append(p)
        returnable.append(p)
        p = p - step
    # returnable.append(end)
    # returnable.append(end)
    # returnable.append(end)
    return returnable

def jump (start, end, time):
    step = ((start-end)/time)*2
    returnable = []
    p = start
    while p > end:
        returnable.append(p)
        returnable.append(end)
        p = p - step
    returnable.append(end)
    returnable.append(end)
    return returnable

def degrade_smooth (start, end, time, function):
    pitches = function(start, end, time) #allows different functions to work in code
    print(function, pitches)
    n.play_note(pitches, 0.6, time)

def degrade_list (start, end, time, function):
    pitches = function(start, end, time)
    print(function, pitches)
    for pitch in pitches:
        n.play_note(pitch, 0.6, (time/len(pitches)))

def bass (pitch, time):
    n.play_note(pitch, cresc, time)

def bass_inf (pitch):
    while True:
        bass(pitch,100)

def trash_bag_sound (time):
    b = s.new_part("Bird")
    s.fork(b.play_note,args=(70, 0.5, time))
    s.fork(degrade_list,args=(60, 50, time, random_function([chrom, jump, osci, tenuto]))) # swap between list and smooth / differing functions

def random_function(options): # takes input list
    return options[random.randint(0,len(options)-1)]

# sprint 1 demo notes
    # need to see audio and visual together in the same scene to figure out the ideas better
    # audio should be more different
    # audio should match up with shapes more + vibes (plastic bottle sounds different than bag etc)
    # music feels ominous but should feel more naturelike, bird/flute, calming, serene
    # background color should be changed to something that works better with the visuals
    # work in large rough strokes to make it easy to show off

# spring 2 demo notes
    # ?
    # ?
    # ?
    # ?
    # ?