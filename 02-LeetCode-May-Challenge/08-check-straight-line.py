def inline(x0, y0, x1, y1, x2, y2):
    slope1 = (y2 - y1) * (x1 - x0)
    slope2 = (y1 - y0) * (x2 - x1)
    
    if slope1 == slope2:
        return True
    else:
        return False


class Solution:
    def checkStraightLine(self, coordinates) -> bool:
        # extracting the first two coordinates
        x0, y0 = coordinates[0][0], coordinates[0][1]
        x1, y2 = coordinates[1][0], coordinates[1][1]
        
        flag = 0
        for i in range(2, len(coordinates[2:])):
            xnew, ynew = coordinates[i][0], coordinates[i][1]
            if inline(x0, y0, x1, y2, xnew, ynew):
                continue
            else:
                flag = 1
                break
                
                
        if flag == 0:
            return True
        else:
            return False