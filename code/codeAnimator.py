import pygame
screenSizeMult = 100
screenWidth = 16 * screenSizeMult
screenHeight = 9 * screenSizeMult
screenName = 'Code Animator'
pygame.init()
screen=pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption(screenName)

colors = {
    'background': (30,30,30),
    'lineNos': (133,133,133),
    'w': (212,212,212), #white
    'n': (167,214,167), #number green
    'v': (134,221,254), #varible blue
    's': (220,139,120), #string red
    'l': (0,213,176),   #library green
    'c': (217,110,192), #command pink/purple
    'b': (255,224,0),   #bracket yellow
}
screen.fill(colors['background'])

pixelSize = 8

fontSize = 5*pixelSize
pixelFont = pygame.font.Font('customPixelFont.ttf',fontSize)

topBarButtons = pygame.transform.scale(pygame.image.load('windowButtons.bmp'),(pygame.image.load('windowButtons.bmp').get_width()*pixelSize, pygame.image.load('windowButtons.bmp').get_height()*pixelSize))
topBarHeight = topBarButtons.get_height() + 2*pixelSize
pygame.draw.rect(screen, (0,0,0), pygame.Rect(0,0,screenWidth,topBarHeight))
screen.blit(topBarButtons,(screenWidth - (topBarButtons.get_width() + pixelSize), pixelSize))
captionText = 'Code - Play Tone.py'
caption = pixelFont.render(captionText, False, (255,255,255))
captionX = (screenWidth - caption.get_width()) / 2
screen.blit(caption, (captionX, 0))

fontSize = 8*pixelSize
pixelFont = pygame.font.Font('customPixelFont.ttf',fontSize)

text = [
    '¤cimport ¤lmusic',
    '',
    '¤lmusic¤w.¤lpitch¤b(¤n600¤w,¤n540¤b)',
]

color = colors['w']
splitText = []
charNo = 0
numWidth = pixelFont.render(str(1),False,colors['n']).get_width()
curY = 0

for iLine in range(len(text)):
    line = text[iLine]
    iChar = 0
    curX = pixelSize*2 + numWidth*2
    curY += pixelSize + fontSize
    num = pixelFont.render(str(iLine),False,colors['n'])
    numRect = num.get_rect(right = pixelSize + numWidth*2, y = curY)
    screen.blit(pixelFont.render(str(iLine),False,colors['n']), numRect)
    curX += pixelSize*2

    while iChar < len(line):
        char = line[iChar]
        if char == '¤':
            color = colors[line[iChar+1]]
            iChar += 2
        else:
            let = pixelFont.render(char,False,color)
            screen.blit(let, (curX, curY))
            curX += let.get_width()
            pygame.display.update()
            pygame.image.save(screen, f'export/{captionText} - {charNo}.bmp')
            charNo += 1
            iChar += 1
            
while True:

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            pygame.quit()
            quit()