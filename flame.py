import tkinter as tk
from PIL import Image, ImageTk

class event_ig():
    def __init__(self, width, height):
        self.width = width
        self.height = height

class layer():
    def __init__(self, type, group):
        self.type = type
        self.group = group

class image(layer):
    def __init__(self, group, sauce="godot.png", relwidth=0, relheight=0, relx=0, rely=0, width=0, height=0, x=0, y=0, maxwidth=-1, maxheight=-1, minwidth=-1, minheight=-1, square=False, incest=0, newcest=0, onclick=None):
        super().__init__("image", group)
        self.sauce = sauce

        self.relwidth = relwidth
        self.relheight = relheight
        self.relx = relx
        self.rely = rely
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.maxwidth = maxwidth
        self.maxheight = maxheight
        self.minwidth = minwidth
        self.minheight = minheight
        self.square = square

        self.incest = incest
        self.newcest = newcest

        self.onclick = onclick

class tk_obj(layer):
    def __init__(self, group, tk_obj, place):
        super().__init__("tk_obj", group)
        self.tk_obj = tk_obj
        self.place = place

class text(layer):
    def __init__(self, group, text="", font="Nunito 20 bold", fill="#2C4666", relwidth=0, relheight=0, relx=0, rely=0, width=0, height=0, x=0, y=0, maxwidth=-1, maxheight=-1, minwidth=-1, minheight=-1, onclick=None):
        super().__init__("text", group)
        self.text = text
        self.font = font
        self.fill = fill

        self.relwidth = relwidth
        self.relheight = relheight
        self.relx = relx
        self.rely = rely
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.maxwidth = maxwidth
        self.maxheight = maxheight
        self.minwidth = minwidth
        self.minheight = minheight

        self.onclick = onclick


class Flame(tk.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layers = []
        self.earea = []
        self.bind("<Configure>", self.layer_inator)
    def refresh(self):
        self.layer_inator(event_ig(
            width=self.winfo_width(),
            height=self.winfo_height(),
        ))
    def layer_inator(self, event):
        canvas_width = event.width
        canvas_height = event.height

        for layer in self.layers:
            if layer.type == "image":
                resized_image = self.image_resizer(layer, canvas_width, canvas_height)
                new_tk_image = ImageTk.PhotoImage(resized_image)

                self.itemconfig(layer.id, image=new_tk_image)
                layer.tkimage = new_tk_image

                self.coords(layer.id, canvas_width * layer.relx + layer.x, canvas_height * layer.rely + layer.y)
            elif layer.type == "text":
                self.itemconfig(layer.id, text=layer.text)
                self.coords(layer.id, canvas_width * layer.relx + layer.x, canvas_height * layer.rely + layer.y)
            elif layer.type == "tk_obj":
                pass
    def idk_just_click(self, event):
        mx, my = event.x, event.y
        canvas_width = self.winfo_width()
        canvas_height = self.winfo_height()
        for layer in self.earea:
            if ((canvas_width * layer.relwidth + layer.width) / 2) > abs(layer.relx * canvas_width + layer.x - mx) and ((canvas_height * layer.relheight + layer.height) / 2) > abs(layer.rely * canvas_height + layer.y - my):
                layer.onclick()
    def add_layer(self, layer):
        if layer.type == "image":
            layer.og_image = Image.open(layer.sauce)
            layer.id = self.create_image(0, 0, image=ImageTk.PhotoImage(layer.og_image))
            if layer.onclick:
                self.earea.append(layer)
                self.bind("<Button-1>", self.idk_just_click, add=False)
        elif layer.type == "text":
            layer.id = self.create_text(0, 0, text=layer.text, font=layer.font, fill=layer.fill)
            if layer.onclick:
                self.earea.append(layer)
                self.bind("<Button-1>", self.idk_just_click, add=False)
        elif layer.type == "tk_obj":
            layer.tk_obj.place(**layer.place)
        self.layers.append(layer)
        return layer
    def remove_layer(self, layer):
        self.layers.remove(layer)
        if layer in self.earea:
            self.earea.remove(layer)
        if layer.type == "image" or layer.type == "text":
            self.delete(layer.id)
        elif layer.type == "text":
            self.delete
        elif layer.type == "tk_obj":
            layer.tk_obj.place_forget()
    def remove_group(self, group):
        for layer in self.layers.copy():
            if group in layer.group.split():
                self.remove_layer(layer)
    def image_resizer(self, layer, canvas_width, canvas_height):
        og_width, og_height = layer.og_image.size
        ratio = og_width / og_height
        if layer.incest > 0:
            incest = layer.incest
            newcest = layer.newcest if layer.newcest > 0 else incest
            newwidth = int(canvas_width * layer.relwidth) + layer.width
            newheight = int(canvas_height * layer.relheight) + layer.height
            og_widthcest = og_width - incest
            og_heightcest = og_height - incest
            newwidthcest = newwidth - newcest
            newheightcest = newheight - newcest
            newwidthcestcest = newwidthcest - newcest
            newheightcestcest = newheightcest - newcest
            nw = layer.og_image.crop((0, 0, incest, incest)).resize((newcest, newcest))
            n  = layer.og_image.crop((incest, 0, og_widthcest, incest)).resize((newwidthcestcest, newcest))
            ne = layer.og_image.crop((og_widthcest, 0, og_width, incest)).resize((newcest, newcest))
            w  = layer.og_image.crop((0, incest, incest, og_heightcest)).resize((newcest, newheightcestcest))
            o  = layer.og_image.crop((incest, incest, og_widthcest, og_heightcest)).resize((newwidthcestcest, newheightcestcest))
            e  = layer.og_image.crop((og_widthcest, incest, og_width, og_heightcest)).resize((newcest, newheightcestcest))
            sw = layer.og_image.crop((0, og_heightcest, incest, og_height)).resize((newcest, newcest))
            s  = layer.og_image.crop((incest, og_heightcest, og_widthcest, og_height)).resize((newwidthcestcest, newcest))
            se = layer.og_image.crop((og_widthcest, og_heightcest, og_width, og_height)).resize((newcest, newcest))

            resized_image = Image.new("RGBA", (newwidth, newheight))
            resized_image.paste(nw, (0, 0))
            resized_image.paste(n, (newcest, 0))
            resized_image.paste(ne, (newwidthcest, 0))
            resized_image.paste(w, (0, newcest))
            resized_image.paste(o, (newcest, newcest))
            resized_image.paste(e, (newwidthcest, newcest))
            resized_image.paste(sw, (0, newheightcest))
            resized_image.paste(s, (newcest, newheightcest))
            resized_image.paste(se, (newwidthcest, newheightcest))
        elif layer.maxwidth > 0 and layer.maxheight > 0:
            maxwidth = layer.maxwidth * canvas_width
            maxheight = layer.maxheight * canvas_height
            if maxwidth > maxheight * ratio:
                resized_image = layer.og_image.resize((int(maxheight * ratio), int(maxheight)))
            else:
                resized_image = layer.og_image.resize((int(maxwidth), int(maxwidth / ratio)))
        elif layer.minwidth > 0 and layer.minheight > 0:
            minwidth = layer.minwidth * canvas_width
            minheight = layer.minheight * canvas_height
            if minwidth > minheight * ratio:
                if layer.square == True:
                    resized_image = layer.og_image.resize((min(int(minwidth), minwidth / ratio), min(minwidth, int(minwidth / ratio))))
                else:
                    resized_image = layer.og_image.resize((minwidth, int(minwidth / ratio)))
            else:
                if layer.square == True:
                    resized_image = layer.og_image.resize((min(int(minheight * ratio), minheight), min(int(minheight * ratio), minheight)))
                else:
                    resized_image = layer.og_image.resize((int(minheight * ratio), minheight))
        else:
            resized_image = layer.og_image.resize((int(canvas_width * layer.relwidth) + layer.width, int(canvas_height * layer.relheight) + layer.height))
        return resized_image