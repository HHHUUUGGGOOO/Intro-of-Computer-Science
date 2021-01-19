import Simulator

def main():
    sim = Simulator.Simulator()
    for i in range(1,7) :
        sim.loadMemory ("input/input"+str(i))
        sim.simulate ()
        sim.storeMemory ("output/output"+str(i))


if __name__ == '__main__':
	main()
