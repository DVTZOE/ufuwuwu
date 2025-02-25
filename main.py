#!/bin/python
import flame
import tkinter as tk
from tkinter import filedialog
import os
import math
import random
class uhh(flame.Flame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind("<Button>", self.on_press)
        root.bind("<KeyPress>", self.on_press)
        self.card_dir = ""
        self.black = []
        self.cards = []
        self.doing = 0

        self.menu()

    def menu(self):
        self.current_group = "menu"
        self.add_layer(flame.image(
            group="menu",
            relx=.5,
            rely=.5,
            minwidth=1,
            minheight=1,
            sauce=os.path.join(ASS_DIR, "bg.png")
        ))
        self.add_layer(flame.image(
            group="menu",
            relx=.5,
            rely=.5,
            incest=20,
            width=300,
            height=400,
            sauce=os.path.join(ASS_DIR, "panel.png")
        ))
        self.add_layer(flame.image(
            group="menu",
            relx=.5,
            rely=.5,
            incest=20,
            newcest=12,
            width=200,
            height=50,
            onclick=self.do_da_start,
            sauce=os.path.join(ASS_DIR, "accent.png")
        ))
        self.add_layer(flame.text(
            group="menu",
            text="Start",
            font="Nunito 16 bold",
            relx=.5,
            rely=.5,
        ))
        self.refresh()

    def selector(self):
        self.current_group = "selector"
        self.add_layer(flame.image(
            group="selector",
            relx=.5,
            rely=.5,
            minwidth=1,
            minheight=1,
            sauce=os.path.join(ASS_DIR, "bg.png")
        ))
        self.add_layer(flame.image(
            group="selector",
            relwidth=.4,
            relheight=.75,
            relx=.25,
            rely=.5,
            incest=20,
            onclick=self.left,
            sauce=os.path.join(ASS_DIR, "panel.png")
        ))
        self.left_img = self.add_layer(flame.image(
            group="selector",
            maxwidth=.35,
            maxheight=.6,
            relx=.25,
            rely=.45,
        ))
        self.left_label = self.add_layer(flame.text(
            group="selector",
            text="",
            maxwidth=.2, 
            maxheight=.05,
            relx=0.25,
            rely=.9,
        ))
        self.add_layer(flame.image(
            group="selector",
            relwidth=.4,
            relheight=.75,
            relx=.75,
            rely=.5,
            incest=20,
            onclick=self.right,
            sauce=os.path.join(ASS_DIR, "panel.png")
        ))
        self.right_img = self.add_layer(flame.image(
            group="selector",
            maxwidth=.35,
            maxheight=.6,
            square=True,
            relx=.75,
            rely=.45,
        ))
        self.right_label = self.add_layer(flame.text(
            group="selector",
            text="",
            maxwidth=.4, 
            maxheight=.2,
            relx=0.75,
            rely=.9,
        ))
        self.progress_label = self.add_layer(flame.text(
            group="selector",
            text="?/?",
            maxwidth=.2,
            maxheight=.2,
            relx=0.5,
            rely=.1,
        ))
        self.refresh()

    def wiener(self, wiener):
        self.current_group = "wiener"
        self.add_layer(flame.image(
            group="wiener",
            relx=.5,
            rely=.5,
            minwidth=1,
            minheight=1,
            sauce=os.path.join(ASS_DIR, "bg.png"),
            onclick=self.made_in_heaven,
        ))
        self.add_layer(flame.image(
            group="wiener",
            relwidth=.4,
            relheight=.9,
            relx=.5,
            rely=.5,
            incest=20,
            sauce=os.path.join(ASS_DIR, "panel.png"),
        ))
        self.add_layer(flame.image(
            group="wiener",
            maxwidth=.35,
            maxheight=.85,
            relx=.5,
            rely=.5,
            sauce=os.path.join(self.card_dir, wiener),
        ))
        self.progress_label = self.add_layer(flame.text(
            group="selector",
            text=f"Winner: {wiener[:self.cards[self.doing].rfind('.')]}",
            maxwidth=.2,
            maxheight=.05,
            relx=0.5,
            rely=.9,
        ))
        self.refresh()

    def on_press(self, k):
        if self.current_group != "selector":
            return
        try:
            if k.num == 8:
                self.left()
            elif k.num == 9:
                self.right()
        except:
            if k.keysym == "a":
                self.left()
            elif k.keysym -- "d":
                self.right()
    def left(self):
        self.royale(True)
    def right(self):
        self.royale(False)

    def royale(self, is_left=None):
        if self.doing >= len(self.cards):
            self.cards = self.black.copy()
            self.black = []
            self.doing = 0
        if is_left == True:
            self.black.append(self.cards[self.doing])
        elif is_left == False:
            self.black.append(self.cards[self.doing + 1])
        else:
            temp_ig = []
            for i in range(0, len(self.cards), 2):
                if self.cards[i] == None:
                    if self.cards[i + 1] != None:
                        self.black.append(self.cards[i + 1])
                elif self.cards[i + 1] == None:
                    self.black.append(self.cards[i])
                else:
                    temp_ig.append(self.cards[i])
                    temp_ig.append(self.cards[i + 1])
            self.cards = temp_ig.copy()
            self.doing -= 2
        self.doing += 2

        if self.doing >= len(self.cards):
            self.cards = self.black.copy()
            self.black = []
            self.doing = 0
        if len(self.cards) == 1:
            print(self.cards[0])
            self.remove_group("selector")
            self.wiener(self.cards[0])
            return
        
        self.progress_label.text = f"{self.doing // 2 + 1} / {len(self.cards) // 2}"
        
        left_name = self.cards[self.doing][:self.cards[self.doing].rfind(".")]
        right_name = self.cards[self.doing + 1][:self.cards[self.doing + 1].rfind(".")]
        
        self.left_label.text = left_name
        self.renew_image(layer=self.left_img, sauce=os.path.join(self.card_dir, self.cards[self.doing]))

        self.right_label.text = right_name
        self.renew_image(layer=self.right_img, sauce=os.path.join(self.card_dir, self.cards[self.doing + 1]))

        self.refresh()
    
    def renew_image(self, layer, sauce):
        layer.sauce = sauce
        cp = layer
        self.remove_layer(layer)
        self.add_layer(cp)

    def do_da_import(self):
        self.card_dir = filedialog.askdirectory(
            title="Open the directory of your images"
        )
    def do_da_start(self):
        while not self.card_dir:
            self.do_da_import()
        self.remove_group("menu")
        self.cards = os.listdir(self.card_dir)
        for _ in range((2**math.ceil(math.log2(len(self.cards)))) - len(self.cards)):
            self.cards.append(None)
        random.shuffle(self.cards)
        self.selector()
        self.royale()
    def made_in_heaven(self):
        self.remove_group("wiener")
        self.menu()

if __name__ == "__main__":
    DIR = os.getcwd()
    ASS_DIR = os.path.join(DIR, "assets")
    root = tk.Tk()
    root.minsize(320, 420)
    main = uhh(root, bg="#161617")
    main.pack(fill=tk.BOTH, expand=1)
    root.mainloop()