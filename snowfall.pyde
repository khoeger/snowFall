import snowflake

global flakes
global numFlakes, probFlake, depthOfField

def setup():
    global flakes
    global numFlakes, probFlake, depthOfField
    
    size( 500, 500, P3D )
    
    noStroke()
    shapeMode( CENTER ) 
    sphereDetail(10)
    ambientLight( 255,255,0)
    
    numFlakes = 10
    depthOfField = 10
    probFlake = 0.5 # Likelihood of a flake being created
    
    flakes = []
    
    # for i in range(numFlakes):
    #     flake = snowflake.Snowflake( depthOfField )
    #     flakes.append( flake )
    #     print(flake.x)
        
    
def draw():
    global flakes
    global numFlakes
    
    background( 200, 225, 250 )

    # new flakes?
    newFlake()
    
    #lights()
    pointLight( 255, 255, 215, 500, 0, -10)
    
    # single
    # fill( 255, 255, 255, 75)
    # translate( width/2, height/2, 0)
    # sphere( floor( min(width, height) / 75 ) )
    
    popList = []
    for i in range( len( flakes) ):
        flake = flakes[i]
        flake.snowdraw()
    
        
        # has the snow reached the bottom?
        if flake.y <= height/2 + flake.rad :
            print(flake.x, flake.y, "advanced")
            flake.snowAdvance()
        else: # if it has
            print(flake.x, flake.y, "popped")
            popList.append(i)
    
    for popIndex in popList:
        flakes.pop(popIndex)
        
    saveFrame("snowfallv0-######.png")

def newFlake():
    global flakes
    global numFlakes, probFlake, depthOfField
    
    """ if makeFlake <= probFlake, make a flake """ 
    makeFlake = random(0.0, 1.0)
    if (len(flakes) < numFlakes) and (makeFlake <= probFlake):
        flake = snowflake.Snowflake( depthOfField )
        flakes.append(flake)
