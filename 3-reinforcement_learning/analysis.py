# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    answerDiscount = 0.9 # Does see quite far
    answerNoise = 0.01 # Almost no noise, direct to the objective
    return answerDiscount, answerNoise


# Prefer the close exit (+1), risking the cliff (-10)
def question3a():
    answerDiscount = 0.2 # Does not see very far
    answerNoise = 0.0 # No noise
    answerLivingReward = 0.0 # Wants to finish ASAP
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'


# Prefer the close exit (+1), but avoiding the cliff (-10)
def question3b():
    answerDiscount = 0.2 # Does not see very far
    answerNoise = 0.2 # A little of noise
    answerLivingReward = 0.0 # Wants to finish ASAP
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'


# Prefer the distant exit (+10), risking the cliff (-10)
def question3c():
    answerDiscount = 0.9 # Does see quite far
    answerNoise = 0.0 # No noise
    answerLivingReward = 0.2 # Willing to spend some more time until arrive to terminal
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'


# Prefer the distant exit (+10), avoiding the cliff (-10)
def question3d():
    answerDiscount = 0.9 # Does see quite far
    answerNoise = 0.2 # A little of noise 
    answerLivingReward = 0.2 # Willing to spend some more time until arrive to terminal
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'


# Avoid both exits and the cliff (so an episode should never terminate)
def question3e():
    answerDiscount = 0.0 # Is blind
    answerNoise = 0.0 # No noise 
    answerLivingReward = 1.0 # Wants to live
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'
    

def question8():
    answerEpsilon = None
    answerLearningRate = None
    return answerEpsilon, answerLearningRate
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
