from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'system')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.utils import platform

# KivMob integration for Google AdMob Banner Ads
try:
    if platform == 'android':
        from kivmob import KivMob, TestIds
    else:
        KivMob = None
except Exception:
    KivMob = None

Window.clearcolor = (1, 1, 1, 1)
Window.softinput_mode = 'below_target'

class SolidBackground(BoxLayout):
    def __init__(self, color=(1, 1, 1, 1), **kwargs):
        super().__init__(**kwargs)
        self.bg_color = color
        with self.canvas.before:
            Color(*self.bg_color)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

class WeightPriceCalculator(App):

    def build(self):
        self.title = "Weight Price Calculator"
        
        # Initialize Ads if running on Android (Play Store Ready)
        if platform == 'android' and KivMob:
            try:
                self.ads = KivMob(TestIds.APP)
                self.ads.new_banner(TestIds.BANNER)
                self.ads.show_banner()
            except Exception:
                pass

        # ScrollView for Calculator Content
        scroll = ScrollView(size_hint=(1, 1), do_scroll_x=False, do_scroll_y=True)

        root = BoxLayout(orientation="vertical", padding=dp(4), spacing=dp(4), size_hint_y=None)
        root.bind(minimum_height=root.setter('height'))
        
        # 1. Rate Section
        rate_card = SolidBackground(color=(0.95, 0.95, 0.97, 1), orientation="vertical", padding=[dp(10), dp(2)], spacing=dp(2), size_hint_y=None, height=dp(65))
        
        rate_top_lbl = Label(text="Kg", font_size='14sp', bold=True, color=(0.2, 0.2, 0.2, 1), halign='center', valign='middle', size_hint_y=None, height=dp(20))
        rate_top_lbl.bind(size=rate_top_lbl.setter('text_size'))
        
        self.rate = TextInput(text="300", multiline=False, input_type='number', input_filter="float", font_size='16sp', size_hint_y=None, height=dp(35), halign='center')
        self.rate.bind(text=self.calculate_live)
        
        rate_card.add_widget(rate_top_lbl)
        rate_card.add_widget(self.rate)
        root.add_widget(rate_card)

        # 2. Main Two-Column Grid (CHAHIYE WAZAN & CHAHIYE PAISA)
        grid = GridLayout(cols=2, spacing=dp(4), size_hint_y=None, height=dp(190))

        # --- Left Column: CHAHIYE WAZAN ---
        left_col = SolidBackground(color=(0.93, 0.96, 1, 1), orientation="vertical", padding=dp(6), spacing=dp(4))
        
        left_title = Label(text="CHAHIYE WAZAN", font_size='11sp', color=(0.1, 0.4, 0.7, 1), bold=True, size_hint_y=None, height=dp(16), halign='center')
        left_title.bind(size=left_title.setter('text_size'))
        left_col.add_widget(left_title)
        
        gram_box = BoxLayout(orientation="horizontal", spacing=dp(3), size_hint_y=None, height=dp(32))
        self.gram = TextInput(text="600", multiline=False, input_type='number', input_filter="float", font_size='14sp')
        self.gram.bind(text=self.calculate_live)
        gram_lbl = Label(text="grm", font_size='11sp', color=(0.3, 0.3, 0.3, 1), size_hint_x=0.35)
        gram_box.add_widget(self.gram)
        gram_box.add_widget(gram_lbl)
        left_col.add_widget(gram_box)
        
        kilo_box = BoxLayout(orientation="horizontal", spacing=dp(3), size_hint_y=None, height=dp(32))
        self.kg = TextInput(text="1", multiline=False, input_type='number', input_filter="float", font_size='14sp')
        self.kg.bind(text=self.calculate_live)
        kilo_lbl = Label(text="Kg", font_size='11sp', color=(0.3, 0.3, 0.3, 1), size_hint_x=0.35)
        kilo_box.add_widget(self.kg)
        kilo_box.add_widget(kilo_lbl)
        left_col.add_widget(kilo_box)
        
        left_jawab_card = SolidBackground(color=(1, 1, 1, 1), orientation="vertical", padding=dp(4), spacing=dp(1), size_hint_y=None, height=dp(60))
        left_jawab_lbl = Label(text="जवाब", font_size='10sp', color=(0.8, 0.5, 0, 1), bold=True, halign='left', size_hint_y=None, height=dp(14))
        left_jawab_lbl.bind(size=left_jawab_lbl.setter('text_size'))
        
        self.left_result = Label(text="Total ₹480.00", font_size='13sp', color=(0.1, 0.3, 0.5, 1), bold=True, halign='left')
        self.left_result.bind(size=self.left_result.setter('text_size'))
        
        left_jawab_card.add_widget(left_jawab_lbl)
        left_jawab_card.add_widget(self.left_result)
        left_col.add_widget(left_jawab_card)
        grid.add_widget(left_col)

        # --- Right Column: CHAHIYE PAISA ---
        right_col = SolidBackground(color=(0.93, 1, 0.95, 1), orientation="vertical", padding=dp(6), spacing=dp(4))
        
        right_title = Label(text="CHAHIYE PAISA", font_size='11sp', color=(0, 0.5, 0.3, 1), bold=True, size_hint_y=None, height=dp(16), halign='center')
        right_title.bind(size=right_title.setter('text_size'))
        right_col.add_widget(right_title)
        
        amount_box = BoxLayout(orientation="horizontal", spacing=dp(3), size_hint_y=None, height=dp(32))
        amount_lbl = Label(text="Amt", font_size='11sp', color=(0.3, 0.3, 0.3, 1), size_hint_x=0.35)
        self.amount = TextInput(text="70", multiline=False, input_type='number', input_filter="float", font_size='14sp')
        self.amount.bind(text=self.calculate_live)
        amount_box.add_widget(amount_lbl)
        amount_box.add_widget(self.amount)
        right_col.add_widget(amount_box)
        
        right_col.add_widget(BoxLayout(size_hint_y=None, height=dp(32)))

        right_jawab_card = SolidBackground(color=(1, 1, 1, 1), orientation="vertical", padding=dp(4), spacing=dp(1), size_hint_y=None, height=dp(60))
        right_jawab_lbl = Label(text="जवाब", font_size='10sp', color=(0.8, 0.5, 0, 1), bold=True, halign='left', size_hint_y=None, height=dp(14))
        right_jawab_lbl.bind(size=right_jawab_lbl.setter('text_size'))
        
        self.right_result = Label(text="Wajan 233 Grm", font_size='12sp', color=(0, 0.5, 0.3, 1), bold=True, halign='left')
        self.right_result.bind(size=self.right_result.setter('text_size'))
        
        right_jawab_card.add_widget(right_jawab_lbl)
        right_jawab_card.add_widget(self.right_result)
        right_col.add_widget(right_jawab_card)
        grid.add_widget(right_col)

        root.add_widget(grid)

        # 3. Clear Button (Centered)
        clear_container = BoxLayout(orientation="horizontal", size_hint_y=None, height=dp(45), padding=[dp(40), dp(0), dp(40), dp(0)])
        self.clear_btn = Button(
            text="🔄 Clear All", 
            font_size='14sp', 
            bold=True, 
            color=(1, 1, 1, 1), 
            background_color=(0.85, 0.2, 0.2, 1)
        )
        self.clear_btn.bind(on_press=self.clear_all_fields)
        clear_container.add_widget(self.clear_btn)
        root.add_widget(clear_container)

        # 4. Yahan Clear Button ke baad thodi si jagah (Spacing/Gap) chhori gayi hai
        root.add_widget(BoxLayout(size_hint_y=None, height=dp(15)))

        # 5. Banner Ad Area (Gap ke theek neeche)
        banner_ad = SolidBackground(color=(0.9, 0.9, 0.9, 1), orientation="horizontal", size_hint_y=None, height=dp(45))
        banner_label = Label(text="[ Live Banner Ad Space ]", font_size='12sp', color=(0.5, 0.5, 0.5, 1), halign='center', valign='middle')
        banner_label.bind(size=banner_label.setter('text_size'))
        banner_ad.add_widget(banner_label)
        root.add_widget(banner_ad)

        scroll.add_widget(root)

        self.calculate_live(None, None)

        return scroll

    def clear_all_fields(self, instance):
        self.rate.text = ""
        self.kg.text = ""
        self.gram.text = ""
        self.amount.text = ""

    def calculate_live(self, instance, value):
        try:
            rate = float(self.rate.text or "0")
            kg = float(self.kg.text or "0")
            gram = float(self.gram.text or "0")

            total = (kg * rate) + ((gram / 1000) * rate)
            self.left_result.text = f"Total ₹{total:.2f}"

            amount = float(self.amount.text or "0")

            if rate > 0:
                total_gram = (amount / rate) * 1000
                kg2 = int(total_gram // 1000)
                gram2 = int(total_gram % 1000)
                if kg2 > 0:
                    self.right_result.text = f"Wajan {kg2} Kg {gram2} Grm"
                else:
                    self.right_result.text = f"Wajan {gram2} Grm"
            else:
                self.right_result.text = "Wajan: Invalid"

        except Exception:
            self.left_result.text = "Total: Invalid"
            self.right_result.text = "Wajan: Invalid"

if __name__ == "__main__":
    WeightPriceCalculator().run()
  
