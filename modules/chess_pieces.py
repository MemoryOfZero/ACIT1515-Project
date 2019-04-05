import pygame

class Pawn(pygame.sprite.Sprite):

    def __init__(self, colour, x, y):
        super().__init__()
        self.colour = colour
        self.x = x
        self.y = y

        self.image = pygame.Surface((60,60), pygame.SRCALPHA, 32)
        self.image.convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.x = self.x * 60
        self.rect.y = self.y * 60

        self.sprite = pygame.image.load('assets/{}Pawn.png'.format(self.colour))
        self.image.blit(self.sprite, (0, 0))

class King(pygame.sprite.Sprite):

    def __init__(self, colour, x, y):
        super().__init__()
        self.colour = colour
        self.x = x
        self.y = y

        self.image = pygame.Surface((60,60), pygame.SRCALPHA, 32)
        self.image.convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.x = self.x * 60
        self.rect.y = self.y * 60

        self.sprite = pygame.image.load('assets/{}King.png'.format(self.colour))
        self.image.blit(self.sprite, (0, 0))

class Queen(pygame.sprite.Sprite):

    def __init__(self, colour, x, y):
        super().__init__()
        self.colour = colour
        self.x = x
        self.y = y

        self.image = pygame.Surface((60,60), pygame.SRCALPHA, 32)
        self.image.convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.x = self.x * 60
        self.rect.y = self.y * 60

        self.sprite = pygame.image.load('assets/{}Queen.png'.format(self.colour))
        self.image.blit(self.sprite, (0, 0))

class Bishop(pygame.sprite.Sprite):

     def __init__(self, colour, x, y):
        super().__init__()
        self.colour = colour
        self.x = x
        self.y = y

        self.image = pygame.Surface((60,60), pygame.SRCALPHA, 32)
        self.image.convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.x = self.x * 60
        self.rect.y = self.y * 60

        self.sprite = pygame.image.load('assets/{}Bishop.png'.format(self.colour))
        self.image.blit(self.sprite, (0, 0))

class Knight(pygame.sprite.Sprite):

    def __init__(self, colour, x, y):
        super().__init__()
        self.colour = colour
        self.x = x
        self.y = y

        self.image = pygame.Surface((60,60), pygame.SRCALPHA, 32)
        self.image.convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.x = self.x * 60
        self.rect.y = self.y * 60

        self.sprite = pygame.image.load('assets/{}Knight.png'.format(self.colour))
        self.image.blit(self.sprite, (0, 0))

class Rook(pygame.sprite.Sprite):

    def __init__(self, colour, x, y):
        super().__init__()
        self.colour = colour
        self.x = x
        self.y = y

        self.image = pygame.Surface((60,60), pygame.SRCALPHA, 32)
        self.image.convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.x = self.x * 60
        self.rect.y = self.y * 60

        self.sprite = pygame.image.load('assets/{}Rook.png'.format(self.colour))
        self.image.blit(self.sprite, (0, 0))
