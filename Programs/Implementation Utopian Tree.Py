def printUtopianTree(cycles):
    heights = [2]
    
    for cycle_nr in xranage(1,max(cycles)+1):
       if cycle_nr % 2 == 1:
          heights.append(heights[-1]*2)
       else:
          heights.append(heights[-1]+1)
          
    for cycle in cycles: 
       print heights[cycle]
if __name__ == '__main__':
    n = int(raw_input())
    
    cycles = []
    
    for i in range(0,n):
       cycles.append(int(raw_input()))
    printUtopianTree(cycles)
