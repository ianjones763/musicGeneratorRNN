import sys
import numpy as np
import matplotlib.pyplot as plt
import midi_util
import suites_util

#output = "NNNEEEETTTTUUUUIIIIIIIIIIIIIIIIIIIIIIIIIIINNIINNIIPPSSNNDDNNSSNNPPNNSSNNGGNNDDNNPPNNSSNNNNNNNIpFFFjjcNNNWENNNNNNNNNNNNNNNNNNcEUPNNSNNNPPNNNNNEEEETTTTUUUUIIIIIIIIIIIIIIIIINNIIPPSSNNDDNNSSNNPPNNSSNNGGNNDDNNPPNNSSNNNNNNNIINNNIINNIINNIINNIINNIINNIINNIINNIINNIINNIINNIQNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNIINNNNNIINNNNNNNNNNNNNNNNNddddNNNNNNNNNNNNNIIIINNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNbbNNNNNNNNN"

## model 9
#output = "egjlzcbQbQcQbQcgQbcbczzcczzlljjsllljjllggeppppppppilggggggbbccbQEbzzzziiiicQQQQbbQgShhlczjjjjjjgdjczlgzcbQEEbzzjdddjjjUgczzggQQRcczljgdspiuuggdddgGzggzzggjkkkggjjkzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzNNNNNNNNNNNNNNNEE"

## model 10
#output = "cvvzzddvvcczzggllzicccczccbbbjgglzzcbczljgbQccbQzcczljgdsicbczlzlzlgjzbbziicccclzccccllzccbbbcczljgggjzzcbzgdbcbcbcbzllzggjjzcPUTeeeegllzzzzzzzzzzzzzzzzNNNNNNNNNNNNNNNccccccccccNNNNNNNNNNNNNNNccNNNNNNNNNjjjjlljNTEEEQtEWEsspzlljjllggjlczclzlggjzbgdgjcvQQcclzgjPSDDiiiiiiiiiiTUUUUNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNddggNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNddggNNNNNNNNNNNNNNNNNN"

## model 16
#output = "QbQjQjilQbQlQlilQbQlQlizbcbzbzizbcbzblijbcbzlzjzlzsgfsfzczczzjczljczlljljllgllcccQEEUbcEQbQQbbccbbcczzlljjllzczzlljjllggggppbQccbiiiqqGccclzcbQbQEbbccIIIIIIIIPPpzcclzlzjjllggggppbgiiiiibbcccllEEbbbbccccppllQQQQbbQEQQbbcczzlljjllzczzlljjllggggppblcllcgjkiksjgkgkzzzzzzzzzzNNNNNNNNNNOOPSSpzzccllgggllccccllccbbNNNNNNNccbbNNNNNNccccNNbbWWEETTUUUUUUNNNNNNNNNNNNNNNNNNzzbzzbbEETTTTUUUUNNNNNNNNNNNNNNNNNNNNNNNNNddddddddggTTvvvvccvvgghhhtbbbbbbbbbbbbbbbbbbbbbccccppll"

## model 18
output = "zchhQbczlzjjssiittttsjzlczljlzWzlzWjlzjpzlgjlgzjlglzcbQcbgigiiiiiiiibQbczljggllzcbQEYYbcbQbQcllhllljjllzcbQEbczljzbcQQbbczlhijbQbQclzlllzcbQETEEQbcEQbbbbcczzlljjllzczzlljjllggggppppeeeeggzzzzggjjpssfjjzzljgdspiglccQQbbcEUjjjllzcbQEbbbbbbccccpDcczljjllzcbQEbczljzbcQbczlczggzzpsszzzcbbzzjljjllggggppppeeeeggzzggppgccQQQbbccbbbbbccccpDcPlzIIbUUUUNNNNNNNNNNNNNNzzzzNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNbbccbbEEEEEUUNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNzzzzNNNNNN"

"""
Generates a .mid file from the output of the LSTM
"""
def generate_midifile():
    chars = []
    for i in range(0, len(output)):
        chars.append(output[i])
    notes = midi_util.convert_to_notes(chars)
    ints = midi_util.convert_to_ints(notes)
    print "ints = "
    print ints

    midi_util.notes_to_midi(ints, "outputMIDIS/model18.mid")


"""
Iterates through an output file of the training process and stores
the loss vs epoch number, then plots it
Currently plotting models 2 and 9
"""
def analyze_epoch_loss():
    files = ['model17output.txt', 'model18output.txt']
    epochList =[]
    lossList = []
    
    for i in range(len(files)):
        f = open(files[i], 'r')
        lineCount = 0
        epochs = []
        loss = []
        for line in f:
            line = line.strip('\n')
            # Epoch num
            if lineCount == 0:
                line = line[:-4]
                currEpoch = line.split()[1]
                epochs.append(int(currEpoch))
            # Loss 
            elif lineCount == 1:
                currLoss = line.split()[4]
                loss.append(float(currLoss))
               
            # Increment lineCount
            if lineCount == 9:
                lineCount = 0
            else:
                lineCount += 1
        epochList.append(epochs)
        lossList.append(loss)
    
    # Loss vs epoch
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('white')
   
    plt.title('Loss Over Training Process')
    plt.xlabel('epoch')
    plt.ylabel('loss')
    line1 = plt.plot(epochList[0], lossList[0], label='model9')   # model17output
    line2 = plt.plot(epochList[1], lossList[1], label='model2')   # model18output

    plt.legend() 
    plt.show()

   


"""
Analyzes the interval changes of the output of the LSTM
compared to the interval changes in the original dataset
"""
def analyze_intervals():
    files = ['model17output.txt', 'model18output.txt']
    intervalsList = []
 
    print "reading in files..."
    # Iterate through output files
    for i in range(len(files)):
        f = open(files[i], 'r')
        outputIntervals = {}

        lineCount = 0
        for line in f:
            line = line.strip('\n')
            # Seed
            #if lineCount == 2 or lineCount == 4 or lineCount == 6 or lineCount == 8:
            #    print "seed line: " + line
            # Generation
            if lineCount == 3 or lineCount == 5 or lineCount == 7 or lineCount == 9:
                # Convert output to integer MIDI values
                chars = []
                for i in range(0, len(line)):
                    chars.append(line[i])
                notes = midi_util.convert_to_notes(chars)
                vals = midi_util.convert_to_ints(notes)
             
                for i in range(len(vals) - 1):
                    interval = np.abs(vals[i+1] - vals[i])
                    if vals[i+1] != 0 and vals[i] != 0:
                        outputIntervals[interval] = outputIntervals.get(interval, 0) + 1
                
            # Increment lineCount
            if lineCount == 9:
                lineCount = 0
            else:
                lineCount += 1
  
        # Convert to frequencies
        totalTransitions = 0
        for key in outputIntervals:
            totalTransitions += outputIntervals[key]
        for key in outputIntervals:
            outputIntervals[key] /= (1.0 * totalTransitions)
        # Append to list of maps
        intervalsList.append(outputIntervals)
  
    # Get the input data map from interval to frequency
    originalDataIntervals = suites_util.calculate_intervalpatterns() 
  
    # Get all interval vals (x vals for the graph) in a list
    intervals = []          # X vals for graph
    for key in originalDataIntervals:
        if key not in intervals:
            intervals.append(key)
    for m in intervalsList:
        for key in m:
            if key not in intervals:
                intervals.append(key)
    intervals = sorted(intervals)

    # Get all frequency vals (y vals for the graph) in a list for each output and original data
    frequencies = []        # list of Y vals for graph
    freqOriginal = []
    freqOutput1 = []
    freqOutput2 = []
    for interval in intervals:
        freqOriginal.append(originalDataIntervals.get(interval, 0))
        freqOutput1.append(intervalsList[0].get(interval, 0))
        freqOutput2.append(intervalsList[1].get(interval, 0))
    frequencies.append(freqOriginal)
    frequencies.append(freqOutput1)
    frequencies.append(freqOutput2)

    
    # Compare output frequencies to input frequencies
    # Loss vs epoch
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('white')
    plt.title('Interval Frequency of Generated Music Compared with Training Data')
    
    plt.xlabel('interval (number of half steps)')
    plt.ylabel('frequency')

    w = 0.25
    
    ax.bar([x - w for x in intervals], frequencies[0], width=w, color='#1996B2', label='Training Data')
    ax.bar(intervals, frequencies[1], width=w, color='#FF1971', label='model9')
    ax.bar([x + w for x in intervals], frequencies[2], width=w, color='#32CC0C', label='model2')
    ax.set_xlim([-.25, 8])
    plt.legend()
    plt.show() 


def graph_maxlen():
    maxlen = [60, 30, 16, 10, 5]
    loss   = [.03, .0612, .0978, .195, .44] 
    
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('white')

    plt.title('Loss Improvement with Larger Input Length')
    plt.xlabel('maxlen')
    plt.ylabel('loss')
    plt.plot(maxlen, loss, '-o')
    plt.show()

def graph_batchsize():
    batchsize = [128, 64, 32]
    loss      = [.0978, .1503, .4989] 

    fig, ax = plt.subplots()
    fig.patch.set_facecolor('white')
    
    plt.title('Loss Improvement with Larger Batch Size')
    plt.xlabel('batch_size')
    plt.ylabel('loss')
    plt.plot(batchsize, loss, '-o')
    plt.show()

def graph_epochs():
    epochs = [100, 200, 300, 400, 500]
    loss   = [.1248, .0451, .0345, .0451, .03] 

    fig, ax = plt.subplots()
    fig.patch.set_facecolor('white')
   
    plt.title('Loss Improvement with Number of Epochs Trained')
    plt.xlabel('epochs')
    plt.ylabel('loss')
    plt.plot(epochs, loss, '-o')
    plt.show()



if __name__ == "__main__":
    if sys.argv[1] == "midi":
        generate_midifile()
    if sys.argv[1] == "epochloss":
        analyze_epoch_loss()
    if sys.argv[1] == "intervals":
        analyze_intervals()
    if sys.argv[1] == "maxlen":
        graph_maxlen()
    if sys.argv[1] == "batchsize":
        graph_batchsize()
    if sys.argv[1] == "epochs":
        graph_epochs()

