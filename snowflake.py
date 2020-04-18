class Snowflake:
    def __init__(self, depth):
        self.d = depth
        self.x = random(-floor(width/2), floor(width/2))
        self.y = -floor(height/2)
        self.z = random(0, self.d)
        self.rad = floor( min(width, height) / (depth ** 2 - (depth ** ( 0.5 ) ) ))
        
        
    def snowdraw(self):
        fill( 255, 255, 215, 75)
        translate( self.x, self.y, 0)
        sphere( self.rad  )
        
    def snowAdvance( self ):
        self.y += 1 
