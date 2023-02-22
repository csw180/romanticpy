import multiprocessing as mp
import playsound as ps

def play():
    ps.playsound("On_the_Bach.mp3",True)

if __name__ == "__main__":
    # process spawning
    p = mp.Process(name="SubProcess", target=play)
    p.start()
    print('here!')
    input('here')
    p.terminate()