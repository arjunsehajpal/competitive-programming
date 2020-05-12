def flood_fill_recursion(img, x, y, m, n, oldColor, newColor):
    """
    a recursive function to implement flood fill
    """
    # Base Case
    if (x < 0 or x >= m or y < 0 or y >= n or img[x][y] != oldColor or img[x][y] == newColor):
        return
    
    # fill new color
    img[x][y] = newColor
    
    # recur in four directions
    flood_fill_recursion(img, x + 1, y, m, n, oldColor, newColor)
    flood_fill_recursion(img, x - 1, y, m, n, oldColor, newColor)
    flood_fill_recursion(img, x, y + 1, m, n, oldColor, newColor)
    flood_fill_recursion(img, x, y - 1, m, n, oldColor, newColor)
    
    
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        oldColor = image[sr][sc]
        image_len = len(image)
        image_wdh = len(image[0])
        flood_fill_recursion(img = image, 
                                        x = sr, 
                                        y = sc, 
                                        m = image_len,
                                        n = image_wdh,
                                        oldColor = oldColor, 
                                        newColor = newColor)
        return image