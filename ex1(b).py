def dfs(image,x,y,oldColour,newColour):
    if(x<0 or x>=len(image)or y<0 or y>= len(image[0]) or image [x][y]!= oldColour):
        return
    image [x][y]=newColour
    dfs(image,x+1,y,oldColour,newColour)
    dfs(image,x-1,y,oldColour,newColour)
    dfs(image,x,y+1,oldColour,newColour)
    dfs(image,x,y-1,oldColour,newColour)
def floodFill (image,sr,sc,newColour):
    if image [sr][sc] == newColour:
        return image
    dfs(image,sr,sc,image[sr][sc],newColour)
    return image
if __name__ == "__main__":
    image = [[1,1,1,0],
             [0,1,1,1],
             [1,0,1,1]]
    print("original image")
    for row in image:
        print("".join (map(str,row)))
    sr,sc,newColour = 1,1,1